# DietPi VisionFive 2 测试报告

## 测试环境

### 操作系统信息

- 系统版本：v9.7.1 (MichaIng/master)
- 下载链接：https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Sid.img.xz
- 参考安装文档：https://dietpi.com/blog/?p=2629

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```bash
xz -d DietPi_VisionFive2-RISC-V-Sid.img.xz
dd if=DietPi_VisionFive2-RISC-V-Sid.img of=/dev/<your-device> 
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 DietPi 镜像，可以选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若您启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### 登录系统

通过串口登录系统。

用户名：`root`
默认密码：`dietpi`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid DietPi ttyS0

DietPi login: root
Password: 
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:02:10 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
 ─────────────────────────────────────────────────────
 DietPi v9.7.1 : 14:51 - Fri 10/25/24
 ─────────────────────────────────────────────────────
 - LAN IP : 192.168.31.87 (eth0)

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Checking for available DietPi update

[  OK  ] DietPi-Update | Checking IPv4 network connectivity
[  OK  ] DietPi-Update | Checking DNS resolver
[  OK  ] DietPi-TimeSync | systemctl start systemd-timesyncd
[ INFO ] DietPi-TimeSync | Waiting for time sync (1/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (2/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (3/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (4/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (5/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (6/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (7/60)
[  OK  ] DietPi-TimeSync | Time sync completed
[  OK  ] DietPi-TimeSync | systemctl stop systemd-timesyncd
[  OK  ] DietPi-TimeSync | mkdir -p /run/systemd/timesync
[ INFO ] DietPi-Update | Getting latest version from: https://raw.githubusercontent.com/MichaIng/DietPi/master/.update/version
[  OK  ] DietPi-Update | Got valid latest version: 9.8.0
[  OK  ] DietPi-Update | Update available:
[ INFO ] DietPi-Update | Current version : v9.7.1
[ INFO ] DietPi-Update | Latest version  : v9.8.0

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Checking for update pre-requirements

[  OK  ] DietPi-Update | DietPi-Userdata validation: /mnt/dietpi_userdata
[  OK  ] DietPi-Update | Free space check: path=/ | available=28171 MiB | required=100 MiB
[ SUB1 ] DietPi-Services > stop 
[  OK  ] DietPi-Services | stop : cron

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Applying pre-patches

[  OK  ] DietPi-Update | Downloading pre-patches
[  OK  ] DietPi-Update | Applying execute permission
[  OK  ] DietPi-Update | Successfully applied pre-patches

 DietPi-Update
StarFive VisionFive 2 (riscv64) | IP: 192.168.31.87 | Use up/down buttons to scr
│ APT update
│  - Command: apt-get -y -eany update
│  - Exit code: 100
│  - DietPi version: v9.7.1 (MichaIng/master) | HW_MODEL: 81 | HW_ARCH: 11 |
│ DISTRO: 8
root@DietPi:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@DietPi:~# uname -a 
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:02:10 UTC 2024 riscv64 GNU/Linux

```

屏幕录像（登录系统）：
[![asciicast](https://asciinema.org/a/IMU31fDOjU2FgiYnFjriTaycE.svg)](https://asciinema.org/a/IMU31fDOjU2FgiYnFjriTaycE)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
