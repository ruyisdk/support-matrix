---
sys: freebsd
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-15
---

# FreeBSD DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/freebsd-d1/freebsd-d1
- Reference Installation Document: https://github.com/freebsd-d1/freebsd-d1

### Hardware Information

- DongshanPI-Nezha STU
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
add host 127.0.0.1: gateway lo0 fib 0: route already in table
add host ::1: gateway lo0 fib 0: route already in table
add net fe80::: gateway ::1
add net ff02::: gateway ::1
add net ::ffff:0.0.0.0: gateway ::1
add net ::0.0.0.0: gateway ::1
fstab: /etc/fstab:0: No such file or directory
fstab: /etc/fstab:0: No such file or directory
Updating motd:.
Creating and/or trimming log files.
Updating /var/run/os-release done.
Clearing /tmp (X related).
Starting syslogd.
Mounting late filesystems:fstab: /etc/fstab:0: No such file or directory
.
fstab: /etc/fstab:0: No such file or directory
Starting cron.
Starting background file system checks in 60 seconds.

Fri Mar  7 21:29:21 UTC 2025

FreeBSD/riscv (freebsd-d1) (rcons)

login: root
Mar  7 21:29:34 freebsd-d1 login[1090]: ROOT LOGIN (root) ON rcons
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
root@freebsd-d1:~ # ps aux
USER  PID  %CPU %MEM   VSZ   RSS    TT  STAT STARTED    TIME COMMAND
root   11 100.0  0.0     0    16     -  RNL  21:28   2:34.20 [idle]
root    0   0.0  0.1     0   192     -  DLs  21:28   0:00.12 [kernel]
root    1   0.0  0.3 11248  1064     -  ILs  21:28   0:00.07 /sbin/init
root    2   0.0  0.0     0    16     -  WL   21:28   0:07.66 [clock]
root    3   0.0  0.0     0    32     -  DL   21:28   0:00.00 [crypto]
root    4   0.0  0.0     0    48     -  DL   21:28   0:00.00 [cam]
root    5   0.0  0.0     0    16     -  DL   21:28   0:00.07 [rand_harvestq]
root    6   0.0  0.0     0    48     -  DL   21:28   0:00.09 [pagedaemon]
root    7   0.0  0.0     0    16     -  DL   21:28   0:00.00 [vmdaemon]
root    8   0.0  0.0     0    32     -  DL   21:28   0:00.01 [bufdaemon]
root    9   0.0  0.0     0    16     -  DL   21:28   0:00.02 [syncer]
root   10   0.0  0.0     0    16     -  DL   21:28   0:00.00 [audit]
root   12   0.0  0.0     0    96     -  WL   21:28   0:00.11 [intr]
root   13   0.0  0.0     0    48     -  DL   21:28   0:00.10 [geom]
root   14   0.0  0.0     0    16     -  DL   21:28   0:00.01 [vnlru]
root   15   0.0  0.0     0    16     -  DL   21:28   0:00.08 [md0]
root   53   0.0  4.0 12404 12488     -  S<s  21:28   0:00.18 /usr/sbin/watchdogd -t 8
root  101   0.0  0.0     0    16     -  DL   21:28   0:00.00 [busdma]
root  113   0.0  0.0     0    16     -  DL   21:28   0:00.02 [mmcsd0: mmc/sd card]
root  866   0.0  0.1 11456   320     -  Is   21:29   0:00.00 /sbin/devd
root 1039   0.0  0.6 12452  1760     -  Ss   21:29   0:00.10 /usr/sbin/syslogd -s
root 1071   0.0  0.6 12624  1800     -  Ss   21:29   0:00.03 /usr/sbin/cron -s
root 1090   0.0  0.9 12988  2888 rcons  Is   21:29   0:00.61 login [pam] (login)
root 1091   0.0  1.0 13024  3144 rcons  S    21:29   0:05.55 -sh (sh)
root 1100   0.0  0.9 13160  2776 rcons  R+   21:32   0:00.05 ps aux
root@freebsd-d1:~ # 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
