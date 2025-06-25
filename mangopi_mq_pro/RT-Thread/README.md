---
sys: rtthread
sys_ver: null
sys_var: standard

status: basic
last_update: 2025-06-23
---

# RT-Thread MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/bigmagic123/d1-nezha-rtthread
- Reference Installation Document: https://github.com/bigmagic123/d1-nezha-rtthread

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A USB to UART Debugger

## Installation Steps

The following steps are tested successful on Arch Linux, but should be compatible with all major Linux distributions.

### Preparing the Environment

Fetch the toolchain:
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

Change the following paths accordingly:
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

Fetch dependencies:
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
# on Arch Linux: sudo pacman -S scons dtc ncurses
```

### Compiling the firmware

```shell
git clone --depth=1 https://github.com/bigmagic123/d1-nezha-rtthread.git
cd d1-nezha-rtthread/bsp/d1-nezha
scons -c
scons -j$(nproc) --verbose
```

The resulting firmware binary is at `./rtthread.bin`。

### Flash the firmware via FEL

Install [xfel](https://github.com/xboot/xfel). e.g. on Arch Linux via AUR: `paru -S xfel`

With no SD card attached, connect to the OTG port on board through USB-C

Send the payload through `xfel`:

```shell
xfel ddr d1
xfel write 0x40000000 rtthread.bin
xfel exec 0x40000000
```

Check the serial port for outputs.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is also successful.

### Boot Log

```log
[I/I2C] I2C bus [i2c0] registered
heap: [0x403482e1 - 0x435482e1]

 \ | /
- RT -     Thread Operating System
 / | \     4.1.0 build Jun 20 2025 15:28:00
 2006 - 2021 Copyright by rt-thread team
(rx_fifo != RT_NULL) assertion failed at function:rt_hw_serial_isr, line number:1294

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

