# FreeRTOS Demo M0sense 测试报告

## 测试环境

### 操作系统信息

- 构建系统：Arch Linux
- 源码链接：https://gitee.com/Sipeed/M0sense_BL702_example
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html
- 工具链：https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux

### 硬件信息

- Sipeed M0sense (BL702)
- USB A to C 或 C to C 线缆一根

## 安装步骤

### 准备构建环境

```shell
sudo pacman -S gcc git base-devel
```

### 构建 FreeRTOS Demo

```shell
git clone https://gitee.com/Sipeed/M0sense_BL702_example.git
cd M0sense_BL702_example
git clone https://gitee.com/bouffalolab/bl_mcu_sdk
git clone https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux
./build.sh patch
PATH=$PWD/toolchain_gcc_sifive_linux/bin:$PATH
gcc -I libs/uf2_format misc/utils/uf2_conv.c -o uf2_convert
./build.sh m0sense_apps/rtos_demos/single_button_control
```

构建结束后，在 `uf2_demos` 目录下会生成 uf2 格式的固件。

```log
mx @ archlinux in ~/M0sense_BL702_example/uf2_demos |17:40:05  |main U:3 ?:2 ✗| 
$ ls
audio_recording.uf2  blink_baremetal.uf2  blink_rtos.uf2  hello_world.uf2  imu.uf2  lcd_flush.uf2  single_button_control.uf2
```

### 烧录镜像

按住开发板上的 BOOT 键后按下 RESET 键，会在电脑上显示为 USB 移动存储设备。将前一步中编译得到的 `single_button_control.uf2` 复制进来。

复制完成后，开发板会自动重启以加载新固件。

#### 若未出现 USB 存储设备

请参照 [此处](https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html#%E7%83%A7%E5%BD%95-bin-%E6%96%87%E4%BB%B6) 烧录固件。

1. 前往博流[官网](https://dev.bouffalolab.com/download)下载烧录光盘工具。
2. 根据系统不同，运行 `BLDevCube`、 `BLDevCube-macos` 或 `BLDevCube-ubuntu`。
3. 短接开发板 `3V` 和 `BOOT` 引脚，然后再将开发板连接至计算机。
4. 打开 `BLDevCube` 软件，选择 `BL702`，选择 `MCU` 模式。
5. 点击 `Refresh`，选择唯一的串口（如果看到的不是唯一串口，重新短接 `boot` 引脚和 `3.3v` 引脚后再上电使 M0sense 进入下载模式），设置波特率 `2000000`，点击`Create & Download`。
6. 重新插拔 USB 使新固件生效。
7. 现在可以可以参照上面的方式，直接拖放 `.uf2` 固件到开发板完成烧录了。

### 连接开发板

通过 USB 连接开发板。计算机上会出现一个串口。

波特率：115200

数据位：8

## 预期结果

构建成功，按住开发板 BOOT 按钮，开发板自带 LED 变色。串口打印 LED 颜色信息。

## 实际结果

构建成功，按住开发板 BOOT 按钮，开发板自带 LED 变色。串口打印 LED 颜色信息。

[![asciicast](https://asciinema.org/a/MjevQgMAxbPcjP0Uj1RJdEdQl.svg)](https://asciinema.org/a/MjevQgMAxbPcjP0Uj1RJdEdQl)

### 启动信息

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。