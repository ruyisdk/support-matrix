---
sys: rtthread
sys_ver: 5.2.0
sys_var: standard

status: basic
last_update: 2024-11-28
---

# RT-Thread Milk-V DuoS Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
- Toolchain: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### Hardware Information

- Milk-V DuoS
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

The following steps are tested on Arch Linux, but should be applicable to all major Linux distributions.

### Fetch Source Code and Compile Firmware

Obtain the toolchain and configure it:
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

Update the following paths as needed:
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

Fetch dependencies:
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
# or on Arch Linux: sudo pacman -S scons dtc ncurses
```

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# Generate configuration
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

Please select `milkv-duos` under the `Board Type` option in menuconfig.

`boot.sd` and `fip.bin` files will be generated in the `cvitek/output/milkv-duos-sd` directory upon completion.

### Prepare microSD Card

Clear the microSD card and create a FAT32 partition:
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

Copy the generated `boot.sd` and `fip.bin` files onto the microSD card. The storage card is now ready to boot RT-Thread on the DuoS.

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system boots up normally and allows access through the serial port.

## Actual Results

The system boots up normally and allows access through the serial port.

### Boot Log

Screencast (from compile to boot): 
[![asciicast](https://asciinema.org/a/i7ZhlS8WrHBRPIkIVUffXN64a.svg)](https://asciinema.org/a/i7ZhlS8WrHBRPIkIVUffXN64a)

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0x000000008029a810 - 0x0x0000000080a9a810]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build Nov 28 2024 11:45:48
 2006 - 2024 Copyright by RT-Thread team
lwIP-2.1.2 initialized!
[I/sal.skt] Socket Abstraction Layer initialize success.
Hello RISC-V!
msh />
 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
