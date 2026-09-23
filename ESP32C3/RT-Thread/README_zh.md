# RT-Thread ESP32-C3 测试报告

## 测试环境

### 操作系统信息

- 源码：https://github.com/RT-Thread/rt-thread/tree/dc3da6d87fa980b5e4fe2f73a828708e69182b90
- 实测 commit：`dc3da6d87fa980b5e4fe2f73a828708e69182b90`（串口横幅为 5.3.1，不是 git 标签 `v5.3.1`）
- BSP：`bsp/ESP/ESP32_C3`
- 板级说明：https://github.com/RT-Thread/rt-thread/blob/dc3da6d87fa980b5e4fe2f73a828708e69182b90/bsp/ESP/ESP32_C3/README_ZH.md
- 工具链：乐鑫 RISC-V GCC 11.2.0（crosstool-NG esp-2022r1）
  - https://github.com/espressif/crosstool-NG/releases/download/esp-2022r1/riscv32-esp-elf-gcc11_2_0-esp-2022r1-win64.zip
- 编译环境：RT-Thread Env v2.0.0（Windows）
  - https://github.com/RT-Thread/env-windows/releases
- 烧录工具：Env 自带的 esptool 4.8.1

`pkgs --update` 会把 `ESP-IDF-latest` 和 `FreeRTOS-Wrapper-latest` 拉到 `packages/`。这个目录在 gitignore 里。BSP 自带的 `packages/SConscript` 是空的，不补上下面这几行就编不到这两个包：

```python
import os
from building import *

cwd = GetCurrentDir()
objs = []

for d in ['ESP-IDF-latest', 'FreeRTOS-Wrapper-latest']:
    if os.path.isfile(os.path.join(cwd, d, 'SConscript')):
        objs = objs + SConscript(os.path.join(d, 'SConscript'))

Return('objs')
```

这块 DevKitM-1 是 ESP32-C3 AZ revision v1.1。默认镜像头写着 `min_rev=3`，esptool 会拒绝烧录。在 `SConstruct` 里、`elf2image` 之前，把 `image.min_rev` 设为 0；有 `min_rev_full` 时也设为 0。`builtin_imgs/bootloader.bin` 的 `min_rev` 同样改为 0。这是针对这块 rev v1.1 的本地修改，不在 [RT-Thread/rt-thread#11816](https://github.com/RT-Thread/rt-thread/pull/11816) 里。

Windows 上 GNU ld 记下的目标文件路径用反斜杠，`idf_port/ld/sections.ld` 里只写 `/` 的通配对不上，IRAM 里的代码会被丢进 Flash，启动时报非法指令。能同时匹配 `/` 和 `\` 的通配在上述 PR，提交 `144e141e4de792cb8ebaca14ba4caaba18dc5e31`。2026-09-22 用这个提交重新编译并烧到这块板，COM10 仍然能进 `msh >`。下面的命令记录来自 2026-09-20 16:49:51 编出来的那份镜像。

### 硬件信息

- ESP32-C3-DevKitM-1（Micro-USB，板载 CP2102N）
- 本机枚举为 Silicon Labs CP210x，COM10
- 芯片：ESP32-C3 AZ（QFN32）revision v1.1，4MB XMC Flash，MAC `90:70:69:d7:46:70`

本报告在 Windows 上验证。

## 安装步骤

### 硬件连接

1. Micro-USB 插到 DevKitM-1。
2. 没有 COM 口时，安装 Silicon Labs CP210x 驱动，拔掉再插。

### 编译

1. 解压乐鑫 RISC-V GCC 11.2.0。`riscv32-esp-elf-gcc --version` 应显示 11.2.0。
2. 安装 RT-Thread Env v2.0.0。
3. 克隆 RT-Thread，进入 BSP：

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout dc3da6d87fa980b5e4fe2f73a828708e69182b90
cd bsp/ESP/ESP32_C3
```

4. 在 Env 里执行 `pkgs --update`，然后用上面的 `packages/SConscript`。
5. Windows 上采用 PR 11816 里的 `sections.ld`。这块 rev v1.1 还要把 `min_rev` 设为 0。
6. 编译：

```
scons --exec-path=工具链的bin目录
```

BSP 目录下会生成 `rtthread.bin`。

### 烧录

在 BSP 目录下，三份镜像按下面的地址写入：

```
esptool.py -p COM10 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 builtin_imgs/bootloader.bin 0x8000 partition-table.bin 0x10000 rtthread.bin
```

`COM10` 换成自己机器上的 CP210x 口。

### 串口

打开该 COM 口，115200 8-N-1。先开串口再复位，否则横幅容易错过。

## 预期结果

开发板启动 RT-Thread。串口出现 RT-Thread 横幅和 `msh >`。

## 实际结果

开发板已启动。串口打出 RT-Thread 5.3.1、`Hello!RT-THREAD!` 和 `msh >`。`help`、`ps`、`version`、`free` 都有回应。

没有打开 Wi-Fi 和 BLE。默认板型是 LUATOS。启动日志把 GPIO12 设成输出。这块 DevKitM-1 的 RGB 灯在 GPIO8，这次没有核对。

### 启动信息

```log
 \ | /
- RT -     Thread Operating System
 / | \     5.3.1 build Sep 20 2026 16:49:51
 2006 - 2026 Copyright by RT-Thread team
Hello!RT-THREAD!
msh >
```

```log
msh >help
RT-Thread shell commands:
pin              - pin [option]
list             - list objects
console          - console setting
version          - show RT-Thread version information
clear            - clear the terminal screen
free             - Show the memory usage in the system
ps               - List threads in the system
help             - RT-Thread shell help

msh >ps
thread       pri  status      sp     stack size max used left tick   error  tcb addr   usage
------------ ---  ------- ---------- ----------  ------  ---------- ------- ---------- -----
tshell        20  running 0x00000120 0x00001000     13%   0x00000009 OK      0x3fca34e0  N/A
sys workq     23  suspend 0x00000120 0x00000800     14%   0x0000000a OK      0x3fca2988  N/A
tidle0        31  ready   0x000000c0 0x00000100     75%   0x00000003 OK      0x3fcb5200  N/A
timer          4  suspend 0x00000100 0x00000200     50%   0x00000009 EINTRPT 0x3fcb5808  N/A
main          10  suspend 0x00000130 0x00000800     83%   0x00000009 EINTRPT 0x3fca2068  N/A

msh >version
RT-Thread 5.3.1 build Sep 20 2026 16:49:51

msh >free
total    : 76704
used     : 10144
maximum  : 10144
available: 66560
```

## 测试判断标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。Wi-Fi、BLE 和 GPIO8 灯不在这次测试里。
