# Debian on Milk-V Mars

## 测试环境

### 操作系统信息

- Debian bookworm/sid
  - 下载链接：https://github.com/milkv-mars/mars-buildroot-sdk/releases/
    - Milk-V 官方提供的 Debian 镜像，同时仓库中提供了 BuildRoot
  - 参考安装文档：https://milkv.io/zh/docs/mars/getting-started/boot

### 硬件开发板信息

- Milk-V Mars

## 安装步骤

### 刷写镜像

使用 `unzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

其中，`/dev/sdc` 为存储卡对应设备。

```bash
unzip mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img.zip
sudo dd if=mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `user`
默认密码： `milkv`

## 预期结果

系统正常启动，能够通过板载串口登录。能进入安装向导。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

屏幕录像：
[![asciicast](https://asciinema.org/a/v8FxrttpHTJVye5N4U5KCgUsT.svg)](https://asciinema.org/a/v8FxrttpHTJVye5N4U5KCgUsT)

```log
Debian GNU/LinuxDebian GNU/Linux bookworm/sid milkv hvc0

milkv login:  bookworm/sid milkv ttyS0

milkv login: user
Password: 
Linux milkv 5.15.0 #1 SMP Mon Nov 13 18:56:24 CST 2023 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
user@milkv:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux bookworm/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
BUILD_ID=40
user@milkv:~$ uname -a
Linux milkv 5.15.0 #1 SMP Mon Nov 13 18:56:24 CST 2023 riscv64 GNU/Linux
user@milkv:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
