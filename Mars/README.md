---
product: Milk-V Mars
cpu: JH7110
cpu_core: SiFive U74 + SiFive S7 + SiFive E24
ram: 1G/2G/4G/8G

vendor: milkv-mars
---

# Milk-V Mars

## Test Environment

### Operating System Information

- BuildRoot/Debian (officially provided)
  - Download Link: <https://github.com/milkv-mars/mars-buildroot-sdk/releases/>
  - Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>
- Ubuntu 25.04
  - Download Link: <https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/milk-v-mars/>
- Ubuntu 24.04.2 LTS
  - Download Link: <https://cdimage.ubuntu.com/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64+milkvmars.img.xz>
  - Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>
- Deepin 25 preview
  - Download Link: <https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-jh7110-20250122-110620.tar.xz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/jh7110>
- eweOS 6.13.8
  - Download Link: <https://github.com/panglars/eweos-vf2-mainline>
  - Reference Installation Document: <https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md>
  - eweOS Website: <https://os.ewe.moe/>
- Fedora 41
  - Download Link: <https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://images.fedoravforce.org/Mars>
- Guix (Build ID: 9893288)
  - Download Link: <https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image>
  - Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>
- NixOS 25.05
  - Download Link: <https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://github.com/NickCao/nixos-riscv>
- OpenWRT 24.10.1
  - Download Link: <https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>
    - <https://firmware-selector.openwrt.org/?version=24.10.1&target=starfive%2Fgeneric&id=visionfive2-v1.3b>
- NuttX 12.9.0
  - Download Link:
    - <https://nuttx.apache.org/download/>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html>
- ArchLinux (VF2_6.12_v5.14.0-cwt24)
  - Download Link: <https://github.com/cwt-vf2/archlinux-image-vf2/releases/download/cwt24/ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst>
  - Reference Installation Document:
    - <https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459>
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>
- Alpine Linux 3.20.0_alpha20231219 (edge)
  - Download Link: <https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://arvanta.net/alpine/alpine-on-visionfive>
- Armbian 25.8.0 (Armbian_community 25.8.0-trunk.38 noble)
  - Download Link: <https://www.armbian.com/visionfive2>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://www.armbian.com/visionfive2>
- DietPi v9.12.1
  - Download Link: <https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Trixie.img.xz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://dietpi.com/blog/?p=2629>
- irradium 3.8
  - Download Link: <https://mirror.serverion.com/irradium/images/visionfive_2/irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img.zst>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://mirror.serverion.com/irradium/images/visionfive_2/README.TXT>
- openKylin 2.0 SP1
  - Download Link: <https://www.openkylin.top/downloads/>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8VisionFive2%E4%B8%8A%E5%AE%89%E8%A3%85openKylin>
- openSUSE Tumbleweed 20250527
  - Download Link: <https://downloadcontent.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw.xz>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://en.opensuse.org/HCL:VisionFive2>

### Hardware Information

- Milk-V Mars

## Test Results

| Software Category      | Package Name | Test Result (Test Report)                    |
| ---------------------- | ------------ | -------------------------------------------- |
| Debian Image Boot      | N/A          | [Successful][Debian] (Milk-V Official Image) |
| BuildRoot Build & Boot | N/A          | [Successful][BuildRoot]                      |
| Ubuntu Image Boot      | N/A          | [Successful][Ubuntu]                         |
| Ubuntu LTS Image Boot  | N/A          | [Successful][Ubuntu LTS]                     |
| Deepin Image Boot      | N/A          | [Successful][Deepin]                         |
| eweOS Image Boot       | N/A          | [Successful][eweOS]                          |
| Fedora Image Boot      | N/A          | [Successful][Fedora]                         |
| Guix Image Boot        | N/A          | [Successful][Guix]                           |
| NixOS Image Boot       | N/A          | [Successful][NixOS]                          |
| OpenWRT Image Boot     | N/A          | [Successful][OpenWRT]                        |
| NuttX Build & Boot     | N/A          | [Successful][NuttX]                          |
| ArchLinux Image Boot   | N/A          | [Successful][ArchLinux]                      |
| Alpine Image Boot      | N/A          | [Successful][Alpine]                         |
| Armbian Image Boot     | N/A          | [Successful][Armbian]                        |
| DietPi Image Boot      | N/A          | [Successful][DietPi]                         |
| irradium Image Boot    | N/A          | [Successful][irradium]                       |
| openKylin Image Boot   | N/A          | [Successful][openKylin]                      |
| openSUSE Image Boot    | N/A          | [Successful][openSUSE]                       |

[Debian]: ./Debian/README.md
[BuildRoot]: ./BuildRoot/README.md
[Ubuntu]: ./Ubuntu/README.md
[Ubuntu LTS]: ./Ubuntu/README_LTS.md
[Deepin]: ./Deepin/README.md
[eweOS]: ./eweOS/README.md
[Fedora]: ./Fedora/README.md
[Guix]: ./Guix/README.md
[NixOS]: ./NixOS/README.md
[OpenWRT]: ./OpenWRT/README.md
[NuttX]: ./NuttX/README.md
[ArchLinux]: ./ArchLinux/README.md
[Alpine]: ./Alpine/README.md
[Armbian]: ./Armbian/README.md
[DietPi]: ./DietPi/README.md
[irradium]: ./irradium/README.md
[openKylin]: ./openKylin/README.md
[openSUSE]: ./openSUSE/README.md
