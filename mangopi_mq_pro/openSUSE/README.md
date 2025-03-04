---
sys: opensuse
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-03
---

# openSUSE Tumbleweed MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz
- Reference Installation Document: https://en.opensuse.org/HCL:MangoPi_MQ-Pro

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz.raw.xz | dd bs=4M of=/dev/your/device iflag=fullblock oflag=direct status=progress; sync
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted normally and login via the onboard serial port is also successful.

### Boot Log

```log
Welcome to openSUSE Tumbleweed 20
Welcome to openSUSE Tumbleweed 20240115 - Kernel 6.5.2-4-default (ttyS0).

wla240115 - Kernel 6.5.2-4-default (hn0:  


localhost login: vc0).

wlan0:  


localhost login: root
Password: 
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.5.2-4-default #1 SMP Wed Sep 13 03:16:12 UTC 2023 (b06df44) riscv64 riscv64 riscv64 GNU/Linux
localhost:~ # cat /etc/os-release
NAME="openSUSE Tumbleweed"
# VERSION="20240115"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20240115"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:opensuse:tumbleweed:20240115"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"
localhost:~ # zypper --version
zypper 1.14.68
localhost:~ # 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
