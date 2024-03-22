# Debian K230 测试报告

## 测试环境

### 操作系统信息

- 系统版本：canmv_debian_sdcard_sdk_1.3
- 下载链接：https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz
- 参考安装文档：https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html

### 硬件信息

- 开发板：Canaan Kendryte K230

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。假设 microSD 卡设备为 `/dev/sdb`。

```bash
wget https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz
gzip -d canmv_debian_sdcard_sdk_1.3.img.gz
sudo dd if=canmv_debian_sdcard_sdk_1.3.img of=/dev/sdb bs=1M status=progress oflag=sync
```

### 登录系统

通过串口登录系统。

默认用户： `root`
默认密码：`root`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

![Debian](image.png)

屏幕录像（从烧录到登录系统）：

[![asciicast](https://asciinema.org/a/WT2Nz2w7OubHlHaQMEpJZCD8x.svg)](https://asciinema.org/a/WT2Nz2w7OubHlHaQMEpJZCD8x)

```log
Debian GNU/Linux trixie/sid v hvc0

v login: oto
Password: 

Login incorrect
v login: root
Password: 
Linux v 5.10.4 #1 SMP Thu Jan 11 19:05:37 CST 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@v:~# uname -a
Linux v 5.10.4 #1 SMP Thu Jan 11 19:05:37 CST 2024 riscv64 GNU/Linux
root@v:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@v:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。