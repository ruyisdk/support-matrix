# openKylin 0.9.5 VisionFive Test Report

## Test Environment

### System Information

- System Version: openKylin 0.9.5
- Download Link: [https://www.openkylin.top/downloads/old_releases.html](https://www.openkylin.top/downloads/old_releases.html)
- Reference Installation Document: [https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unxz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
unxz /path/to/openKylin.img.xz
sudo dd if=/path/to/openKylin.img of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

Default Username: `openkylin`
Default Password: `openkylin`

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted up normally and login through the onboard serial port was successful.

### Boot Log

Screen recording (from flashing image to system login):

[![asciicast](https://asciinema.org/a/TgWQuZfKq1nb1CKJYuO4eyr8i.svg)](https://asciinema.org/a/TgWQuZfKq1nb1CKJYuO4eyr8i)

```log
openKylin 0.9.5 openkylin ttyS0

openkylin login: openkylin
密码： 
Welcome to openKylin 0.9.5 (GNU/Linux 5.18.0-rc4-starfive-rc5 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

openkylin@openkylin:~$ uname -a
Linux openkylin 5.18.0-rc4-starfive-rc5 #1 SMP Wed Apr 27 17:02:33 CST 2022 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="0.9.5 (yangtze)"
VERSION_US="0.9.5 (yangtze)"
ID=openkylin
PRETTY_NAME="openKylin 0.9.5"
VERSION_ID="0.9.5"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=yangtze
PRODUCT_FEATURES=3
openkylin@openkylin:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
