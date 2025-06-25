# RT-Thread DongshanPI-Nezha STU 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/bigmagic123/d1-nezha-rtthread
- 参考安装文档：https://github.com/bigmagic123/d1-nezha-rtthread

### 硬件信息

- DongshanPI-Nezha STU
- 两根 Type-C 线

## 安装步骤

以下步骤在 Arch Linux 上测试通过，但应适用各大主流 Linux 发行版。

### 准备系统环境

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
# 在 Arch Linux 上为：sudo pacman -S scons dtc ncurses
```

### 拉取源码并编译固件

```shell
git clone --depth=1 https://github.com/bigmagic123/d1-nezha-rtthread.git
cd d1-nezha-rtthread/bsp/d1-nezha
scons -c
scons -j$(nproc) --verbose
```

生成的固件文件位于 `./rtthread.bin`。

### 通过 FEL 刷写固件

安装 [xfel](https://github.com/xboot/xfel). 如在 Arch Linux 下可通过 AUR 获取：`paru -S xfel`

在不插入 SD 卡的情况下，按住开发板上的 FEL 按键，通过两根 USB-C 线同时连接到开发板的 OTG 接口和 DEBUG 接口。

使用 `xfel` 发送固件：
```shell
xfel ddr d1
xfel write 0x40000000 rtthread.bin
xfel exec 0x40000000
```

观察串口输出。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

串口输出可能明显错位，属正常现象。

```log
[I/I2C] I2C bus [i2c0] registered
heap: [0x403482e1 - 0x435482e1]

 \ | /
- RT -     Thread Operating System
 / | \     4.1.0 build Jun 20 2025 15:28:00
 2006 - 2021 Copyright by rt-thread team
[E/gt911] soft reset failed
[I/touch] rt_touch init success
[I/gt911] touch device gt911 init success
file system initialization done!
Hello RISC-V!
msh />ps
thread               pri  status      sp     stack size max used left tick  error
-------------------- ---  ------- ---------- ----------  ------  ---------- ---
tshell                20  running 0x000002f8 0x00002800    18%   0x00000008 000
sys_work              23  suspend 0x00000288 0x00001000    15%   0x0000000a 000
mmcsd_detect          22  suspend 0x000002e8 0x00002800    07%   0x00000014 000
tidle0                31  ready   0x00000620 0x00004000    09%   0x0000001c 000
timer                  4  suspend 0x00000278 0x00004000    04%   0x00000009 000
main                  10  suspend 0x000002f8 0x00004000    10%   0x0000000d 000
msh />

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。