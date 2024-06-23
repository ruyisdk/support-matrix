# Debian DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/DongshanPI/NezhaSTU-ReleaseLinux/releases/download/v0.1.0-alpha/DshanNezhaSTU-APTok-Sdcard.img.gz
- Reference Installation Document: https://github.com/DongshanPI/NezhaSTU-ReleaseLinux

### Hardware Information

- DongshanPI-Nezha STU
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image

Use `gzip` to decompress the image.
Clear your sd card.
Use `dd` to write the image to the microSD card.

```bash
gzip -kd /path/to/DshanNezhaSTU-APTok-Sdcard.img.gz
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/DshanNezhaSTU-APTok-Sdcard.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `100ask`

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing the image to logging into the system):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
