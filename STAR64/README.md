---
product: Star64
cpu: JH7110
cpu_core: SiFive U74 + SiFive S7 + SiFive E24
ram: 4G/8G

vendor: pine64-star64
board_variant: [
    generic,
]
cpu_arch: [
    sifive-u74,
    sifive-s7,
    sifive-e24,
]
---

# Pine64 Star64

## Test Environment

### Operating System Information

**Note: Star64 could theoretically use all Visionfive2 images, but USB, WiFi, and PCI might not work (see [Bringup Notes](https://wiki.pine64.org/wiki/STAR64))**

- NuttX
    - Source Link: https://github.com/apache/nuttx
    - Reference Installation Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
    - Toolchain:
        - Boot Image: https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
        - DTB: https://github.com/starfive-tech/VisionFive2/releases
        - Toolchain: https://github.com/sifive/freedom-tools/releases
        - kflash: https://github.com/kendryte/kflash.py
- Armbian
    - Download Link: https://www.armbian.com/star64/
    - Reference Installation Document: https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429
- Yocto
    - Download Link: https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
    - Reference Installation Document: https://github.com/Fishwaldo/meta-pine64
- Ubuntu 25.04:
    - Download Link: https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
    - Reference Installation Document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/
- Arch Linux
    - Source code Link: https://github.com/yogo1212/arch-linux-star64
    - Reference Installation Document: https://github.com/yogo1212/arch-linux-star64
- NixOS
    - Source code link: https://git.sr.ht/~fgaz/nixos-star64
    - Reference Installation Document: https://git.sr.ht/~fgaz/nixos-star64
- irradium
    - Download Link: https://dl.irradium.org/irradium/images/star64/irradium-3.8-riscv64-xfce-star64-6.12.33-build-20250613.img.zst
    - Reference Installation Document: https://dl.irradium.org/irradium/images/star64/
- DietPi
    - Download Link: https://dietpi.com/downloads/images/DietPi_Star64-RISC-V-Trixie.img.xz
    - Reference Installation Document: https://dietpi.com/blog/?p=2629
- NetBSD
    - Download Link: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)
- Deepin
    - Download Link: https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img.zst.0
    - Reference Installation Document: https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt

### Hardware Information

- Pine64 Star64

## Test Results

| Software Category             | Package Name | Test Result (Test Report) |
| ----------------------------- | ------------ | ------------------------- |
| NuttX Image Build & Boot      | N/A          | [Basic][NuttX]            |
| Armbian Image Boot            | N/A          | [CFH][Armbian]            |
| Yocto Image Boot              | N/A          | [Basic][Yocto]            |
| Ubuntu Image Boot             | N/A          | [Basic][Ubuntu]           |
| Arch Linux Image Build & Boot | N/A          | [CFH][ArchLinux]          |
| NixOS Image Build & Boot      | N/A          | [CFH][NixOS]              |
| Deepin Image Boot             | N/A          | [Basic][Deepin]           |
| DietPi Image Boot             | N/A          | [Basic][DietPi]           |
| irradium Image Boot           | N/A          | [Basic][irradium]         |
| NetBSD Image Boot             | N/A          | [Basic][NetBSD]           |

[NuttX]: ./NuttX/README.md
[NixOS]: ./NixOS/README.md
[Armbian]: ./Armbian/README.md
[Yocto]: ./Yocto/README.md
[Ubuntu]: ./Ubuntu/README.md
[ArchLinux]: ./ArchLinux/README.md
[Deepin]: ./Deepin/README.md
[DietPi]: ./DietPi/README.md
[irradium]: ./irradium/README.md
[NetBSD]: ./NetBSD/README.md
