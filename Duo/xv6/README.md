---
sys: xv6
sys_ver: null
sys_var: null

status: basic
last_update: 2025-04-15
---

# Debian Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- Reference Installation Document: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### Hardware Information

- Milk-V Duo 64M
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

The system boots up normally and has output through the serial port.

### Boot Log

```log
U-Boot 2021.10 (Feb 29 2024 - 16:53:07 +0800)cvitek_cv180x

DRAM:  63.3 MiB
gd->relocaddr=0x83ef8000. offset=0x3cf8000
MMC:   cv-sd@4310000: 0
Loading Environment from <NULL>... OK
In:    serial
Out:   serial
Err:   serial
Net:
Warning: ethernet@4070000 (eth0) using random MAC address - 32:59:49:10:31:37
eth0: ethernet@4070000
Hit any key to stop autoboot:  0
Boot from SD ...
switch to partitions #0, OK
mmc0 is current device
1590733 bytes read in 71 ms (21.4 MiB/s)
## Loading kernel from FIT Image at 81400000 ...
   Using 'config-cv1800b_milkv_duo_sd' configuration
   Trying 'kernel-1' kernel subimage
   Verifying Hash Integrity ... crc32+ OK
## Loading fdt from FIT Image at 81400000 ...
   Using 'config-cv1800b_milkv_duo_sd' configuration
   Trying 'fdt-1' fdt subimage
   Verifying Hash Integrity ... sha256+ OK
   Booting using the fdt blob at 0x8158315c
   Loading Kernel Image
   Decompressing 1585152 bytes used 2ms
   Loading Device Tree to 00000000836ac000, end 00000000836aff73 ... OK

Starting kernel ...


xv6 kernel is booting

SBI specification v0.3 detected
SBI TIME extension detected
SBI IPI extension detected
SBI RFNC extension detected
SBI HSM extension detected

init: starting sh
                 $
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

