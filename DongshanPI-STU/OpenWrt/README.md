# OpenWrt 23.05.2 DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=dongshan_nezha_stu
- Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> The OpenWrt Firmware Selector allows you to custom build a system image online with the pre-installed packages you need. For this test, we used the original image without any modifications.

### Hardware Information

- DongshanPI-Nezha STU
- A USB-A power supply
- A USB-A to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flash Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
gzip -kd openwrt-d1-generic-dongshan_nezha_stu-ext4-sdcard.img.gz
sudo dd if=openwrt-d1-generic-dongshan_nezha_stu-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the image to system login):

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
