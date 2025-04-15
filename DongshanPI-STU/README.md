---
product: DongshanPI-Nezha STU
cpu: D1 (D1-H)
cpu_core: XuanTie C906
ram: 256MB
---

# DongshanPI-Nezha STU

## Test Environment

### Operating System Information

- Tina Linux
  - Download Link: https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7
  - Reference Installation Document: https://d1.docs.aw-ol.com/study/study_1tina/
- Debian
  - Download Link: https://github.com/DongshanPI/NezhaSTU-ReleaseLinux
  - Reference Installation Document: https://github.com/DongshanPI/NezhaSTU-ReleaseLinux
- OpenWrt
  - Download Link (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=dongshan_nezha_stu
  - Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- BuildRoot
  - Download Link: https://github.com/DongshanPI/buildroot_dongshannezhastu
  - Reference Installation Document: https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/
- Arch Linux
  - Build Script: https://github.com/sehraf/d1-riscv-arch-image-builder
- postmarketOS
  - Download link (pmbootstrap): https://wiki.postmarketos.org/wiki/Pmbootstrap
  - Reference Installation Document: https://wiki.postmarketos.org/wiki/DongshanPi_NeZha_STU_(dongshanpi-nezhastu)
- FreeBSD
  - Download Link: https://github.com/freebsd-d1/freebsd-d1
  - Reference Installation Document: https://github.com/freebsd-d1/freebsd-d1
- Fedora
  - Download Link: https://mirror.iscas.ac.cn/fedora-riscv/old_dl/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
  - Reference Installation Document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html
- Gentoo
  - Download Link: https://github.com/RevySR/riscv-calculate/releases/download/v20220929/gentoo-d1-20220929153235.img.zst
  - Reference Installation Document: https://github.com/RevySR/riscv-calculate
- xv6
  - Source code link: https://github.com/michaelengel/xv6-d1
  - Reference Installation Document: https://github.com/michaelengel/xv6-d1

### Hardware Information

- DongshanPI-Nezha STU Development Board

## Test Results

| Software Category             | Package Name | Test Results (Test Report) |
| ----------------------------- | ------------ | -------------------------- |
| Tina Linux Image Boot         | N/A          | [Success][Tina]            |
| OpenWrt Image Boot            | N/A          | [Success][OpenWrt]         |
| Debian Image Boot             | N/A          | [Success][Debian]          |
| Arch Linux Image Boot         | N/A          | [CFT][Arch]                |
| BuildRoot Image Boot          | N/A          | [CFI][BuildRoot]           |
| postmarketOS Bootstrap & Boot | N/A          | [Success][pmOS]            |
| FreeBSD Image Compile & Boot  | N/A          | [Success][FreeBSD]         |
| Fedora Image Compile & Boot   | N/A          | [Failed][Fedora]           |
| Gentoo Image Compile & Boot   | N/A          | [Success][Gentoo]          |
| xv6 Compile & Boot            | N/A          | [Success][xv6]             |

[Tina]: ./TinaLinux/README.md
[OpenWrt]: ./OpenWrt/README.md
[Debian]: ./Debian/README.md
[BuildRoot]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[pmOS]: ./postmarketOS/README.md
[FreeBSD]: ./FreeBSD/README.md
[Fedora]: ./Fedora/README.md
[Gentoo]: ./Gentoo/README.md
[xv6]: ./xv6/README.md
