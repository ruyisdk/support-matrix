---
sys: yocto
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-05-28
---

# Yocto Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
- Reference Installation Document: https://github.com/Fishwaldo/meta-pine64

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flashing Image

After downloading, extract and flash the image (example is using the Plasma version):
```bash
wget https://github.com/Fishwaldo/meta-pine64/releases/download/v2.1/star64-image-plasma-star64.wic.bz2
bzip2 -kd star64-image-plasma-star64.wic.bz2
sudo dd if=star64-image-plasma-star64.wic of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port.

Upon startup, the system will prompt the user to manually set up username, password, timezone, language, etc.

For the Xfce version, you must complete the configuration to enter the desktop.

Configuration can be done through the serial port. If a keyboard and monitor are connected, you can also configure through the keyboard.

## Expected Results

The development board outputs boot information normally.

## Actual Results

U-Boot fails to load the system from the image.

### Boot Log

```log

U-Boot 2021.10 (Jun 05 2023 - 16:23:55 +0000)05062023

CPU:   rv64imacu_zba_zbb
Model: Pine64 Star64
DRAM:  8 GiB
MMC:   sdio0@16010000: 0, sdio1@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
OK
StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : PINE64
Product full SN: STAR64V1-2310-D008E000-00000005
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:75:61
Ethernet MAC1 address: 6c:cf:39:00:75:62
--------EEPROM INFO--------

In:    serial
Out:   serial
CFT
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
Unknown command 'usb' - try 'help'
Hit any key to stop autoboot:  0
Unknown command 'bootflow' - try 'help'
Star64 #
Star64 #

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
