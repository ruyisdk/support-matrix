---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-04-28
---

# FreeRTOS Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 24.04 LTS x86_64
- System Version: Duo-V1.1.4
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

The system booted successfully, and login via the onboard serial port was achieved without issues.

The mailbox_test binary executed successfully, and the behavior of the LED matched expectations.

### Boot Information

```log
[root@milkv-duo]~#
[root@milkv-duo]~# ls
mailbox_test
[root@milkv-duo]~# ./mailbox_test
[root@milkv-duo]~# find / -name *rtos*
find: /proc/355: No such file or directory
/sys/class/misc/cvi-rtos-cmdqu
/sys/class/cvi-rtos-cmdqu
/sys/devices/platform/1900000.rtos_cmdqu
/sys/devices/virtual/misc/cvi-rtos-cmdqu
/sys/bus/platform/devices/1900000.rtos_cmdqu
/sys/bus/platform/drivers/cvi-rtos-cmdqu
/sys/bus/platform/drivers/cvi-rtos-cmdqu/1900000.rtos_cmdqu
/sys/firmware/devicetree/base/rtos_cmdqu
/sys/firmware/devicetree/base/reserved-memory/rtos_dram@0x9fe00000
/dev/cvi-rtos-cmdqu
[root@milkv-duo]~#
```

Screen recording:

[![asciicast](https://asciinema.org/a/3JlGE9DBVemEnRqIffzKhNKcT.svg)](https://asciinema.org/a/3JlGE9DBVemEnRqIffzKhNKcT)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
