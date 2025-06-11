---
sys: deepin
sys_ver: eic7700-riscv64-25
sys_var: null
status: good
last_update: 2025-06-03
---

## Test Environment

### System Information

- System Version: deepin 25-crimson-preview EIC7700 20250422
- Download Link: https://deepin-community.github.io/sig-deepin-ports/images/riscv/download

### Hardware Information

- PINE64 StarPro64
- Power Adapter
- USB to TTL cable
- USB flash disk
- MicroSD card

## Installation Steps

### Connect with UART

Connect the USB to TTL cable to following pins:

| StarPro64   | USB UART |
|-------------|----------|
| GND (Pin 6) | GND      |
| TX (Pin 8)  | RX       |
| RX (Pin 10) | TX       |

See [the example](https://lupyuen.org/articles/starpro64.html#boot-without-microsd).

After plugged in, connect your computer with the USB-C UART serial port. For example:

``` shell
sudo screen /dev/ttyUSB0 115200
```

### Update bootloader

First we need to update the bootloader to the newest version, to ensure our system can be found and boot.

#### Getting bootloader

Download the latest `uboot-eic770x-rockos` from the most recent "build all" action from https://github.com/deepin-community/deepin-riscv-kernel/actions . We use [this version](https://github.com/deepin-community/deepin-riscv-kernel/actions/runs/15407166179/artifacts/3246357043) here.

Then, unpack the downloaded package, find `./uboot-eic770x-rockos/pine64-starpro64/bootloader_secboot_ddr5.bin` . Format the USB flash disk into a single FAT partition, and copy this file to the root of this partition. 

#### Flashing bootloader

Plug the USB flash disk into one of the USB-2.0 slot of the board, then power-on the board. Terminal will be connected via the UART serial port. Disrupt autoboot process to get into the `uboot` command line. Use the command below to read the bootloader file into the board:

``` shell
fatload usb 0 0x90000000 bootloader_secboot_ddr5.bin
```

> If you plugged the USB stick after the board have powered on, run `usb reset` to re-detect usb devices.

Use the following command to burn the file into SPI flash:

``` shell
es_burn write 0x90000000 flash
```

Restart to finish updating.

### Write the SD card

Make the SD card into 2 ext4 partitions: `boot` and `root`. 1GB of `boot` is enough. Then flash the corresponding image into the partition:

``` shell
sudo dd if=deepin-eic7700-riscv64-25-desktop-installer.boot.ext4 of=/dev/sdd1 status=progress
sudo dd if=deepin-eic7700-riscv64-25-desktop-installer.root.ext4 of=/dev/sdd2 status=progress
```

Insert the SD card into the board, then power-on the board.

### Initialize the System

If you've connected a display, you can complete the deepin Installation guide

If you don't have a GUI interface, you can login via UART:

Default username: `root`
Password: `deepin`

## Expected Results

The system should boot successfully, allowing login via the GUI.

## Actual Results

The system boots up successfully, and login via the GUI is successful.

![screenshot](./screenshot.jpeg)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
