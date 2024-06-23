# BuildRoot LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: 20240401
- Download Link: [https://github.com/sipeed/LicheeRV-Nano-Build/releases](https://github.com/sipeed/LicheeRV-Nano-Build/releases)
- Reference Installation Documentation: [https://github.com/sipeed/LicheeRV-Nano-Build/releases](https://github.com/sipeed/LicheeRV-Nano-Build/releases)

### Hardware Information

- LicheeRV Nano
- A Type-C power cable
- A UART to USB debugger

## Installation Steps

### Using `dd` to Flash Image onto microSD Card

Download the image, then decompress and flash it:

```shell
gzip -kd c906-2024-04-10-14-19-16d76b.img.gz
sudo dd if=c906-2024-04-10-14-19-16d76b.img of=/dev/your_device bs=1M status=progress

```

### Logging into the System

Logging into the system via serial port.

Default Username: root
Default Password: root

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing image to login):

[![asciicast](https://asciinema.org/a/yNDWWKvYyXReaexbXm1t5dLxi.svg)](https://asciinema.org/a/yNDWWKvYyXReaexbXm1t5dLxi)

```log
Welcome to Linux
licheervnano-b6c0 login: root
licheervnano-b6c0 login: root
Password: 
# cat /etc/os-release 
NAME=Buildroot
VERSION=-g16d76badf-dirty
ID=buildroot
VERSION_ID=2023.11.2
PRETTY_NAME="Buildroot 2023.11.2"
# uname -a
Linux licheervnano-b6c0 5.10.4-tag- #1 PREEMPT Wed Apr 10 14:12:37 HKT 2024 riscv64 GNU/Linux
# 
 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

