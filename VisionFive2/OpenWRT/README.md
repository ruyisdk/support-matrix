# OpenWRT SnapShot VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b)
- Reference Installation Document: [https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html](https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html)

### Hardware Information

- StarFive VisionFive2
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `gzip` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
wget https://downloads.openwrt.org/snapshots/targets/starfive/generic/openwrt-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz
gzip -d /path/to/openwrt.img.gz
sudo dd if=/path/to/openwrt.img of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Login to the system via the serial port.

By default, there is no password, and root login is automatic.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system booted up successfully and login through the onboard serial port was successful.

### Boot Log

Screen recording (From flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/cNB8FumIO4mB00Ppi1OoMCFyq.svg)](https://asciinema.org/a/cNB8FumIO4mB00Ppi1OoMCFyq)

```log
BusyBox v1.36.1 (2024-03-25 22:00:37 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25665-79e9ce354e
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.82 #0 SMP Mon Mar 25 22:00:37 2024 riscv64 GNU/Linux
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
BUILD_ID="r25665-79e9ce354e"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r25665-79e9ce354e"
root@OpenWrt:/# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
