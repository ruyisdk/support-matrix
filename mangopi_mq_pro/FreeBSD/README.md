---
sys: freebsd
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-07
---

# FreeBSD MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/freebsd-d1/freebsd-d1
- Reference Installation Document: https://github.com/freebsd-d1/freebsd-d1

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Building and flashing Image

**A FreeBSD environment is required for the following steps; consider using a virtual machine.**

```bash
git clone https://github.com/freebsd-d1/freebsd-d1.git
cd freebsd-d1
pkg install gmake ccache llvm14 riscv64-none-elf-gcc python3 bison swig py39-setuptools
git submodule update --init
gmake
dd if=freebsd-d1.img of=/dev/your/device
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`

No password by default.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and allows login through the onboard serial port.

### Boot Log

```log
Fri Mar  7 21:29:20 UTC 2025

FreeBSD/riscv (freebsd-d1) (rcons)

login: root
Mar  7 21:29:23 freebsd-d1 login[1090]: ROOT LOGIN (root) ON rcons
FreeBSD 14.0-CURRENT #0 n258218-3243c065a44f: Fri Mar  7 21:25:14 UTC 2025     root@freebsd:/root/freebsd-d1/freebsd/obj/riscv.riscv64/sys/GENERIC

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List:        https://www.FreeBSD.org/lists/questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

To change this login announcement, see motd(5).
root@freebsd-d1:~ # uname -a
FreeBSD freebsd-d1 14.0-CURRENT FreeBSD 14.0-CURRENT #0 n258218-3243c065a44f: Fri Mar  7 21:25:14 UTC 2025     root@freebsd:/root/freebsd-d1/freebsd/obj/riscv.riscv64/sys/GENERIC riscv
root@freebsd-d1:~ # cat /etc/os-release 
NAME=FreeBSD
VERSION="14.0-CURRENT"
VERSION_ID="14.0"
ID=freebsd
ANSI_COLOR="0;31"
PRETTY_NAME="FreeBSD 14.0-CURRENT"
CPE_NAME="cpe:/o:freebsd:freebsd:14.0"
HOME_URL="https://FreeBSD.org/"
BUG_REPORT_URL="https://bugs.FreeBSD.org/"
root@freebsd-d1:~ # 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
