# Deepin MangoPi MQ-Pro 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin 23 beige 20221209
- 下载链接：https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-d1-20221208175445.img.zst.0
- 参考安装文档：https://github.com/deepin-community/deepin-riscv-board/

### 硬件信息

- MangoPi MQ-Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `dd` 将镜像写入 microSD 卡。

```bash
sudo dd if=deepin-d1-20221208175445.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口或图形界面登录系统。

串口默认用户名：`root`
密码：`Riscv2022#`

GUI 默认用户名：`deepin`
密码：`deepin`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。
有视频输出，可以进入桌面。

### 启动信息
```log
deepin-riscv login:
deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 6.1.0-rc3+ #1 PREEMPT Thu Dec  8 17:52:42 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


Last login: Fri Apr 29 08:30:58 UTC 2022 on ttyS0
root@deepin-riscv:~# �
root@deepin-riscv:~# uname -a
Linux deepin-riscv 6.1.0-rc3+ #1 PREEMPT Thu Dec  8 17:52:42 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@deepin-riscv:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

root@deepin-riscv:~#
```

![](./image.webp)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
