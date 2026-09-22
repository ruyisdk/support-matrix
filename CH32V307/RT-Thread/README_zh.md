# RT-Thread CH32V307 测试报告

## 测试环境

### 操作系统信息

- 源码：https://github.com/RT-Thread/rt-thread/tree/dc3da6d87fa980b5e4fe2f73a828708e69182b90
- 实测 commit：`dc3da6d87fa980b5e4fe2f73a828708e69182b90`（串口横幅为 5.3.1，不是 git 标签 `v5.3.1`）
- BSP：`bsp/wch/risc-v/ch32v307v-r1`
- 板级说明：https://github.com/RT-Thread/rt-thread/blob/dc3da6d87fa980b5e4fe2f73a828708e69182b90/bsp/wch/risc-v/ch32v307v-r1/README_zh.md
- 工具链：WCH RISC-V GCC 8.2.0
  - https://github.com/NanjingQinheng/sdk-toolchain-RISC-V-GCC-WCH/archive/refs/tags/V1.0.0.zip
- 编译环境：RT-Thread Env v2.0.0（Windows）
  - https://github.com/RT-Thread/env-windows/releases
- 下载工具：WCH-LinkUtility 3.1
  - https://www.wch.cn/downloads/WCH-LinkUtility_EXE.html
- SDK 软件包（提供 `ch32v30x.h`）：[CH32V307-SDK-for-RTT](https://github.com/kaidegit/CH32V307-SDK-for-RTT)

### 硬件信息

- CH32V307V-EVT-R1（芯片 CH32V307VCT6）
- 板载 WCH-LinkE（靠近两个按键的 Type-C）
- USB Type-C 线
- 可选：网线，用于板载 10M PHY

本报告在 Windows 上验证。

## 安装步骤

### 硬件连接

1. Type-C 插板载 WCH-LinkE，口在两个按键旁边，不要插另一侧 USB。
2. 打开板上电源开关。
3. 设备管理器应出现 **WCH-LinkRV** 和一个 COM 口。没有的话先装 WCH-Link 驱动。

### 编译

1. 下载并解压 WCH RISC-V GCC 8.2.0。`riscv-none-embed-gcc --version` 应显示 8.2.0。
2. 安装 RT-Thread Env v2.0.0。
3. 克隆 RT-Thread，在 BSP 目录打开 Env：

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout dc3da6d87fa980b5e4fe2f73a828708e69182b90
cd bsp\wch\risc-v\ch32v307v-r1
```

4. `board.h` 会 `#include "ch32v30x.h"`，该头文件不在 RT-Thread 仓内。在 Env 里勾选 CH32V307 SDK 软件包并执行 `pkgs --update`，或将 [CH32V307-SDK-for-RTT](https://github.com/kaidegit/CH32V307-SDK-for-RTT) 解到当前 BSP 的 `packages` 目录。
5. 编译：

```
scons --exec-path=你的路径\sdk-toolchain-RISC-V-GCC-WCH\bin
```

通过后会在 BSP 目录生成 `rtthread.bin`。

### 下载

1. 打开 WCH-LinkUtility，Target File 指向 `rtthread.bin`。
2. Chip Mem 选 **224K ROM + 96K RAM**，并点击 **Set**。只改下拉框不点 Set 无效。CH32V307 的 Flash/SRAM 可配置（288K+32K / 256K+64K / 224K+96K / 192K+128K）。开发板总表里的 `ram: 64KB(SRAM)` 对应手册常见的 256K+64K 切法。本 BSP 的 `board.h` 用 224K Flash + 96K SRAM（`SRAM_SIZE 96`），下载必须跟这个切分一致。这不是多出来的物理内存，也不用来改总表那一格。
3. 勾选 Erase、Program、Verify、Reset，然后下载。

### 串口

打开 WCH-Link 对应 COM 口，115200 8-N-1。先开串口再复位，否则启动横幅容易丢。

## 预期结果

板子启动 RT-Thread。串口出现 RT-Thread 横幅和 `msh >` 提示符。

## 实际结果

板子已启动。串口输出 RT-Thread 5.3.1 和 `msh >`。`help`、`ps`、`version`、`free` 均有响应。

板载 LED1、LED2 只接到排针 J3，不跳线不亮。官方 `main.c` 翻转的是 PB5（Arduino 丝印 D5）。灯不闪不代表没起来。

### 启动信息

```log
 \ | /
- RT -     Thread Operating System
 / | \     5.3.1 build Sep 18 2026 19:21:26
 2006 - 2026 Copyright by RT-Thread team
msh >
```

### 可选：板载 10M 以太网

官方 `ch32v307v-r1` 默认关闭以太网。Env 里 `menuconfig`：**Hardware Drivers Config → On-chip Peripheral Drivers → Enable Ethernet**。勾上后 lwIP、netdev、SAL 会带上，DHCP 默认开启。按同样的 224K+96K Chip Mem 重新编译下载。

RJ45 插局域网路由器（不要插电脑网口）。复位后 `ifconfig` 可见 `e0` `LINK_UP` 并拿到 DHCP 地址，对本网关 `ping` 成功。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
