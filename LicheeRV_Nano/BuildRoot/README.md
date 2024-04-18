# BuildRoot LicheeRV Nano 测试报告

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

### 使用 `dd` 刷写镜像到 microSD 卡

下载镜像后进行解压和刷写：

```shell
gzip -kd c906-2024-04-10-14-19-16d76b.img.gz
sudo dd if=c906-2024-04-10-14-19-16d76b.img of=/dev/your_device bs=1M status=progress

```

### 登录系统

通过串口登录系统。

默认用户名：root
默认密码：root

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/yNDWWKvYyXReaexbXm1t5dLxi.svg)](https://asciinema.org/a/yNDWWKvYyXReaexbXm1t5dLxi)

```log
Welcome to Linux
licheervnano-b6c0 login: root
licheervnano-b6c0 login: root
Password: 
# cat /etc/os-release 
NAME=Buildroot
VERSION=-g16d76badf-dirty
ID=buildroot
VERSION_ID=2023.11.2
PRETTY_NAME="Buildroot 2023.11.2"
# uname -a
Linux licheervnano-b6c0 5.10.4-tag- #1 PREEMPT Wed Apr 10 14:12:37 HKT 2024 riscv64 GNU/Linux
# 
 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。