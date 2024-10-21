---
sys: debian
sys_ver: null
sys_var: null

status: basic
last_update: 2024-06-21
---

# Debian on Milk-V Mars Test Report

## Test Environment

### Operating System Information

- Debian bookworm/sid
  - Download Link: https://github.com/milkv-mars/mars-buildroot-sdk/releases/
    - Official Debian image is provided by Milk-V, with BuildRoot available in the repository
  - Reference Installation Document: https://milkv.io/zh/docs/mars/getting-started/boot

### Hardware Information

- Milk-V Mars

## Installation Steps

### Flashing the Image

Use `unzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

Note that `/dev/sdc` corresponds to the storage card device.

```bash
unzip mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img.zip
sudo dd if=mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `user`
Default password: `milkv`

## Expected Results

The system should boot normally and allow login via the onboard serial port. You should be able to enter the installation wizard.

## Actual Results

The system booted successfully and output was successfully viewed through the serial port.

### Boot Information

Screen recording:
[![asciicast](https://asciinema.org/a/v8FxrttpHTJVye5N4U5KCgUsT.svg)](https://asciinema.org/a/v8FxrttpHTJVye5N4U5KCgUsT)

```log
Debian GNU/LinuxDebian GNU/Linux bookworm/sid milkv hvc0

milkv login:  bookworm/sid milkv ttyS0

milkv login: user
Password: 
Linux milkv 5.15.0 #1 SMP Mon Nov 13 18:56:24 CST 2023 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
user@milkv:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux bookworm/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
BUILD_ID=40
user@milkv:~$ uname -a
Linux milkv 5.15.0 #1 SMP Mon Nov 13 18:56:24 CST 2023 riscv64 GNU/Linux
user@milkv:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
