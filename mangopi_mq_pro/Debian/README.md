# Debian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
- Reference Installation Document: https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unzip` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
unzip /path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
sudo dd if=/path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `rvboards`

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