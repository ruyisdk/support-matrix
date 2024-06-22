# Ubuntu K230 测试报告

## 测试环境

### 操作系统信息

- 系统版本：canmv_ubuntu_sdcard_sdk_1.3
- 下载链接：https://kendryte-download.canaan-creative.com/developer/k230/canmv_ubuntu_sdcard_1.3.img.gz
- 参考安装文档：https://developer.canaan-creative.com/k230/dev/zh/CanMV_K230_%E6%95%99%E7%A8%8B.html

### 硬件信息

- 开发板：Canaan Kendryte K230

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。假设 microSD 卡设备为 `/dev/sdb`。

```bash
wget https://kendryte-download.canaan-creative.com/developer/k230/canmv_ubuntu_sdcard_1.3.img.gz
gzip -d canmv_ubuntu_sdcard_1.3.img.gz
sudo dd if=canmv_ubuntu_sdcard_1.3.img of=/dev/sdb bs=1M status=progress oflag=sync
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

![Ubuntu](image.png)

屏幕录像（从烧录到登录系统）：

[![asciicast](https://asciinema.org/a/rFklZEOMyjSQCPaSjrS3OStOF.svg)](https://asciinema.org/a/rFklZEOMyjSQCPaSjrS3OStOF)

```log
Ubuntu 23.10 k230 hvc0

k230 login: 
Ubuntu 23.10 k230 ttyS0

k230 login: root
Password: 
Welcome to Ubuntu 23.10 (GNU/Linux 5.10.4 riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@k230:~# uname -a
Linux k230 5.10.4 #1 SMP Thu Jan 11 19:05:37 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
root@k230:~# cat /etc/os-release 
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