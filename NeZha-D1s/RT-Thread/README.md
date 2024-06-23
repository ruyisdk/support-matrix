# RT-Thread D1s NeZha Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/allwinner/d1s/README-M7.md

### Hardware Information

- D1s NeZha
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

Set up the toolchain:
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

Unzip the tools in xfel_v1.2.9.7z; prepare to use xfel to flash to eMMC:
```bash
xfel write 8192 boot0_sdcard_sun20iw1p1_f133.bin
xfel sd write 57344 sd.bin
xfel reset
```


### Logging into the System

Login to the system via the serial port.

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

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
