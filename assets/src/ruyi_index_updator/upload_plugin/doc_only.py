# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
"""
This plugin will do nothing but mark the info with doc_only
"""

from typing import Optional, TypedDict, Required

from .prelude import *

__version__ = "1.0.0"


class InfoDecl(TypedDict):
    id: Optional[str]
    vendor: Required[str]
    system: Required[str]
    variant: Required[str]


class DocOnly(UploadPluginBase):

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
                self.logger.info("Doc Only loads: %s", _id)
                self.handler_lst.append(i)

    @staticmethod
    def get_name() -> str:
        return "doc_only"

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
        raise RuntimeError("Doc Only unreachable")

    def system_image_files(self, info, board_variant=None):
        raise RuntimeError("Doc Only unreachable")

    def handle_version(self, info):
        return None

    def handle_report(self, info):
        raise RuntimeError("Doc Only unreachable")


def register():
    return DocOnly()
