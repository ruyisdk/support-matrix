---
sys: openwrt
sys_ver: "24.10.1"
sys_var: null

status: basic
last_update: 2025-04-26
---

# OpenWrt Milk-V Mars Test Report

## Test Environment

### Hardware Information

- Development Board: Milk-V Mars (8GB RAM)
- Other Hardware:
  - A USB power adapter and A USB-A to C or C to C cable
  - A microSD card
  - A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

### Operating System Information

- OS Version: OpenWrt 24.10.1 (Build ID: r28597-0425664679)
- Download Link: <https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>
  - <https://firmware-selector.openwrt.org/?version=24.10.1&target=starfive%2Fgeneric&id=visionfive2-v1.3b>

## Installation Steps

### Flashing the Image

Use `gzip` command to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
wget https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz

gzip -d openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz

sudo dd if=openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img of=/dev/sdX bs=1M status=progress

sync
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root` (automatic login)

No password by default

Since the image does not have SPL and U-Boot, the dip switch of the board needs to be set to `00` in order to use the built-in SPL and U-Boot in the SPI-Flash on the board to boot the OpenWrt image in the MicroSD card.

## Expected Results

The system should boot normally, allowing login via the onboard serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Information

```log
BusyBox v1.36.1 (2025-04-13 16:38:32 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 24.10.1, r28597-0425664679
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:~# 

root@OpenWrt:~# cat /etc/os-release
NAME="OpenWrt"
VERSION="24.10.1"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 24.10.1"
VERSION_ID="24.10.1"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r28597-0425664679"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 24.10.1 r28597-0425664679"
OPENWRT_BUILD_DATE="1744562312"

root@OpenWrt:~# uname -a
Linux OpenWrt 6.6.86 #0 SMP Sun Apr 13 16:38:32 2025 riscv64 GNU/Linux

root@OpenWrt:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
