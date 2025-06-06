---
sys: fedora
sys_ver: "41"
sys_var: fvf

status: basic
last_update: 2025-06-04
---

# Fedora Minimal 41 Lichee Pi 3A Test Report

## Test Environment

### System Information

- System version: fedora-v-force Fedora Minimal 41
- Download Links: https://mirror.iscas.ac.cn/fedora-riscv/dl/SpacemiT/K1_M1/images/latest/k1-fedora-minimal.img.gz
- Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/K1/lpi3a/1_intro.html

### Hardware Information

- Lichee Pi 3A
- Power Adapter
- A USB to UART Debugger
- A microSD Card

## Installation Steps

### Using `dd` to flash the image to SD card

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
gzip -d k1-fedora-minimal.img.gz
sudo dd if=k1-fedora-minimal.img of=/dev/your-device bs=1M status=progress oflag=dsync
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `riscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system should boot normally and allow login via the onboard serial port.

### Boot Log

Screen recording (From flashing image to system login):
[![asciicast](https://asciinema.org/a/xXecoLrIq2cKdvmbVfMWDzJYU.svg)](https://asciinema.org/a/xXecoLrIq2cKdvmbVfMWDzJYU)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon Jul  1 03:20:03 UTC 2024

Kernel 6.1.15 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
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
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 6.1.15 #4 SMP PREEMPT Mon Jul 15 09:53:57 CST 2024 riscv64 GNU/Linux
[root@fedora-riscv ~]# lscpu
Architecture:           riscv64
  Byte Order:           Little Endian
CPU(s):                 8
  On-line CPU(s) list:  0-7
Vendor ID:              0x710
  Model name:           Spacemit(R) X60
    CPU family:         0x8000000058000001
    Model:              0x1000000049772200
    Thread(s) per core: 1
    Core(s) per socket: 8
    Socket(s):          1
    CPU(s) scaling MHz: 100%
    CPU max MHz:        1600.0000
    CPU min MHz:        614.4000
Caches (sum of all):    
  L1d:                  256 KiB (8 instances)
  L1i:                  256 KiB (8 instances)
  L2:                   1 MiB (2 instances)
[root@fedora-riscv ~]# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.