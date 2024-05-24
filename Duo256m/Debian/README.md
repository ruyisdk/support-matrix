# Debian Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian
- 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian
- 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
wget https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.3.0/duo256_sd.img.lz4
lz4 -d duo256_sd.img.lz4
dd if=duo256_sd.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`rv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
```

启动流程屏幕录像：


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT