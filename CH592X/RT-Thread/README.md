# RT-Thread CH592X 官方版本 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://www.wch.cn/downloads/CH592EVT_ZIP.html
- 参考文档：https://www.wch.cn/downloads/CH592EVT_ZIP.html
    - wchisp：https://github.com/ch32-rs/wchisp
- 刷写工具：
    - https://github.com/ch32-rs/wchisp/

### 硬件信息

- CH592X-EVT-R1-1v0
- USB to UART 调试器一个
- USB type-c 口线一根


## 安装步骤

### 烧写镜像

预编译镜像已位于 `EVT/EXAM/RT-Thread/obj/rt-thread-nano.hex`

下载并解压源码与 wchisp 工具之后，先不要上电，**一直按住** boot(download) 按钮后，将板子与电脑通过 type-c 线连接上电。

使用 wchisp 工具进行烧写：
```bash
./wchisp flash EVT/EXAM/RT-Thread/obj/rt-thread-nano.hex

```

### 登录系统

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从刷写到启动）：
[![asciicast](https://asciinema.org/a/Xxc0CepVpSfyC09MEVNL7Nljl.svg)](https://asciinema.org/a/Xxc0CepVpSfyC09MEVNL7Nljl)

```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.5 build Jan 16 2024
 2006 - 2020 Copyright by rt-thread team
task1
task2
msh >task2
task1
task2
task1

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功