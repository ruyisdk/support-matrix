# RT-Thread Smart Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 源码链接：
  - https://github.com/RT-Thread/rt-thread
  - 用户态应用：https://github.com/RT-Thread/userapps
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
   - 工具链：https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 构建步骤

以下步骤在 Arch Linux 上测试通过，但应适用各大主流 Linux 发行版。

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
# 在 Arch Linux 上为：sudo pacman -S scons dtc ncurses
```

```bash
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# 生成配置文件
scons --menuconfig
```

在 `menuconfig` 中，Board Type 请选择 `milkv-duo256m`。进入 `RT-Thread Kernel` 菜单 ---> 选中 `Enable RT-Thread Smart (microkernel on kernel/userland)` 选项以启用 RT-Smart 内核。


```bash
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

执行结束后，会在 `cvitek/output/milkv-duo256m` 目录下生成 boot.sd 和 fip.bin 两个文件。

### 拉取源码并编译 RT-Smart 用户态应用

获取依赖：
```bash
sudo apt install -y unzip xmake
```

编译：
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
source env.sh
cd apps
xmake f -a riscv64gc
xmake -j$(nproc)
```

构建镜像：
```bash
xmake smart-rootfs
xmake smart-image -f ext4 
```
生成的应用镜像位于 `userapps/apps/build/ext4.img`。

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

系统正常启动，能够通过串口登录。

### 启动信息

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0xffffffc0002fb110 - 0x0xffffffc000afb110]

 \ | /
- RT -     Thread Smart Operating System
 / | \     5.2.0 build Nov 29 2024 12:03:11
 2006 - 2024 Copyright by RT-Thread team
lwIP-2.1.2 initialized!
[I/sal.skt] Socket Abstraction Layer initialize success.
[I/drivers.serial] Using /dev/ttyS0 as default console
Hello RT-Smart!
msh />

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。