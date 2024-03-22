# Ubuntu VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：Ubuntu 23.10
- 下载链接：[https://ubuntu.com/download/risc-v](https://ubuntu.com/download/risc-v)
- 参考安装文档：[https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive](https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive)

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/ubuntu.img.xz
sudo dd if=/path/to/ubuntu.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `ubuntu`
默认密码： `ubuntu`

初次启动后会强制要求更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/yNX1czhlpU8K0CwIDzan6PZ9Q.svg)](https://asciinema.org/a/yNX1czhlpU8K0CwIDzan6PZ9Q)

```log
Welcome to Ubuntu 23.10 (GNU/Linux 6.5.0-1002-starfive riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Sep 19 15:58:17 UTC 2023

  System load:  0.71              Swap usage:  0%       Users logged in: 0
  Usage of /:   3.3% of 57.48GB   Temperature: 51.8 C
  Memory usage: 2%                Processes:   105

0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.5.0-1002-starfive #3-Ubuntu SMP Sat Oct  7 21:23:58 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 23.10"
NAME="Ubuntu"
VERSION_ID="23.10"
VERSION="23.10 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。