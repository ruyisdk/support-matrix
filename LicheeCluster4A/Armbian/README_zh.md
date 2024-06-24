# Armbian Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 20.04 LTS 
- 下载链接：[https://github.com/chainsx/armbian-riscv-build/tree/main](https://github.com/chainsx/armbian-riscv-build/tree/main)
    - u-boot: [https://github.com/chainsx/thead-u-boot/actions](https://github.com/chainsx/thead-u-boot/actions)
- 参考安装文档：[https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_zh.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_zh.md)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)


### 硬件信息

- Lichee Cluster 4A 8G / 16G
- DC 12V 电源
- USB-A to A
    - 或 LPi4A 底板
- microSD 卡一张
- 网络和网线（注意连接到 BMC 而非交换机）

## 安装步骤

*以下以刷写到集群中一号板为例*

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/Armbian.img.xz
sudo dd if=/path/to/Armbian.img of=/dev/your_device bs=1M status=progress
```

### 刷写 bootloader

此处使用上面下载的 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc` **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

初次启动会要求设置用户及密码。

### 常见问题

若无法使用 USB，是因为 Linux 设备树需要 patch。[patch 下载](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/glbyZg6rjqfWu1YiQhyj62Zww.svg)](https://asciinema.org/a/glbyZg6rjqfWu1YiQhyj62Zww)


```log
Welcome to ARMBIAN! 

Documentation: https://docs.armbian.com | Community: https://forum.armbian.com

Create root password: ********
Repeat root password: ********
Rejected - it does not contain enough DIFFERENT characters. Try again [3].
Create root password: ********
Repeat root password: ********

Choose default system command shell:

1) bash
2) zsh

Shell: BASH

Creating a new user account. Press <Ctrl-C> to abort

Desktop environment will not be enabled if you abort the new user creation

Please provide a username (eg. your first name): plct
Create user (plct) password: ********
Repeat user (plct) password: ********

Please provide your real name: Plct

Dear Plct, your account plct has been created and is sudo enabled.
Please use this account for your daily work from now on.

Detected timezone: Asia/Hong_Kong

Set user language based on your location? [Y/n] 


At your location, more locales are possible:

1) en_HK.UTF-8              3) Skip generating locales
2) zh_HK.UTF-8
Please enter your choice:1) en_HK.UTF-8             3) Skip generating locales
2) zh_HK.UTF-8
Please enter your choice:1

Generating locales: en_HK.UTF-8

Now starting desktop environment...

root@licheepi-4a:~# uname -a
Linux licheepi-4a 5.10.113-thead-g052b22ef8baf #riscv SMP PREEMPT Sun Sep 24 07:26:26 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
root@licheepi-4a:~# cat /etc/os-release 
NAME="Ubuntu"
VERSION="20.04 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Armbian-riscv 23.09.15-riscv Focal"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
root@licheepi-4a:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。