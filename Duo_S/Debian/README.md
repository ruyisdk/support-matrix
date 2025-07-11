---
sys: debian
sys_ver: null
sys_var: null

status: basic
last_update: 2025-07-11
---

# Debian Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.35
- Reference Installation Document: https://github.com/scpcom/sophgo-sg200x-debian

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB power adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger
- Three DuPont wires

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card

```shell
lz4 -dk duos-e_sd.img.lz4
sudo dd if=duos-e_sd.img of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Information

```log
Debian GNU/Linux 13 duos-a0d7 ttyS0

duos-a0d7 login: debian
Password:

Debian GNU/Linux 13 duos-a0d7 ttyS0

duos-a0d7 login: root
Password:
Linux duos-a0d7 5.10.235-20250615-6+duos #1 PREEMPT Mon Jun 16 00:47:42 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos-a0d7:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@duos-a0d7:~# uname -a
Linux duos-a0d7 5.10.235-20250615-6+duos #1 PREEMPT Mon Jun 16 00:47:42 UTC 2025 riscv64 GNU/Linux
root@duos-a0d7:~#

```

Screen recording:

[![asciicast](https://asciinema.org/a/wg2iVMT950W3x8gLiZEFRPch3.svg)](https://asciinema.org/a/wg2iVMT950W3x8gLiZEFRPch3)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
