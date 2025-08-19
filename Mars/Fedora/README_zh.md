# Fedora Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Fedora 41 Workstaion (20241201-091200更新版本)
- 下载链接：<https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz>
- 参考安装文档：
  1. <https://milkv.io/zh/docs/mars/getting-started/boot>
  2. <https://images.fedoravforce.org/Mars>

### 硬件信息

- Milk-V Mars (8GB RAM)
- USB 电源适配器和USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- HDMI线缆、USB鼠标、USB键盘

## 安装步骤

### 解压并刷写镜像到 microSD 卡

- 使用 `gzip` 解压镜像，并使用 `dd` 命令或者 `balenaEtcher` 软件将镜像写入 microSD 卡。（假定/dev/sdX为microSD 卡设备）

    ```bash
    wget https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz

    gzip -d fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz

    sudo dd if=fedora-disk-gnome-workstation_starfive_vf2-sda.raw of=/dev/sdX bs=1M status=progress

    sync
    ```

### 登录系统

通过串口登录系统。

默认用户名：`root`

默认密码：`riscv`

## 预期结果

系统正常启动，能够通过串口登录，连接HDMI至显示屏能够正常显示登录图像，并支持USB鼠标和USB键盘。

## 实际结果

系统正常启动，成功通过串口查看输出，连接HDMI至显示屏能够正常显示登录图像，并支持USB鼠标和USB键盘。

### 启动信息

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Sat Nov 30 15:56:44 UTC 2024

Kernel 6.6.20+ on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password:
[root@fedora-riscv ~]# cat /etc/os-release
NAME="Fedora Linux"
VERSION="41 (Workstation Edition Prerelease)"
ID=fedora
VERSION_ID=41
VERSION_CODENAME=""
PLATFORM_ID="platform:f41"
PRETTY_NAME="Fedora Linux 41 (Workstation Edition Prerelease)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
SUPPORT_END=2025-05-13
VARIANT="Workstation Edition"
VARIANT_ID=workstation

[root@fedora-riscv ~]# cat /etc/fedora-release
Fedora release 41 (Rawhide)

[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 6.6.20+ #1 SMP Mon Nov 25 20:30:54 CST 2024 riscv64 GNU/Linux

[root@fedora-riscv ~]# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

[root@fedora-riscv ~]#
```

登录的图形界面：

![登录的图形界面](./image_login.jpg)

桌面的图形界面：

![桌面的图形界面](./image_desktop.jpg)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
