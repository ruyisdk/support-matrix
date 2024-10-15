---
sys: deepin
sys_ver: null
sys_var: null

status: cft
last_update: 2024-06-21
---

# Deepin HiFive Unmatched Report

## Test Environment

### System Information

- System Version: Deepin
- Download Link: https://cdimage.deepin.com/RISC-V/Unmatched-image/deepin-sifive.7z
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/Unmatched-image/README.txt

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- NVME SSD

## Installation Steps

### Flashing Image

**The image is NOT for SD card, a NVME SSD is needed!**

Use `7z` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
7z e deepin-sifive.7z
sudo dd if=deepin-sifive.img of=/dev/your/device bs=1M status=progress
```


### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `Riscv2022#`

Default Username: `deepin`
Default Password: `deepin#`

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing the image to logging into the system):


```log


```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
