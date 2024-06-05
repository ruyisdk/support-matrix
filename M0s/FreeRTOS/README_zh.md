# FreeRTOS Sipeed M0s Dock 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/sipeed/M0S_BL616_example
    - 工具链：https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux
- 参考安装文档：https://github.com/sipeed/M0S_BL616_example
    - https://bl-mcu-sdk.readthedocs.io/zh-cn/latest/get_started/get_started.html

### 硬件信息

- Sipeed M0s Dock
- type-c 线一根

## 安装步骤

### 获取 SDK 和工具链

clone 相关仓库到工作目录：
```bash
git clone https://github.com/sipeed/M0S_BL616_example.git
git clone https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux.git
```

配置环境：
```bash
export PATH=path/to/toolchain_gcc_t-head_linux/bin:$PATH
```

### 编译

编译 FreeRTOS 例程：
```bash
cd M0S_BL616_example/examples/freertos
make CHIP=bl616 BOARD=bl616dk
```

### 刷写程序


使用 type-c 线连接电脑和 C 口

先按住 boot，再连接 C 口上电。

而后：
```bash
make flash CHIP=bl616 COMX=/dev/ttyACM0 # Change com on your machine
```

### 连接串口

需要连接的串口位于 C 口旁，波特率为 2000000。

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

系统正常启动，能够看到串口输出。

### 启动信息

```log
  ____               __  __      _       _       _     
 |  _ \             / _|/ _|    | |     | |     | |    
 | |_) | ___  _   _| |_| |_ __ _| | ___ | | __ _| |__  
 |  _ < / _ \| | | |  _|  _/ _` | |/ _ \| |/ _` | '_ \ 
 | |_) | (_) | |_| | | | || (_| | | (_) | | (_| | |_) |
 |____/ \___/ \__,_|_| |_| \__,_|_|\___/|_|\__,_|_.__/ 

Build:11:07:19,Apr 28 2024
Copyright (c) 2022 Bouffalolab team
flash init fail!!!
=========== flash cfg ==============
jedec id   0x000000
mid            0xC8
iomode         0x11
clk delay      0x00
clk invert     0x03
read reg cmd0  0x05
read reg cmd1  0x35
write reg cmd0 0x01
write reg cmd1 0x31
qe write len   0x01
cread support  0x00
cread code     0x20
burst wrap cmd 0x77
=====================================
dynamic memory init success,heap size = 187 Kbyte 
sig1:ffffffff
sig2:0000f32f
cgen1:9f7ffffd
[I][MAIN] [OS] Starting consumer task...
[I][MAIN] [OS] Starting producer task...
[I][MAIN] Consumer task enter 
[I][MAIN] Producer task enter 
[I][MAIN] Consumer task start 
[I][MAIN] begin to loop /home/lw/Work/plct/boards/m0s/M0S_BL616_example/examples/freertos/main.c
[I][MAIN] Consumer get:
[I][MAIN] Producer task start 
[I][MAIN] Producer generates:101
[I][MAIN] Consumer get:101
[I][MAIN] Producer generates:102
[I][MAIN] Consumer get:102
[I][MAIN] Producer generates:103
[I][MAIN] Consumer get:103
[I][MAIN] Producer generates:104
[I][MAIN] Consumer get:104
[I][MAIN] Producer generates:105
[I][MAIN] Consumer get:105



```

屏幕录像：

[![asciicast](https://asciinema.org/a/zH5ndg9eZTbjEHEkWFfAxVNQk.svg)](https://asciinema.org/a/zH5ndg9eZTbjEHEkWFfAxVNQk)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。