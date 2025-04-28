---
sys: buildroot
sys_ver: v1.1.4
sys_var: sd-v1

status: basic
last_update: 2025-04-14
---

# BuildRoot Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: DuoS-V1.1.4
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases/
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk/

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
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duos-sd-v1.1.4.img.zip
unzip milkv-duos-sd-v1.1.4.img.zip
```

### Flashing the Image

```bash
sudo dd if=milkv-duos-sd-v1.1.4.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Information

> The aic8800 insmod failure occurred because the Duo S used in the test does not have a Wi-Fi chip.
>
> This is normal.

```log
Starting app...

[root@milkv-duo]~# insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri Nov 22 13:36:20 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release
NAME=Buildroot
VERSION=20241122-1345
ID=buildroot
VERSION_ID=2021.05
PRETTY_NAME="Buildroot 2021.05"
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

[root@milkv-duo]~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
