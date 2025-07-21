---
sys: rtthread
sys_ver: 5.2.1
sys_var: standard

status: basic
last_update: 2025-07-21
---

# RT-Thread Milk-V DuoS Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/RT-Thread/rt-thread/releases/tag/v5.2.1
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
# or on Arch Linux: sudo pacman -S scons dtc ncurses uboot-tools
```

```shell
m@n:~/.../tmp/rt-thread-5.2.1$ ls
bsp           components     examples  Kconfig  LICENSE      README_de.md  README.md     src
ChangeLog.md  documentation  include   libcpu   MAINTAINERS  README_es.md  README_zh.md  tools
m@n:~/.../tmp/rt-thread-5.2.1$ cd bsp/cvitek/
c906_little  cv18xx_aarch64  cv18xx_risc-v  drivers  output  rttpkgtool  README.md  build.sh  tools.sh
m@n:~/.../bsp/cvitek$ cd cv18xx_risc-v/
# Generate configuration
m@n:~/.../cvitek/cv18xx_risc-v$ scons --menuconfig
m@n:~/.../cvitek/cv18xx_risc-v$ source ~/.env/env.sh
m@n:~/.../cvitek/cv18xx_risc-v$ pkgs --update
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
[Use Github server - auto decision based on IP location]
/home/mitchell/Documents/tmp/rt-thread-5.2.1/bsp/cvitek/cv18xx_risc-v/packages/zlib-latest
==============================>  zlib update done

Operation completed successfully.
# Build boot.sd
m@n:~/.../cvitek/cv18xx_risc-v$ scons -j$(nproc) --verbose

m@n:~/.../cvitek/cv18xx_risc-v$ cd ../c906_little/
# Generate configuration
m@n:~/.../cvitek/c906_little$ scons --menuconfig
m@n:~/.../cvitek/c906_little$ source ~/.env/env.sh
m@n:~/.../cvitek/c906_little$ pkgs --update
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Operation completed successfully.

# Build fip.bin
m@n:~/.../cvitek/c906_little$ scons -j$(nproc) --verbose
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

Screencast:
[![asciicast](https://asciinema.org/a/WvrrTMHJyKlhT2GLEKolzIzw0.svg)](https://asciinema.org/a/WvrrTMHJyKlhT2GLEKolzIzw0)

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0x000000008029b968 - 0x0x0000000080a9b968]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.1 build Jul 21 2025 14:03:06
 2006 - 2024 Copyright by RT-Thread team
lwIP-2.1.2 initialized!
[I/sal.skt] Socket Abstraction Layer initialize success.
Hello RISC-V/C906B !
msh />

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
