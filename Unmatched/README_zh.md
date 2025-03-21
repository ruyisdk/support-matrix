# HiFive Unmatched

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/
    - 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt
- openKylin 1.0
    - 下载链接：https://www.openkylin.top/downloads
    - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Ubuntu 24.10
    - 下载链接：https://cdimage.ubuntu.com/releases/24.10/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched
- Ubuntu 24.04.2 LTS
    - 下载链接：https://cdimage.ubuntu.com/releases/24.04.2/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched
- FreeBSD 14.0
    - 下载链接：https://mirrors.ustc.edu.cn/freebsd/releases/riscv/riscv64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz
    - 参考安装文档：https://wiki.freebsd.org/riscv/HiFiveUnmatched
- OpenBSD 7.4
    - 下载链接：https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img
    - 参考安装文档：https://ftp.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Zephyr
    - 参考安装文档：https://docs.zephyrproject.org/latest/boards/sifive/hifive_unmatched/doc/index.html
- OpenWrt 23.05.2
    - 下载链接（Firmware Selector）：https://firmware-selector.openwrt.org/?version=23.05.2&target=sifiveu%2Fgeneric&id=sifive_unmatched
    - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.sifive
- Debian sid
    - 下载链接：https://people.debian.org/~deiv/riscv/debian-sid-risc-v-sifive-unmatched.tar.xz
    - 参考安装文档：https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched
- OpenSUSE Tumbleweed
    - 下载链接：https://download.opensuse.org/repositories/home:/Andreas_Schwab:/riscv:/unmatched/images/openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz
    - 参考安装文档：https://en.opensuse.org/HCL:HiFive_Unmatched
- Fedora 38
    - 下载链接：https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz
    - 参考安装文档：https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/README_zh.md
- Deepin
    - 下载链接：https://cdimage.deepin.com/RISC-V/Unmatched-image/deepin-sifive.7z
    - 参考安装文档：https://cdimage.deepin.com/RISC-V/Unmatched-image/README.txt

### 硬件开发板信息

- HiFive Unmatched

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）        |
| ----------------------- | -------- | --------------------------- |
| Debian 镜像启动         | N/A      | [成功][Debian]              |
| openEuler/Base 镜像启动 | N/A      | [成功][oERV]                |
| openEuler/Xfce 镜像启动 | N/A      | [成功][oERV]                |
| openKylin 镜像启动      | N/A      | [成功][oK]（官方支持）      |
| OpenSUSE 镜像启动       | N/A      | [成功][SUSE]                |
| Ubuntu 镜像启动         | N/A      | [CFT][Ubuntu]（官方支持）   |
| Ubuntu LTS 镜像启动     | N/A      | [CFT][Ubuntu LTS]（官方支持）|
| FreeBSD 镜像启动        | N/A      | [成功][FreeBSD]（官方支持） |
| OpenBSD 镜像启动        | N/A      | [成功][OpenBSD]（官方支持） |
| Zephyr 启动             | N/A      | [成功][Zephyr]（官方支持）  |
| OpenWrt 启动            | N/A      | [成功][OpenWrt]（官方支持） |
| Fedora 启动             | N/A      | [成功][Fedora]（官方支持）  |
| Deepin 启动             | N/A      | [CFT][Deepin]（官方支持）   |

[Debian]: ./Debian/README_zh.md
[oERV]: ./openEuler/README_zh.md
[oK]: ./openKylin/README_zh.md
[SUSE]: ./OpenSUSE/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu LTS]: ./Ubuntu/README_LTS_zh.md
[FreeBSD]: ./FreeBSD/README_zh.md
[OpenBSD]: ./OpenBSD/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Deepin]: ./Deepin/README_zh.md