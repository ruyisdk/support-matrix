# Armbian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://disk.yandex.ru/d/da8qJ8wyE1hhcQ/Nezha_D1/ArmbianTV/20220722/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz
- Reference Installation Document: https://mangopi.org/mqpro

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xz -kd /path/to/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz
sudo dd if=/path/to/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
You will set a password on the first login.

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
