# Tina Linux MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: [Link](https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol) Password: awol
- Reference Installation Document: [Installation Guide](https://d1.docs.aw-ol.com/study/study_1tina/)

### Hardware Information

- MangoPi MQ Pro
- A microSD card
- USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Compiling the SDK

Download and extract the SDK, then add a new target:
```bash
git clone https://github.com/Tina-Linux/Tina_d1x_mangopi-sbc.git
cp -r Tina_d1x_mangopi-sbc tina_d1_open_v2_2
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

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing image to system login):
```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT