# Deepin VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin
- 下载链接：https://cdimage.deepin.com/RISC-V/VisionFive-v1-image/deepin-visionfive.7z
- 参考安装文档：https://cdimage.deepin.com/RISC-V/VisionFive-v1-image/README.txt


### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `7z` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
7z e deepin-visionfive.7z
sudo dd if=deepin-visionfive.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `Riscv2022#`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/9I4jUIPPdKEWBnNBO7ANzmvwB.svg)](https://asciinema.org/a/9I4jUIPPdKEWBnNBO7ANzmvwB)

```log
Deepin GNU/Linux 23 deepin-riscv ttyS0

deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 6.1.0-rc4-visionfive+ #1 SMP Thu Nov 10 01:12:06 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv:~# uname -a
Linux deepin-riscv 6.1.0-rc4-visionfive+ #1 SMP Thu Nov 10 01:12:06 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release 
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。