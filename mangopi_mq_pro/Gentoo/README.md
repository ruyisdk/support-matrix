---
sys: gentoo
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-04
---

# Gentoo MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/RevySR/riscv-calculate/releases/download/v20220929/gentoo-d1-20220929153235.img.zst
- Reference Installation Document: https://github.com/RevySR/riscv-calculate

> Note: This image is provided by a community developer and is not an official image.

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -d gentoo-d1-20220929153235.img.zst
sudo dd if=/path/to/gentoo-d1-20220929153235.img.zst of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Plug in the power via the USB-C "OTG" port (instead of "HOST") to avoid issues with faulty power supply (see https://forums.100ask.net/t/topic/876/6).

Logging into the system via the serial port.

Default username: `root`
Default password: `Riscv2022#`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted normally and login via the onboard serial port is also successful.

### Boot Log

```log
[   31.849891] fbcon: Taking over console


This is gentoo-riscv.unknown_doma

This is gentooin (Linux riscv64-riscv.unknown_d 5.19.0-rc1-gfe178cf0153d-dirty) 09:10:30

gentoo-riscv login: omain (Linux riscv64 5.19.0-rc1-gfe178cf0153d-dirty) 09:10:30

gentoo-riscv login: root
Password: 

root@gentoo-riscv ~ # uname -a
Linux gentoo-riscv 5.19.0-rc1-gfe178cf0153d-dirty #1 PREEMPT Thu Sep 29 15:28:12 UTC 2022 riscv64 GNU/Linux
root@gentoo-riscv ~ # ls
root@gentoo-riscv ~ # cat /etc/os-release 
NAME=Gentoo
ID=gentoo
PRETTY_NAME="Gentoo Linux"
ANSI_COLOR="1;32"
HOME_URL="https://www.gentoo.org/"
SUPPORT_URL="https://www.gentoo.org/support/"
BUG_REPORT_URL="https://bugs.gentoo.org/"
VERSION_ID="2.9"

root@gentoo-riscv ~ # portageq  --help
>>> Portage information query tool
>>> 3.0.37
>>> Usage: portageq <command> [<option> ...]

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.