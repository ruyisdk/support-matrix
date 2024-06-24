# FreeRTOS CH32V103C 官方示例 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://www.wch.cn/downloads/CH32V103EVT_ZIP.html
- 参考文档：官方文档位于压缩包内
    - PlatformIO 提供文档：https://github.com/Community-PIO-CH32V/platform-ch32v
- 工具链：http://mounriver.com/download
    - WCH-Link 工具链：https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html

### 硬件信息

- CH32V103C8T6-EVT-R1
- USB to UART 调试器一个
- WCH-Link(E) 一个

## 安装步骤

### 准备构建环境

将源码与工具链解压后放到工作区中。

由于官方示例不带有 Makefile 或任何构建脚本，而是采用官方 IDE 进行构建，若要直接使用工具链，请下载这个改好的 [Makefile](./Makefile)，并放到源码文件夹下 `EVB/EXAM/FreeRTOS/FreeRTOS` 下。

将刚才获取的 Makefile 中的工具链路径进行修改，即替换 `TOOL_CHAIN_PATH` 和 `OPENOCD_PATH` 中的内容。

接下来进行 `make prepare` 来复制一些必要的代码。

### 构建镜像

若 Makefile 配置正确，应当运行 `make` 后即可自动构建。

#### 可能出现的问题

- 找不到符号 `__freertos_irq_stack_top`：
    - 将 ../FreeRTOS.bak/Ld 中的链接脚本手动复制到当前目录

### 刷写镜像

若配置正确，应当运行 `make flash` 后即可自动刷写。

#### 常见问题

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - 这是由于 WCH-Link 固件版本过低造成的。（见[important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)）。
    - 请使用[WCH-Link 工具链](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)连接一次 W2 有 CH-Link 即可自动更新。**该工具目前仅有 Windows 版本**
- Error: Read-Protect Status Currently Enabled
    - 这是由于芯片开启了写保护导致的。Winodws 下我们可以使用 [WCH-Link 工具链](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)解保护，Linux 下可以使用 OpenOCD 解保护：
```bash
cd path/to/openocd/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd - # 别忘了回到工作目录
```

### 登录系统

通过串口连接开发板。

## 预期结果

构建成功，开发板正常输出 OS 信息。

## 实际结果

构建成功，开发板正常输出 OS 信息。

### 启动信息

屏幕录像（从刷写系统到启动）：
[![asciicast](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv.svg)](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv)

```log
SystemClk:72000000
ChipID:2500410f
FreeRTOS Kernel Version:V10.4.6
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功