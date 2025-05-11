# ArchLinux Milk-V Mars 测试报告

## 测试环境

### 硬件信息

- 开发板：Milk-V Mars (8GB RAM)
- 其他硬件：
  - USB 电源适配器和USB-A to C 或 C to C 线缆一条
  - microSD 卡一张
  - USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

### 操作系统信息

- 操作系统版本：ArchLinux (VF2_6.12_v5.14.0-cwt24)
- 下载链接：<https://github.com/cwt-vf2/archlinux-image-vf2/releases/download/cwt24/ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst>
- 参考安装文档：
  - <https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459>
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>

## 安装步骤

### 刷写镜像

使用 `zstd` 命令解压镜像，并使用 `dd` 命令或 `balenaEtcher` 软件将镜像写入 microSD 卡。

其中，`/dev/sdc` 为存储卡对应设备。

```bash
wget https://github.com/cwt-vf2/archlinux-image-vf2/releases/download/cwt24/ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst

zstd -d ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst

sudo dd if=ArchLinux-VF2_6.12_v5.14.0-cwt24.img of=/dev/sdc bs=1M status=progress

sync
```

### 登录系统

通过串口登录系统。

用户名：root

默认密码：archriscv

或者

用户名：user

密码：user

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
Arch Linux 6.12.18-cwt-5.14.0-2 (ttyS0)

ArchVF2 login: root
Password:
[root@ArchVF2 ~]#

[root@ArchVF2 ~]# uname -a
Linux ArchVF2 6.12.18-cwt-5.14.0-2 #1 SMP PREEMPT_DYNAMIC Tue Apr  8 17:15:39 +07 2025 riscv64 GNU/Linux

[root@ArchVF2 ~]# cat /etc/os-release
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

[root@ArchVF2 ~]# cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

[root@ArchVF2 ~]#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
