---
sys: freebsd
sys_ver: "14.2"
sys_var: null

status: basic
last_update: 2025-04-11
---

# FreeBSD 14.2 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: FreeBSD 14.2
- Download Link: https://download.freebsd.org/releases/riscv/riscv64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-riscv-riscv64-mini-memstick.img.xz
- Reference Installation Document: https://wiki.freebsd.org/riscv/HiFiveUnmatched

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB Cable (comes with HiFive Unmatched)
- An ATX Power Supply
- A microSD Card, pre-flashed with Freedom U SDK (or any other U-Boot image)
- A USB Drive

## Installation Steps

For HiFive Unmatched there are multiple ways to boot, according to the [software reference manual](https://www.sifive.com/document-file/hifive-unmatched-software-reference-manual).

For booting FreeBSD, we have two options
- Choose a image that comes with U-Boot, (e.g. Freedom U SDK), flash it to microSD and set DIP switch to `MSEL[3:0]=1011` (factory default)
- Manually compile mainline U-Boot, flash it to SPI Flash, DIP switch set to `MSEL[3:0]=0110`
    - Requires an OS already installed and is capable of flashing SPI
    - See U-Boot's documentation here: https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### U-Boot on microSD

Ensure the dip switch is set to boot from the microSD card. If you haven't changed it, the factory default is to boot from the microSD card.

The dip switch should be set as follows: `MSEL[3:0]=1011`

#### Flashing Freedom U SDK

Download the demo-coreip-cli-unmatched.rootfs.wic.xz image from [here](https://github.com/sifive/freedom-u-sdk/releases/latest).

Uncompress and flash the image to the microSD card. Here, `/dev/sdc` is the location of the microSD card.

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdX status=progress
```

### U-Boot on SPI Flash

Assuming you already have an OS up and running on Unmatched.

You need to manually build U-Boot.

#### Building U-Boot

Below is only a rough guideline: you'll need to install required packages, and configure toolchains (both cross build and native build are okay).

For full documentation please check out U-Boot's official website: https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

```shell
git clone https://github.com/riscv/opensbi.git
pushd opensbi
make PLATFORM=generic -j$(nproc)
popd
wget https://github.com/u-boot/u-boot/archive/refs/tags/v2025.04.tar.gz
tar xvf v2025.04.tar.gz
cd u-boot-2025.04
export OPENSBI=../opensbi/build/platform/generic/firmware/fw_dynamic.bin
make sifive_unmatched_defconfig
make -j$(nproc)
```

#### Flash U-Boot images to SPI

The following steps are from the official U-Boot documentation.

```shell
sgdisk --clear -a 1 \
    --new=1:40:2087     --change-name=1:spl   --typecode=1:5B193300-FC78-40CD-8002-E86C45580B47 \
    --new=2:2088:10279  --change-name=2:uboot --typecode=2:2E54B353-1271-4842-806F-E436D6AF6985 \
    --new=3:10280:10535 --change-name=3:env   --typecode=3:3DE21764-95BD-54BD-A5C3-4ABE786F38A8 \
    /dev/mtdblock0
dd if=spl/u-boot-spl.bin of=/dev/mtdblock0 bs=4096 seek=5 conv=sync
dd if=u-boot.itb  of=/dev/mtdblock0 bs=4096 seek=261 conv=sync
```

### Flashing the Installation Image to the USB Drive

Uncompress the image and use the `dd` command to flash the image to USB.

`/dev/sdX` is the location of the USB drive.

```shell
xz -dk FreeBSD-14.2-RELEASE-riscv-riscv64-mini-memstick.img.xz
sudo dd if=FreeBSD-14.2-RELEASE-riscv-riscv64-mini-memstick.img of=/dev/sdX status=progress
```

## Logging into the System

Logging into the system via the onboard serial port (using the microUSB cable to connect to another computer).

Default username of LiveCD is `root`, no password required.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted normally and login via the onboard serial port was successful.

### Boot Log

```log
login: root
Apr 11 07:19:47  login[881]: ROOT LOGIN (root) ON ttyu0
FreeBSD 14.2-RELEASE (GENERIC) releng/14.2-n269506-c8918d6c7412

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List:        https://www.FreeBSD.org/lists/questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

To change this login announcement, see motd(5).
root@:~ # uname -a
FreeBSD  14.2-RELEASE FreeBSD 14.2-RELEASE releng/14.2-n269506-c8918d6c7412 GENERIC riscv
root@:~ # cat /etc/os-release
NAME=FreeBSD
VERSION="14.2-RELEASE"
VERSION_ID="14.2"
ID=freebsd
ANSI_COLOR="0;31"
PRETTY_NAME="FreeBSD 14.2-RELEASE"
CPE_NAME="cpe:/o:freebsd:freebsd:14.2"
HOME_URL="https://FreeBSD.org/"
BUG_REPORT_URL="https://bugs.FreeBSD.org/"
root@:~ # 
```

Screen record:

[![asciicast](https://asciinema.org/a/5dxQalniYzBi2YWpozwhs4jdv.svg)](https://asciinema.org/a/5dxQalniYzBi2YWpozwhs4jdv)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
