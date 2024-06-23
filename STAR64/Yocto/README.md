# Yocto Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
- Reference Installation Document: https://github.com/Fishwaldo/meta-pine64

### Hardware Information

- Development Board: Star64
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

After downloading, extract and flash the image (example is using the Plasma version):
```bash
wget https://github.com/Fishwaldo/meta-pine64/releases/download/v2.1/star64-image-plasma-star64.wic.bz2
bzip2 -kd star64-image-plasma-star64.wic.bz2
sudo dd if=star64-image-plasma-star64.wic of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port.

Upon startup, the system will prompt the user to manually set up username, password, timezone, language, etc.

For the Xfce version, you must complete the configuration to enter the desktop.

Configuration can be done through the serial port. If a keyboard and monitor are connected, you can also configure through the keyboard.

## Expected Results

The development board outputs boot information normally.

## Actual Results

CFT

### Boot Log

Screen recording (from system flashing to boot):
```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
