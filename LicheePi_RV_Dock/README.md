---
product: LicheePi RV Dock
cpu: D1 (D1-H)
cpu_core: XuanTie C906
---

# LicheePi RV Dock

## Test Environment

### Operating System Information

- openEuler RISC-V 23.03 Preview
  - Download link: [ISCAS Mirror][oERVDL]
    - Options available for images with Xfce desktop or command-line only Base images
  - Reference Installation Document: [openEuler/RISC-V][oERVXfce]
- Tina Linux
  - Download links: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
  - Reference Installation Document: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Ubuntu
  - 24.10 Download link: https://ubuntu.com/download/risc-v
  - 24.04.1 LTS Download link: https://ubuntu.com/download/risc-v
  - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/LicheeRV
- OpenWrt 23.05.2
  - Download links (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
  - Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- Debian
  - Download link: https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA
  - Reference Installation Document: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Arch Linux
  - Base Image: Ubuntu 24.10: [ubuntu-24.10](https://ubuntu.com/download/risc-v)
    - Or any arbitrary image for D1
    - Rootfs：[archriscv-2024-09-22.tar.zst](https://archriscv.felixc.at/images/archriscv-2024-09-22.tar.zst)
    - Reference Installation Document: https://github.com/felixonmars/archriscv-packages/wiki/RV64-%E6%9D%BF%E5%AD%90%E6%9B%B4%E6%8D%A2-rootfs-%E6%8C%87%E5%8D%97
- openSUSE Tumbleweed
  - Download link: [https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/)
  - Reference Installation Document: [https://en.opensuse.org/HCL:Nezha](https://en.opensuse.org/HCL:Nezha)
- NixOS
  - Download link: https://github.com/chuangzhu/nixos-sun20iw1p1/releases
  - Reference Installation Document: https://github.com/chuangzhu/nixos-sun20iw1p1

### Hardware Information

- Sipeed LicheePi RV Dock

## Test Results

| Software Category         | Package Name | Test Result (Test Report)                  |
|---------------------------|--------------|--------------------------------------------|
| openEuler/Base Image Boot | N/A          | [Successful][oERV]                         |
| openEuler/Xfce Image Boot | Xfce Desktop | [Successful][oERV]                         |
| Tina-Linux Image Boot     | N/A          | [Successful][TinaNezha] (Official Support) |
| Ubuntu Image Boot         | N/A          | [CFT][Ubuntu] (Official Support)           |
| Ubuntu LTS Image Boot     | N/A          | [CFT][Ubuntu LTS] (Official Support)       |
| OpenWrt Image Boot        | N/A          | [Successful][OpenWrt] (Official Support)   |
| Debian Image Boot         | N/A          | [Successful][Debian]                       |
| openSUSE Image Boot       | N/A          | [Successful][openSUSE]                     |
| Arch Linux Image Boot     | N/A          | [Successful][Arch]                         |
| NixOS Image Boot          | N/A          | [Successful][NixOS]                        |

[oERVDL]: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
[oERV]: ./openEuler/README.md
[TinaNezha]: ./TinaLinux/README.md
[Ubuntu]: ./Ubuntu/README.md
[Ubuntu LTS]: ./Ubuntu/README_LTS.md
[OpenWrt]: ./OpenWrt/README.md
[Debian]: ./Debian/README.md
[openSUSE]: ./openSUSE/README.md
[Arch]: ./ArchLinux/README.md
[NixOS]: ./NixOS/README.md
