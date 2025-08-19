---
sys: openeuler
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-04-05
---

# openEuler/oERV Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- System version: openEuler RISC-V 20241231
- Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241231/v0.5/k1/
- Reference Installation Document: https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
tar -xvf openEuler-Mega24.03SP1-V1-xfce-k1-testing.img.zst
sudo dd if=openEuler-Mega24.03SP1-V1-xfce-k1-testing.img of=/dev/sdX bs=4M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root` or `openeuler`
Default password: `openEuler12#$`

## Expected Results

The system should boot up normally and allow login through the onboard serial port and/or HDMI.

## Actual Results

No outputs from both the serial console and HDMI.

### Boot Log

No outputs.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
