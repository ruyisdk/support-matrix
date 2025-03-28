---
sys: debian
sys_ver: v1.4.0
sys_var: sd

status: basic
last_update: 2024-06-21
---

# Debian Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.4.0
- Reference Installation Document: https://github.com/Fishwaldo/sophgo-sg200x-debian

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB power adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger   
    - Only CP210x series is recommeneded (e.g. CP2102/CP2104). Be aware you'll only get garbled text output on WCH CH340/341 series; you can still use other USB-UART chips like FT232 and CH343 series, although you might still get garbled output but only before U-Boot loads, this is expected. If UART isn't working at all please consider try another USB-UART adaptor.
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
Debian GNU/Linux trixie/sid duos ttyS0

duos login: debian
Password:
Linux duos 5.10.4-20240527-2+ #1 Sat Jun 1 14:15:39 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
2004hdebian@duos:~$ cat /[  OK  ] Finished finalize-image.service - Finalize the Image.
         Starting ssh.service - OpenBSD Secure Shell server...
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.
         Starting systemd-update-utmp-runle…- Record Runlevel Change in UTMP...
[  OK  ] Finished systemd-update-utmp-runle…e - Record Runlevel Change in UTMP.
[   84.662830] cvi_rtc 5026000.rtc: time set to 1721370282. 7/19/2024 6:24:42
[   84.676348] cvi_rtc 5026000.rtc: time read as 1721370282. 7/19/2024 6:24:42
^C
debian@duos:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
4hdebian@duos:~$ uname -a
Linux duos 5.10.4-20240527-2+ #1 Sat Jun 1 14:15:39 UTC 2024 riscv64 GNU/Linux
debian@duos:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

[?2004hdebian@duos:~$
```

Screen recording:

[![asciicast](https://asciinema.org/a/SJ7sck8RtdUvHapuyqs0rPmS4.svg)](https://asciinema.org/a/SJ7sck8RtdUvHapuyqs0rPmS4)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
