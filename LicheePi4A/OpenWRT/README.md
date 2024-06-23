# OpenWRT LPi4A Test Report

## Test Environment

### System Information

- System Version: OpenWRT
- Download Link: [https://github.com/chainsx/openwrt-th1520/releases](https://github.com/chainsx/openwrt-th1520/releases)
- Reference Installation Document: [https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)
- fastboot Links:
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 64GB eMMC)
- Power Adapter
- A microSD card
- A USB to UART debugger

## Installation Steps

### Flashing Image

Use `gzip` to extract the image.
Use `dd` to flash the image to the microSD card.

```bash
gzip -d /path/to/openwrt.img.xz
sudo dd if=/path/to/openwrt.img of=/dev/your_device bs=1M status=progress
```

### Flashing Bootloader

Enter fastboot mode.
- Confirm the boot switch is set to eMMC for the official version.
- Press the BOOT button while powering up.
- (Refer to the official tutorial)
Use fastboot to flash the u-boot with the following commands.

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### Logging into the System

Logging into the system via serial port.

Upon initial boot, it will automatically log in as the root user.

## Expected Results

The system should boot up properly and allow login via the onboard serial port.

## Actual Results

The system boots up successfully and allows login via the onboard serial port.

### Boot Log

Screen recording (from flash the image to logging into the system):

[![asciicast](https://asciinema.org/a/DNRiqiUpdDxlAWHnSkQTvqsNt.svg)](https://asciinema.org/a/DNRiqiUpdDxlAWHnSkQTvqsNt)

```log
BusyBox v1.36.1 (2023-11-11 16:56:38 UTC) built-in shell (ash)


                              |/
                             _/_
    +-----------------+ ____  O
    |                 ||    \
    |                 ||     \     O     O
    |   ___   RISC-V  ||  ___ |   /|\_  /|\_
    +--/ o \----------++-/ o \+  _/ \  _/ \
       \___/             \___/
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r0-707f69c
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
