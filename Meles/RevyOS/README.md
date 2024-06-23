# RevyOS Meles Version Test Report

## Test Environment

### Operating System Information

- System Version: root-meles-20231210_134926.ext4.tar.gz
- Download Link: https://github.com/milkv-meles/meles-images/releases
- Reference Installation Document: https://milkv.io/zh/docs/meles/getting-started/boot

### Hardware Information

- Milk-V Meles 4GB/8GB
- eMMC module > 16GB
- A USB A to C cable
- Optional: A USB-TTL Debugger
- Optional: Keyboard, monitor, mouse (for graphical interface testing)

## Installation Steps

### Flashing Image using `fastboot` onto the Development Board

Download the system image and U-Boot SPL from [GitHub release](https://github.com/milkv-meles/meles-images/releases).

U-Boot with SPL version selection:
- 4GB Version -> u-boot-with-spl-**single**rank.bin
- 8GB Version -> u-boot-with-spl-**dual**rank.bin

Press and hold the download button near the GPIO interface on the development board and connect the board to the computer.

Check connection status:

```shell
$ lsusb | grep T-HEAD
Bus 001 Device 045: ID 2345:7654 T-HEAD USB download gadget
```

Next, use `fastboot` to flash the image.

If `fastboot` doesn't recognize the device or you encounter flashing issues, check the device connection and try running `fastboot` as a privileged user (`sudo`).

```shell
fastboot flash ram u-boot-with-spl-dualrank.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-dualrank.bin
fastboot flash boot boot.ext4
tar xvf root-meles-20231210_134926.ext4.tar.gz
fastboot flash root root-meles-20231210_134926.ext4
```

### Logging into the System

Logging into the system via serial port or graphical interface.

Default Username: `debian`
Default Password: `debian`

## Expected Results

The system should boot up normally and allow login through the serial port.

## Actual Results

CFT

### Boot Information

CFT

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
