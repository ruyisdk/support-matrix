---
sys: rtthread
sys_ver: null
sys_var: standard

status: basic
last_update: 2024-12-05
---

# RT-Thread M0sense Test Report

## Test Environment

### Operating System Information
- Source Code Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/bouffalo_lab/README.md
- Toolchain: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### Hardware Information

- Sipeed M0sense (BL702)
- A USB A to C or C to C cable
- One Dupont Line

## Installation Steps

The following steps are tested on Arch Linux, but should be applicable to all major Linux distributions.

### Preparing the System Environment

Install the required packages:

```shell
sudo apt install -y scons libncurses5-dev device-tree-compiler
# or on Arch Linux: sudo pacman -S scons dtc ncurses 
```

Get the toolchain:

```shell
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

Update the following paths as needed:
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

### Fetching the Source Code and Compiling the Firmware

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/bouffalo_lab/bl70x
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
```
The generated firmware file is at `./rtthread.bin`

### Flash firmware

Short the `BOOT` pin and the `3V` pin on the board with a Dupont cable, then power it on to enter flashing mode.

Flash the firmware to board (the board has built-in serial device):
```shell
cd ../
sudo ./bouffalo_flash_cube.sh bl702 /dev/ttyACM0
```
(The script will automatically detect and download `bouffalo_flash_cube` to the compilation directory.)

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the serial port.

## Actual Results

The system booted successfully, and login through the serial port was successful.

### Boot Log

Note that user inputs may not be able to echo immediately in `msh`.
```log
Now can [init] goio set o[rgbled_task] start loop

Now: command not found.
bouffalolab />
bouffalolab />help
shell commands list:
memtrace
help

bouffalolab />memtrace
write memory: 0x42000000 0xabcd 10
read memory: 0x42000000 10
bouffalolab />hello
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
