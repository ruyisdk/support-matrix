---
sys: fedora
sys_ver: 41
sys_var: null

status: basic
last_update: 2024-11-6
---

# Fedora 41 Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 41
- Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/Duo/images/latest/milkv-duo-fedora-minimal.img.gz
- Reference Installation Document: https://fedoraproject.org/wiki/Architectures/RISC-V/Installing

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- A USB power adapter
- A USB-A to C or USB-C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires
- The Milk-V Duo has pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Flashing the Image to microSD Card Using `dd`

```shell
zcat milkv-duo-fedora-minimal.img.gz | sudo dd of=/dev/sda bs=4M iflag=fullblock status=progress 
```

### Logging into the System

Log into the system via the serial port.

Username: `root`
Password: `riscv`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 5.10.4-tag- #1 PREEMPT Wed Jul 10 16:47:07 CST 2024 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="41 (Rawhide Prerelease)"
ID=fedora
VERSION_ID=41
VERSION_CODENAME=""
PLATFORM_ID="platform:f41"
PRETTY_NAME="Fedora Linux 41 (Rawhide Prerelease)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
SUPPORT_END=2025-05-13
```

Screen recording of the boot process:

[![asciicast](https://asciinema.org/a/88V2VC1BWeFEVYRoj5s4YHO8o.svg)](https://asciinema.org/a/88V2VC1BWeFEVYRoj5s4YHO8o)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
