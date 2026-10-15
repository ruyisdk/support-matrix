# RT-Thread Smart Milk-V DuoS 测试报告

## 测试环境

### 操作系统信息

- 源码链接：
  - https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
   - 工具链：https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

### 硬件信息

- Milk-V DuoS
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 构建步骤

### 拉取源码并编译固件

获取工具链并配置：
```bash
wget https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

tar -xjvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
```

自行更改以下路径：
```bash
export RTT_CC_PREFIX=riscv64-unknown-linux-musl-
export RTT_EXEC_PATH=/opt/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

获取依赖：
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
```

```bash
git clone -b v5.2.2 --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# 生成配置文件
scons --menuconfig
```

在 `menuconfig` 中，Board Type 请选择 `milkv-duos`。进入 `RT-Thread Kernel` 菜单 ---> 选中 `Enable RT-Thread Smart (microkernel on kernel/userland)` 选项以启用 RT-Smart 内核。

```bash
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
```

编译完成后，`boot.sd` 生成在 `cvitek/output/duos/` 目录下。

使用 ELF 工具链编译小核固件：

```bash
mkdir -p "$HOME/toolchains"
wget -O "$HOME/toolchains/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz" \
    https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
tar -xzf "$HOME/toolchains/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz" -C "$HOME/toolchains"

cd ../c906_little
source ~/.env/env.sh
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH="$HOME/toolchains/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin"
scons --menuconfig

```

在 menuconfig 中，将 `Board Type` 设置为 `milkv-duos`，并保持小核的 `Enable RT-Thread Smart (microkernel on kernel/userland)` 选项关闭。保存配置并退出，然后编译：
```bash
pkgs --update
scons -j$(nproc) --verbose
ls -lh rtthread.bin ../output/duos/boot.sd ../output/duos/fip.bin

```

小核构建会生成 `rtthread.bin`，并自动调用 `build.sh -l` 打包 `fip.bin`。大小核构建脚本会自动获取 `rttpkgtool`。`boot.sd` 和 `fip.bin` 均位于 `bsp/cvitek/output/duos/`，后续准备 microSD 卡时使用这两个文件。

### 准备 microSD 卡

清空 microSD 卡，并创建一个 FAT32 分区：
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```
将构建出的 boot.sd 和 fip.bin 复制进 microSD 卡。至此，存储卡已经可用来在 DuoS 上启动 RT-Smart。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口访问。

## 实际结果

系统正常启动，能够通过串口访问。

### 启动信息

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0xffffffc0002cb588 - 0x0xffffffc000acb588]

 \ | /
- RT -     Thread Smart Operating System
 / | \     5.2.2 build Sep 24 2026 12:46:47
 2006 - 2024 Copyright by RT-Thread team
[I/drivers.serial] Using /dev/ttyS0 as default console
Hello RISC-V/C906B !
msh />

```

屏幕录像：

[![asciicast](https://asciinema.org/a/r7hGuyq4ZuQPkfLf.svg)](https://asciinema.org/a/r7hGuyq4ZuQPkfLf)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
