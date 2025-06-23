# DongshanPI-哪吒 STU

## 测试环境

### 操作系统信息

- Tina Linux
  - 下载链接：https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7
  - 参考安装文档：https://d1.docs.aw-ol.com/study/study_1tina/
- Debian
  - 下载链接：https://github.com/DongshanPI/NezhaSTU-ReleaseLinux
  - 参考安装文档：https://github.com/DongshanPI/NezhaSTU-ReleaseLinux
- OpenWrt
  - 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=dongshan_nezha_stu
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- BuildRoot:
  - 下载链接：https://github.com/DongshanPI/buildroot_dongshannezhastu
  - 参考安装文档：https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/
- Arch Linux
  - 打包脚本：https://github.com/sehraf/d1-riscv-arch-image-builder
- postmarketOS
  - 下载链接（pmbootstrap）: https://wiki.postmarketos.org/wiki/Pmbootstrap
  - 参考安装文档：https://wiki.postmarketos.org/index.php?title=MangoPi_MQ-Pro_(mangopi-mq-pro)&direction=prev&oldid=46021
- FreeBSD
  - 下载链接：https://github.com/freebsd-d1/freebsd-d1
  - 参考安装文档：https://github.com/freebsd-d1/freebsd-d1
- Fedora
  - 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
  - 参考安装文档：https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html
- Deepin 23 beige 20221209
  - 下载链接：https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-d1-20221208175445.img.zst.0
  - 参考安装文档：https://github.com/deepin-community/deepin-riscv-board/
- RT-Thread
  - 源码链接：https://github.com/bigmagic123/d1-nezha-rtthread
  - 参考安装文档：https://github.com/bigmagic123/d1-nezha-rtthread
- xv6
  - 源码链接：https://github.com/michaelengel/xv6-d1
  - 参考安装文档：https://github.com/michaelengel/xv6-d1

### 硬件开发板信息

- DongshanPI-哪吒 STU 开发板

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告） |
| ----------------------- | -------- | -------------------- |
| Tina-Linux 镜像启动     | N/A      | [成功][Tina]         |
| OpenWrt 镜像启动        | N/A      | [成功][OpenWrt]      |
| Debian 镜像启动         | N/A      | [成功][Debian]       |
| Arch Linux 镜像启动     | N/A      | [成功][Arch]         |
| BuildRoot 镜像启动      | N/A      | [CFI][BuildRoot]     |
| postmarketOS 编译和启动 | N/A      | [成功][pmOS]         |
| FreeBSD 镜像编译和启动  | N/A      | [成功][FreeBSD]      |
| Fedora 镜像启动         | N/A      | [失败][Fedora]       |
| Gentoo 镜像启动         | N/A      | [成功][Gentoo]       |
| Deepin 镜像启动         | N/A      | [成功][Deepin]       |
| RT-Thread 编译和启动    | N/A      | [成功][RT-Thread]    |
| xv6 编译和启动          | N/A      | [成功][xv6]          |

[Tina]: ./TinaLinux/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Arch]: ./ArchLinux/README_zh.md
[pmOS]: ./postmarketOS/README_zh.md
[FreeBSD]: ./FreeBSD/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Gentoo]: ./Gentoo/README_zh.md
[Deepin]: ./Deepin/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[xv6]: ./xv6/README_zh.md
