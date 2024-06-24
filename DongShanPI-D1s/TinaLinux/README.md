# Tina Linux DongshanPI-D1s Test Report

## Test Environment

### Operating System Information

- Download Link: https://gitlab.com/dongshanpi/tools/-/raw/main/tina_d1s-nezha_sd_uart0.zip
- Reference Installation Document: https://dongshanpi.com/DongshanPI-D1s/03-1_FlashSystem/

### Hardware Information

- DongshanPI-D1s
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Flashing Image

After downloading and extracting, use `dd` to flash the image to the SD card:
```bash
sudo dd if=tina_d1s-nezha_sd_uart0.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing image to logging into the system):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
