# pylint: disable=import-outside-toplevel, missing-function-docstring
"""
Upload plugin for Th1520 Revy
"""
from .prelude import *  # pylint: disable=wildcard-import, unused-wildcard-import

__version__ = "0.0.2"


class Th1520Revy(UploadPluginBase):
    """
    Class for LM4A Revy plugin
    """

    import urllib
    import bs4

    @staticmethod
    def get_name() -> str:
        return "th1520_revy"

    can_handle_tup = {
        "revyos-sipeed-lpi4a": ("sipeed_licheepi4a", "debian", "null"),
        "revyos-sipeed-lc4a": ("sipeed_licheecluster4a", "debian", "null"),
        "uboot-revyos-sipeed-lpi4a-16g": ("sipeed_licheepi4a", "debian", "null"),
        "uboot-revyos-sipeed-lpi4a-8g": ("sipeed_licheepi4a", "debian", "null"),
        "uboot-revyos-sipeed-lc4a-16g": ("sipeed_licheecluster4a", "debian", "null"),
        "uboot-revyos-sipeed-lc4a-8g": ("sipeed_licheecluster4a", "debian", "null"),
        "revyos-milkv-meles": ("milkv_meles", "debian", "null"),
    }

    def can_handle(self, vinfo: VInfo) -> bool:
        return vinfo in self.can_handle_tup.values()

    def all_index_can_handle(self):
        return self.can_handle_tup

    def is_mapped_ruyi_index(self, vinfo: VInfo, index: str) -> bool:
        if index in self.can_handle_tup and self.can_handle_tup[index] == vinfo:
            return True
        return False

    def handle_version(self, vinfo: VInfo) -> str:
        # Wait for ruyi to give a more specific definition
        # If it is milkv_meles, the version should be greater than 1.0.0
        # to override old vendor release
        if vinfo == ("milkv_meles", "debian", "null"):
            return f"1.{vinfo.version}.0"
        return f"0.{vinfo.version}.0"

    def handle_report(self, vinfo: VInfo,
                      index: str, last_index: list[BoardImages]) -> BoardImages:
        if index == "revyos-sipeed-lpi4a" or index == "revyos-sipeed-lc4a" \
                or index == "revyos-milkv-meles":
            return self.handle_report_image(vinfo, index, last_index)
        if index == "uboot-revyos-sipeed-lpi4a-8g" or index == "uboot-revyos-sipeed-lc4a-8g":
            return self.handle_report_uboot_8g(vinfo, index, last_index)
        if index == "uboot-revyos-sipeed-lpi4a-16g" or index == "uboot-revyos-sipeed-lc4a-16g":
            return self.handle_report_uboot_16g(vinfo, index, last_index)
        raise ValueError(f"Unknown index {index}")

    def handle_report_image(self, vinfo: VInfo,
                            index: str, last_index: list[BoardImages]) -> BoardImages | None:
        if index == "revyos-sipeed-lpi4a":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/{
                vinfo.version}/"
        elif index == "revyos-sipeed-lc4a":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/{
                vinfo.version}/"
        elif index == "revyos-milkv-meles":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/meles/{
                vinfo.version}/"
        else:
            return None

        html = self.requests.get(base_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        selector = "#list > tbody > tr > td.link > a"

        root_dist = None
        boot_dist = None

        for link in soup.select(selector):
            if 'root-' in link.contents[0]:
                root_url = self.urljoin(
                    base_url, str(link["href"]))
                root_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                root_file = self.download_file(root_path, root_url)
                root_dist = self.gen_distfile(root_file, root_url)
            elif 'boot-' in link.contents[0] and 'u-boot' not in link.contents[0]:
                boot_url = self.urljoin(
                    base_url, str(link["href"]))
                boot_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                boot_file = self.download_file(boot_path, boot_url)
                boot_dist = self.gen_distfile(boot_file, boot_url)

        if index == "revyos-sipeed-lpi4a":
            desc = f"RevyOS {vinfo.version} image for Sipeed LicheePi 4A"
        elif index == "revyos-sipeed-lc4a":
            desc = f"RevyOS {vinfo.version} image for Sipeed LicheeCluster 4A"
        elif index == "revyos-milkv-meles":
            desc = f"RevyOS {vinfo.version} image for Milk-V Meles (vendor release v1.0.0)"
        else:  # unreachable
            raise ValueError(f"Unknown index {index}")
        res = self.copy.copy(last_index[-1])
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info["metadata"]["desc"] = desc
        res.info["distfiles"] = [
            root_dist, boot_dist
        ]
        res.info["blob"]["distfiles"] = [
            root_dist["name"],
            boot_dist["name"]
        ]
        res.info["provisionable"]["partition_map"] = {
            "boot": ".".join(boot_dist["name"].split(".")[:-1]),
            "root": ".".join(root_dist["name"].split(".")[:-1])
        }
        return res

    def handle_report_uboot_8g(self, vinfo: VInfo,
                               index: str, last_index: list[BoardImages]) -> BoardImages | None:
        if index == "uboot-revyos-sipeed-lpi4a-8g":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/{
                vinfo.version}/"
        elif index == "uboot-revyos-sipeed-lc4a-8g":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/{
                vinfo.version}/"
        else:
            return None

        html = self.requests.get(base_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        selector = "#list > tbody > tr > td.link > a"

        uboot_dist = None

        if index == "uboot-revyos-sipeed-lpi4a-8g"  \
                and self.cmp_version(vinfo.version, "20240720") <= 0:
            bname = "u-boot-with-spl-lpi4a"
        elif index == "uboot-revyos-sipeed-lpi4a-8g" \
                and self.cmp_version(vinfo.version, "20240720") > 0:
            bname = "u-boot-with-spl-lpi4a-main"
        elif index == "uboot-revyos-sipeed-lc4a-8g":
            bname = "u-boot-with-spl-lc4a-main"
        else:  # unreachable
            raise ValueError(f"Unknown index {index}")

        for link in soup.select(selector):
            if link.contents[0] == f"{bname}.bin":
                uboot_url = self.urljoin(
                    base_url, str(link["href"]))
                uboot_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                uboot_file = self.download_file(uboot_path, uboot_url)
                uboot_dist = self.gen_distfile(uboot_file, uboot_url)
                uboot_dist["name"] = f"{bname}.{
                    vinfo.version}.bin"

        if index == "uboot-revyos-sipeed-lpi4a-8g":
            desc = f"U-Boot image for LicheePi 4A (8G RAM) and RevyOS {
                vinfo.version}"
        elif index == "uboot-revyos-sipeed-lc4a-8g":
            desc = f"U-Boot image for LicheeCluster 4A (8G RAM) and RevyOS {
                vinfo.version}"
        else:  # unreachable
            raise ValueError(f"Unknown index {index}")
        res = self.copy.copy(last_index[-1])
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info["metadata"]["desc"] = desc
        res.info["distfiles"] = [uboot_dist]
        res.info["blob"]["distfiles"] = [
            uboot_dist["name"]
        ]
        res.info["provisionable"]["partition_map"] = {
            "uboot": uboot_dist["name"]
        }
        return res

    def handle_report_uboot_16g(self, vinfo: VInfo,
                                index: str, last_index: list[BoardImages]) -> BoardImages | None:
        if index == "uboot-revyos-sipeed-lpi4a-16g":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/{
                vinfo.version}/"
        elif index == "uboot-revyos-sipeed-lc4a-16g":
            base_url = f"https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/{
                vinfo.version}/"
        else:
            return None
        html = self.requests.get(base_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        selector = "#list > tbody > tr > td.link > a"

        uboot_dist = None

        if index == "uboot-revyos-sipeed-lpi4a-16g"  \
                and self.cmp_version(vinfo.version, "20240720") <= 0:
            bname = "u-boot-with-spl-lpi4a-16g"
        elif index == "uboot-revyos-sipeed-lpi4a-16g" \
                and self.cmp_version(vinfo.version, "20240720") > 0:
            bname = "u-boot-with-spl-lpi4a-16g-main"
        elif index == "uboot-revyos-sipeed-lc4a-16g":
            bname = "u-boot-with-spl-lc4a-16g-main"
        else:  # unreachable
            raise ValueError(f"Unknown index {index}")

        for link in soup.select(selector):
            if link.contents[0] == f"{bname}.bin":
                uboot_url = self.urljoin(
                    base_url, str(link["href"]))
                uboot_path = self.os.path.join(
                    self.__tmppath__, link.contents[0])
                uboot_file = self.download_file(uboot_path, uboot_url)
                uboot_dist = self.gen_distfile(uboot_file, uboot_url)
                uboot_dist["name"] = f"{bname}.{
                    vinfo.version}.bin"

        if index == "uboot-revyos-sipeed-lpi4a-16g":
            desc = f"U-Boot image for LicheePi 4A (16G RAM) and RevyOS {
                vinfo.version}"
        elif index == "uboot-revyos-sipeed-lc4a-16g":
            desc = f"U-Boot image for LicheeCluster 4A (16G RAM) and RevyOS {
                vinfo.version}"
        else:  # unreachable
            raise ValueError(f"Unknown index {index}")
        res = self.copy.copy(last_index[-1])
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info["metadata"]["desc"] = desc
        res.info["distfiles"] = [uboot_dist]
        res.info["blob"]["distfiles"] = [
            uboot_dist["name"]
        ]
        res.info["provisionable"]["partition_map"] = {
            "uboot": uboot_dist["name"]
        }
        return res


def register() -> UploadPluginBase | None:
    """
    Register the plugin
    """
    return Th1520Revy()
