# FreeRTOS LicheeRV Nano 测试报告

## 测试环境

### 操作系统信息

- 系统版本：20240401
- 下载链接：https://github.com/sipeed/LicheeRV-Nano-Build/releases
- 参考安装文档：https://github.com/sipeed/LicheeRV-Nano-Build/releases

### 硬件信息

- LicheeRV Nano
- type-c 电源线一根
- UART 转 USB 调试器一个

## 安装步骤

LicheeRV Nano 的 FreeRTOS 被集成在了 Linux SDK 中，使用 mailbox 与 Linux 系统进行交互。

### 查看 FreeRTOS 设备

FreeRTOS 与 Linux 之间的交互通过 mailbox 实现，可以在 `/dev` 中找到 `cvi-rtos-cmdqu`。

### 登录系统

通过串口登录系统。

默认用户名：root
默认密码：root

## 预期结果

系统正常启动，能够看到 rtos 设备。

## 实际结果

系统正常启动，能够看到 rtos 设备。

### 启动信息

```log

Welcome to Linux
licheervnano-b6c0 login: root
licheervnano-b6c0 login: root
Password: 
# ls /dev/ | grep rtos
cvi-rtos-cmdqu
# 

```

屏幕录像：

[![asciicast](https://asciinema.org/a/zG1HsQyGWkGTVHFI74Nwhxcv8.svg)](https://asciinema.org/a/zG1HsQyGWkGTVHFI74Nwhxcv8)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功