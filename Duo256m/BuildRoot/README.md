# BuildRoot Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo 256M
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等

## 安装步骤

### 下载 Duo 256m 的镜像

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/Duo-V1.1.0/milkv-duo256m-v1.1.0-2024-0410.img.zip
unzip milkv-duo256m-v1.1.0-2024-0410.img
```

### 刷写镜像

用 dd 刷写镜像到 sd 卡：
```bash
sudo dd if=milkv-duo256m-v1.1.0-2024-0410.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息


屏幕录像（从刷写镜像到登录系统）：

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT