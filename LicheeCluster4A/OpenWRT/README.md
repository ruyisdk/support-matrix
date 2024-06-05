
# OpenWRT Lichee Cluster 4A Test Report

## Test Environment

### System Information

- System Version: OpenWRT
- Download Link: [https://github.com/chainsx/openwrt-th1520/releases](https://github.com/chainsx/openwrt-th1520/releases)
- Reference Installation Document: [https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)
- Fastboot Links:
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### Hardware Information

- Lichee Cluster 4A 8G/16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A Dock
- One microSD card
- Network and Ethernet cable (connect to BMC, not the switch)

## Installation Steps

*The following steps apply to flashing the image to the first board in the cluster*

### Flashing Image

Use `gzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
gzip -d /path/to/openwrt.img.xz
sudo dd if=/path/to/openwrt.img of=/dev/your_device bs=1M status=progress
```

### Flashing Bootloader

Use the u-boot downloaded above for this step.

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### Logging into the System

Login to the system via SOL (Serial Over LAN).

Default BMC username: `root`

Default BMC password: `0penBmc` **Note that it is `0` not `O`**

Connect using `ssh -p 2301 root@lichee-rv.local`

Upon initial boot, automatically logged in as root.

### Common Issues

If USB is not working, it may be due to Linux device tree require patching. [Download patch here](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

## Expected Results

The system should start up correctly and allow login via SOL (Serial Over LAN).

## Actual Results

The system booted successfully and login via SOL (Serial Over LAN) was possible.

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/z6gochTcLaWlL9m0f1Gj6vyoe.svg)](https://asciinema.org/a/z6gochTcLaWlL9m0f1Gj6vyoe)

```log
BusyBox v1.36.1 (2023-11-11 16:56:38 UTC) built-in shell (ash)


                              |/
                             _/_
    +-----------------+ ____  O
    |                 ||    \
    |                 ||     \     O     O
    |   ___   RISC-V  ||  ___ |   /|\_  /|\_
    +--/ o \----------++-/ o \+  _/ \  _/ \
       \___/             \___/
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r0-707f69c
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname pa
BusyBox v1.36.1 (2023-11-11 16:56:38 UTC) multi-call binary.

Usage: uname [-amnrspvio]

Print system information

        -a      Print all
        -m      Machine (hardware) type
        -n      Hostname
        -r      Kernel release
        -s      Kernel name (default)
        -p      Processor type
        -v      Kernel version
        -i      Hardware platform
        -o      OS name
root@OpenWrt:/# uname -a
Linux OpenWrt 5.10.113-g707f69c27511 #0 SMP PREEMPT Sat Nov 11 16:56:38 2023 riscv64 GNU/Linux
root@OpenWrt:/# cat /etc/os-release 
NAME="OpenWrt"
VERSION="SNAPSHOT"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt SNAPSHOT"
VERSION_ID="snapshot"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r0-707f69c"
OPENWRT_BOARD="thead/th1520"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS="no-all"
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r0-707f69c"
root@OpenWrt:/# [   33.853164] soc_dovdd18_scan: disabling

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
