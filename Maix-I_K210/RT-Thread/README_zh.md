# RT-Thread Maix-I K210 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/RT-Thread/rt-thread/
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210
- 工具链：https://github.com/xpack-dev-tools/riscv-none-embed-gcc-xpack/releases
    - kflash：https://github.com/kendryte/kflash.py

### 硬件信息

- Sipeed Maix-Bit (K210)

## 安装步骤

### 准备源码及环境

获取工具链，下载并解压。

注：kendryte 的官方工具链会报浮点类型不兼容的错误，risc-v 工具链 8.2.0 之前的版本会出现头文件不兼容的问题。（见[安装文档](https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210)）

clone 仓库并进行配置：
```bash
git clone https://github.com/RT-Thread/rt-thread/
cd rt-thread/bsp/k210
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

在 menuconfig 中需要检查以下选项是否正确：
> RT-Thread online packages --->
> > peripheral libraries and drivers --->
> > > Kendryte SDK --->
> > > > [*] kendryte K210 SDK

> RT-Thread Components --->  C++ features

而后打开 rtconfig.py，找到第 18 行，并将 EXEC_PATH 替换为你工具链解压后 bin 所在的位置。

### 进行编译

使用 scons 进行编译：
```bash
scons --exec-path="path/to/toolchain/bin"
```

### 烧写镜像

使用 k_flash 进行烧写，工具链文档可见：https://github.com/kendryte/kflash.py

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx rtthread.bin
```

### 登录系统

通过串口连接开发板。

## 预期结果

构建成功，开发板正常输出 RT-Thread 启动信息。

## 实际结果

构建成功，开发板正常输出 RT-Thread 启动信息。

### 启动信息

屏幕录像（从刷写系统到启动）：
[![asciicast](https://asciinema.org/a/UeYag1L9qPvAPgcuuWKMpF7ye.svg)](https://asciinema.org/a/UeYag1L9qPvAPgcuuWKMpF7ye)

```log
heap: [0x80076c43 - 0x80600000]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build Apr 18 2024 18:23:42
 2006 - 2024 Copyright by RT-Thread team
(rt_hw_interrupt_is_disabled()) assertion failed at function:rt_sched_post_ctx_switch, line number:1045 
[0] W/kernel.service: rt_hw_backtrace_frame_unwind is not implemented
please use: addr2line -e rtthread.elf -a -f 0x80013392[0] W/kernel.service: rt_hw_backtrace_frame_unwind is not implemented


```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功