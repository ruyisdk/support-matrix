# OpenWrt 23.05.2 D1 Test Report

## Test Environment

### Operating System Information

- System Version: OpenWrt 23.05.2
- Download Links (OpenWrt Firmware Selector):
  - Nezha D1: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=nezha
  - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
- Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> In the OpenWrt Firmware Selector, you can custom-build the system image online, adding the pre-installed packages you need. For this test, we used the **unmodified** original image.

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- A USB-A power adapter
- A USB-A to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
xz -dkv openwrt-d1-lichee_rv_dock-squashfs-sdcard.img.gz
sudo dd if=openwrt-d1-lichee_rv_dock-squashfs-sdcard.img of=/dev/sdc status=progress
```

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
BusyBox v1.36.1 (2024-03-13 22:51:23 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25540-7b89388674
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.81 #0 SMP Wed Mar 13 22:51:23 2024 riscv64 GNU/Linux
root@OpenWrt:/# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
```

Screen recording (From flashing image to logging into the system):

[![asciicast](https://asciinema.org/a/FtuRf4hQ7gWi0lTR4JkBxXJMw.svg)](https://asciinema.org/a/FtuRf4hQ7gWi0lTR4JkBxXJMw)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
