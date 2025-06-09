---
sys: debian
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-27
---

# Debian Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.31
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
Linux duos-a0d7 5.10.235-20250531-6+duos #1 PREEMPT Sun Jun 8 03:30:58 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
debian@duos-a0d7:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.0
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@duos-a0d7:~$ uname -a
Linux duos-a0d7 5.10.235-20250531-6+duos #1 PREEMPT Sun Jun 8 03:30:58 UTC 2025 riscv64 GNU/Linux
debian@duos-a0d7:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

debian@duos-a0d7:~$
```

Screen recording:

[![asciicast](https://asciinema.org/a/f2rfBYYV0SuSLxsjZSJ8VHNLV.svg)](https://asciinema.org/a/f2rfBYYV0SuSLxsjZSJ8VHNLV)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
