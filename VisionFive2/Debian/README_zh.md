# Debian VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian bookworm (starfive-jh7110-202403-SD-minimal-desktop-wayland.img.bz2)
- 下载链接：https://debian.starfivetech.com/
- 参考安装文档：https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
bzip2 -dk starfive-jh7110-202403-SD-minimal-desktop-wayland.img.bz2
sudo dd if=starfive-jh7110-202403-SD-minimal-desktop-wayland.img of=/dev/sdc bs=1M status=progress
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动原厂 Debian 镜像，可以选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若您启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

若不更新固件，请选择 microSD 卡引导（即：`RGPIO_0 = 1`, `RGPIO_1 = 0`）。

> 注意，此模式下有小概率出现启动失败的情况，如遇到启动失败，串口输出类似如下信息：
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> 您可以尝试重新给开发板上电，或点按一下 USB Type-C 供电接口附近的按钮。通常这可以解决无法启动的问题。

### 登录系统

通过串口登录系统。

默认用户名：`user`
默认密码：`starfive`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid starfive ttyS0

starfive login: [   37.039220] mipi_0p9: disabling

starfive login: user
Password: 
Linux starfive 6.6.20-starfive #41SF SMP Fri Sep 20 17:48:26 CST 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
user@starfive:~$ uname -a
Linux starfive 6.6.20-starfive #41SF SMP Fri Sep 20 17:48:26 CST 2024 riscv64 GNU/Linux
user@starfive:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
BUILD_ID=32
BUILD_DATE=T2024-09-23
user@starfive:~$ cat /proc/cpuinfo 
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

user@starfive:~$ 
```

![](./image.png)

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/CCoYSyfdX7TWoiXM8Kct8nTVF.svg)](https://asciinema.org/a/CCoYSyfdX7TWoiXM8Kct8nTVF)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
