# Debian Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Debian trixie/sid
- Download Link: https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing
- Reference Installation Document: https://github.com/hongwenjun/riscv64/tree/main/milkv-duo

> Note: This image is provided by a community developer and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- One USB power adapter
- One USB-A to C or USB C to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires
- Milk-V Duo with pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card

```shell
7z x duo-debian-full.7z
dd if=debian.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port.

Username: `root`
Password: `riscv`

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
Debian GNU/Linux trixie/sid milkv-duo ttyS0

milkv-duo login: root
Password: 
Linux milkv-duo 5.10.4-tag- #7 PREEMPT Tue Oct 24 23:07:12 JST 2023 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Jul 24 19:51:14 UTC 2023 on ttyS0
root@milkv-duo:~# uname -a
Linux milkv-duo 5.10.4-tag- #7 PREEMPT Tue Oct 24 23:07:12 JST 2023 riscv64 GNU/Linux
root@milkv-duo:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@milkv-duo:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@milkv-duo:~# 
```

Boot process screen recording:

[![asciicast](https://asciinema.org/a/oOEaHElWFYEJMCmsOkqDZfbEv.svg)](https://asciinema.org/a/oOEaHElWFYEJMCmsOkqDZfbEv)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

