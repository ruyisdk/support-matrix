---
sys: alpine
sys_ver: 3.20.0_alpha20231219 (edge)
sys_var: null

status: CFT
last_update: 2024-10-24
---

# Deepin VisionFive Test Report

## Test Environment

### System Information

- System Version: 3.20.0_alpha20231219 (edge)
- Download Link: https://dev.alpinelinux.org/~mps/riscv64/visionfive-v1-mmc.img.xz
- Reference Installation Document: https://arvanta.net/alpine/alpine-on-visionfive/

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xz -d visionfive-v1-mmc.img.xz
dd if=visionfive-v1-mmc.img of=/dev/<your-device> 
```

### Logging into the System
Log into system as root, without password. 

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

CFT

### Boot Log

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
