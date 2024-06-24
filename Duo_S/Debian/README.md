# Debian Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.1.0
- Reference Installation Document: https://github.com/Fishwaldo/sophgo-sg200x-debian

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB power adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger (e.g., CP2102, FT2232, etc. Be aware that WCH CH340/341 series will cause garbled text output, DO NOT USE)
- Three DuPont wires

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card

```shell
lz4 -dk duos_sd.img.lz4
sudo dd if=duos_sd.img of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Information

```log
Linux duos 5.10.4-20240329-1+ #1 PREEMPT Wed Apr 24 11:26:16 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@duos:~# uname -a
Linux duos 5.10.4-20240329-1+ #1 PREEMPT Wed Apr 24 11:26:16 UTC 2024 riscv64 GNU/Linux
root@duos:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@duos:~#
```

Screen recording:

[![asciicast](https://asciinema.org/a/SHxcbudKKPuuuARa7iMAhW0RO.svg)](https://asciinema.org/a/SHxcbudKKPuuuARa7iMAhW0RO)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
