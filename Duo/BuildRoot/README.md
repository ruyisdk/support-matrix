---
sys: buildroot
sys_ver: v1.1.4
sys_var: null

status: basic
last_update: 2025-1-1
---

# BuildRoot Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Duo-V1.1.4
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- Milk-V Duo 64M
- A USB-A to C or USB C to C cable
- A microSD card

## Installation Steps

### Download Duo Image

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip
unzip milkv-duo-sd-v1.1.4.img.zip
```

### Flashing the Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=milkv-duo-sd-v1.1.4.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port or SSH.

Default username: `root`
Default password: `milkv`

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri Nov 22 11:31:04 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=20241122-1139
ID=buildroot
VERSION_ID=2021.05
PRETTY_NAME="Buildroot 2021.05"
```

Screen recording (from flashing the image to system login):

[![asciicast](https://asciinema.org/a/pendFyzvbk51Sf8uaeozKjYRb.svg)](https://asciinema.org/a/pendFyzvbk51Sf8uaeozKjYRb)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
