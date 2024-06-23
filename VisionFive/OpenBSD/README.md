# OpenBSD 7.5 VisionFive Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
    - Official Fedora Image (for extracting dtb files): https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst
- Reference Installation Document: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
    - Community Tutorial: https://gist.github.com/csgordon/74658096f7838382b40bd64e11f6983e

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger
- Wired Internet Connection

## Installation Steps

### Extracting dtb File

Decompress the Fedora image, mount the boot partition, and copy the `jh7100-starfive-visionfive-v1.dtb` file from the dtb folder.

### Flashing Installation Image

Use `gzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
wget https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/install75.img
sudo dd if=install75.img of=/dev/your-device bs=1M status=progress
```

Place the dtb file into the EFI root directory:

```bash
mkdir -p mnt
sudo mount /dev/your-device-p1 mnt
cp jh7100-starfive-visionfive-v1.dtb mnt/
sudo umount mnt
```

### Booting the System

Manually interrupt the u-boot process and input the boot command:
```bash
load mmc 0:1 0x88000000 jh7100-starfive-visionfive-v1.dtb
load mmc 0:1 0x84000000 efi/boot/bootriscv64.efi
bootefi 0x84000000 0x88000000
```

Follow the installation flow and place the dtb file into the EFI root directory again (if it was overwritten).

### Persistent Uboot

```bash
env default -a -f
setenv bootcmd "load mmc 0:1 0x88000000 jh7100-starfive-visionfive-v1.dtb; load mmc 0:1 0x84000000 efi/boot/bootriscv64.efi; bootefi 0x84000000 0x88000000"
saveenv
```

### Logging into the System

Login via the serial port.

User and password are set during installation.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to system login):

[![asciicast](https://asciinema.org/a/dNtdx7un7CxaAbKEqeFsWF9Cw.svg)](https://asciinema.org/a/dNtdx7un7CxaAbKEqeFsWF9Cw)

```log
Sat Mar 23 10:02:30 CST 2024

OpenBSD/riscv64 (plct.my.domain) (console)

login: root
Password:
OpenBSD 7.5 (GENERIC.MP) #1: Fri Mar 22 19:01:44 MDT 2024

Welcome to OpenBSD: The proactively secure Unix-like operating system.

Please use the sendbug(1) utility to report bugs in the system.
Before reporting a bug, please try to reproduce it with the latest
version of the code.  With bug reports, please try to ensure that
enough information to reproduce the problem is enclosed, and if a
known fix for it exists, include that as well.

You have new mail.
plct# uname -a
OpenBSD plct.my.domain 7.5 GENERIC.MP#1 riscv64
plct# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test partially successful.
