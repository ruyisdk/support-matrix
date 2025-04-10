---
sys: debian
sys_ver: v1.6.7
sys_var: null

status: basic
last_update: 2025-04-09
---

# Debian LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/licheervnano-e_sd.img.lz4
- Reference Installation Document: https://github.com/scpcom/sophgo-sg200x-debian/

### Hardware Information

- LicheeRV Nano
- A Type-C power cable
- A UART to USB debugger

## Installation Steps

### Using `dd` to flash the image to the microSD card

Download the image and perform decompression and flashing:

```shell
wget https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/licheervnano-e_sd.img.lz4
lz4 -dk licheervnano-e_sd.img.lz4
sudo dd if=licheervnano-e_sd.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system through the serial port.

| Username | Password |
| -------- | -------- |
| root     | rv       |
| debian   | rv       |


## Expected Results

The system should boot up normally and allow login through the serial port.

## Actual Results

The system booted up successfully, and login through the serial port was successful.

### Boot Log

```log
Debian GNU/Linux trixie/sid licheervnano-6681 ttyS0

licheervnano-6681 login: [  OK  ] Finished e2scrub_reap.service - Remove Stale Online ext4 Metadata Check Snapshots.
[  OK  ] Finished finalize-image.service - Finalize the Image.
         Starting ssh.service - OpenBSD Secure Shell server...
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.

licheervnano-6681 login: root
Password:
Linux licheervnano-6681 5.10.235-20250403-6+licheervnano #1 PREEMPT Sat Apr 5 17:40:58 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@licheervnano-6681:~# uname -a
Linux licheervnano-6681 5.10.235-20250403-6+licheervnano #1 PREEMPT Sat Apr 5 17:40:58 UTC 2025 riscv64 GNU/Linux
root@licheervnano-6681:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@licheervnano-6681:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@licheervnano-6681:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@licheervnano-6681:~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

