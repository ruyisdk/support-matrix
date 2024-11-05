# RT-Thread Milk-V Duo 测试报告

## 测试环境

### 操作系统信息
- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针

## 构建步骤

以下步骤在 Arch Linux 上测试通过，但应适用各大主流 Linux 发行版。

### 准备系统环境

获取工具链：

```shell
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
# 在 Arch Linux 上为：sudo pacman -S scons dtc ncurses 
```

### 拉取源码并编译固件

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# 生成配置文件
scons --menuconfig
source ~/.env/env.sh
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```
在 `menuconfig` 中，Board Type 请选择 `milkv-duo`。进入 `RT-Thread Kernel` 菜单 ---> 选中 `Enable RT-Thread Smart (microkernel on kernel/userland)` 选项以启用 RT-Smart 内核。

执行结束后，会在 `cvitek/output/milkv-duo` 目录下生成 boot.sd 和 fip.bin 两个文件。

### 准备 microSD 卡

清空 microSD 卡，并创建一个 FAT32 分区：
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

将构建出的 boot.sd 和 fip.bin 复制进 microSD 卡。至此，存储卡已经可用来在 Duo 上启动 RT-Thread。

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
184124 bytes read in 11 ms (16 MiB/s)
## Loading kernel from FIT Image at 81400000 ...
   Using 'config-cv1800b_milkv_duo_sd' configuration
   Trying 'kernel-1' kernel subimage
   Verifying Hash Integrity ... crc32+ OK
## Loading fdt from FIT Image at 81400000 ...
   Using 'config-cv1800b_milkv_duo_sd' configuration
   Trying 'fdt-cv1800b_milkv_duo_sd' fdt subimage
   Verifying Hash Integrity ... sha256+ OK
   Booting using the fdt blob at 0x81427e78
   Uncompressing Kernel Image
   Decompressing 475312 bytes used 63ms
   Loading Device Tree to 0000000081bdd000, end 0000000081be4b60 ... OK

Starting kernel ...

heap: [0x802aa328 - 0x812aa328]

 \ | /
- RT -     Thread Smart Operating System
 / | \     5.1.0 build Nov  3 2024 12:31:40
 2006 - 2024 Copyright by RT-Thread team
Hello RT-Smart!
msh />
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl.svg)](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。