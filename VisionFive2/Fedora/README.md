---
sys: fedora
sys_ver: 
sys_var: null

status: good
last_update: 2025-01-15
---

# Fedora VisionFive2 Test Report

## Test Environment

### System Information

- System Version: Fedora 33
- Download Link: https://images.fedoravforce.com/VisionFive%20V2

### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -d /path/to/fedora.raw.zst
sudo dd if=/path/to/fedora of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

Default Username: `root`
Default Password: `starfive`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
