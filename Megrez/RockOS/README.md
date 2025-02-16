---
sys: rockos
sys_ver: 2025-0117
sys_var: null

status: cft
last_update: 2025-01-23
---

# Milk-V Megrez Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/milkv-megrez/megrez-build/releases/tag/2025-0117
- Reference Installation Document: https://milkv.io/zh/docs/megrez/getting-started/boot

### Hardware Information

- Development Board: Milk-V Megrez
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

After downloading, unzip and flash the image (using the xfce version as an example):
```bash
cat sdcard-rockos-milkv-megrez-2025-0117.img.zip.001 sdcard-rockos-milkv-megrez-2025-0117.img.zip.002 > sdcard-rockos-milkv-megrez-2025-0117.img.zip
unxz -k sdcard-rockos-milkv-megrez-2025-0117.img.zip
sudo dd if=sdcard-rockos-milkv-megrez-2025-0117.img.zip of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port.

Default username: `debian`
Default password: `debian`

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the system to booting up):
```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT