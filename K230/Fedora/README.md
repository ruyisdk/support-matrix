---
sys: fedora
sys_ver: 38
sys_var: null

status: basic
last_update: 2024-06-21
---

# Fedora 38 K230 Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 38
- Download Link: [https://github.com/ruyisdk/mkimg-k230-rv64ilp32/releases](https://github.com/ruyisdk/mkimg-k230-rv64ilp32/releases)
- Reference Installation Document: [https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html](https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html)

### Hardware Information

- Development Board: Canaan Kendryte K230

## Installation Steps

### Flashing the Image

Use `unzstd` to decompress the image.
Wipe your sd card.
Use `dd` to flash the image to the microSD card.

```bash
unzstd /path/to/fedora.img.zst
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/fedora.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging to the system via serial port.

Default user: `root`
Default password: `riscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Information

Screen recording (from flashing the image to login):

[![asciicast](https://asciinema.org/a/urysrirhMB8fivXe1JHQ65Hyv.svg)](https://asciinema.org/a/urysrirhMB8fivXe1JHQ65Hyv)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Tue Aug 15 19:14:20 UTC 2023

Kernel 6.6.0+ on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Sun Mar  3 02:47:32 on ttyS0
-bash-5.2# uname -a
Linux fedora-riscv 6.6.0+ #1 SMP Wed Mar 13 09:16:28 UTC 2024 riscv64 GNU/Linux
-bash-5.2# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="38 (Thirty Eight)"
ID=fedora
VERSION_ID=38
VERSION_CODENAME=""
PLATFORM_ID="platform:f38"
PRETTY_NAME="Fedora Linux 38 (Thirty Eight)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:38"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f38/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=38
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=38
SUPPORT_END=2024-05-14

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
