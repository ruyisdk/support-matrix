---
sys: buildroot
sys_ver: v1.1.3
sys_var: null

status: basic
last_update: 2024-11-4
---

# BuildRoot Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Duo-V1.1.3
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- Milk-V Duo 64M
- A USB-A to C or USB C to C cable
- A microSD card

## Installation Steps

### Using `ruyi` CLI to Flash the Image to the microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Thu Aug 1 13:44:06 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /proc/cpuinfo 
processor	: 0
hart		: 0
isa		: rv64imafdvcsu
mmu		: sv39
```

Screen recording (from flashing the image to system login):

[![asciicast](https://asciinema.org/a/1Vp9JeYdRiyORXXGFlx5F9JY0.svg)](https://asciinema.org/a/1Vp9JeYdRiyORXXGFlx5F9JY0)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
