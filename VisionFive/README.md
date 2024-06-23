# StarFive VisionFive

## Test Environment

### Operating System Information

- Fedora
    - Download Link: https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst
    - Reference Installation Document: https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf
- openEuler
    - Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/
    - Reference Installation Document: https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive
    - Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/
    - Reference Installation Document: https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive
- Ubuntu
    - Download Link: https://ubuntu.com/download/risc-v
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive
- openKylin
    - Download Link: https://www.openkylin.top/downloads/old_releases.html
    - Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- openSUSE
    - Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/
    - Reference Installation Document: https://en.opensuse.org/HCL:VisionFive
- Armbian
    - Download Link: https://www.armbian.com/vision-five/
    - Reference Installation Document: https://docs.armbian.com/User-Guide_Getting-Started/
- OpenWRT
    - Download Link: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1
    - Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive
- OpenBSD
    - Download Link: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
    - Reference Installation Document: https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Buildroot
    - Source Code Link: https://buildroot.org/download.html
    - Reference Installation Document: https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads

### Hardware Information

- StarFive VisionFive

## Test Results

| Software Category              | Package Name | Test Result (Test Report)               |
| ------------------------------ | ------------ | --------------------------------------- |
| openEuler/Base Image Boot      | N/A          | [Successful][oERVBase]                  |
| openEuler/Xfce Image Boot      | N/A          | [Successful][oERVXfce]                  |
| Fedora Image Boot              | N/A          | [Successful][Fedora] (official support) |
| Ubuntu Image Boot              | N/A          | [Successful][Ubuntu]                    |
| openKylin Image Boot           | N/A          | [Successful][oK] (official support)     |
| openSUSE Image Boot            | N/A          | [Successful][openSUSE]                  |
| Armbian Image Boot             | N/A          | [Successful][Armbian]                   |
| OpenWRT Image Boot             | N/A          | [Successful][OpenWRT]                   |
| OpenBSD Image Boot             | N/A          | [Successful][OpenBSD]                   |
| Buildroot Image Build and Boot | N/A          | [Successful][Buildroot]                 |

[oERVBase]: ./openEuler/README.md
[oERVXfce]: ./openEuler/README.md
[Fedora]: ./Fedora/README.md
[Ubuntu]: ./Ubuntu/README.md
[oK]: ./openKylin/README.md
[openSUSE]: ./openSUSE/README.md
[Armbian]: ./Armbian/README.md
[OpenWRT]: ./OpenWRT/README.md
[OpenBSD]: ./OpenBSD/README.md
[Buildroot]: ./BuildRoot/README.md
