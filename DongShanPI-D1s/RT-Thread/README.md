# RT-Thread DongshanPI-D1s Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/allwinner/d1s/README-MQ.md

### Hardware Information

- DongshanPI-D1s
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Download Code

Download the RT-Thread code:
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
git clone -b rt-smart https://gitee.com/rtthread/rt-thread.git
```

Configure the toolchain:
```bash
python3 get_toolchain.py riscv64
source smart-env.sh riscv64
```

Compile the kernel:
```bash
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

### Flashing Image

Partition the SD card: reserve 8M of space at the beginning to accommodate the bootloader:
```bash
sudo fdisk /dev/your/device
# In fdisk
o
n
p
1
16384
w
```

Flash the system onto the SD card:
```bash
sudo dd if=boot0_sdcard_sun20iw1p1.bin of=/dev/your/device bs=1024 seek=8
sudo dd if=sd.bin of=/dev/your/device bs=1024 seek=56
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
