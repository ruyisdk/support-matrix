# Armbian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz
- Reference Installation Document: https://en.opensuse.org/HCL:MangoPi_MQ-Pro

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz.raw.xz | dd bs=4M of=/dev/your/device iflag=fullblock oflag=direct status=progress; sync
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

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
