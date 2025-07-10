# NetBSD MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
使用 `dd` 或`balenaEtcher`等工具将镜像写入 microSD 卡

```bash
sudo dd if=riscv64.img of=/dev/<your-device> bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`, 无须密码

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

串口无任何输出，未进入 U-Boot.

### 启动信息

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。
