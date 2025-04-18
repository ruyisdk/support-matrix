---
sys: fedora
sys_ver: "41"
sys_var: null

status: cft
last_update: 2025-01-23
---

# Milk-V Megrez Test Report

## Test Environment

### Operating System Information

- Download Link: https://images.fedoravforce.org/Megrez
- Reference Installation Document: https://milkv.io/zh/docs/megrez/getting-started/boot

### Hardware Information

- Development Board: Milk-V Megrez
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

After downloading, extract and flash the image (example is using the desktop version):
```bash
gzip -d fedora-disk-multi-desktops_eswin_eic7700-sda.raw.gz
sudo dd if=fedora-disk-multi-desktops_eswin_eic7700-sda.raw of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port.

Default username: `root`
Default password: `riscv`

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
