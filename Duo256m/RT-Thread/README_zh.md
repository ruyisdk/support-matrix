# RT-Thread Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
- 工具链：https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 构建步骤

### 拉取源码并编译固件

获取工具链并配置：
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

自行更改以下路径：
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

获取依赖：
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
```

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# 生成配置文件
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

menuconfig 中的 Board Type 请选择 `milkv-duo256m`。

执行结束后，会在 `output` 目录下生成 boot.sd 和 fip.bin 两个文件。

### 准备 microSD 卡

清空 microSD 卡，并创建一个 FAT32 分区：
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

将构建出的 boot.sd 和 fip.bin 复制进 microSD 卡。至此，存储卡已经可用来在 Duo 256M 上启动 RT-Thread。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

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

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功