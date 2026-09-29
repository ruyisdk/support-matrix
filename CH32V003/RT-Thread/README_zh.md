# RT-Thread CH32V003 测试报告

## 测试环境

### 操作系统信息

- 源码：https://github.com/RT-Thread/rt-thread/tree/6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4
- 实测 commit：`6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4`（串口横幅为 5.3.1，不是 git 标签 `v5.3.1`）
- BSP：`bsp/wch/risc-v/ch32v003f4p6-evt`，由 [RT-Thread/rt-thread#11838](https://github.com/RT-Thread/rt-thread/pull/11838) 合入，Rbb666 于 2026-09-28 合并
- 板级说明：https://github.com/RT-Thread/rt-thread/blob/6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4/bsp/wch/risc-v/ch32v003f4p6-evt/README.md
- 工具链：WCH RISC-V GCC 8.2.0
  - https://github.com/NanjingQinheng/sdk-toolchain-RISC-V-GCC-WCH
- 编译环境：RT-Thread Env v2.0.0（Windows）
  - https://github.com/RT-Thread/env-windows/releases
- 下载工具：WCH-LinkUtility 3.1
  - https://www.wch.cn/downloads/WCH-LinkUtility_EXE.html

本 BSP 依赖的沁恒 SDK 源码（`libraries/ch32v00x`）已经在 BSP 目录里，不用再另外下载软件包。

### 硬件信息

- CH32V003F4P6-EVT（芯片 CH32V003F4P6，TSSOP20，主频最高 48MHz，16KB Flash + 2KB SRAM）
- 外接 WCH-LinkE，这块板没有板载调试器
- 调试线和串口线用的杜邦线
- USB Type-C 线。这块板上的 Type-C 只供电。

本报告在 Windows 上验证。

## 安装步骤

### 硬件连接

1. 用杜邦线把 WCH-LinkE 接到板子：3V3 接板子丝印 VCC，GND 对 GND，SWDIO 接 PD1。SWCLK 不接。不要用 LinkE 的 5V 给板子供电。
2. 串口是另外一组针，要交叉接：LinkE 的 TX 接板子 PD6，LinkE 的 RX 接板子 PD5。控制台是 USART1（TX PD5、RX PD6）。
3. 设备管理器应出现 **WCH-LinkRV** 和一个 COM 口（本机是 COM11）。没有的话先装 WCH-Link 驱动。

### 编译

1. 下载并解压 WCH RISC-V GCC 8.2.0。`riscv-none-embed-gcc --version` 应显示 8.2.0。
2. 安装 RT-Thread Env v2.0.0。
3. 克隆 RT-Thread，在 BSP 目录打开 Env：

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout 6f99d7bf97911c47a19ce9c52ccdc74d6b31cab4
cd bsp\wch\risc-v\ch32v003f4p6-evt
```

4. 编译：

```
scons --exec-path=你的路径\sdk-toolchain-RISC-V-GCC-WCH\bin
```

通过后会在 BSP 目录生成 `rtthread.bin`。默认镜像只开 UART1。这颗芯片只有 16KB Flash 和 2KB SRAM，所以其余外设都没有打开。

### 下载

1. 打开 WCH-LinkUtility，Series 选 **CH32V003**（不要选成 CH32V20X），Target File 指向 `rtthread.bin`。
2. 不要勾选 **Erase All**。Chip Mem 不要点 **Set**：这颗片是 16KB Flash + 2KB SRAM。
3. 芯片正在运行时直接下载会失败（工具报 10002），要先拉住复位再下载。

### 串口

打开 WCH-Link 对应 COM 口，115200 8-N-1。先开串口再复位，否则启动横幅容易丢。

## 预期结果

板子启动 RT-Thread。串口出现 RT-Thread 横幅和 `msh >` 提示符。

## 实际结果

板子已启动。COM11 串口看到 RT-Thread 5.3.1 横幅、BSP 自己打印的 `MCU: CH32V003F4P6`，以及 `msh >`。烧到板上跑的那版镜像占 16KB Flash 里的 15680 字节。

这块板上只跑了串口控制台。GPIO、ADC、SPI 没有在这块板上跑过，本版写待支持；I2C 和 TIM 同样没跑过。

### 启动信息

```log
 \ | /
- RT -     Thread Operating System
 / | \     5.3.1 build Sep 25 2026 20:46:44
 2006 - 2026 Copyright by RT-Thread team
MCU: CH32V003F4P6
msh >
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
