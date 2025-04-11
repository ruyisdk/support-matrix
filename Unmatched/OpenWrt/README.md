---
sys: openwrt
sys_ver: "24.10.0"
sys_var: null

status: basic
last_update: 2025-04-11
---

# OpenWrt 24.10.0 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: OpenWrt 24.10.0
- Download Link (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=24.10.0&target=sifiveu%2Fgeneric&id=sifive_unmatched
- Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.sifive

> In OpenWrt Firmware Selector, you can customize the system image online, adding necessary pre-installed packages. For this test, we use the **unmodified** original image.

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card

## Installation Steps

### Boot Device Selection

Ensure the DIP switch is set to boot from the microSD card. If you haven't changed it, the default factory setting is to boot from the microSD card.

The DIP switch should be set as follows: `MSEL[3:0]=1011`

### Using dd to flash the image to the microSD card

`/dev/sdX` is the microSD card. Change accordingly.

```shell
wget https://downloads.openwrt.org/releases/24.10.0/targets/sifiveu/generic/openwrt-24.10.0-sifiveu-generic-sifive_unmatched-ext4-sdcard.img.gz
gzip -d openwrt-24.10.0-sifiveu-generic-sifive_unmatched-ext4-sdcard.img.gz
sudo dd if=openwrt-24.10.0-sifiveu-generic-sifive_unmatched-ext4-sdcard.img of=/dev/sdX bs=1M status=progress; sync
sudo eject /dev/sdX
```

### Logging into the System

Log into the system via the onboard serial port (using a microUSB cable to connect to another computer).

## Expected Results

The system should boot up normally, allowing login through the onboard serial port.

## Actual Results

The system booted successfully, and login through the onboard serial port was successful.

### Boot Log

```log
BusyBox v1.36.1 (2025-02-03 23:09:37 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 24.10.0, r28427-6df0e3d02a
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:~# cat /etc/os-release
NAME="OpenWrt"
VERSION="24.10.0"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 24.10.0"
VERSION_ID="24.10.0"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r28427-6df0e3d02a"
OPENWRT_BOARD="sifiveu/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 24.10.0 r28427-6df0e3d02a"
OPENWRT_BUILD_DATE="1738624177"
root@OpenWrt:~# cat /etc/openwrt_
openwrt_release  openwrt_version
root@OpenWrt:~# cat /etc/openwrt_version
r28427-6df0e3d02a
root@OpenWrt:~# cat /etc/openwrt_release
DISTRIB_ID='OpenWrt'
DISTRIB_RELEASE='24.10.0'
DISTRIB_REVISION='r28427-6df0e3d02a'
DISTRIB_TARGET='sifiveu/generic'
DISTRIB_ARCH='riscv64_riscv64'
DISTRIB_DESCRIPTION='OpenWrt 24.10.0 r28427-6df0e3d02a'
DISTRIB_TAINTS=''
root@OpenWrt:~# uname -a
Linux OpenWrt 6.6.73 #0 SMP Mon Feb  3 23:09:37 2025 riscv64 GNU/Linux
root@OpenWrt:~# cat /proc/cpuinfo
processor       : 0
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

root@OpenWrt:~#
```

Screen record:

[![asciicast](https://asciinema.org/a/kWBM8bOzlgglxaWfDXBe9fEiQ.svg)](https://asciinema.org/a/kWBM8bOzlgglxaWfDXBe9fEiQ)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
