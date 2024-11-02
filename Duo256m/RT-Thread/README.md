---
sys: rtthread
sys_ver: null
sys_var: standard

status: basic
last_update: 2024-11-02
---

# RT-Thread Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
- Toolchain: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### Hardware Information

- Milk-V Duo 256M
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

Please select `milkv-duo256m` under the `Board Type` option in menuconfig.

`boot.sd` and `fip.bin` files will be generated in the `cvitek/output/milkv-duo256m` directory upon completion.

### Prepare microSD Card

Clear the microSD card and create a FAT32 partition:
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

Copy the generated `boot.sd` and `fip.bin` files onto the microSD card. The storage card is now ready to boot RT-Thread on the Duo 256M.

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
Boot from SD ...
switch to partitions #0, OK
mmc0 is current device
177764 bytes read in 11 ms (15.4 MiB/s)
## Loading kernel from FIT Image at 81800000 ...
   Using 'config-cv1812cp_milkv_duo256m_sd' configuration
   Trying 'kernel-1' kernel subimage
     Description:  cvitek kernel
     Type:         Kernel Image
     Compression:  lzma compressed
     Data Start:   0x818000d8
     Data Size:    151272 Bytes = 147.7 KiB
     Architecture: RISC-V
     OS:           Linux
     Load Address: 0x80200000
     Entry Point:  0x80200000
     Hash algo:    crc32
     Hash value:   aa58e975
   Verifying Hash Integrity ... crc32+ OK
## Loading fdt from FIT Image at 81800000 ...
   Using 'config-cv1812cp_milkv_duo256m_sd' configuration
   Trying 'fdt-cv1812cp_milkv_duo256m_sd' fdt subimage
     Description:  cvitek device tree - cv1812cp_milkv_duo256m_sd
     Type:         Flat Device Tree
     Compression:  uncompressed
     Data Start:   0x818250dc
     Data Size:    24599 Bytes = 24 KiB
     Architecture: RISC-V
     Hash algo:    sha256
     Hash value:   fca09bd9678df89606a7d31d37d033745f23ef47701ba482f4637fc0ddbb0715
   Verifying Hash Integrity ... sha256+ OK
   Booting using the fdt blob at 0x818250dc
   Uncompressing Kernel Image
   Decompressing 423684 bytes used 47ms
   Loading Device Tree to 000000008a777000, end 000000008a780016 ... OK

Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x8029af58 - 0x81200000]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build Nov  2 2024 20:34:48
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
