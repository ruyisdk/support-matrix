---
sys: bianbu
sys_ver: null
sys_var: null

status: cft
last_update: 2024-07-19
---

# Milk-V Jupiter Bianbu Test report

## Test Environment

### System Information

- Download Link: https://github.com/milkv-jupiter/jupiter-bianbu-build/releases
- Reference Install manual: https://milkv.io/docs/jupiter/getting-started/boot

### Hardware Information

- Milk-V Jupiter Board
- DC or USB PD power adapter
- A microSD card, or install eMMC module
- A USB to UART debugger

## Installation Steps

### Flash Image (microSD Card)

**Please make sure to choose the file ending with `.img.zip`**

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

Notice: there are two file, zip.001 and zip.002, download them all to extract the image.

```bash
sudo dd if=/path/to/milkv-jupiter-bianbu-23.10-desktop-k1-v1.0.8-release-2024-0716.img of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `milkv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

CFT

### Boot Log

CFT

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT