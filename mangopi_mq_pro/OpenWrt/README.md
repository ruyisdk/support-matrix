# OpenWrt MangoPi MQ Pro Test Report

## Test Environment

### System Information

- Download Link (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=mangopi_mq_pro
- Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> In OpenWrt Firmware Selector, you can customize and build system images online, adding the pre-installed software packages you need. For this test, we used the unmodified original image.

### Hardware Information

- MangoPi MQ Pro
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Flashing the Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
gzip -kd openwrt-d1-generic-mangopi_mq_pro-ext4-sdcard.img.gz
sudo dd if=openwrt-d1-generic-mangopi_mq_pro-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing the image to login):

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
