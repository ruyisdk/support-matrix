# Zephyr Longan Nano 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
- 参考文档：https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### 硬件信息

- Longan Nano
- USB to UART 调试器一个
- type-c 线一根

## 安装步骤

### 安装 Zephyr

创建虚拟环境：

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

获取 Zephyr：
```bash
west init ~/zephyrproject
cd ~/zephyrproject
west update
```

配置环境：
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

### 编译代码

使用 west 编译代码：
```bash
west build -p always -b longan_nano samples/basic/blinky

```

### 烧写镜像

按住 boot 后再按 reset，再松开 boot。
使用 USB 口烧写：
```bash
west flash --runner dfu-util

```

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/Kz2OGHEaRjIODgvzJWO5dPTWm.svg)](https://asciinema.org/a/Kz2OGHEaRjIODgvzJWO5dPTWm)

```log
*** Booting Zephyr OS build v3.6.0-1803-gf419ea799099 ***
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
LED state: OFF

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功