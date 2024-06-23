# MangoPi MQ Pro

## Test Environment

### Operating System Information

- Tina Linux
  - Download Link: [Link](https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol) Code: awol
  - Reference Installation Document: [Tina Setup Guide](https://d1.docs.aw-ol.com/study/study_1tina/)
- Armbian
  - Download Link: [ArmbianTV Image](https://disk.yandex.ru/d/da8qJ8wyE1hhcQ/Nezha_D1/ArmbianTV/20220722/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz)
  - Reference Installation Document: [MangoPi MQ Pro Installation Guide](https://mangopi.org/mqpro)
- OpenWrt
  - Download Link (OpenWrt Firmware Selector): [Link](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=mangopi_mq_pro)
  - Reference Installation Document: [OpenWrt Hardware Guide](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1)
- Debian
  - Download Link: [Debian Image](https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip)
  - Reference Installation Document: [Debian Installation Guide](https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html)
- Arch Linux
  - Download Links:
      - Image Builder: [GitHub](https://github.com/sehraf/d1-riscv-arch-image-builder)
      - U-Boot: [GitHub](https://github.com/smaeul/u-boot.git)
      - RootFS: [Arch RISC-V](https://archriscv.felixc.at)
  - Reference Installation Document: [Arch Image Builder Guide](https://github.com/sehraf/d1-riscv-arch-image-builder)
- Fedora
  - Download Link: [Fedora Image](https://openkoji-bj.isrc.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst)
  - Reference Installation Document: [Fedora Installation Guide](https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html)
- FreeBSD
  - Download Link: [FreeBSD D1 Repository](https://github.com/freebsd-d1/freebsd-d1)
  - Reference Installation Document: [FreeBSD D1 Guide](https://github.com/freebsd-d1/freebsd-d1)
- openSUSE
  - Download Link: [openSUSE Image](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz)
  - Reference Installation Document: [MangoPi MQ Pro HCL](https://en.opensuse.org/HCL:MangoPi_MQ-Pro)
- Ubuntu
  - Download Link: [Ubuntu Image](https://cdimage.ubuntu.com/releases/23.10/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz)
  - Reference Installation Document: [MangoPi MQ Pro Installation Guide](https://mangopi.org/mqpro)

### Hardware Information

- MangoPi MQ Pro

## Test Results

| Software Category            | Package Name | Test Result (Test Report)   |
|----------------------------|--------------|---------------------------|
| Tina-Linux Image Boot       | N/A          | [CFT][Tina]           |
| OpenWrt Image Boot          | N/A          | [CFT][OpenWrt]        |
| Armbian Image Boot          | N/A          | [CFT][Armbian]        |
| Debian Image Boot           | N/A          | [CFT][Debian]         |
| Arch Linux Image Boot       | N/A          | [CFT][Archlinux]      |
| Fedora Image Boot           | N/A          | [CFT][Fedora]         |
| FreeBSD Image Boot          | N/A          | [CFT][FreeBSD]        |
| openSUSE Image Boot         | N/A          | [CFT][openSUSE]       |
| Ubuntu Image Boot           | N/A          | [CFT][Ubuntu]         |

[Tina]: ./TinaLinux/README.md
[OpenWrt]: ./OpenWrt/README.md
[Debian]: ./Debian/README.md
[Armbian]: ./Armbian/README.md
[Archlinux]: ./Archlinux/README.md
[Fedora]: ./Fedora/README.md
[FreeBSD]: ./FreeBSD/README.md
[openSUSE]: ./openSUSE/README.md
[Ubuntu]: ./Ubuntu/README.md
