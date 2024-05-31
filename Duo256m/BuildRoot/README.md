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

通过串口或 ssh 登录系统。

默认用户名：`root`
默认密码： `milkv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息


屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/ptdjXiBZX2FuisTBuEZis7JoK.svg)](https://asciinema.org/a/ptdjXiBZX2FuisTBuEZis7JoK)

```log
The authenticity of host '192.168.42.1 (192.168.42.1)' can't be established.
ED25519 key fingerprint is SHA256:Lt+dfAQr7Ih8tgb+j9KPZaQDKNRhbHSZfWLIjNYB0Ko.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.42.1' (ED25519) to the list of known hosts.
root@192.168.42.1's password: 
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=20240410-2139
ID=buildroot
VERSION_ID=2021.05
PRETTY_NAME="Buildroot 2021.05"
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Wed Apr 10 21:37:02 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功