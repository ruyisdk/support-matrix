# HiFive Unmatched

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.09 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/
    - 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt
- openKylin
    - 下载链接：https://www.openkylin.top/downloads
    - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Ubuntu 23.10
    - 下载链接：https://cdimage.ubuntu.com/releases/23.10/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched
- FreeBSD 14.0
    - 下载链接：https://mirrors.ustc.edu.cn/freebsd/releases/riscv/riscv64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz
    - 参考安装文档：https://wiki.freebsd.org/riscv/HiFiveUnmatched
- OpenBSD 7.4
    - 下载链接：https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img
    - 参考安装文档：https://ftp.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Zephyr
    - 参考安装文档：https://docs.zephyrproject.org/latest/boards/riscv/index.html
- OpenWrt 23.05.2
    - 下载链接（Firmware Selector）：https://firmware-selector.openwrt.org/?version=23.05.2&target=sifiveu%2Fgeneric&id=sifive_unmatched
    - 参考安装文档：https://github.com/Pagerd/PLCT/blob/main/Report/week/week33/OpenWrt.md

### 硬件开发板信息

- HiFive Unmatched

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）                                                                               |
|-----------------------|----------|------------------------------------------------------------------------------------------------|
| openEuler/Base 镜像启动 | N/A      | [成功](https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/tree/master/Unmatched)   |
| openEuler/Xfce 镜像启动 | N/A      | [成功](https://gitee.com/yunxiangluo/openEuler-RISC-V-23.09-independent/tree/master/Unmatched)   |
| openKylin 镜像启动      | N/A      | [成功](https://github.com/ruyisdk/ruyi/issues/65#issuecomment-1970489466)                        |
| Ubuntu 镜像启动         | N/A      | [成功](https://github.com/ruyisdk/ruyi/issues/65#issuecomment-1970489466)                        |
| FreeBSD 镜像启动        | N/A      | [成功](https://github.com/ruyisdk/ruyi/issues/65#issuecomment-1970489466)                        |
| OpenBSD 镜像启动        | N/A      | [成功](https://github.com/ruyisdk/ruyi/issues/65#issuecomment-1970489466)                        |
| Zephyr 启动             | N/A      | [成功](https://github.com/KevinMX/PLCT-Tarsier-Works/blob/main/misc/month10/Zephyr_Unmatched.md) |
| OpenWrt 启动            | N/A      | [成功](https://github.com/Pagerd/PLCT/blob/main/Report/week/week33/OpenWrt.md)                   |
