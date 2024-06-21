# openKylin 2.0 alpha RISC-V Test Report

## Test Environment

- System Version: openKylin 2.0 alpha RISC-V
- Download Link: [[Google Drive](https://www.openkylin.top/downloads/)](https://www.openkylin.top/downloads/)
- Reference Installation Document: [https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)


### Hardware Information

- Milk-V Pioneer Box v1.1
- One microSD card
- HDMI cable + Monitor

## Installation Steps

### Flashing Image

Use `unxz` to extract the image.
Use `dd` to write the image to the microSD card.

```bash
unxz /path/to/openKylin.img.xz
sudo dd if=/path/to/openKylin.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging to the system through the graphical interface.

Default username: `openKylin`
Default password: `openkylin`

## Expected Results

The system boots up normally and allows login through the graphical interface.

## Actual Results

The system boots up normally and login through the graphical interface is successful.

### Boot Log

![desktop_uname](./desktop_uname.png)

Serial port logs (from flashing image to system boot):
[![asciicast](https://asciinema.org/a/LrlBd3N4GZWvXRKHP8vikgTBF.svg)](https://asciinema.org/a/LrlBd3N4GZWvXRKHP8vikgTBF)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
