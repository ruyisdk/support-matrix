# StarFive VisionFive 2

## Test Environment

### Operating System Information

- openEuler RISC-V 23.09 Preview
    - Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive2/
    - Reference Installation Document: https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md
- Debian (officially provided)
    - Download Link: https://debian.starfivetech.com/
- openKylin
    - Download Link: https://www.openkylin.top/downloads
    - Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Ubuntu 23.10
    - Download Link: https://cdimage.ubuntu.com/releases/23.10/release/
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202
- BuildRoot (VisionFive 2 SDK)
    - Download Link: https://github.com/starfive-tech/VisionFive2/releases
    - Reference Installation Document: https://github.com/starfive-tech/VisionFive2
- Arch Linux
    - Download Link: https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt21.1
    - Reference Installation Document: https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459
- Gentoo
    - Download Link: https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing
    - Reference Installation Document: https://forum.rvspace.org/t/experimental-gentoo-image/1807
- openSUSE
    - Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/
    - Reference Installation Document: https://en.opensuse.org/HCL:VisionFive2
- OpenBSD
  - Download Link: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
  - Reference Installation Document: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Armbian Noble Minimal & Armbian Jammy Xfce
    - Download Link: https://www.armbian.com/visionfive2/
    - Reference Installation Document: https://www.armbian.com/visionfive2/
- OpenWrt SNAPSHOT
    - Download Link: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b
    - Reference Installation Document: https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html
- RT-Thread
    - Source Code Link: https://github.com/starfive-tech/VisionFive2
    - Reference Installation Document: https://doc.rvspace.org/VisionFive2/Application_Notes/RT-Thread/index.html
- Zephyr
    - Reference Installation Document: https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html

### Hardware Information

- StarFive VisionFive 2

## Test Results

| Software Category       | Software Package | Test Results (Test Report)             |
|-------------------------|------------------|----------------------------------------|
| openEuler/Base Image    | N/A              | [Successful][oERV]                         |
| openEuler/Xfce Image    | Xfce             | [Successful][oERV]                         |
| Debian Image            | N/A              | [Successful][Debian] (Official StarFive Image)   |
| openKylin Image         | N/A              | [Successful][oK] (Official Support)         |
| Ubuntu Image            | N/A              | [Successful][Ubuntu] (Official Support)     |
| BuildRoot Image         | N/A              | [Successful][BuildRoot] (Official StarFive Image) |
| Arch Linux Image        | N/A              | [Successful][Arch]                         |
| Gentoo Image            | N/A              | [Successful][Gentoo]                       |
| openSUSE Image          | N/A              | [Successful][SUSE] (Official Support)       |
| OpenBSD Image           | N/A              | [Successful][OpenBSD]                      |
| Armbian/Minimal Image   | N/A              | [Successful][Armbian]                      |
| Armbian/Xfce Image      | Xfce             | [Successful][Armbian]                      |
| OpenWrt Image           | N/A              | [Successful][OpenWrt]                      |
| RT-Thread Image         | N/A              | [Successful][RT-Thread] (Official Support)  |
| Zephyr Image            | N/A              | [Failure][Zephyr]                       |
| NuttX Image             | N/A              | [Successful][NuttX]                        |

[oERV]: ./openEuler/README.md
[Debian]: ./Debian/README.md
[oK]: ./openKylin/README.md
[Ubuntu]: ./Ubuntu/README.md
[BuildRoot]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[Gentoo]: ./Gentoo/README.md
[openSUSE]: ./openSUSE/README.md
[OpenBSD]: ./OpenBSD/README.md
[Armbian]: ./Armbian/README.md
[OpenWrt]: ./OpenWRT/README.md
[RT-Thread]: ./RT-Thread/README.md
[Zephyr]: ./Zephyr/README.md
[NuttX]: ./NuttX/README.md
