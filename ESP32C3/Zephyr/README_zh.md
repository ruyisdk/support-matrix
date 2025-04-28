# zephyr ESP32-C3 测试报告

## 测试环境
Ubuntu 20.04
### 操作系统信息

- 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/hello_world
            https://docs.zephyrproject.org/latest/boards/luatos/esp32c3_luatos_core/doc/index.html
- 参考文档：
    - ESP32-C3：https://www.espressif.com/en/support/documents/technical-documents?keys=esp32-c3

### 硬件信息

- 合宙ESP32-C3
- USB to UART 调试器一个

## 安装步骤

### 安装 zephyr
根据zephyr文档配置zephyr环境，连接：https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### 准备工程仓库
```bash
cd zephyr
```
### 编译代码
```bash
west build -b esp32c3_luatos_core --sysbuild samples/hello_world
```

### 烧写镜像

确认连接到esp32c3后，烧写镜像。
在linux开发环境中，可能需要提前添加 udev 规则并应用（根据发行版不同可能需要更改 GROUP）
```bash
west flash
west espressif monitor
```
（要退出串行监视器，请键入 。Ctrl-]）

### 观察log

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息
屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/NWBb9aYkRNBGzoq83srOwMxg5.svg)](https://asciinema.org/a/NWBb9aYkRNBGzoq83srOwMxg5)
```log

*** Booting Zephyr OS build v4.0.0-3624-ge658bc1b2baa ***
Hello World! esp32c3_luatos_core/esp32c3

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功