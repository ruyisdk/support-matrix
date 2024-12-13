---
sys: buildroot
sys_ver: "20241129"
sys_var: null

status: cft
last_update: 2024-06-21
---

# BuildRoot LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: 20241129
- Download Link: [https://github.com/sipeed/LicheeRV-Nano-Build/releases](https://github.com/sipeed/LicheeRV-Nano-Build/releases)
- Reference Installation Documentation: [https://github.com/sipeed/LicheeRV-Nano-Build/releases](https://github.com/sipeed/LicheeRV-Nano-Build/releases)

### Hardware Information

- LicheeRV Nano
- A Type-C power cable
- A UART to USB debugger

## Installation Steps

### Using `dd` to Flash Image onto microSD Card

Download the image, then decompress and flash it:

```shell
gzip -kd 2024-11-29-11-46-540e94.img.xz
sudo dd if=2024-11-29-11-46-540e94.img of=/dev/your_device bs=1M status=progress

```

### Logging into the System

Logging into the system via serial port.

Default Username: root
Default Password: root

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing image to login):


```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
