---
sys: opencloudos
sys_ver: 23
sys_var: null
status: basic
last_update: 2025-08-24
---

# Milk-V Megrez OpenCloudOS Test Report

## Test Environment

### Operating System Information

- Download Link: https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/ocs_developer_sdcard-megrez.img.xz

### Hardware Information

- Milk-V Megrez
- USB A to C / USB C to C Cable
- microSD Card
- DC 12V / ATX PSU

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `riscv666!`

## Actual Results

### Boot Log

[![asciicast](https://asciinema.org/a/YWKSf8oS0nbcdNVny1qE6Czow.svg)](https://asciinema.org/a/YWKSf8oS0nbcdNVny1qE6Czow)

## Test Conclusion

The system boots up normally and login through the serial port is successful.

