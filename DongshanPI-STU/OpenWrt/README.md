---
sys: openwrt
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-14
---

# OpenWrt DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=100ask_dongshan-nezha-stu
- Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> The OpenWrt Firmware Selector allows you to custom build a system image online with the pre-installed packages you need. For this test, we used the original image without any modifications.

### Hardware Information

- DongshanPI-Nezha STU
- A USB-A power supply
- A USB-A to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flash Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
gzip -kd openwrt-d1-generic-100ask_dongshan-nezha-stu-ext4-sdcard.img
sudo dd if=openwrt-d1-generic-100ask_dongshan-nezha-stu-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is also successful.

### Boot Log

```log
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[   12.025361] platform 2009400.temperature-sensor: deferred probe pending
[   12.660696] mount_root: mounting /dev/root with options 
[   12.713795] EXT4-fs (mmcblk0p2): re-mounted ff313567-e9f1-5a5d-9895-3ba130b4a864 r/w. Quota mode: disabled.
[   12.728088] urandom-seed: Seed file not found (/etc/urandom.seed)
[   12.813271] procd: - early -
[   12.817219] procd: - watchdog -
[   14.358989] procd: - watchdog -
[   14.364085] procd: - ubus -
[   14.431764] procd: - init -
Please press Enter to activate this console.
[   16.022288] kmodloader: loading kernel modules from /etc/modules.d/*
[   16.813941] PPP generic driver version 2.4.2
[   16.823881] NET: Registered PF_PPPOX protocol family
[   16.865974] kmodloader: done loading kernel modules from /etc/modules.d/*
[   17.489387] urngd: v1.0.2 started.



BusyBox v1.37.0 (2025-03-13 10:23:03 UTC) built-in shell (ash)

  _______                     ________        __
 |     | .-----.-----.-----. |  |  |  | .----. |  | _ |
 | --- ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r28979-9a79cdc7ee
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------

 OpenWrt recently switched to the "apk" package manager!

 OPKG Command           APK Equivalent      Description
 ------------------------------------------------------------------
 opkg install <pkg>     apk add <pkg>       Install a package
 opkg remove <pkg>      apk del <pkg>       Remove a package
 opkg upgrade           apk upgrade         Upgrade all packages
 opkg files <pkg>       apk info -L <pkg>   List package contents
 opkg list-installed    apk info            List installed packages
 opkg update            apk update          Update package lists
 opkg search <pkg>      apk search <pkg>    Search for packages
 ------------------------------------------------------------------

For more https://openwrt.org/docs/guide-user/additional-software/opkg-to-apk-cheatsheet

root@OpenWrt:~# uname -a
Linux OpenWrt 6.6.82 #0 SMP Thu Mar 13 10:23:03 2025 riscv64 GNU/Linux
root@OpenWrt:~# cat /etc/os-release 
NAME="OpenWrt"
VERSION="SNAPSHOT"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt SNAPSHOT"
VERSION_ID="snapshot"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
FIRMWARE_URL="https://downloads.openwrt.org/"
BUILD_ID="r28979-9a79cdc7ee"
OPENWRT_BOARD="d1/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r28979-9a79cdc7ee"
OPENWRT_BUILD_DATE="1741861383"
root@OpenWrt:~# o[   40.876902] dwmac-sun8i 4500000.ethernet eth0: Register MEM_TYPE_PAGE_POOL RxQ-0
p[   41.064498] dwmac-sun8i 4500000.ethernet eth0: PHY [stmmac-0:01] driver [RTL8211F Gigabit Ethernet] (irq=POLL)
[   41.074732] dwmac-sun8i 4500000.ethernet eth0: No Safety Features support found
[   41.082082] dwmac-sun8i 4500000.ethernet eth0: No MAC Management Counters available
[   41.089916] dwmac-sun8i 4500000.ethernet eth0: PTP not supported by HW
[   41.096557] dwmac-sun8i 4500000.ethernet eth0: configuring for phy/rgmii-id link mode
[   41.175571] br-lan: port 1(eth0) entered blocking state
[   41.180841] br-lan: port 1(eth0) entered disabled state
[   41.186365] dwmac-sun8i 4500000.ethernet eth0: entered allmulticast mode
[   41.193645] dwmac-sun8i 4500000.ethernet eth0: entered promiscuous mode

-ash: op: not found
root@OpenWrt:~#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
