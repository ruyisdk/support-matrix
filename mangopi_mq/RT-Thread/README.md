---
sys: rtthread
sys_ver: null
sys_var: standard

status: basic
last_update: 2025-09-26
---

# RT-Thread MangoPi MQ Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/bigmagic123/d1-nezha-rtthread
- Reference Installation Document: https://github.com/bigmagic123/d1-nezha-rtthread

### Hardware Information

- MangoPi MQ
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

Connect to the OTG port on board through USB-C

Send the payload through `xfel`:

```shell
xfel ddr f133
xfel write 0x40000000 rtthread.bin
xfel exec 0x40000000
```

Check the serial port for outputs.

The board's TX and RX pins are pins 7, 8 on connector P3, respectively.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is also successful.

### Boot Log

```log
ZQ value = 0x2f***********
get_pmu_exist() = 4294967295
ddr_efuse_type: 0xb
[AUTO DEBUG] single rank and full DQ!
ddr_efuse_type: 0xb
[AUTO DEBUG] rank 0 row = 13
[AUTO DEBUG] rank 0 bank = 4
[AUTO DEBUG] rank 0 page size = 2 KB
DRAM BOOT DRIVE INFO: %s
DRAM CLK = 528 MHz
DRAM Type = 2 (2:DDR2,3:DDR3)
DRAMC read ODT  off.
DRAM ODT off.
ddr_efuse_type: 0xb
DRAM SIZE =64 M
DRAM simple test OK.
[I/I2C] I2C bus [i2c0] registered
heap: [0x403482e1 - 0x435482e1]

 \ | /
- RT -     Thread Operating System
 / | \     4.1.0 build Jun 20 2025 15:28:00
 2006 - 2021 Copyright by rt-thread team
[I/touch] rt_touch init success
[I/gt911] touch device gt911 init success
file system initialization done!
Hello RISC-V!
msh />help
RT-Thread shell commands:
test_i2c         - test i2c
test_lcd         - test lcd
test_thead_custo - test thead custom
reboot           - reboot system...
memcheck         - check memory data
memtrace         - dump memory trace information
list_fd          - list file descriptor
help             - RT - Thread shell help.
ps               - List threads in the system.
free             - Show the memory usage in the system.
ls               - List information about the FILEs.
cp               - Copy SOURCE to DEST.
mv               - Rename SOURCE to DEST.
cat              - Concatenate FILE(s)
rm               - Remove(unlink) the FILE(s).
cd               - Change the shell working directory.
pwd              - Print the name of the current working directory.
mkdir            - Create the DIRECTORY.
mkfs             - format disk with file system
mount            - mount <device> <mountpoint> <fstype>
umount           - Unmount device from file system
df               - disk free
echo             - echo string to file
tail             - print the last N - lines data of the given file
hello            - say hello world
clear            - clear the terminal screen
version          - show RT - Thread version information
list_thread      - list thread
list_sem         - list semaphore in system
list_event       - list event in system
list_mutex       - list mutex in system
list_mailbox     - list mail box in system
list_msgqueue    - list message queue in system
list_mempool     - list memory pool in system
list_timer       - list timer in system
list_device      - list device in system
list             - list all commands in system

msh />test_thead_custom
aa is 3077
msh />ps
thread               pri  status      sp     stack size max used left tick  error
-------------------- ---  ------- ---------- ----------  ------  ---------- ---
tshell                20  running 0x000002f8 0x00002800    18%   0x00000004 000
sys_work              23  suspend 0x00000288 0x00001000    15%   0x0000000a 000
mmcsd_detect          22  suspend 0x000002e8 0x00002800    07%   0x00000014 000
tidle0                31  ready   0x00000620 0x00004000    10%   0x00000015 000
timer                  4  suspend 0x00000278 0x00004000    04%   0x00000009 000
main                  10  suspend 0x000002f8 0x00004000    10%   0x0000000f 000
msh />

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

