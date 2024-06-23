# Ubuntu MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: [Ubuntu 23.10](https://cdimage.ubuntu.com/releases/23.10/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz)
- Reference Installation Document: [MangoPi MQ Pro Guide](https://mangopi.org/mqpro)

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xz -kd /path/to/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz
sudo dd if=/path/to/ubuntu-23.10-preinstalled-server-riscv64+nezha.img  of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `ubuntu`
Default Password: `ubuntu`

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