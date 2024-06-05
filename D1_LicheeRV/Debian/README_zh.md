# Debian 11 D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian
- 下载链接：[http://www.perfxlab.cn:8080/rvboards/](http://www.perfxlab.cn:8080/rvboards/)
    - 网盘：[https://pan.baidu.com/s/1leAXR2VPHvTqkaDqfeY9ag](https://pan.baidu.com/s/1leAXR2VPHvTqkaDqfeY9ag) 提取码：3o5v
- 参考安装文档：[https://d1.docs.aw-ol.com/strong/strong_4debian/#v041](https://d1.docs.aw-ol.com/strong/strong_4debian/#v041)

### 硬件信息

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unzip` 解压镜像。
清空你的 sd 卡。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip /path/to/RVBoards_D1_Debian_lxde_img_linux.img.zip
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/RVBoards_D1_Debian_lxde_img_linux.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`rvboards`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/7osW4u2FvkucqlfODK4nEBMQm.svg)](https://asciinema.org/a/7osW4u2FvkucqlfODK4nEBMQm)

```log
Debian GNU/Linux 11 RVBoards ttyS0

RVBoards login: root
Password: 

Login incorrect
RVBoards login: root
Password: 
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 19 18:39:24 CST 2021 on ttyS0
root@RVBoards:~# uname -a
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64 GNU/Linux
root@RVBoards:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@RVBoards:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。