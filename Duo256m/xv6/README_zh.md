# xv6 Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- 参考安装文档：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### 硬件信息

- Milk-V Duo 256M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
dd if=milkv-duo_sdcard.img of=/dev/your/device bs=1M status=progress
```

可能需要使用官方 Buildroot SDK 中的 fip.bin 替换镜像中的相应文件。

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

U-Boot 无法引导内核, 启动失败。

### 启动信息

```log

U-Boot 2021.10 (Nov 22 2024 - 11:42:00 +0800) cvitek_cv181x

DRAM:  254 MiB
gd->relocaddr=0x8b0c8000. offset=0xaec8000
MMC:   cv-sd@4310000: 0
Loading Environment from nowhere... OK
In:    serial
Out:   serial
Err:   serial
Net:
Warning: ethernet@4070000 (eth0) using random MAC address - 9a:dc:e9:b6:f3:45
eth0: ethernet@4070000
Hit any key to stop autoboot:  0
Boot from SD ...
switch to partitions #0, OK
mmc0 is current device
1578445 bytes read in 72 ms (20.9 MiB/s)
## Loading kernel from FIT Image at 81800000 ...
Could not find configuration node
ERROR: can't get kernel image!
cv181x_c906#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。