---
sys: rtthread
sys_ver: null
sys_var: standard

status: basic
last_update: 2024-11-02
---

# RT-Thread Milk-V Duo Test Report

## Test Environment

### Operating System Information
- Source Code Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md
- Toolchain: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Lines
- Headers pre-soldered on the Milk-V Duo for debugging purposes

## Installation Steps

### Preparing the System Environment

Install the required packages:

```shell
sudo apt install -y scons libncurses5-dev device-tree-compiler
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
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# Generate configuration
scons --menuconfig
source ~/.env/env.sh
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

Please select `milkv-duo` under the `Board Type` option in menuconfig.

`boot.sd` and `fip.bin` files will be generated in the `cvitek/output/milkv-duo` directory upon completion.

### Preparing the microSD Card

Clear the microSD card and create a FAT32 partition:
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

Copy the generated `boot.sd` and `fip.bin` files onto the microSD card. The storage card is now ready to boot RT-Thread on the Duo.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the serial port.

## Actual Results

The system booted successfully, and login through the serial port was successful.

### Boot Log

```log
Boot from SD ...
switch to partitions #0, OK
mmc0 is current device
147784 bytes read in 8 ms (17.6 MiB/s)
## Loading kernel from FIT Image at 81400000 ...
   Using 'config-cv1800b_milkv_duo_sd' configuration
   Trying 'kernel-1' kernel subimage
   Verifying Hash Integrity ... crc32+ OK
## Loading fdt from FIT Image at 81400000 ...
   Using 'config-cv1800b_milkv_duo_sd' configuration
   Trying 'fdt-cv1800b_milkv_duo_sd' fdt subimage
   Verifying Hash Integrity ... sha256+ OK
   Booting using the fdt blob at 0x8141f084
   Uncompressing Kernel Image
   Decompressing 365360 bytes used 49ms
   Loading Device Tree to 0000000081bdd000, end 0000000081be4b60 ... OK

Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x8028a780 - 0x81200000]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build Nov  1 2024 20:34:41
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
