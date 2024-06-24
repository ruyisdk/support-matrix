# HiFive Unmatched

## Test Environment

### Operating System Information

- openEuler RISC-V 23.09 Preview
    - Download link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/
    - Reference Installation Document: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt
- openKylin
    - Download link: https://www.openkylin.top/downloads
    - Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Ubuntu 23.10
    - Download link: https://cdimage.ubuntu.com/releases/23.10/release/
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched
- FreeBSD 14.0
    - Download link: https://mirrors.ustc.edu.cn/freebsd/releases/riscv/riscv64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz
    - Reference Installation Document: https://wiki.freebsd.org/riscv/HiFiveUnmatched
- OpenBSD 7.4
    - Download link: https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img
    - Reference Installation Document: https://ftp.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Zephyr
    - Reference Installation Document: https://docs.zephyrproject.org/latest/boards/riscv/index.html
- OpenWrt 23.05.2
    - Download link (Firmware Selector): https://firmware-selector.openwrt.org/?version=23.05.2&target=sifiveu%2Fgeneric&id=sifive_unmatched
    - Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.sifive
- Debian sid
    - Download link: https://people.debian.org/~deiv/riscv/debian-sid-risc-v-sifive-unmatched.tar.xz
    - Reference Installation Document: https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched
- OpenSUSE Tumbleweed
    - Download link: https://download.opensuse.org/repositories/home:/Andreas_Schwab:/riscv:/unmatched/images/openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz
    - Reference Installation Document: https://en.opensuse.org/HCL:HiFive_Unmatched

### Hardware Information

- HiFive Unmatched

## Test Results

| Software Category       | Package Name | Test Results (Test Report)          |
|-------------------------|--------------|-------------------------------------|
| Debian Image Boot       | N/A          | [Successful][Debian]                |
| openEuler/Base Image Boot | N/A        | [Successful][oERV]                  |
| openEuler/Xfce Image Boot| N/A         | [Successful][oERV]                  |
| openKylin Image Boot    | N/A          | [Successful][oK] (Official Support) |
| OpenSUSE Image Boot     | N/A          | [Successful][SUSE]                  |
| Ubuntu Image Boot       | N/A          | [Successful][Ubuntu] (Official Support) |
| FreeBSD Image Boot      | N/A          | [Successful][FreeBSD] (Official Support) |
| OpenBSD Image Boot      | N/A          | [Successful][OpenBSD] (Official Support) |
| Zephyr Boot             | N/A          | [Successful][Zephyr] (Official Support) |
| OpenWrt Boot            | N/A          | [Successful][OpenWrt] (Official Support) |

[Debian]: ./Debian/README.md
[oERV]: ./openEuler/README.md
[oK]: ./openKylin/README.md
[SUSE]: ./OpenSUSE/README.md
[Ubuntu]: ./Ubuntu/README.md
[FreeBSD]: ./FreeBSD/README.md
[OpenBSD]: ./OpenBSD/README.md
[Zephyr]: ./Zephyr/README.md
[OpenWrt]: ./OpenWrt/README.md
