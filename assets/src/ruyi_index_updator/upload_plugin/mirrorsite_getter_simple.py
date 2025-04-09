# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
# pylint: disable=eval-used
"""
To use simple getter, here are a few restrictions:
1. The device should have no variant (i.e.: only generic)
2. Only one image file for each release
"""

from typing import Optional, TypedDict, Required

from .prelude import *

__version__ = "1.0.0"


class FilterDecl(TypedDict):
    type: Optional[Literal["regex", "lambda"]]  # Default to "regex"

    # if type is "lambda", this should be the lambda function
    #       lambda should be like:
    #           def lambda_func(name: str, info: SystemInfo) -> bool
    # if type is "regex", this should be a regex tester, given a name only
    filter: Required[str]


class MapperDecl(TypedDict):
    type: Optional[Literal["regex", "lambda"]]  # Default to "regex"
    regex: Optional[str]

    # if type is "lambda", this should be the lambda function
    #       lambda should be like:
    #           def lambda_func(name: str, info: SystemInfo) -> str
    # if type is "regex", this should be a format string,
    #     format args is the regex groups
    mapper: Required[str]


class InfoDecl(TypedDict):
    id: Optional[str]
    vendor: Required[str]
    board_variant: Optional[str]
    system: Required[str]
    variant: Required[str]

    # The given str is the vinfo.version
    url: Required[MapperDecl]

    # To filter a file name
    file_filter: Required[FilterDecl]

    # To map the system version to a symver
    version_mapper: Required[MapperDecl]

    strategy: Optional[str]  # Default to "dd_v1"

    partition_map: Optional[str]  # In simple, only one file. Default to "disk"

    # For the description of the system
    # This doesn't follow the original MapperDecl design
    # If the type is "lambda", this should be the lambda function
    #      A SystemInfo will be passed to the lambda, return a str
    # If the type is "regex", this should be a format string,
    #      format args is a SystemInfo object named "info"
    #      eg: "System {info.system} as {info.variant}"
    desc_mapper: Required[MapperDecl]

    # Optional: generate display name for the system
    # If not provided, a default name will be generated
    # Defination is the same as desc_mapper
    name_mapper: Optional[MapperDecl]


class MirrorsiteGetter(UploadPluginBase):

    handler_lst: list[InfoDecl]

    def __init__(self):
        super().__init__()
        self.handler_lst = []
        for i in config["handler"]:
            if i["plugin"] == self.get_name():
                _id = i.get(
                    "id", f"{i["system"]}-{i["vendor"]}{f"-{i["variant"]}" if i["variant"]
                                                        != "null" else ""}"
                )
                self.logger.info("Mirrorsite Getter Simple loads: %s", _id)
                self.handler_lst.append(i)
        for i in self.load_sep_config():
            if i.get("handler", None) is None:
                continue
            for j in i["handler"]:
                if j.get("plugin", None) != self.get_name():
                    continue
                _id = j.get(
                    "id", f"{j["system"]}-{j["vendor"]}{f"-{j["variant"]}" if j["variant"]
                                                            != "null" else ""}"
                )
                self.logger.info("Mirrorsite Getter Simple loads: %s", _id)
                self.handler_lst.append(j)

    @staticmethod
    def get_name() -> str:
        return "mirrorsite_getter_simple"

    def __gen_ident(self, info: InfoDecl) -> SystemIdentifier:
        return self.SystemIdentifier(
            vendor=info["vendor"],
            system=info["system"],
            variant=info["variant"]
        )

    def all_can_handle(self):
        res = []

        for handler in self.handler_lst:
            res.append(self.__gen_ident(handler))
        return res

    def system_display_name(self, info, board_variant=None):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if board_variant is not None and board_variant != handler.get("board_variant", None):
                continue
            if handler.get("name_mapper") is not None:
                if handler["name_mapper"].get("type") is None or \
                        handler["name_mapper"]["type"] == "regex":
                    return handler["name_mapper"]["mapper"].format(info=info)
                elif handler["name_mapper"]["type"] == "lambda":
                    func = self.eval(handler["name_mapper"]["mapper"])
                    return func(board_variant, info)
                else:
                    raise ValueError("Unknown MapperDecl type")
        return f"{info.system} {info.variant or ''} for {info.product}"

    def system_image_files(self, info, board_variant=None):
        res = []
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if board_variant is not None and board_variant != handler.get("board_variant", None):
                continue
            if board_variant is not None:
                name = self.util.file_id(info, board_variant, None)
                res.append(name)
            elif handler.get("board_variant", None) is not None:
                name = self.util.file_id(info, handler["board_variant"], None)
                res.append(name)
            else:
                for i in info.board_variants:
                    name = self.util.file_id(info, i, None)
                    res.append(name)
        return self.unique_list(res)

    def __handle_version(self, info, handler):
        if handler["version_mapper"].get("type") is None or \
                handler["version_mapper"]["type"] == "regex":
            r = handler["version_mapper"]["regex"]
            m = self.re.findall(r, info.version)
            return handler["version_mapper"]["mapper"].format(*m)
        elif handler["version_mapper"]["type"] == "lambda":
            func = self.eval(handler["version_mapper"]["mapper"])
            return func(info.version, info)
        else:
            raise ValueError("Unknown MapperDecl type")

    def handle_version(self, info):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if handler.get("board_variant", None) is not None and \
                handler["board_variant"] not in info.board_variants:
                continue
            return self.__handle_version(info, handler)
        raise RuntimeError(f"No handler found for {info}")

    def __get_page_url(self, info: SystemInfo, handler: InfoDecl):
        if handler["url"].get("type") is None or \
                handler["url"]["type"] == "regex":
            r = handler["url"]["regex"]
            m = self.re.findall(r, info.version)
            return handler["url"]["mapper"].format(*m)
        elif handler["url"]["type"] == "lambda":
            func = self.eval(handler["url"]["mapper"])
            return func(info.version, info)
        else:
            raise ValueError("Unknown MapperDecl type")

    import bs4

    def __get_mirrorsite_asset(self, info: SystemInfo, handler: InfoDecl):
        page_url = self.__get_page_url(info, handler)
        html = self.requests.get(page_url, timeout=60).text
        soup = self.bs4.BeautifulSoup(html, "html5lib")

        hyperlinks = soup.select('a')
        for link in hyperlinks:
            if not link.has_attr("href"):
                continue
            file_link = self.urljoin(
                page_url, str(link["href"]))
            file_name = self.urlbasename(file_link)
            if handler["file_filter"].get("type") is None or \
                    handler["file_filter"]["type"] == "regex":
                if self.re.search(handler["file_filter"]["filter"], file_name):
                    return file_link
            elif handler["file_filter"]["type"] == "lambda":
                func = self.eval(handler["file_filter"]["filter"])
                if func(file_name, info):
                    return file_link
            else:
                raise ValueError("Unknown FilterDecl type")
        raise ValueError(
            f"No download file found in page {page_url} for {info}"
        )

    def __gen_desc(self, info, handler):
        if handler.get("desc_mapper") is None:
            return f"{info.system} {info.variant or ''} for {info.product} with version {info.version}"
        if handler["desc_mapper"].get("type") is None or \
                handler["desc_mapper"]["type"] == "regex":
            return handler["desc_mapper"]["mapper"].format(info=info)
        elif handler["desc_mapper"]["type"] == "lambda":
            func = self.eval(handler["desc_mapper"]["mapper"])
            return func(info)
        else:
            raise ValueError("Unknown MapperDecl type")

    def handle_report(self, info):
        for handler in self.handler_lst:
            if self.__gen_ident(handler) != info:
                continue
            if handler.get("board_variant", None) is not None and \
                handler["board_variant"] not in info.board_variants:
                continue
            img_url = self.__get_mirrorsite_asset(info, handler)
            img_name = self.urlbasename(img_url)
            img_path = self.os.path.join(
                self.__tmppath__, img_name
            )
            img_file = self.download_file(
                img_path, img_url
            )
            img_dist = self.gen_distfile(
                img_file, img_url
            )
            desc = self.__gen_desc(info, handler)
            partition_map = handler.get("partition_map", "disk")
            partition_map = {
                partition_map: self.util.remove_file_extension(img_name)
            }
            generator = self.BoardImagesGenerator(
                version=self.__handle_version(info, handler),
                upstream_version=info.version,
                desc=desc,
                vendor=info.vendor,
                distfiles=[img_dist],
                strategy=handler.get("strategy", "dd_v1"),
                partition_map=partition_map,
                status=info.raw_data.status
            )
            return {
                self.util.file_id(info, handler.get("board_variant", None), None): generator
            }

        raise RuntimeError(f"No handler found for {info}")


def register():
    return MirrorsiteGetter()
