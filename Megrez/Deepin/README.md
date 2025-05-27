---
sys: deepin
sys_ver: eic7700-riscv64-25
sys_var: null

status: good
last_update: 2025-05-27
---

## Test Environment

### Operating System Information

- System Version: deepin 25-crimson-preview EIC7700 20250422
- Download Link: https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
- Reference Installation Document: https://milkv.io/zh/docs/megrez/getting-started/boot

### Hardware Information

- Development Board: Milk-V Megrez
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

First, partition your SD Card into `boot` and `root`. Then flash the corresponding image into the partition:

``` shell
sudo dd if=deepin-eic7700-riscv64-25-desktop-installer.boot.ext4 of=/dev/sdd1 status=progress
sudo dd if=deepin-eic7700-riscv64-25-desktop-installer.root.ext4 of=/dev/sdd2 status=progress
```

### Initialize the System

If you've connected a display, you can complete the deepin Installation guide

If you don't have a GUI interface, you can login via UART:

Default username: `root`
Password: `deepin`

## Expected Results

The system should boot successfully, allowing login via the GUI. RuyiSDK IDE Running successful.

## Actual Results

The system boots up successfully, and login via the GUI is successful. RuyiSDK IDE Running successful.

![screenshot](./screenshot.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Successful
