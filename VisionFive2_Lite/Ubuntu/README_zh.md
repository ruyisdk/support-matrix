# Ubuntu 24.04.4 VisionFive 2 Lite 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04.4 LTS Server
- 系统镜像：`ubuntu-24.04.4-preinstalled-server-riscv64+jh7110.img.xz`
- 下载链接：https://cdimage.ubuntu.com/ubuntu/releases/24.04.4/release/
- 参考安装文档：https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/starfive-visionfive-2/

### 硬件信息

- StarFive VisionFive 2 Lite
- Type-C 电源适配器
- Type-C 数据线
- USB 转 TTL 串口模块
- 杜邦线三根

## 安装步骤

### 解压系统镜像

下载系统镜像：

```
ubuntu-24.04.4-preinstalled-server-riscv64+jh7110.img.xz
```

解压得到对应的 `.img` 镜像文件，用于后续 eMMC 烧录。

### 连接串口并进入 Fastboot

下载并解压 SFFB Tool：

```
https://files.waveshare.net/wiki/VisionFive2/SFFB_Tool_V1.0.7z
```

准备 Tera Term 串口工具。

使用 USB 转 TTL 串口模块连接 VisionFive 2 Lite 40Pin 上对应的串口引脚。

开发板一侧：

```
GND    TX    RX
```

分别连接串口模块：

```
GND    RX    TX
```

将串口模块连接电脑 USB 口，打开 Tera Term，将波特率设置为：

```
115200
```

给开发板上电，同时在串口窗口中按任意键打断自动启动，进入 U-Boot 命令行。

执行：

```
fastboot usb 0
```

进入 Fastboot 模式。

### 安装驱动并烧录镜像

打开 Windows 设备管理器，确认出现：

```
USB Download Gadget
```

选择：

```
更新驱动程序
→ 浏览我的电脑以查找驱动程序
```

驱动目录选择：

```
SFFB_Tool_V1.0\usb_driver
```

完成驱动安装。

打开 SFFB Tool，选择解压后的系统镜像，然后点击：

```
Start All
```

或：

```
Action → Run
```

开始烧录镜像。

等待镜像传输完成后给开发板断电。

### 首次启动

重新给 VisionFive 2 Lite 上电，通过串口观察启动过程，等待系统进入 Ubuntu 登录界面。

### 登录系统

通过串口登录系统。

默认用户名：

```
user
```

默认密码：

```
starfive
```

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```
Ubuntu 24.04.4 LTS starfive ttyS0

starfive login: user
Password:
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.12.5-starfive riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

System information as of Wed Jul 15 14:34:55 UTC 2026

  System load:            2.37
  Usage of /:             49.1% of 51.40GB
  Memory usage:           8%
  Swap usage:             0%
  Temperature:            48.0 C
  Processes:              213
  Users logged in:        0
  IPv4 address for wlan0: 192.0.2.1
  IPv6 address for wlan0: 2001:db8::1
  IPv6 address for wlan0: 2001:db8::2

Expanded Security Maintenance for Applications is not enabled.

48 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

41 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm

17 updates could not be installed automatically. For more details,
see /var/log/unattended-upgrades/unattended-upgrades.log

user@starfive:~$ uname -a
Linux starfive 6.12.5-starfive #70SF SMP Sun Sep 28 11:33:07 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux

user@starfive:~$ lscpu
Architecture:             riscv64
Byte Order:               Little Endian
CPU(s):                   4
On-line CPU(s) list:      0-3
Vulnerabilities:
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Not affected
  Spectre v1:             Not affected
  Spectre v2:             Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected

user@starfive:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
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

user@starfive:~$
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
