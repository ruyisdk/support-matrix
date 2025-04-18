# xv6 Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- 参考安装文档：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### 硬件信息

- Milk-V Duo S
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

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

无法正常拉起 OpenSBI 和 U-Boot, 启动失败。

### 启动信息

```log
FSBL Jb28g9:gf2df47913:2024-02-29T16:35:38+08:00
 E:ra=0xc00a0f6
 E:RESET:panic:-1
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。