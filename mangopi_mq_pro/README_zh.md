# MangoPi MQ Pro

## 测试环境

### 操作系统信息

- Tina Linux
  - 下载链接：链接：https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol 提取码：awol
  - 参考安装文档：https://d1.docs.aw-ol.com/study/study_1tina/
- Armbian
  - 下载链接：https://disk.yandex.ru/d/da8qJ8wyE1hhcQ/Nezha_D1/ArmbianTV/20220722/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz
  - 参考安装文档：https://mangopi.org/mqpro
- OpenWrt
  - 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=mangopi_mq_pro
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
  - 下载链接：https://openkoji-bj.isrc.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
  - 参考安装文档：https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html
- FreeBSD
  - 下载链接：https://github.com/freebsd-d1/freebsd-d1
  - 参考安装文档：https://github.com/freebsd-d1/freebsd-d1
- openSUSE
  - 下载链接：https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz
  - 参考安装文档：https://en.opensuse.org/HCL:MangoPi_MQ-Pro
- Ubuntu
  - 下载链接：https://cdimage.ubuntu.com/releases/23.10/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz
  - 参考安装文档：https://mangopi.org/mqpro

### 硬件开发板信息

- MangoPi MQ Pro

## 测试结果

| 软件分类                       | 软件包名     | 测试结果（测试报告）        |
|----------------------------|--------------|---------------------------|
| Tina-Linux 镜像启动            | N/A          | [CFT][Tina]            |
| OpenWrt 镜像启动               | N/A          | [CFT][OpenWrt]         |
| Armbian 镜像启动               | N/A          | [CFT][Armbian]         |
| Debian 镜像启动                | N/A          | [CFT][Debian]          |
| Arch Linux 镜像启动            | N/A          | [CFT][Archlinux]       |
| Fedora 镜像启动                | N/A          | [CFT][Fedora]          |
| FreeBSD 镜像启动               | N/A          | [CFT][FreeBSD]         |
| openSUSE 镜像启动              | N/A          | [CFT][openSUSE]        |
| Ubuntu 镜像启动                | N/A          | [CFT][Ubuntu]          |

[Tina]: ./TinaLinux/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[Archlinux]: ./Archlinux/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[FreeBSD]: ./FreeBSD/README_zh.md
[openSUSE]: ./openSUSE/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md