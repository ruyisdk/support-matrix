---
sys: pmos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-07
---

# postmarketOS DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download link (pmbootstrap): https://wiki.postmarketos.org/wiki/Pmbootstrap
- Reference Installation Document: https://wiki.postmarketos.org/wiki/DongshanPi_NeZha_STU_(dongshanpi-nezhastu)

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Install via `pmbootstrap`

Get `pmbootstrap`, e.g. under Arch Linux:
```bash
pacman -S pmbootstrap
```

Bootstrap and flash the system via `pmbootstrap`:
```bash
pmbootstrap init
pmbootstrap install --sdcard=/dev/sdX
pmbootstrap shutdown
```

Various configurations would also be made in the above process. Remember to select the target vendor as `dongshanpi`, and the target board as `nezhastu`。

### Logging into the System

Logging into to the system via the serial port.

Username and password should be set during installation.

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

## Actual Results

The system booted up normally and login via the onboard serial port was also successful.

### Boot Log

```log
Welcome to postmarketOS
Kernel 6.1.0-rc3 on an riscv64 (/dev/ttyS0)
dongshanpi-nezhastu login: pmosriscv
Password: 
Welcome to postmarketOS! o/

This distribution is based on Alpine Linux.
First time using postmarketOS? Make sure to read the cheatsheet in the wiki:

-> https://postmarketos.org/cheatsheet

You may change this message by editing /etc/motd.
dongshanpi-nezhastu:~$ uname -a
Linux dongshanpi-nezhastu 6.1.0-rc3 #1 Wed Jul 31 00:22:22 UTC 2024 riscv64 Linux
dongshanpi-nezhastu:~$ cat /etc/os-release 
PRETTY_NAME="postmarketOS edge"
NAME="postmarketOS"
VERSION_ID="edge"
VERSION="edge"
ID="postmarketos"
ID_LIKE="alpine"
HOME_URL="https://www.postmarketos.org/"
SUPPORT_URL="https://gitlab.postmarketos.org/postmarketOS"
BUG_REPORT_URL="https://gitlab.postmarketos.org/postmarketOS/pmaports/issues"
LOGO="postmarketos-logo"
ANSI_COLOR="0;32"
dongshanpi-nezhastu:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
