# OpenWrt MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=mangopi_mq_pro
- 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> 在 OpenWrt Firmware Selector 中可以在线定制构建系统镜像，添加用户所需要的预装软件包。本次测试使用的为**未经修改**的原版镜像。

### 硬件信息

- MangoPi MQ Pro
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。

```bash
gzip -kd openwrt-d1-generic-mangopi_mq_pro-ext4-sdcard.img.gz
sudo dd if=openwrt-d1-generic-mangopi_mq_pro-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

```log

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT