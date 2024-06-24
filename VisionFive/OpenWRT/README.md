# OpenWRT SnapShot VisionFive Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1)
- Reference Installation Document: [https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive)

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- USB to UART Debugger

## Installation Steps

### Flashing Image

Use `gzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
wget https://downloads.openwrt.org/snapshots/targets/starfive/generic/openwrt-starfive-generic-visionfive-v1-ext4-sdcard.img.gz
gzip -d /path/to/openwrt.img.gz
sudo dd if=/path/to/openwrt.img of=/dev/your-device bs=1M status=progress
```

### Updating/Booting Bootloader

If u-boot fails to boot and enters the command line, u-boot needs to be updated (see: (pr 31) [https://github.com/starfive-tech/u-boot/pull/31]):

Official Documentation: [https://starfivetech.com/uploads/VisionFive%20Single%20Board%20Computer%20Quick%20Start%20Guide.pdf](https://starfivetech.com/uploads/VisionFive%20Single%20Board%20Computer%20Quick%20Start%20Guide.pdf)

U-Boot Download: https://github.com/starfive-tech/Fedora_on_StarFive/releases

Or manually enter the following commands to boot the system:

```u-boot
fatload mmc 0:3 0x84000000 Image
fatload mmc 0:3 0x88000000 dtb
setenv bootargs "earlyprintk console=ttyS0,115200 debug rootwait earlycon=sbi root=/dev/mmcblk0p4"
booti 0x84000000 - 0x88000000
```

### Logging into the System

Log into the system via the serial port.

The default is no password, auto login as root.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/GwgQgY4G4s2PihEHoXxsLyjP9.svg)](https://asciinema.org/a/GwgQgY4G4s2PihEHoXxsLyjP9)

```log

BusyBox v1.36.1 (2024-03-25 10:02:16 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25661-bf4c04a4d0
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# [   16.898199] starfive-dwmac 10020000.ethernet eth0: Register MEM_TYPE_PAGE_POOL RxQ-0
[   16.912314] starfive-dwmac 10020000.ethernet eth0: PHY [stmmac-0:00] driver [YT8521 Gigabit Ethernet] (irq=POLL)
[   16.932602] dwmac1000: Master AXI performs fixed burst length
[   16.938387] starfive-dwmac 10020000.ethernet eth0: No Safety Features support found
[   16.946043] starfive-dwmac 10020000.ethernet eth0: No MAC Management Counters available
[   16.954027] starfive-dwmac 10020000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[   16.962864] starfive-dwmac 10020000.ethernet eth0: registered PTP clock
[   16.969491] starfive-dwmac 10020000.ethernet eth0: configuring for phy/rgmii-txid link mode
[   16.980763] br-lan: port 1(eth0) entered blocking state
[   16.986006] br-lan: port 1(eth0) entered disabled state
[   16.991454] device eth0 entered promiscuous mode

root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.82 #0 SMP Mon Mar 25 10:02:16 2024 riscv64 GNU/Linux
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
BUILD_ID="r25661-bf4c04a4d0"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r25661-bf4c04a4d0"

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
