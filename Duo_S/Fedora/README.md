---
sys: fedora
sys_ver: "41"
sys_var: null

status: basic
last_update: 2024-11-24
---

# Fedora 41 Milk-V DuoS Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 41
- Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/DuoS/images/latest/
- Reference Installation Document: https://fedoraproject.org/wiki/Architectures/RISC-V/Installing

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo S
- A USB power adapter
- A USB-A to C or USB-C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires
- The Milk-V Duo has pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Flashing the Image to microSD Card Using `dd`

```shell
zcat milkv-duos-fedora-minimal.img.gz | sudo dd of=/dev/sda bs=4M iflag=fullblock status=progress 
```

### Logging into the System

Log into the system via the serial port.

Username: `root`
Password: `riscv`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

Screen recording of the boot process:

[![asciicast](https://asciinema.org/a/5dJWtw2u1EB1f78SyIeFJ4Jqd)](https://asciinema.org/a/5dJWtw2u1EB1f78SyIeFJ4Jqd)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
