---
sys: alpine
sys_ver: 3.20.0_alpha20231219 (edge)
sys_var: null

status: basic
last_update: 2025-06-04
---

# Deepin VisionFive Test Report

## Test Environment

### System Information

- System Version: 3.20.0_alpha20231219 (edge)
- Download Link: https://dev.alpinelinux.org/~mps/riscv64/visionfive-v1-mmc.img.xz
- Reference Installation Document: https://arvanta.net/alpine/alpine-on-visionfive/

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xz -d visionfive-v1-mmc.img.xz
dd if=visionfive-v1-mmc.img of=/dev/<your-device> 
```

### Logging into the System
Log into system as root, without password. 

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system should boot up normally and allow login through the onboard serial port.

### Boot Log

Screen recording (from flash to login):
[![asciicast](https://asciinema.org/a/ui1P6rp5yjFTxO7YehuV7jC8s.svg)](https://asciinema.org/a/ui1P6rp5yjFTxO7YehuV7jC8s)

```log
Welcome to Alpine Linux 3.20.0_alpha20231219 (edge)
Kernel 6.8.0-rc2-0-vf1 on an riscv64 (ttyS0)

[press ENTER to login]
localhost login: root (automatic login)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

localhost:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.0_alpha20231219
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
localhost:~# uname -a
Linux localhost 6.8.0-rc2-0-vf1 #1-Alpine SMP PREEMPT Fri, 02 Feb 2024 18:42:11 +0000 riscv64 Linux
localhost:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                2
  On-line CPU(s) list: 0,1
localhost:~# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
