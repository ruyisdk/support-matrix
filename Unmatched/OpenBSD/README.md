---
sys: openbsd
sys_ver: "7.6"
sys_var: null

status: basic
last_update: 2025-04-11
---

# OpenBSD 7.6 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: OpenBSD 7.6
- Download Link: https://cdn.openbsd.org/pub/OpenBSD/7.6/riscv64/install76.img
- Reference Installation Document: https://cdn.openbsd.org/pub/OpenBSD/7.6/riscv64/INSTALL.riscv64

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card pre-flashed with Freedom U SDK
- A USB drive

## Installation Steps

For HiFive Unmatched there are multiple ways to boot, according to the [software reference manual](https://www.sifive.com/document-file/hifive-unmatched-software-reference-manual).

For booting OpenBSD, we have two options:
- Choose a image that comes with U-Boot, (e.g. Freedom U SDK), flash it to microSD and set DIP switch to `MSEL[3:0]=1011` (factory default)
- Manually compile mainline U-Boot, flash it to SPI Flash, DIP switch set to `MSEL[3:0]=0110`
    - Requires an OS already installed and is capable of flashing SPI
    - See U-Boot's documentation here: https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### U-Boot on microSD

Ensure the DIP switches are set to boot from the microSD card. The factory default is to boot from the microSD card if unchanged.

The DIP switch settings should be: `MSEL[3:0]=1011`

#### Flashing Freedom U SDK

Download the demo-coreip-cli-unmatched.rootfs.wic.xz image from [here](https://github.com/sifive/freedom-u-sdk/releases/latest).

Decompress and flash the image to the microSD card. Replace `/dev/sdc` with the location of your microSD card.

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdc status=progress
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

### Flashing Installation Image to USB Drive

Use the `dd` command to flash the image to the USB drive.

`/dev/sdX` is our drive here, change accordingly.

```bash
sudo dd if=install76.img of=/dev/sdX status=progress
```

### Logging into the System

Logging into the system via the onboard serial port using the microUSB cable connected to another computer.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

[![asciicast](https://asciinema.org/a/Mg53YxiOoNSGNImOs5WMei5uf.svg)](https://asciinema.org/a/Mg53YxiOoNSGNImOs5WMei5uf)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
