---
sys: debian
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-20
---

# Debian Pine64 Oz64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.10
- Reference Installation Document: https://github.com/scpcom/sophgo-sg200x-debian

### Hardware Information

- Pine64 Oz64
- 5V3A DC Barrel power adapter
- A microSD card
- A USB card reader
- A USB to UART Debugger
- DuPont wires

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

Debian GNU/Linux trixie/sid duos-e007 ttyS0

duos-e007 login: root
Password:
Linux duos-e007 5.10.235-20250430-6+duos #1 PREEMPT Mon May 12 16:53:24 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos-e007:~# uname -a
Linux duos-e007 5.10.235-20250430-6+duos #1 PREEMPT Mon May 12 16:53:24 UTC 2025 riscv64 GNU/Linux
root@duos-e007:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@duos-e007:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@duos-e007:~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
