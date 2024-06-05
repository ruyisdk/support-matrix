# Tina Linux Mangopi MQ Test Report

## Test Environment

### Operating System Information

- Download Link: https://mangopi.org/_media/mq-r-f133-rtl8189fs-5113-dns-uart0.zip
- Reference Installation Document: https://mangopi.org/mangopi_mq

### Hardware Information

- Mangopi MQ
- One microSD card
- One USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Flashing Image

Download and extract, then use `dd` to flash the image to the SD card:
```bash
sudo dd if=mq-r-f133-rtl8189fs-5113-dns-uart0.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system boots up normally and login through the onboard serial port is possible.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Log

Screen recording (from flashing image to system login):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT


> This doc was automatically translated by GPT and has not been proofread yet. Please give us feedback in issue if any omissions.
