# Debian 11 D1 Test Report

## Test Environment

### Operating System Information

- System Version: Debian
- Download Link: [http://www.perfxlab.cn:8080/rvboards/](http://www.perfxlab.cn:8080/rvboards/)
    - Web Disk: [https://pan.baidu.com/s/1leAXR2VPHvTqkaDqfeY9ag](https://pan.baidu.com/s/1leAXR2VPHvTqkaDqfeY9ag) Access Code: 3o5v
- Reference Installation Document: [https://d1.docs.aw-ol.com/strong/strong_4debian/#v041](https://d1.docs.aw-ol.com/strong/strong_4debian/#v041)

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unzip` to decompress the image.
Clear your SD card.
Use `dd` to write the image to the microSD card.

```bash
unzip /path/to/RVBoards_D1_Debian_lxde_img_linux.img.zip
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/RVBoards_D1_Debian_lxde_img_linux.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

Default Username: `root`
Default Password: `rvboards`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/7osW4u2FvkucqlfODK4nEBMQm.svg)](https://asciinema.org/a/7osW4u2FvkucqlfODK4nEBMQm)

```log
Debian GNU/Linux 11 RVBoards ttyS0

RVBoards login: root
Password: 

Login incorrect
RVBoards login: root
Password: 
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 19 18:39:24 CST 2021 on ttyS0
root@RVBoards:~# uname -a
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64 GNU/Linux
root@RVBoards:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@RVBoards:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
