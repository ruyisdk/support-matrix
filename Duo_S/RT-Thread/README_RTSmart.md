---
sys: rtthread
sys_ver: 5.2.2
sys_var: smart

status: basic
last_update: 2026-09-13
---

# RT-Thread Milk-V DuoS Test Report

## Test Environment

### Operating System Information

- Source Code Link:
  - https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
   - Toolchain: https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

### Hardware Information

- Milk-V DuoS
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Fetch Source Code and Compile Firmware

Obtain the toolchain and configure it:
```bash
wget https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

tar -xjvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
```

Update the following paths as needed:
```bash
export RTT_CC_PREFIX=riscv64-unknown-linux-musl-
export RTT_EXEC_PATH=/opt/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

Fetch dependencies:
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
```

```bash
git clone -b v5.2.2 --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# Generate configuration
scons --menuconfig
```

In menuconfig, please select `milkv-duos` under the `Board Type` option. Enter `RT-Thread Kernel` submenu ---> Select `Enable RT-Thread Smart (microkernel on kernel/userland)` to enable the RT-Smart kernel.

```bash
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
```

Upon completion, `boot.sd` will be generated in the `cvitek/output/duos/` directory.

Compile the little core firmware:

```bash
cd ../c906_little
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose

```

Upon completion, `rtthread.bin` will be generated in the `c906_little/` directory.

`fip.bin` needs to be packaged separately. Use the rttpkgtool tool to generate it:

```bash
cd ../
git clone https://github.com/plctlab/rttpkgtool.git
cd rttpkgtool
DPT_PATH_KERNEL=~/rt-thread DPT_BOARD_TYPE=duos DPT_ARCH=riscv ./script/mkpkg.sh -l
```

The generated `fip.bin` is located in `rttpkgtool/output/duos/`. Copy it to `~/rt-thread/bsp/cvitek/output/duos/`.

### Prepare microSD Card

Clear the microSD card and create a FAT32 partition:
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

Copy the generated `boot.sd` and `fip.bin` files onto the microSD card. The storage card is now ready to boot RT-Smart on the DuoS.

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system boots up normally and allows access through the serial port.

## Actual Results

The system boots up normally and allows access through the serial port.

### Boot Log

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0xffffffc0002bcd88 - 0x0xffffffc000abcd88]

 \ | /
- RT -     Thread Smart Operating System
 / | \     5.2.2 build Sep 13 2026 18:36:24
 2006 - 2024 Copyright by RT-Thread team
[I/drivers.serial] Using /dev/ttyS0 as default console
Hello RISC-V/C906B !
msh />

```

Screencast:

[![asciicast](https://asciinema.org/a/NcTTBELyYyMbGlCc.svg)](https://asciinema.org/a/NcTTBELyYyMbGlCc)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
