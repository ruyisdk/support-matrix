# BuildRoot LicheeRV Nano 测试报告

## 测试环境

### 操作系统信息

- 系统版本：20240401
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- LicheeRV Nano

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
gzip -dc c906-2024-04-01-15-48-55a549.img.gz | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT