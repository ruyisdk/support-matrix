---
sys: netbsd
sys_ver: null
sys_var: null

status: cft
last_update: 2024-10-08
---

# NetBSD MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing the Installation Image

Use `gzip` to decompress the image.
Use `dd` or `balenaEtcher` to flash the image to the microSD card.

```bash
sudo dd if=riscv64.img of=/dev/<your-device> bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`, without password.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing image to login):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT

