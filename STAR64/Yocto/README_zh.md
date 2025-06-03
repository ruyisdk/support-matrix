# Yocto Star64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
- 参考安装文档：https://github.com/Fishwaldo/meta-pine64

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 烧写镜像

下载后，解压并烧写镜像（以下以 plasma 版为例）：
```bash
wget https://github.com/Fishwaldo/meta-pine64/releases/download/v2.1/star64-image-plasma-star64.wic.bz2
bzip2 -kd star64-image-plasma-star64.wic.bz2
sudo dd if=star64-image-plasma-star64.wic of=/dev/your/sdcard bs=1M status=progress
```

### 登录系统

通过串口连接开发板。

启动后，系统会要求用户手动配置用户名、密码、时区、语言等。

Xfce 版本需要配置完成后方可进入桌面。

可通过串口配置。若接入了键盘和显示器，亦可通过键盘配置。

## 预期结果

开发板正常输出启动信息。

## 实际结果

U-Boot 启动时出错，无法进入系统。

### 启动信息

```log

U-Boot 2021.10 (Jun 05 2023 - 16:23:55 +0000)05062023

CPU:   rv64imacu_zba_zbb
Model: Pine64 Star64
DRAM:  8 GiB
MMC:   sdio0@16010000: 0, sdio1@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
OK
StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : PINE64
Product full SN: STAR64V1-2310-D008E000-00000005
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:75:61
Ethernet MAC1 address: 6c:cf:39:00:75:62
--------EEPROM INFO--------

In:    serial
Out:   serial
Err:   serial
Model: Pine64 Star64
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
Unknown command 'usb' - try 'help'
Hit any key to stop autoboot:  0
Unknown command 'bootflow' - try 'help'
Star64 #
Star64 #

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。