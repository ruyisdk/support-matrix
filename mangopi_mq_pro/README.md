---
product: MangoPi MQ Pro
cpu: D1 (D1-H)
cpu_core: XuanTie C906
ram: 512MB/1G

vendor: mangopi-mq-pro
board_variant: [
    generic,
]
cpu_arch: [
    xuantie-c906,
]
---

# MangoPi MQ Pro

## Test Environment

### Operating System Information

- Tina Linux
  - Download Link: [Link](https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol) Code: awol
  - Reference Installation Document: [Tina Setup Guide](https://d1.docs.aw-ol.com/study/study_1tina/)
- Armbian
  - Download Link: [Armbian Image](https://xogium.performanceservers.nl/archive/mangopi-mq/archive/Armbian_23.8.1_Mangopi-mq_jammy_edge_6.1.0-rc3_xfce_desktop.img.xz)
  - Reference Installation Document: [MangoPi MQ Pro Installation Guide](https://mangopi.org/mqpro)
- OpenWrt
  - Download Link (OpenWrt Firmware Selector): [OpenWrt Firmware Selector](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=widora_mangopi-mq-pro)
  - Reference Installation Document: [OpenWrt Hardware Guide](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1)
- Debian
  - Download Link: [RVBoards Debian Image](https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip)
  - Reference Installation Document: [Debian Installation Guide](https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html)
- Arch Linux
  - Download Links:
      - Image Builder: [GitHub](https://github.com/sehraf/d1-riscv-arch-image-builder)
      - U-Boot: [GitHub](https://github.com/smaeul/u-boot.git)
      - RootFS: [Arch RISC-V](https://archriscv.felixc.at)
  - Reference Installation Document: [Arch Image Builder Guide](https://github.com/sehraf/d1-riscv-arch-image-builder)
- Fedora
  - Download Link: [Fedora Image](https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst)
  - Reference Installation Document: [Fedora Installation Guide](https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html)
- FreeBSD
  - Download Link: [FreeBSD D1 Repository](https://github.com/freebsd-d1/freebsd-d1)
  - Reference Installation Document: [FreeBSD D1 Guide](https://github.com/freebsd-d1/freebsd-d1)
- openSUSE
  - Download Link: [openSUSE Image](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz)
  - Reference Installation Document: [MangoPi MQ Pro HCL](https://en.opensuse.org/HCL:MangoPi_MQ-Pro)
- Ubuntu
  - Download Link: [Ubuntu Image](https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz)
  - Reference Installation Document: [MangoPi MQ Pro Installation Guide](https://mangopi.org/mqpro)
- NetBSD
  - Download Link: https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/
- Slackware
  - Download Link：http://dl.slarm64.org/slackware/images/mangopi_mq_pro/slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img.zst
  - Reference Installation Document：http://dl.slarm64.org/slackware/images/mangopi_mq_pro/
- postmarketOS
  - Download link (pmbootstrap): https://wiki.postmarketos.org/wiki/Pmbootstrap
  - Reference Installation Document: https://wiki.postmarketos.org/index.php?title=MangoPi_MQ-Pro_(mangopi-mq-pro)&direction=prev&oldid=46021
- Gentoo
  - Download Link: https://github.com/RevySR/riscv-calculate/releases/download/v20220929/gentoo-d1-20220929153235.img.zst
  - Reference Installation Document: https://github.com/RevySR/riscv-calculate
- NixOS
  - Source code link: https://github.com/chuangzhu/nixos-sun20iw1p1/releases/download/hdmi/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img.zst
  - Reference Installation Document: https://github.com/chuangzhu/nixos-sun20iw1p1/
- irradium
  - Download Link: https://dl.irradium.org/irradium/images/visionfive_2/
  - Reference Installation Document: https://dl.irradium.org/irradium/images/visionfive_2/README.TXT
- Deepin 23 beige 20221209
  - Download Link: https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-d1-20221208175445.img.zst.0
  - Reference Installation Document: https://github.com/deepin-community/deepin-riscv-board/
- xv6
  - Source code link: https://github.com/michaelengel/xv6-d1
  - Reference Installation Document: https://github.com/michaelengel/xv6-d1

### Hardware Information

- MangoPi MQ Pro (Allwinner D1/D1-H)

## Test Results

| Software Category               | Package Name | Test Result (Test Report) |
| ------------------------------- | ------------ | ------------------------- |
| Tina-Linux Image Boot           | N/A          | [CFT][Tina]               |
| OpenWrt Image Boot              | N/A          | [Success][OpenWrt]        |
| Armbian Image Boot              | N/A          | [Failed][Armbian]         |
| Debian Image Boot               | N/A          | [Success][Debian]         |
| Arch Linux Image Compile & Boot | N/A          | [Success][Archlinux]      |
| Fedora Image Boot               | N/A          | [Success][Fedora]         |
| FreeBSD Image Boot              | N/A          | [Success][FreeBSD]        |
| openSUSE Image Boot             | N/A          | [Success][openSUSE]       |
| Ubuntu Image Boot               | N/A          | [Success][Ubuntu]         |
| NetBSD Image Boot               | N/A          | [CFT][NetBSD]             |
| Slackware Image Boot            | N/A          | [Success][Slackware]      |
| postmarketOS Bootstrap & Boot   | N/A          | [Success][pmOS]           |
| Gentoo Image Boot               | N/A          | [Success][Gentoo]         |
| NixOS Image Boot                | N/A          | [Success][NixOS]          |
| irradium Image Boot             | N/A          | [Success][irradium]       |
| Deepin Image Boot               | N/A          | [Success][Deepin]         |
| xv6 Build & Boot                | N/A          | [Success][xv6]            |

[Tina]: ./TinaLinux/README.md
[OpenWrt]: ./OpenWrt/README.md
[Debian]: ./Debian/README.md
[Armbian]: ./Armbian/README.md
[Archlinux]: ./Archlinux/README.md
[Fedora]: ./Fedora/README.md
[FreeBSD]: ./FreeBSD/README.md
[openSUSE]: ./openSUSE/README.md
[Ubuntu]: ./Ubuntu/README.md
[NetBSD]: ./NetBSD/README.md
[Slackware]: ./Slackware/README.md
[pmOS]: ./postmarketOS/README.md
[Gentoo]: ./Gentoo/README.md
[NixOS]: ./NixOS/README.md
[irradium]: ./irradium/README.md
[Deepin]: ./Deepin/README.md
[xv6]: ./xv6/README.md
