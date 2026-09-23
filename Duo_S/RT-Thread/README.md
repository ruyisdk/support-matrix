---
sys: rtthread
sys_ver: 5.2.2
sys_var: standard

status: basic
last_update: 2026-09-09
---

# RT-Thread Milk-V DuoS Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/RT-Thread/rt-thread/releases/tag/v5.2.2
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
- Toolchain: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### Hardware Information

- Milk-V DuoS
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

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
```

```shell
$ cd rt-thread
$ ls
bsp           components     examples  Kconfig  LICENSE      README_de.md  README.md     src
ChangeLog.md  documentation  include   libcpu   MAINTAINERS  README_es.md  README_zh.md  tools
$ cd bsp/cvitek/
c906_little  cv18xx_aarch64  cv18xx_risc-v  drivers  output  rttpkgtool  README.md  build.sh  tools.sh
$ cd cv18xx_risc-v/
# Generate configuration
$ scons --menuconfig
$ source ~/.env/env.sh
$ pkgs --update
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
[Use Github server - auto decision based on IP location]
packages/zlib-latest
==============================>  zlib update done

Operation completed successfully.
# Build boot.sd
$ scons -j$(nproc) --verbose

$ cd ../c906_little/
# Generate configuration
$ scons --menuconfig
$ source ~/.env/env.sh
$ pkgs --update
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Operation completed successfully.

# Build fip.bin
$ scons -j$(nproc) --verbose
```

Please select `milkv-duos` under the `Board Type` option and disable `Enable RT-Thread Smart (microkernel on kernel/userland)` under the `RT-Thread Kernel` option in menuconfig.

`boot.sd` and `fip.bin` files will be generated in the `cvitek/output/duos` directory upon completion.

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

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0x000000008023fce0 - 0x0x0000000080a3fce0]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.2 build Sep  9 2026 20:02:47
 2006 - 2024 Copyright by RT-Thread team
Hello RISC-V/C906B !
msh />

```

Screencast:

[![asciicast](https://asciinema.org/a/hdg2nOJPZFg74qMg.svg)](https://asciinema.org/a/hdg2nOJPZFg74qMg)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
