# BuildRoot DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/DongshanPI/buildroot_dongshannezhastu
- Reference Installation Document: https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/

### Hardware Information

- DongshanPI-Nezha STU
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Compiling SDK

Download the SDK:
```bash
git clone  https://github.com/DongshanPI/buildroot_dongshannezhastu
cd buildroot_dshannezhastu
git submodule update --init --recursive
git submodule update --recursive --remote
```

Compile the SD card image:
```bash
cd buildroot-awol/
make  BR2_EXTERNAL="../br2lvgl  ../br2qt5 ../br2nezhastu"  dongshannezhastu_sdcard_core_defconfig
make -j$(nproc)
```

### Flashing Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=dongshannezhastu-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

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
