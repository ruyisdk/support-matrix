# Ubuntu 24.04 LTS on Milk-V Mars

## 测试环境

### 操作系统信息

- Ubuntu
  - 下载链接：https://cdimage.ubuntu.com/releases/24.04/release/ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
  - 参考安装文档：https://milkv.io/zh/docs/mars/getting-started/boot

### 硬件开发板信息

- Milk-V Mars

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

其中，`/dev/sdc` 为存储卡对应设备。

```bash
unxz -d ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
sudo dd if=ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img of=/dev/sdc bs=1M status=progress
```

### 更新 U-Boot

**若出现启动时 Kernel Panic，需要更新 U-Boot**

插入烧好镜像的 SD 卡，在串口终端中出现 Hit any key to stop autoboot 时迅速按下回车键，进入 U-boot 命令行终端。
进入 U-Boot 控制台后，依次输入：
```bash
sf probe
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot-spl.bin.normal.out
sf update $kernel_addr_r 0 $filesize
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot.itb
sf update $kernel_addr_r 0x100000 $filesize
```

### 登录系统

通过串口登录系统。

默认用户名： `ubuntu`
默认密码： `ubuntu`

## 预期结果

系统正常启动，能够通过板载串口登录。能进入安装向导。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

屏幕录像：
[![asciicast](https://asciinema.org/a/a3DgDMfhYPQgWhUjTTScbJ04n.svg)](https://asciinema.org/a/a3DgDMfhYPQgWhUjTTScbJ04n)

```log
Welcome to Ubuntu 24.04 LTS (GNU/Linux 6.8.0-31-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information disabled due to load higher than 1.0

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ cat /etc-o
cat: /etc-o: No such file or directory
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Lix
ubuntu@ubuntu:~$ 
 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
