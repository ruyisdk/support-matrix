# FreeRTOS CH32V303 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/Community-PIO-CH32V/ch32-pio-projects
- 参考文档：
    - PlatformIO Core：https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO CH32V：https://pio-ch32v.readthedocs.io/en/latest/installation.html

### 硬件信息

- CH32V303VCT6-EVT-R0-1v0
- USB to UART 调试器一个
- WCH-Link(E) 一个

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
cd platform-ch32v/examples/blinky-freertos
pio run
```

### 烧写镜像

确认 WCH-Link(E) 连接到 SWD 调试口后，使用 pio 烧写镜像：
```bash
pio run --target upload
```

pio 会自行检测开发板。若烧录不成功也可尝试手动指定：
```bash
pio run -e your_board --target upload
```

#### 添加开发板

**若使用的是 C8T6 系列请忽略**
这是由于其它芯片不在默认芯片列表中，我们需要手动添加。
你可以在 `platform-ch32v/boards` 中找到你的板子对应 json 名。
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### 常见问题

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - 这是由于 WCH-Link 固件版本过低造成的。（见[important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)）。
    - 请使用[WCH-Link 工具链](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)连接一次 W2 有 CH-Link 即可自动更新。**该工具目前仅有 Windows 版本**
- Error: Read-Protect Status Currently Enabled
    - 这是由于芯片开启了写保护导致的。Winodws 下我们可以使用 [WCH-Link 工具链](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)解保护，Linux 下可以使用 OpenOCD 解保护：
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd - # 别忘了回到工作目录
```


### 登录系统

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/Ha0YoNiwW9DkkJQuNdPKVQGuH.svg)](https://asciinema.org/a/Ha0YoNiwW9DkkJQuNdPKVQGuH)

```log
SystemClk:96000000
ChipID: 30300514
FreeRTOS Kernel Version:V10.4.6
task2 entry
task1 entry
task1 entry
task2 entry
task1 entry

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功