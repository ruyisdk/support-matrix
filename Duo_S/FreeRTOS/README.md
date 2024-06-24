# FreeRTOS Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.4 LTS x86_64
- System Version: Duo-V1.1.0
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
    - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB Power Adapter
- A USB-A to C or USB C to C Cable for powering the development board
- A microSD Card
- A USB Card Reader
- A USB to UART Debugger (e.g., CP2102, FT2232, etc. Be aware that WCH CH340/341 series will cause garbled text output, DO NOT USE)
- Three DuPont Wires

## Installation Steps

### Building the mailbox-test Binary

Clone the `duo-examples` repository locally and build it.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

### Flashing Image to microSD Card with `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

#### Copying the Built Binary to the microSD Card

```shell
sudo mount /dev/sdX2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo eject /dev/sdX2
```

With this, the storage card is prepared. Insert it into the development board and get ready to boot.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally. Upon logging in via the onboard serial port and running the `mailbox_test` binary, the onboard blue LED should briefly turn on and then off.

(In standby mode, the blue LED should blink.)

## Actual Results

The system booted successfully, and login via the onboard serial port was successful. The official Duo S image does not currently support wiringX, so `mailbox_test` did not run correctly, though the system detected the RTOS device.

### Boot Information

```log
[root@milkv-duo]~# ls
mailbox_test
[root@milkv-duo]~# insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device
[root@milkv-duo]~# ./mailbox_test
Error loading shared library libwiringx.so: No such file or directory (needed by ./mailbox_test)
[root@milkv-duo]~# find / -name *rtos*
find: /proc/338: No such file or directory
/sys/devices/platform/1900000.rtos_cmdqu
/sys/bus/platform/devices/1900000.rtos_cmdqu
/sys/firmware/devicetree/base/rtos_cmdqu
[root@milkv-duo]~#
```

Screen recording:

[![asciicast](https://asciinema.org/a/y8YaDpY5YnKWgw4ydZPVDf4YB.svg)](https://asciinema.org/a/y8YaDpY5YnKWgw4ydZPVDf4YB)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test partial success.
