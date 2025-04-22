# MangoPi MQ Pro

## 测试环境

### 操作系统信息

- Tina Linux
  - 下载链接：链接：https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol 提取码：awol
  - 参考安装文档：https://d1.docs.aw-ol.com/study/study_1tina/
- Armbian
  - 下载链接：https://xogium.performanceservers.nl/archive/mangopi-mq/archive/Armbian_23.8.1_Mangopi-mq_jammy_edge_6.1.0-rc3_xfce_desktop.img.xz
  - 参考安装文档：https://mangopi.org/mqpro
- OpenWrt
  - 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=widora_mangopi-mq-pro
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- Debian
  - 下载链接：https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
  - 参考安装文档：https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html
- Arch Linux
  - 下载链接：
      - Image Builder: https://github.com/sehraf/d1-riscv-arch-image-builder
      - U-Boot: https://github.com/smaeul/u-boot.git
      - RootFS: https://archriscv.felixc.at
  - 参考安装文档：https://github.com/sehraf/d1-riscv-arch-image-builder
- Fedora
  - 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
  - 参考安装文档：https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html
- FreeBSD
  - 下载链接：https://github.com/freebsd-d1/freebsd-d1
  - 参考安装文档：https://github.com/freebsd-d1/freebsd-d1
- openSUSE
  - 下载链接：https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz
  - 参考安装文档：https://en.opensuse.org/HCL:MangoPi_MQ-Pro
- Ubuntu
  - 下载链接：https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz
  - 参考安装文档：https://mangopi.org/mqpro
- NetBSD
  - 下载链接：https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/
- Slackware
  - 下载链接：http://dl.slarm64.org/slackware/images/mangopi_mq_pro/slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img.zst
  - 参考安装文档：http://dl.slarm64.org/slackware/images/mangopi_mq_pro/
- postmarketOS
  - 下载链接（pmbootstrap）: https://wiki.postmarketos.org/wiki/Pmbootstrap
  - 参考安装文档：https://wiki.postmarketos.org/index.php?title=MangoPi_MQ-Pro_(mangopi-mq-pro)&direction=prev&oldid=46021
- Gentoo
  - 下载链接：https://github.com/RevySR/riscv-calculate/releases/download/v20220929/gentoo-d1-20220929153235.img.zst
  - 参考安装文档：https://github.com/RevySR/riscv-calculate
- NixOS
  - 下载链接: https://github.com/chuangzhu/nixos-sun20iw1p1/releases/download/hdmi/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img.zst
  - 参考安装文档: https://github.com/chuangzhu/nixos-sun20iw1p1
- irradium 3.7
  - 下载链接：https://dl.irradium.org/irradium/images/mangopi_mq_pro/
  - 参考安装文档：https://dl.irradium.org/irradium/images/mangopi_mq_pro/README.TXT
- Deepin 23 beige 20221209
  - 下载链接：https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-d1-20221208175445.img.zst.0
  - 参考安装文档：https://github.com/deepin-community/deepin-riscv-board/
### 硬件开发板信息

- MangoPi MQ Pro (Allwinner D1/D1-H)

## 测试结果

| 软件分类                  | 软件包名 | 测试结果（测试报告） |
| ------------------------- | -------- | -------------------- |
| Tina-Linux 镜像启动       | N/A      | [CFT][Tina]          |
| OpenWrt 镜像启动          | N/A      | [成功][OpenWrt]      |
| Armbian 镜像启动          | N/A      | [失败][Armbian]      |
| Debian 镜像启动           | N/A      | [成功][Debian]       |
| Arch Linux 镜像编译和启动 | N/A      | [成功][Archlinux]    |
| Fedora 镜像启动           | N/A      | [成功][Fedora]       |
| FreeBSD 镜像编译和启动    | N/A      | [成功][FreeBSD]      |
| openSUSE 镜像启动         | N/A      | [成功][openSUSE]     |
| Ubuntu 镜像启动           | N/A      | [成功][Ubuntu]       |
| NetBSD 镜像启动           | N/A      | [CFT][NetBSD]        |
| Slackware 镜像启动        | N/A      | [成功][Slackware]    |
| postmarketOS 编译和启动   | N/A      | [成功][pmOS]         |
| Gentoo 镜像启动           | N/A      | [成功][Gentoo]       |
| NixOS 镜像启动            | N/A      | [成功][NixOS]        |
| irradium 镜像启动         | N/A      | [成功][irradium]     |
| Deepin 镜像启动           | N/A      | [成功][Deepin]       |

[Tina]: ./TinaLinux/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[Archlinux]: ./Archlinux/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[FreeBSD]: ./FreeBSD/README_zh.md
[openSUSE]: ./openSUSE/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[NetBSD]: ./NetBSD/README_zh.md
[Slackware]: ./Slackware/README_zh.md
[pmOS]: ./postmarketOS/README_zh.md
[Gentoo]: ./Gentoo/README_zh.md
[NixOS]: ./NixOS/README_zh.md
[irradium]: ./irradium/README_zh.md
[Deepin]: ./Deepin/README_zh.md
