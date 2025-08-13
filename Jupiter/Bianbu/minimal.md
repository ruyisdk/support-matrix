---
sys: bianbu
sys_ver: 3.0
sys_var: minimal
status: basic
last_update: 2025-08-13
---

# Milk-V Jupiter Bianbu Test report

## Test Environment

### System Information

- Download Link: https://archive.spacemit.com/image/k1/version/bianbu/v3.0/
- Reference Install manual: https://milkv.io/docs/jupiter/getting-started/boot

### Hardware Information

- Milk-V Jupiter Board (Key Stone K1/M1, 4G/8G/16G)
    -  M1 + 16G is tested in this report
- DC 5.5*2.5mm 12V PSU / USB PD (12V required) / ATX PSU
    - 12V 3A is recommended for DC PSU, if more power is needed (e.g. using PCI-E peripherals) then ATX PSU is preferred
    - USB Type-C port isn't available when flashing using `titanflasher` or `fastboot`, external DC/ATX PSU is required
    - In this test report we're using a 12V 3A DC power supply
- A microSD card, or eMMC module, or NVMe SSD
    - Boot priority: `microSD > NVMe SSD > eMMC`
    - When booting from SD, the board won't go through SPI Flash
    - If either NVMe SSD or eMMC module is installed, `titanflasher` will only flash U-Boot to SPI Flash
    - In this test report we're using NVMe SSD, model: Samsung PM961 128GB
- A USB to UART debugger
    - In this test report we're using CH343P
- USB Type-C cables (depends on your usage, at least one for flashing OS image)

## Installation Steps

### Flash Image (microSD Card)

**Please make sure to choose the file ending with `.img.zip`**

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
unzip bianbu-25.04-minimal-k1-v3.0-release-20250725114639.img.zip
sudo dd if=bianbu-25.04-minimal-k1-v3.0-release-20250725114639.img of=/dev/<your-device> bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `bianbu`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system should boot normally and allow login via the onboard serial port.

### Boot Log

[![asciicast](https://asciinema.org/a/P5ESOCw24RkgWlMo2ARyWUEiz.svg)](https://asciinema.org/a/P5ESOCw24RkgWlMo2ARyWUEiz)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
