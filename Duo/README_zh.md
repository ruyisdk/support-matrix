# Milk-V Duo

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Milk-V 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
- Arch Linux
  - 下载链接：https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing
  - 参考安装文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image
- Alpine Linux 3.21.3
  - 下载链接：
    - Alpine minirootfs: https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/riscv64/alpine-minirootfs-3.21.3-riscv64.tar.gz
    - 官方 Buildroot 镜像: https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip
  - 参考安装文档：
    - https://wiki.alpinelinux.org/wiki/Installation
    - https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot
    - https://community.milkv.io/t/alpine-linux-on-the-duo/700/18
- Debian trixie/sid
  - 下载链接：https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing
  - 参考安装文档：https://github.com/hongwenjun/riscv64/tree/main/milkv-duo
- Fedora 41
  - 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo/images/latest/milkv-duo-fedora-minimal.img.gz
  - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/Installing
- RT-Thread / RT-Thread Smart
  - 源码链接：https://github.com/RT-Thread/rt-thread
  - 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md
- ThreadX
  - 源码链接: https://github.com/saicogn/ThreadX-to-RISC-V64
  - 参考安装文档: https://github.com/saicogn/ThreadX-to-RISC-V64/blob/main/README.md
- Zephyr
  - 源码链接: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - 参考安装文档:
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- openEuler 23.09 riscv64
  - 下载链接：
    - buildroot: https://github.com/milkv-duo/duo-buildroot-sdk.git
    - rootfs: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/openeuler-rootfs.tar.gz
  - 参考安装文档：https://blog.inuyasha.love/linuxeveryday/33.html
- UniProton
  - 下载链接: https://share.weiyun.com/0gIkzesF
  - 参考安装文档: https://github.com/openeuler-riscv/duo-buildroot-sdk/blob/develop/uni_pedestal/WORK.md
- Ubuntu 22.04
  - 下载链接：https://drive.google.com/file/d/1y1NQamzUDzot_kVT2yKkbusoJmtvH5tD/view?usp=sharing
  - 参考安装文档：
    - https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#Ubuntu_Disk_Image
    - https://github.com/bassusteur/milkv-duo-ubuntu
- Yocto
  - 源码链接：https://github.com/kinsamanka/meta-milkv
  - 参考安装文档：https://github.com/kinsamanka/meta-milkv/blob/master/README.md
- NixOS
  - 源码链接: https://github.com/NickCao/nixos-riscv
  - 参考安装文档: https://github.com/NickCao/nixos-riscv/README.md
- OpenWrt
  - 源码链接：https://github.com/draftbottle/VizOS
  - 参考安装文档：https://community.milkv.io/t/milk-v-duo-openwrt/2399
- xv6
  - 下载链接：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
  - 参考安装文档：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### 硬件开发板信息

- Milk-V Duo (64M, CV1800B)

## 测试结果

| 软件分类                       | 软件包名 | 测试结果（测试报告）                               |
| ------------------------------ | -------- | -------------------------------------------------- |
| BuildRoot 镜像启动             | N/A      | [成功][Duo]                                        |
| BuildRoot (v2) 镜像启动        | N/A      | [成功][Duo2]                                       |
| FreeRTOS 启动                  | N/A      | [成功][FreeRTOS]（已包含在 BuildRoot 镜像内）      |
| Arch Linux 镜像启动            | N/A      | [成功][Arch]                                       |
| Alpine Linux 启动              | N/A      | [成功][Alpine] （可使用社区镜像或手工构建 rootfs） |
| Debian 镜像启动                | N/A      | [成功][Debian]                                     |
| RT-Thread 镜像构建及启动       | N/A      | [成功][RT-Thread]                                  |
| RT-Thread Smart 镜像构建及启动 | N/A      | [成功][RT-Smart]                                   |
| Fedora 镜像启动                | N/A      | [成功][Fedora]                                     |
| openEuler                      | N/A      | [成功][oE]                                         |
| ThreadX 镜像构建及启动         | N/A      | [成功][ThreadX]                                    |
| Zephyr  镜像构建及启动         | N/A      | [成功][Zephyr]                                     |
| UniProton 启动                 | N/A      | [成功][UniProton]                                  |
| xv6 启动                       | N/A      | [成功][xv6]                                        |
| Ubuntu 启动                    | N/A      | [成功][Ubuntu]                                     |
| Yocto  镜像构建及启动          | N/A      | [成功][Yocto]                                      |
| NixOS  镜像构建及启动          | N/A      | [成功][NixOS]                                      |
| OpenWrt  镜像构建及启动        | N/A      | [成功][OpenWrt]                                    |

[Duo]: ./BuildRoot/README_zh.md
[Duo2]: ./BuildRoot/README_v2_zh.md
[Arch]: ./ArchLinux/README_zh.md
[Alpine]: ./Alpine/README_zh.md
[Debian]: ./Debian/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[RT-Smart]: ./RT-Smart/README_RTSmart_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[oE]: ./openEuler/README_zh.md
[ThreadX]: ./ThreadX/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[UniProton]: ./UniProton/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Yocto]: ./Yocto/README_zh.md
[NixOS]: ./NixOS/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[xv6]: ./xv6/README_zh.md