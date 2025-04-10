---
sys: guix
sys_ver: null
sys_var: null

status: CFT
last_update: 2025-04-10
---

# Guix System VisionFive 2 Test Report

## Test Environment

### Operating System Information

- Source code link: https://git.savannah.gnu.org/cgit/guix.git/tree/gnu/system/images/visionfive2.scm
- Download Link: https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image

### Hardware Information

- StarFive VisionFive 2
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A microSD Card Reader
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

username: root
no password

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
