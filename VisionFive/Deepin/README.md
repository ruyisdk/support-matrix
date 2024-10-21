---
sys: deepin
sys_ver: 23
sys_var: null

status: basic
last_update: 2024-06-21
---

# Deepin VisionFive Test Report

## Test Environment

### System Information

- System Version: Deepin
- Download Link: https://cdimage.deepin.com/RISC-V/VisionFive-v1-image/deepin-visionfive.7z
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/VisionFive-v1-image/README.txt

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `7z` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
7z e deepin-visionfive.7z
sudo dd if=deepin-visionfive.img of=/dev/your/device bs=1M status=progress
```


### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `Riscv2022#`

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted up normally, and login via the onboard serial port was successful.

### Boot Log

Screen recording (From flashing the image to logging into the system):
[![asciicast](https://asciinema.org/a/9I4jUIPPdKEWBnNBO7ANzmvwB.svg)](https://asciinema.org/a/9I4jUIPPdKEWBnNBO7ANzmvwB)

```log
Deepin GNU/Linux 23 deepin-riscv ttyS0

deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 6.1.0-rc4-visionfive+ #1 SMP Thu Nov 10 01:12:06 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv:~# uname -a
Linux deepin-riscv 6.1.0-rc4-visionfive+ #1 SMP Thu Nov 10 01:12:06 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release 
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
