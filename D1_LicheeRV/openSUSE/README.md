---
sys: opensuse
sys_ver: 20240115
sys_var: null

status: basic
last_update: 2024-06-21
---

# openSUSE Tumbleweed D1 Test Report

## Test Environment

### Operating System Information

- System Version: openSUSE Tumbleweed
- Download Link: [openSUSE-Tumbleweed-RISC-V-JeOS-licheervdock.riscv64.raw.xz](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/)
- Reference Installation Document: [https://en.opensuse.org/HCL:Nezha](https://en.opensuse.org/HCL:Nezha)

### Hardware Information

- Sipeed Lichee RV Dock
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unxz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
unxz /path/to/openSUSE-Tumbleweed-RISC-V-JeOS-licheervdock.riscv64.raw.xz.raw.xz
sudo dd if=/path/to/openSUSE-Tumbleweed-RISC-V-JeOS-licheervdock.riscv64.raw of=/dev/your-device bs=1M status=progress
```

### Logging into the System

*System boot may be slow.*

Logging into the system via serial port.

Default Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to logging into the system):

[![asciicast](https://asciinema.org/a/qGx3Er1vKkhIuC19Ixbj50HNk.svg)](https://asciinema.org/a/qGx3Er1vKkhIuC19Ixbj50HNk)

```log
Welcome to openSUSE Tumbleweed 20
Welcome to openSUSE Tumbleweed 20240115 - Kernel240115 - Kernel 6.5.2-4-default (h 6.5.2-4-default (ttyS0).

wlan0:  


localhost login: vc0).

wlan0:  


localhost login: root
Password: 
Have a lot of fun...
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
localhost:~ # uname -a
Linux localhost.localdomain 6.5.2-4-default #1 SMP Wed Sep 13 03:16:12 UTC 2023 (b06df44) riscv64 riscv64 riscv64 GNU/Linux
localhost:~ # cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

localhost:~ # 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
