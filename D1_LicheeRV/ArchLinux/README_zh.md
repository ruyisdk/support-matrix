# Arch Linux LicheeRV / AWOL Nezha D1 测试报告

## 测试环境

### 操作系统信息

- 基础镜像：Ubuntu 24.10 Beta: [ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz) 
  - 或任意 D1 的镜像
- Rootfs：[archriscv-20220727.tar.zst](https://archriscv.felixc.at/images/archriscv-20220727.tar.zst)
- 参考安装文档：https://github.com/felixonmars/archriscv-packages/wiki/RV64-%E6%9D%BF%E5%AD%90%E6%9B%B4%E6%8D%A2-rootfs-%E6%8C%87%E5%8D%97
h

### 硬件信息

- Nezha D1
- Type-C 电源线一根
- UART 转 USB 调试器一个
- SD 卡

## 安装步骤

### 获取镜像和 rootfs

下载基础镜像和 rootfs。任何 D1 的镜像都可以作为基础镜像。

Debian 镜像和 Ubuntu 镜像曾被验证过能工作。接下来以 Ubuntu 镜像为例。

```bash
wget https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz
wget https://archriscv.felixc.at/images/archriscv-20220727.tar.zst
xz -kd ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz
mkdir rfs
tar -xf archriscv-20220727.tar.zst -C rfs
mndir mnt
```

### 替换 rootfs

用 Arch Linux 的 rootfs 替换 Ubuntu 镜像中的 rootfs。将下面的分区更改为正确的 rootfs 分区。

```bash
sudo losetup -f
sudo losetup -P /dev/loopx ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img
sudo mount /dev/loopxp1 mnt
cd mnt
sudo mkdir old
sudo mv etc home media mnt opt root srv var usr old/
sudo cp -r ../rfs/{etc,home,mnt,opt,root,srv,var,usr} .
sudo cp -r old/usr/lib/firmware usr/lib/
sudo cp -r old/usr/lib/modules/ usr/lib/
rm etc/fstab
sudo rm etc/fstab
sudo cp -r old/etc/fstab etc/fstab
```

清理工作。

```bash
cd ..
sudo umount mnt
sudo losetup -d /dev/loopx
```

### 刷写镜像

将镜像刷写到 SD 卡。

```bash
sudo wipefs -a /dev/sdX
sudo dd if=ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img of=/dev/sdX bs=4M status=progress
```


### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`archriscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/G3j3MjoOZ8rcTD28kfMLDao6a.svg)](https://asciinema.org/a/G3j3MjoOZ8rcTD28kfMLDao6a)

```log
[root@archlinux ~]# cat /etc/os-release
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo
[root@archlinux ~]# uname -a
Linux archlinux 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 GNU/Linux
[root@archlinux ~]# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm


```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功