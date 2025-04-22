---
sys: revyos
sys_ver: "20240720"
sys_var: null

status: good
last_update: 2025-04-17
---

# RevyOS Lichee Console 4A Version Testing Report

## Test Environment

### System Information

- System Version: RevyOS
- Download Link: 
  - [sipeed](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html)
  - [iscas mirror](https://fast-mirror.isrc.ac.cn/revyos/extra/images/lcon4a/20240720/)
- Reference Installation Document: [sipeed](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/4_burn_image.html)

### Hardware Information

- Lichee Console 4A 8G / 16G
- Power supply come with the board
- A USB A to C cable

## Installation Steps

### Accessing `fastboot` Environment

The boot button and rst button are located inside the nvme disk compartment: ![boot_btn](image.png)

Press and hold the boot button while pressing the power button on the keyboard to enter fastboot mode, `lsusb` should display:
```
ID 2345:7654 T-HEAD USB download gadget
```

### Flashing Image to Onboard eMMC using `fastboot`

Decompress the image using lz4:
```bash
zstd -d boot-console-20240720_171948.ext4.zst
zstd -d root-console-20240720_171948.ext4.zst
```

Connect the USB cable to the Type-C port at the back of the device and burn the image using `fastboot`.

```bash
fastboot flash ram u-boot-with-spl-lcon4a-$(ramsize).bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-lcon4a-$(ramsize).bin
fastboot flash boot boot-console-20240720_171948.ext4
fastboot flash root root-console-20240720_171948.ext4
```

### Logging into the System

Logging into the system via serial port or graphical interface.

The default image account password configurations are as follows:

Account: `sipeed`, Password: `licheepi`

Account: `debian`, Password: `debian`

The root account does not have a password ny default.

## Expected Results

The system starts up correctly, and login is successful.

## Actual Results

The system boots up correctly, allows successful login, and access to the system.

### Boot Log

Screen recording (flashing the system):

[![asciicast](https://asciinema.org/a/8nPSD9mkfabBKQLRPOkqAu8oI.svg)](https://asciinema.org/a/8nPSD9mkfabBKQLRPOkqAu8oI)

```log
debian@revyos-console:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@revyos-console:~$ uname -a
Linux revyos-console 5.10.113-th1520 #2024.07.20.13.28+d8f77de53 SMP PREEMPT Sat Jul 20 13:29:42 UTC  riscv64 GNU/Linux
debian@revyos-console:~$ cat /etc/revyos-release 
BUILD_ID=20240720_171948
BUILD_DATE=20240720
BOARD_NAME=console
RELEASE_ID=20240720
COMMIT_ID=40e0de7b829084698dc825c623a52e66e178ad37
RUNNER_ID=10021766410

```

![machine](image-1.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
