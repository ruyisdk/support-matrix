# RevyOS Lichee Console 4A Version Testing Report

## Test Environment

### System Information

- System Version: RevyOS
- Download Link: [sipeed](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html)
- Reference Installation Document: [sipeed](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/4_burn_image.html)

### Hardware Information

- Lichee Cluster 4A 8G / 16G
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
lz4 -d path/to/boot.ext4.lz4
lz4 -d path/to/root.ext4.lz4
```

Connect the USB cable to the Type-C port at the back of the device and burn the image using `fastboot`.

```bash
fastboot flash ram u-boot-with-spl-console-ramsize.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-console-ramsize.bin
fastboot flash boot path/to/boot.ext4
fastboot flash root path/to/root.ext4
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

[![asciicast](https://asciinema.org/a/hZHlwXaPj9W1AQgADtrgYRB4m.svg)](https://asciinema.org/a/hZHlwXaPj9W1AQgADtrgYRB4m)

```log
debian@lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lpi4a:~$ uname -a
Linux lpi4a 5.10.113-sipeed-20240312+ #10 SMP PREEMPT Tue Mar 12 14:33:06 HKT 2024 riscv64 GNU/Linux
debian@lpi4a:~$ cat /etc/revyos-release 
BUILD_ID=20240202_141632
BUILD_DATE=20240202
RELEASE_ID=20240202
COMMIT_ID=09f8aabe9ed5ca28639a4df84bad507e746118d3
RUNNER_ID=7757184473
debian@lpi4a:~$ 
```

![machine](image-1.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
