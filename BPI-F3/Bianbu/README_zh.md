# Bianbu 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 下载链接：
  - 百度网盘：https://pan.baidu.com/s/15owwUEjIU_i26cI1iigAew?pwd=8888 (pincode: 8888)
  - 谷歌网盘：https://drive.google.com/drive/folders/1LQoioz6N5YQpSOxY47OmetnPX4yggtT0?usp=sharing
- 下载链接 (桌面版)：
  - 百度网盘：https://pan.baidu.com/s/1zvFkX92f5gpZdKjP-vGJvA?pwd=8888 (pincode: 8888)
  - 谷歌网盘：https://drive.google.com/drive/folders/1kCHiMwjnhvZaRBy5vkj6UlPeAlpRQ14P?usp=sharing
- 参考安装文档：https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）


**请务必选择以 `.img.zip` 结尾的压缩包**
下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip Bianbu-23.10-desktop-k1-v1.0rc1-release-20240429194149.img
sudo dd if=/path/to/Bianbu-23.10-desktop-k1-v1.0rc1-release-20240429194149.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `bianbu`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/TFRjqFjOEIHc38Wha93bw0ti8.svg)](https://asciinema.org/a/TFRjqFjOEIHc38Wha93bw0ti8)

```log
Bianbu 1.0rc1 k1 ttyS0k1 login: root
密码： 
Welcome to Bianbu 1.0rc1 (GNU/Linux 6.1.15 riscv64)

 * Documentation:  coming soon
 * Management:     coming soon
 * Support:        coming soon

0 updates can be applied immediately.


The programs included with the Bianbu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Bianbu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@k1:~# cat /etc/os-release 
PRETTY_NAME="Bianbu 1.0rc1"
NAME="Bianbu"
VERSION_ID="1.0rc1"
VERSION="1.0rc1 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=bianbu
ID_LIKE=debian
HOME_URL="coming soon"
SUPPORT_URL="coming soon"
BUG_REPORT_URL="coming soon"
PRIVACY_POLICY_URL="coming soon"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo
root@k1:~# uname -a
Linux k1 6.1.15 #1.0~rc1 SMP PREEMPT Mon Apr 29 09:05:59 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@k1:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
