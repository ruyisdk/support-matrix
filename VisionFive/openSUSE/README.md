# openSUSE Tumbleweed VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：openSUSE Tumbleweed
- 下载链接：[https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/)
- 参考安装文档：[https://en.opensuse.org/HCL:VisionFive](https://en.opensuse.org/HCL:VisionFive)

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
unxz /path/to/openSUSE.raw.xz
sudo dd if=/path/to/openSUSE.raw of=/dev/your-device bs=1M status=progress
```

### patch 镜像

挂载 SD 卡后：

创建 `/boot/uEnv.txt` 并加入以下内容：

```
fdt_high=0xffffffffffffffff
initrd_high=0xffffffffffffffff

scriptaddr=0x88100000
script_offset_f=0x1fff000
script_size_f=0x1000

kernel_addr_r=0x84000000
kernel_comp_addr_r=0x90000000
kernel_comp_size=0x10000000

fdt_addr_r=0x88000000
ramdisk_addr_r=0x88300000

fdtfile=starfive/jh7100-starfive-visionfive-v1.dtb

bootcmd=load mmc 0:1 0xa0000000 /EFI/BOOT/bootriscv64.efi; bootefi 0xa0000000
bootcmd_mmc0=devnum=0; run mmc_boot
```

在 `/boot/grub2/grub.cfg` 中每个入口后加入以下内容（在`linux`之后）：

```
devicetree /boot/dtb/starfive/jh7100-starfive-visionfive-v1.dtb
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `linux`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/bTRGI0BeLsyA2Fg9xMZtXeVHU.svg)](https://asciinema.org/a/bTRGI0BeLsyA2Fg9xMZtXeVHU)

```log
Welcome to openSUSE Tumbleweed 20240321 - Kernel 6.8.1-130-default (ttyS0).

eth0:  
wlan0:  


localhost login: root
Password: 
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.8.1-130-default #1 SMP PREEMPT_DYNAMIC Mon Mar 18 09:49:44 UTC 2024 (74a8025) riscv64 riscv64 risx
localhost:~ # cat /etc/os-release 
NAME="openSUSE Tumbleweed"
# VERSION="20240321"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20240321"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
# CPE 2.3 format, boo#1217921
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240321:*:*:*:*:*:*:*"
#CPE 2.2 format
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240321"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。