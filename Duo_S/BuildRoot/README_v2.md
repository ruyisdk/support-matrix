---
sys: buildroot
sys_ver: v2.0.0
sys_var: sd-v2

status: basic
last_update: 2025-04-14
---

# BuildRoot (v2) Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: DuoS-V2.0.0 (musl riscv64 version)
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk-v2

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB Power Adapter
- A USB-A to C or USB C to C Cable for powering the development board
- A microSD Card
- A USB Card Reader
- A USB to UART Debugger (e.g., CP2102, FT2232, etc. Be aware that WCH CH340/341 series will cause garbled text output, DO NOT USE)

## Installation Steps

### Download DuoS Image and extract

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.0/milkv-duos-musl-riscv64-sd_v2.0.0.img.zip
unzip milkv-duos-musl-riscv64-sd_v2.0.0.img.zip
```

### Flashing the Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=milkv-duos-musl-riscv64-sd_v2.0.0.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port and ssh.

## Actual Results

The system booted successfully and login via the onboard serial port and ssh was also successful.

### Boot Information

> The aic8800 insmod failure occurred because the Duo S used in the test does not have a Wi-Fi chip.
>
> This is normal.

```log
Starting app...

[root@milkv-duo]~# [    5.417921] aicbsp: sdio_err:<aicwf_sdio_bus_pwrctl,1431>: bus down
[    6.149662] ieee80211 phy0:
[    6.149662] *******************************************************
[    6.149662] ** CAUTION: USING PERMISSIVE CUSTOM REGULATORY RULES **
[    6.149662] *******************************************************

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Dec 9 10:28:13 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release
NAME=Buildroot
VERSION=-g2b4e5fdbc
ID=buildroot
VERSION_ID=2024.02.3
PRETTY_NAME="Buildroot 2024.02.3"
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

```

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/48Jw8Gwh6NqCJpnVejBntLIxd.svg)](https://asciinema.org/a/48Jw8Gwh6NqCJpnVejBntLIxd)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
