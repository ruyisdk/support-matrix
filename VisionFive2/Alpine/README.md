---
sys: alpine
sys_ver: 3.20.0_alpha20231219 (edge)
sys_var: null

status: basic
last_update: 2024-10-22
---

# Alpine linux VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: 3.20.0_alpha20231219 (edge)
- Download Link: https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz
- Reference Installation Document: https://arvanta.net/alpine/alpine-on-visionfive/

### Hardware Information

- StarFive VisionFive 2
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Installation Image

Use `xz` to decompress the image.
Use `dd` or `balenaEtcher` to flash the image to the microSD card.

```bash
xz -d visionfive-v2-mmc.img.xz
dd if=visionfive-v2-mmc.img of=/dev/<your-device> 
```

### Boot Mode Selection

The StarFive VisionFive 2 offers multiple boot modes, configurable via onboard dip switches prior to powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html).

The board also has silk-screen labels for guidance.

To boot the Alpine image, select the SDIO3.0 mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

### Logging into the System
Log into system as root,without password. 

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.
But can't connect ethernet.

### Boot Log

```log

Welcome to Alpine Linux 3.20.0_alpha20231219 (edge)
Kernel 6.7.4-0-starfive on an riscv64 (ttyS0)

[press ENTER to login]
localhost login: root (automatic login)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

localhost:~# uname -a
Linux localhost 6.7.4-0-starfive #1-Alpine SMP PREEMPT_DYNAMIC Tue, 06 Feb 2024 12:21:03 +0000 riscv64 Linux
localhost:~# [   12.258155] mmc0: Failed to initialize a non-removable card
[   22.005472] platform 16000000.crypto: deferred probe pending

localhost:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.0_alpha20231219
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
localhost:~# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

