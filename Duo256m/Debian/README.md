# Debian Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System Version: Debian
- Download Link: https://github.com/Fishwaldo/sophgo-sg200x-debian
- Reference Installation Document: https://github.com/Fishwaldo/sophgo-sg200x-debian

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 256M
- One USB-A to C or USB C to C cable
- One microSD card
- One USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Using `dd` to Flash Image to microSD Card 

```shell
wget https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.3.0/duo256_sd.img.lz4
lz4 -d duo256_sd.img.lz4
sudo dd if=duo256_sd.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Password: `rv`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully, and login via the serial port was also successful.

### Boot Log

```log
Debian GNU/Linux trixie/sid duo256 ttyS0

duo256 login: root
Password: 
Linux duo256 5.10.4-20240329-1+ #1 Sat May 18 10:13:53 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duo256:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@duo256:~# uname -a\
> 
Linux duo256 5.10.4-20240329-1+ #1 Sat May 18 10:13:53 UTC 2024 riscv64 GNU/Linux
root@duo256:~# 

```

Screen recording of the boot process:
[![asciicast](https://asciinema.org/a/4p20IBBlCuE8jMxEExj19vMqd.svg)](https://asciinema.org/a/4p20IBBlCuE8jMxEExj19vMqd)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

