# RT-Thread Milk-V DuoS 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
- 工具链：https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### 硬件信息

- Milk-V DuoS
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
$ cd rt-thread
$ ls
bsp           components     examples  Kconfig  LICENSE      README_de.md  README.md     src
ChangeLog.md  documentation  include   libcpu   MAINTAINERS  README_es.md  README_zh.md  tools
$ cd bsp/cvitek/
c906_little  cv18xx_aarch64  cv18xx_risc-v  drivers  output  rttpkgtool  README.md  build.sh  tools.sh
$ cd cv18xx_risc-v/
# 生成配置文件
$ scons --menuconfig
$ source ~/.env/env.sh
$ pkgs --update
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
[Use Github server - auto decision based on IP location]
packages/zlib-latest
==============================>  zlib update done

Operation completed successfully.
# 构建 boot.sd
$ scons -j$(nproc) --verbose

$ cd ../c906_little/
# 生成配置文件
$ scons --menuconfig
$ source ~/.env/env.sh
$ pkgs --update
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Failed to read env.json: [Errno 2] No such file or directory: 'env.json'
Operation completed successfully.

# 构建 fip.bin
$ scons -j$(nproc) --verbose
```

menuconfig 中的 Board Type 请选择 `milkv-duos`，并关闭 `Enable RT-Thread Smart (microkernel on kernel/userland)` 选项。

执行结束后，会在 `output` 目录下生成 boot.sd 和 fip.bin 两个文件。

### 准备 microSD 卡

清空 microSD 卡，并创建一个 FAT32 分区：
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

将构建出的 boot.sd 和 fip.bin 复制进 microSD 卡。至此，存储卡已经可用来在 DuoS 上启动 RT-Thread。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口访问。

## 实际结果

系统正常启动，成功通过串口访问。

### 启动信息

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

屏幕录像：

[![asciicast](https://asciinema.org/a/hdg2nOJPZFg74qMg.svg)](https://asciinema.org/a/hdg2nOJPZFg74qMg)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
