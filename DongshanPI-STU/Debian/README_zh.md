# Debian DongshanPI-Nezha STU 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/DongshanPI/NezhaSTU-ReleaseLinux/releases/download/v0.1.0-alpha/DshanNezhaSTU-APTok-Sdcard.img.gz
- 参考安装文档：https://github.com/DongshanPI/NezhaSTU-ReleaseLinux

### 硬件信息

- DongshanPI-Nezha STU
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
清空你的 sd 卡。
使用 `dd` 将镜像写入 microSD 卡。

```bash
gzip -kd /path/to/DshanNezhaSTU-APTok-Sdcard.img.gz
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/DshanNezhaSTU-APTok-Sdcard.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`100ask`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

```log
[   18.939791] fbcon: Taking over console

Debian GNU/Linux bookworm/sid nezhastu ttyS0

nezhastu login: 
Debian GNU/Linux bookworm/sid nezhastu hvc0

nezhastu login: root
Password: 
Linux nezhastu 5.18.0-rc4-396532-gf4bce410a6b4 #4 PREEMPT Fri May 6 05:21:39 EDT 2022 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@nezhastu:~# [   33.854677] ldob: disabling

root@nezhastu:~# uname -a
Linux nezhastu 5.18.0-rc4-396532-gf4bce410a6b4 #4 PREEMPT Fri May 6 05:21:39 EDT 2022 riscv64 GNU/Linux
root@nezhastu:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux bookworm/sid"
NAME="Debian GNU/Linux"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@nezhastu:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@nezhastu:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。