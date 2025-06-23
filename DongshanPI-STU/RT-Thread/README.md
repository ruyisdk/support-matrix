---
sys: rtthread
sys_ver: null
sys_var: standard

status: basic
last_update: 2025-06-23
---

# RT-Thread DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/bigmagic123/d1-nezha-rtthread
- Reference Installation Document: https://github.com/bigmagic123/d1-nezha-rtthread

### Hardware Information

- DongshanPI-Nezha STU
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

With no SD card attached, press and hold the FEL button, and connect to both the OTG and DEBUG ports on board through two USB-C cables.

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
[E/gt911] soft reset failed
[I/touch] rt_touch init success
[I/gt911] touch device gt911 init success
file system initialization done!
Hello RISC-V!
msh />ps
thread               pri  status      sp     stack size max used left tick  error
-------------------- ---  ------- ---------- ----------  ------  ---------- ---
tshell                20  running 0x000002f8 0x00002800    18%   0x00000008 000
sys_work              23  suspend 0x00000288 0x00001000    15%   0x0000000a 000
mmcsd_detect          22  suspend 0x000002e8 0x00002800    07%   0x00000014 000
tidle0                31  ready   0x00000620 0x00004000    09%   0x0000001c 000
timer                  4  suspend 0x00000278 0x00004000    04%   0x00000009 000
main                  10  suspend 0x000002f8 0x00004000    10%   0x0000000d 000
msh />

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

