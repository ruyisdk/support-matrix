---
sys: ubuntu
sys_ver: jammy
sys_var: null

status: basic
last_update: 2025-07-08
---

# Ubuntu LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/Z841973620/licheervnano-ubuntu/releases/tag/jammy
- Reference Installation Document: https://github.com/Z841973620/licheervnano-ubuntu

### Hardware Information

- LicheeRV Nano
- A Type-C power cable
- A UART to USB debugger

## Installation Steps

### Using `dd` to flash the image to the microSD card

Download the image and perform decompression and flashing:

```shell
wget https://github.com/Z841973620/licheervnano-ubuntu/releases/download/jammy/licheervnano-ubuntu22.04-riscv64.img.xz
xz -d licheervnano-ubuntu22.04-riscv64.img.xz
sudo dd if=licheervnano-ubuntu22.04-riscv64.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system through the serial port.

Username: `root`
Password: `ubuntu`

## Expected Results

The system should boot up normally and allow login through the serial port.

## Actual Results

The system booted up successfully, and login through the serial port was successful.

### Boot Log

```log
Ubuntu 22.04 LTS LicheeRV-Nano ttyS0

LicheeRV-Nano login: root
Password:
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.10.4 riscv64)

 System information disabled due to load higher than 1.0

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@LicheeRV-Nano:~# uname -a
Linux LicheeRV-Nano 5.10.4 #1 Sat Jul 5 08:49:26 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
root@LicheeRV-Nano:~# cat /etc/os-release
PRETTY_NAME="Ubuntu 22.04 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04 (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
root@LicheeRV-Nano:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@LicheeRV-Nano:~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

