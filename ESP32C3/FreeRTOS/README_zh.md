# FreeRTOS ESP32-C3 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/espressif/esp-idf/tree/v5.4/examples/system/freertos/real_time_stats
- 参考文档：
    - ESP32-C3：https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4/esp32c3/

### 硬件信息

- 合宙ESP32-C3
- USB to UART 调试器一个

## 安装步骤

### 安装 ESP-IDF

ESP32-IDF的环境安装可以主要参考官网连接：
https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4/esp32c3/get-started/index.html#get-started-how-to-get-esp-idf
不管是图形化界面还是命令行开发都有不错的效果。

### 准备工程仓库
```bash
git clone https://github.com/espressif/esp-idf
```
### 编译代码
```bash
cd esp-idf/examples/system/freertos/real_time_stats
idf.py menuconfig
idf.py build
```
根据使用的board在menuconfig调整参数
### 烧写镜像

确认连接到esp32c3后，烧写镜像。
在linux开发环境中，可能需要提前添加 udev 规则并应用（根据发行版不同可能需要更改 GROUP）
```bash
idf.py -p PORT flash monitor
```
（将 PORT 替换为要使用的串行端口的名称。

（要退出串行监视器，请键入 。Ctrl-]

有关配置和使用 ESP-IDF 构建项目的完整步骤，请参阅入门指南。
### 观察log

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口或USB_SERIAL_JTAG 查看信息。

## 实际结果

系统正常启动，能够通过板载串口或USB_SERIAL_JTAG 查看信息。

### 启动信息

屏幕录像（从编译到启动）：

[![asciicast](https://asciinema.org/a/JGcZ72E7j5dNoPRrxqJNyzQQu.svg)](https://asciinema.org/a/JGcZ72E7j5dNoPRrxqJNyzQQu)
```log
| Task | Run Time | Percentage
| stats | 875 | 0%
| spin1 | 107595 | 10%
| spin2 | 107595 | 10%
| spin3 | 107594 | 10%
| spin4 | 107596 | 10%
| spin5 | 107627 | 10%
| spin0 | 107597 | 10%
| IDLE | 352937 | 35%
| main | Deleted
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 605 | 0%
| spin0 | 109494 | 10%
| spin1 | 109493 | 10%
| spin5 | 109494 | 10%
| spin2 | 99502 | 9%
| spin3 | 99500 | 9%
| spin4 | 109529 | 10%
| IDLE | 362383 | 36%
Real time stats obtained
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功