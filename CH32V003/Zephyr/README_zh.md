# Zephyr CH32V003-EVT 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
    - 刷写工具：https://github.com/cnlohr/ch32fun/tree/master/minichlink
    - 预编译二进制：https://github.com/AlexanderMandera/minichlink-binaries
- 参考文档：https://docs.zephyrproject.org/latest/boards/wch/ch32v003evt/doc/index.html

### 硬件信息

- CH32V003-EVT
- WCH-Link 调试器一个

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
west build -p always -b ch32v003evt samples/basic/blinky

```

### 烧写镜像

连接开发板至 WCH-Link:
VCC -> VCC （或通过Type-C供电）
GND -> GND
SWDIO -> PD1

烧写：
```bash
west flash --minichlink /path/to/minichlink
```

## 启动系统

连接串口：
UART RX -> PD5
UART TX -> PD6

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
*** Booting Zephyr OS build v4.1.0-rc2-120-g4212408bf57e ***
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
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

测试成功。