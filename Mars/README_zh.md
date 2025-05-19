# Milk-V Mars

## 测试环境

### 操作系统信息

- BuildRoot/Debian（官方提供）
  - 下载链接：<https://github.com/milkv-mars/mars-buildroot-sdk/releases/>
  - 参考安装文档：<https://milkv.io/zh/docs/mars/getting-started/boot>
- Ubuntu 25.04
  - 下载链接：<https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/milk-v-mars/>
- Ubuntu 24.04.2 LTS
  - 下载链接：<https://cdimage.ubuntu.com/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64+milkvmars.img.xz>
  - 参考安装文档：<https://milkv.io/zh/docs/mars/getting-started/boot>
- Deepin 25 preview
  - 下载链接：<https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-jh7110-20250122-110620.tar.xz>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/jh7110>
- eweOS 6.13.8
  - 下载链接：<https://github.com/panglars/eweos-vf2-mainline>
  - 参考安装文档：<https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md>
  - eweOS官网：<https://os.ewe.moe/>
- Fedora 41
  - 下载链接：<https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://images.fedoravforce.org/Mars>
- Guix (Build ID: 9893288)
  - 下载链接：<https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image>
  - 参考安装文档：<https://milkv.iso/zh/docs/mars/getting-started/boot>
- NixOS 25.05
  - 下载链接：<https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://github.com/NickCao/nixos-riscv>
- OpenWRT 24.10.1
  - 下载链接：<https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>
    - <https://firmware-selector.openwrt.org/?version=24.10.1&target=starfive%2Fgeneric&id=visionfive2-v1.3b>
- NuttX 12.9.0
  - 下载链接：
    - <https://nuttx.apache.org/download/>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html>
- ArchLinux (VF2_6.12_v5.14.0-cwt24)
  - 下载链接：<https://github.com/cwt-vf2/archlinux-image-vf2/releases/download/cwt24/ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst>
  - 参考安装文档：
    - <https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459>
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>
- Alpine Linux 3.20.0_alpha20231219 (edge)
  - 下载链接：<https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz>
  - 参考安装文档：
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://arvanta.net/alpine/alpine-on-visionfive>

### 硬件开发板信息

- Milk-V Mars

## 测试结果

| 软件分类             | 软件包名 | 测试结果（测试报告）               |
| -------------------- | -------- | ------------------------------- |
| Debian 镜像启动      | N/A      | [成功][Debian]（Milk-V 厂商镜像） |
| BuildRoot 构建及启动 | N/A      | [成功][BuildRoot]                |
| Ubuntu 镜像启动      | N/A      | [成功][Ubuntu]                   |
| Ubuntu LTS 镜像启动  | N/A      | [成功][Ubuntu LTS]               |
| Deepin 镜像启动      | N/A      | [成功][Deepin]                   |
| eweOS 镜像启动       | N/A      | [成功][eweOS]                    |
| Fedora 镜像启动      | N/A      | [成功][Fedora]                   |
| Guix 镜像启动        | N/A      | [成功][Guix]                     |
| NixOS 镜像启动       | N/A      | [成功][NixOS]                    |
| OpenWRT 镜像启动     | N/A      | [成功][OpenWRT]                  |
| NuttX 构建及启动     | N/A      | [成功][NuttX]                    |
| ArchLinux 镜像启动   | N/A      | [成功][ArchLinux]                |
| Alpine 镜像启动      | N/A      | [成功][Alpine]                   |

[Debian]: ./Debian/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu LTS]: ./Ubuntu/README_LTS_zh.md
[Deepin]: ./Deepin/README_zh.md
[eweOS]: ./eweOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Guix]: ./Guix/README_zh.md
[NixOS]: ./NixOS/README_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md
[NuttX]: ./NuttX/README_zh.md
[ArchLinux]: ./ArchLinux/README_zh.md
[Alpine]: ./Alpine/README_zh.md
