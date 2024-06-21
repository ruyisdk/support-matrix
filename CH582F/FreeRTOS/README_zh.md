# FreeRTOS CH582F 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/Community-PIO-CH32V/ch32-pio-projects
- 参考文档：
    - PlatformIO Core：https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO CH32V：https://pio-ch32v.readthedocs.io/en/latest/installation.html

### 硬件信息

-  CH582F-EVT-R2-1v0-BC
- USB to UART 调试器一个
- USB type-c 口线一根

## 安装步骤

### 安装 PlatformIO Core

可以先尝试包管理器中是否带有如 [platformio-core](https://archlinux.org/packages/?name=platformio-core) 包。若无可采用安装脚本安装：

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### 配置 PlatformIO 环境

安装 ch32v 开发环境：
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

添加 udev 规则并应用（根据发行版不同可能需要更改 GROUP）：
```bash
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
cat << EOF | sudo tee -a /etc/udev/rules.d/99-platformio-udev.rules
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8010", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="4348", ATTR{idProduct}=="55e0", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8012", GROUP="plugdev"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
```

添加用户组：
- Debian 系：
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch 系：
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### 准备工程仓库

clone 相关仓库：
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### 编译代码

使用 pio 编译代码：
```bash
cd platform-ch32v/examples/blinky-freertos-ch58x
pio run
```

### 烧写镜像

使用 type-c 线连接开发板和电脑后，按住 boot 按键拨动开关。而后迅速运行：
```bash
pio run -e your_board --target upload
```


### 登录系统

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/ZGVaNo7NxIiI7lJA0w0cM6nCX.svg)](https://asciinema.org/a/ZGVaNo7NxIiI7lJA0w0cM6nCX)

```log
start.
      task2 entry 1
                   task1 entry 1
                                task1 entry 2
                                             task2 entry 2
                                                          task1 entry 1

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功