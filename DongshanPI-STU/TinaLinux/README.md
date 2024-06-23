# Tina Linux DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: [Link](https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7) Password: qcw7
- Reference Installation Document: [Link](https://d1.docs.aw-ol.com/study/study_1tina/)

### Hardware Information

- DongshanPI-Nezha STU
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Compiling SDK

After downloading, you can find the SDK under DongshanNezhaSTU-TinaV2.0-SDK.
Merge and extract the SDK:
```bash
cat tina-d1-h.tar.bz2.* | tar -zxv
```

Compile and package:
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### Flashing Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=tina_d1-h.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

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
