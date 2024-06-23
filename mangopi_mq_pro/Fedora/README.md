# Fedora MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://openkoji-bj.isrc.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
- Reference Installation Document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -kd fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220117-135925.n.0-sda.raw.zst
sudo dd if=/path/to/fedora-riscv64-d1-developer-xfce-rawhide-Rawhide-20220104-012902.n.0-sda.raw of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `riscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing image to login):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
