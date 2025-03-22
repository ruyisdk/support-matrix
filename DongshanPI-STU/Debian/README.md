---
sys: debian
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-14
---

# Debian DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/DongshanPI/NezhaSTU-ReleaseLinux/releases/download/v0.1.0-alpha/DshanNezhaSTU-APTok-Sdcard.img.gz
- Reference Installation Document: https://github.com/DongshanPI/NezhaSTU-ReleaseLinux

### Hardware Information

- DongshanPI-Nezha STU
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image

Use `gzip` to decompress the image.
Clear your sd card.
Use `dd` to write the image to the microSD card.

```bash
gzip -kd /path/to/DshanNezhaSTU-APTok-Sdcard.img.gz
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/DshanNezhaSTU-APTok-Sdcard.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `100ask`

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is also successful.

### Boot Log

```log
[   18.939791] fbcon: Taking over console

Debian GNU/Linux bookworm/sid nezhastu ttyS0

nezhastu login: 
Debian GNU/Linux bookworm/sid nezhastu hvc0

nezhastu login: root
Password: 
Linux nezhastu 5.18.0-rc4-396532-gf4bce410a6b4 #4 PREEMPT Fri May 6 05:21:39 EDT 2022 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@nezhastu:~# [   33.854677] ldob: disabling

root@nezhastu:~# uname -a
Linux nezhastu 5.18.0-rc4-396532-gf4bce410a6b4 #4 PREEMPT Fri May 6 05:21:39 EDT 2022 riscv64 GNU/Linux
root@nezhastu:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux bookworm/sid"
NAME="Debian GNU/Linux"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@nezhastu:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@nezhastu:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
