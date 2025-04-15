---
sys: xv6
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-04-15
---

# Debian Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- Reference Installation Document: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### Hardware Information

- Milk-V Duo S
- A USB power adapter
- A USB-A to C or USB C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires
- Milk-V Duo with pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card

```shell
dd if=milkv-duo_sdcard.img of=/dev/your/device bs=1M status=progress
```

## Expected Results

The system boots up normally and has output through the serial port.

## Actual Results

Unable to enter OpenSBI and U-Boot.

### Boot Log

```log
FSBL Jb28g9:gf2df47913:2024-02-29T16:35:38+08:00
 E:ra=0xc00a0f6
 E:RESET:panic:-1
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.

