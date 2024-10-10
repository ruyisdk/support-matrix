---
product: LicheeRV/AWOL Nezha
cpu: D1 (D1-H)
cpu_core: XuanTie C906
---

# LicheeRV / AWOL Nezha D1

## Test Environment

### Operating System Information

- openEuler RISC-V 23.03 Preview
  - Download link: [ISCAS Mirror][oERVDL]
    - Options available for images with Xfce desktop or command-line only Base images
  - Reference Installation Document: [openEuler/RISC-V][oERVXfce]
- Tina Linux
  - Download links:
    - Nezha D1: https://d1.docs.aw-ol.com/source/3_getimg/
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
  - Reference Installation Document:
    - Nezha D1: https://d1.docs.aw-ol.com/study/study_1tina/
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Ubuntu
  - Download link: https://ubuntu.com/download/risc-v
    - Mirror: [Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Blicheerv.img.xz)
  - Reference Installation Document:
    - Nezha D1: https://wiki.ubuntu.com/RISC-V/Nezha%20D1
    - Sipeed Lichee RV Dock: https://wiki.ubuntu.com/RISC-V/LicheeRV
- OpenWrt 23.05.2
  - Download links (OpenWrt Firmware Selector):
    - Nezha D1: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=nezha
    - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
  - Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- Debian
  - Download link: http://www.perfxlab.cn:8080/rvboards/
  - Reference Installation Document: https://d1.docs.aw-ol.com/strong/strong_4debian/#v041
- Fedora 36
  - Download link: https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/
  - Reference Installation Document: https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn
- Arch Linux
  - Base Image: Ubuntu 24.10 Beta: [ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz) 
    - Or any arbitrary image for D1
  - Rootfs: [archriscv-20220727.tar.zst](https://archriscv.felixc.at/images/archriscv-20220727.tar.zst)
  - Reference Installation Document: https://github.com/felixonmars/archriscv-packages/wiki/RV64-%E6%9D%BF%E5%AD%90%E6%9B%B4%E6%8D%A2-rootfs-%E6%8C%87%E5%8D%97
- openSUSE Tumbleweed
  - Download link: [https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/)
  - Reference Installation Document: [https://en.opensuse.org/HCL:Nezha](https://en.opensuse.org/HCL:Nezha)

### Hardware Information

- Sipeed Lichee RV Dock
- AWOL Nezha D1

## Test Results

| Software Category                | Package Name | Test Result (Test Report)                  |
| -------------------------------- | ------------ | ------------------------------------------ |
| openEuler/Base Image Boot        | N/A          | [Successful][oERV]                         |
| openEuler/Xfce Image Boot        | Xfce Desktop | [Successful][oERV]                         |
| Tina-Linux Image Boot - Nezha D1 | N/A          | [Successful][TinaNezha] (Official Support) |
| Ubuntu Image Boot                | N/A          | [Successful][Ubuntu] (Official Support)    |
| OpenWrt Image Boot               | N/A          | [Successful][OpenWrt] (Official Support)   |
| Debian Image Boot                | N/A          | [Successful][Debian]                       |
| Fedora Image Boot                | N/A          | [Successful][Fedora]                       |
| openSUSE Image Boot              | N/A          | [Successful][openSUSE]                     |
| Arch Linux Image Boot            | N/A          | [Successful][Arch]                         |

[oERVDL]: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
[oERV]: ./openEuler/README.md
[TinaNezha]: ./TinaLinux/README.md
[Ubuntu]: ./Ubuntu/README.md
[OpenWrt]: ./OpenWrt/README.md
[Debian]: ./Debian/README.md
[Fedora]: ./Fedora/README.md
[openSUSE]: ./openSUSE/README.md
[Arch]: ./ArchLinux/README.md
