---
sys: xv6
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-04-15
---

# xv6 Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- Reference Installation Document: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### Hardware Information

- Milk-V Duo 256M
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

You might want to replace the `fip.bin` in the image with the one from Milk-V's official Buildroot SDK.

## Expected Results

The system boots up normally and has output through the serial port.

## Actual Results

Unable to enter the kernel from U-Boot.

### Boot Log

```log

U-Boot 2021.10 (Nov 22 2024 - 11:42:00 +0800) cvitek_cv181x

DRAM:  254 MiB
gd->relocaddr=0x8b0c8000. offset=0xaec8000
MMC:   cv-sd@4310000: 0
Loading Environment from nowhere... OK
In:    serial
Out:   serial
Err:   serial
Net:
Warning: ethernet@4070000 (eth0) using random MAC address - 9a:dc:e9:b6:f3:45
eth0: ethernet@4070000
Hit any key to stop autoboot:  0
Boot from SD ...
switch to partitions #0, OK
mmc0 is current device
1578445 bytes read in 72 ms (20.9 MiB/s)
## Loading kernel from FIT Image at 81800000 ...
Could not find configuration node
ERROR: can't get kernel image!
cv181x_c906#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.

