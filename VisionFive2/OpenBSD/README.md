# OpenBSD 7.5 VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: OpenWRT SnapShot
- Download Link: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
    - dtb File: https://marc.info/?l=openbsd-misc&m=169046816826966&w=2
- Reference Installation Document: [https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
    - Community Tutorial: https://gist.github.com/csgordon/74658096f7838382b40bd64e11f6983e

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger
- Wired Internet Connection

## Installation Steps

### Flashing the Installation Image

Use `gzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
wget https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/install75.img
sudo dd if=install75.img of=/dev/your-device bs=1M status=progress
```

Place the dtb file in the EFI root directory:

```bash
mkdir -p mnt
sudo mount /dev/your-device-p1 mnt
cp jh7110-starfive-visionfive-2-v1.3b.dtb mnt/
sudo umount mnt
```

### Booting the System

Manually interrupt the u-boot process and input the boot command:
```bash
load mmc 1:1 ${fdt_addr_r} jh7110-starfive-visionfive-2-v1.3b.dtb
load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

Follow the installation process and place the dtb file again in the EFI root directory (if it has been overwritten).

### Persist Uboot

```bash
env default -a -f
setenv bootcmd "load mmc 1:1 ${fdt_addr_r} jh7110-starfive-visionfive-2-v1.3b.dtb; load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

### Logging into the System

Log into the system via the serial port.

User and password are set during installation.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from image flashing to system login):

[![asciicast](https://asciinema.org/a/Cz0uvucqmbP1P0yzgZ2hnMbZY.svg)](https://asciinema.org/a/Cz0uvucqmbP1P0yzgZ2hnMbZY)

```log
Tue Mar 26 22:01:09 CST 2024

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

Test successful.
