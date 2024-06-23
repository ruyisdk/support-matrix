# BuildRoot Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System Version: Duo 256M
- Download Link: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Reference Installation Document: [https://github.com/milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk)

### Hardware Information

- Milk-V Duo 256M
- A USB-A to C or USB C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Download Duo 256M Image

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/Duo-V1.1.0/milkv-duo256m-v1.1.0-2024-0410.img.zip
unzip milkv-duo256m-v1.1.0-2024-0410.img
```

### Flashing the Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=milkv-duo256m-v1.1.0-2024-0410.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port or SSH.

Default username: `root`
Default password: `milkv`

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully, and login through the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to system login):
[![asciicast](https://asciinema.org/a/ptdjXiBZX2FuisTBuEZis7JoK.svg)](https://asciinema.org/a/ptdjXiBZX2FuisTBuEZis7JoK)

```log
The authenticity of host '192.168.42.1 (192.168.42.1)' can't be established.
ED25519 key fingerprint is SHA256:Lt+dfAQr7Ih8tgb+j9KPZaQDKNRhbHSZfWLIjNYB0Ko.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.42.1' (ED25519) to the list of known hosts.
root@192.168.42.1's password: 
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=20240410-2139
ID=buildroot
VERSION_ID=2021.05
PRETTY_NAME="Buildroot 2021.05"
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Wed Apr 10 21:37:02 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
