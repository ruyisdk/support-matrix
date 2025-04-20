---
vendor: milkv_mars
product: Milk-V Mars
cpu: JH7110
cpu_core: SiFive U74 + SiFive S7 + SiFive E24
ram: 1G/2G/4G/8G
---

# Milk-V Mars

## Test Environment

### Operating System Information

- BuildRoot/Debian (officially provided)
  - Download Link: <https://github.com/milkv-mars/mars-buildroot-sdk/releases/>
  - Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>
- Ubuntu 24.10
  - Download Link: <https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+milkvmars.img.xz>
- Ubuntu 24.04.2 LTS
  - Download Link: <https://cdimage.ubuntu.com/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64+milkvmars.img.xz>
  - Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>
- Deepin 25 preview
  - Download Link: <https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-jh7110-20250122-110620.tar.xz>
  - Reference Installation Document:
    1. <https://milkv.io/zh/docs/mars/getting-started/boot>
    2. <https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/jh7110>
- eweOS 6.13.8
  - Download Link: <https://github.com/panglars/eweos-vf2-mainline>
  - Reference Installation Document: <https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md>
  - eweOS Website: <https://os.ewe.moe/>
- Fedora 41
  - Download Link: <https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz>
  - Reference Installation Document:
    1. <https://milkv.io/zh/docs/mars/getting-started/boot>
    2. <https://images.fedoravforce.org/Mars>
- NixOS 25.05
  - Download Link: <https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst>
  - Reference Installation Document:
    - <https://milkv.io/zh/docs/mars/getting-started/boot>
    - <https://github.com/NickCao/nixos-riscv>

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

[Debian]: ./Debian/README.md
[BuildRoot]: ./BuildRoot/README.md
[Ubuntu]: ./Ubuntu/README.md
[Ubuntu LTS]: ./Ubuntu/README_LTS.md
[Deepin]: ./Deepin/README.md
[eweOS]: ./eweOS/README.md
[Fedora]: ./Fedora/README.md
[Guix]: ./Guix/README.md
[NixOS]: ./NixOS/README.md
