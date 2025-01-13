# RevyOS LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS 20250110
- 下载链接：[ISCAS mirror](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
- 参考安装文档：https://revyos.github.io/docs/

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C 电源适配器 / DC 电源一个
- USB-UART 调试器一个

## 安装步骤

### 下载并解压镜像

下载镜像，使用 `zstd` 解压镜像：

```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250110/boot-lpi4a-20250110_151339.ext4.zst
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250110/u-boot-with-spl-lpi4a-16g-main.bin
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250110/root-lpi4a-20250110_151339.ext4.zst
zstd -d boot-lpi4a-20250110_151339.ext4.zst
zstd -d root-lpi4a-20250110_151339.ext4.zst
```

### 通过 `fastboot` 刷写到板载 eMMC

有两种方式进入 fastboot 模式：

#### 使用 boot 按钮进入 fastboot 模式

按住 **BOOT** 按钮，然后连接 USB-C 线（另一端连接 PC）进入 USB 烧录模式。

#### 使用 u-boot 进入 fastboot 模式

进入 u-boot 控制台后，中断 u-boot，使用以下命令进入 fastboot 模式：

```shell
fastboot usb 0
```

---

在 Linux 中使用 `lsusb` 命令，你会看到一个设备：`ID 2345:7654 T-HEAD USB download gadget`。

使用以下命令刷写镜像。

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot flash boot boot-lpi4a-20250110_151339.ext4
sudo fastboot flash root root-lpi4a-20250110_151339.ext4
```

### 登录系统

通过串口或图形界面登录系统。

默认用户名：`debian`
默认密码：`debian`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

屏幕录制（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/4kw9rznzmMGsEdD2lSqJOSm3h.svg)](https://asciinema.org/a/4kw9rznzmMGsEdD2lSqJOSm3h)

```log

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux trixie/sid (kernel 6.6.66-th1520)

Linux revyos-lpi4a 6.6.66-th1520 #2025.01.10.02.53+1c6721ec2 SMP Fri Jan 10 03:09:24 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Sep  2 05:03:30 2024
debian@revyos-lpi4a:~$ uname -a
Linux revyos-lpi4a 6.6.66-th1520 #2025.01.10.02.53+1c6721ec2 SMP Fri Jan 10 03:09:24 UTC 2025 riscv64 GNU/Linux
debian@revyos-lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@revyos-lpi4a:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

debian@revyos-lpi4a:~$  
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
