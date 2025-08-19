# DietPi Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：DietPi v9.12.1
- 下载链接：<https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Trixie.img.xz>
- 参考安装文档：
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://dietpi.com/blog/?p=2629>

### 硬件信息

- Milk-V Mars (8GB RAM)
- USB 电源适配器和USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 解压并刷写镜像到 microSD 卡

使用 `xz` 解压镜像，并使用 `dd` 命令或者 `balenaEtcher` 软件将镜像写入 microSD 卡。（假定/dev/sdc为microSD 卡设备）

```bash
wget https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz

xz -d visionfive-v2-mmc.img.xz

sudo dd if=visionfive-v2-mmc.img of=/dev/sdX bs=1M status=progress

sync
```

### 引导模式选择

Milk-V Mars 在V1.2的硬件版本后提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 Armbian 镜像，选择 SPI Flash 启动模式（即：`GPIO_0 = 0`, `GPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件。

### 登录系统

通过串口登录系统。

默认用户名：`root`

默认密码：`dietpi`

进入系统后将联网开始更新。若出现网络问题，可在交互界面更改网络检查命令的ip地址为 `8.8.8.8` 。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

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
 DietPi v9.12.1 : 17:21 - Sun 05/25/25
 ─────────────────────────────────────────────────────
 - LAN IP : 192.168.137.102 (eth0)
tee: /var/tmp/dietpi/logs/dietpi-firstrun-setup.log: No such file or directory

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Checking for available DietPi update

[.     ]PING 9.9.9.9 (9.9.9.9) 56(84) bytes of data.ctivity (2/2)

--- 9.9.9.9 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms

[FAILED] DietPi-Update | Checking IPv4 network connectivity
 - Command: ping -4nc 1 -W 10 9.9.9.9
StarFive VisionFive 2 (riscv64) | IP: 192.168.137.102




  ┌──────────────────────────────────────────────────┤ DietPi-Update ├───────────────────────────────────────────────────┐
  │ Checking IPv4 network connectivity                                                                                   │
  │  - Command: ping -4nc 1 -W 10 9.9.9.9                                                                                │
  │  - Exit code: 1                                                                                                      │
  │  - DietPi version: v9.12.1 (MichaIng/master) | HW_MODEL: 81 | HW_ARCH: 11 | DISTRO: 8                                │
  │  - Error log:                                                                                                        │
  │ PING 9.9.9.9 (9.9.9.9) 56(84) bytes of data.                                                                         │
  │                                                                                                                      │
  │ --- 9.9.9.9 ping statistics ---                                                                                      │
  │ 1 packets transmitted, 0 received, 100% packet loss, time 0ms                                                        │
  │                                                                                                                      │
  │                    Retry               : Re-run the last command that failed                                         │
  │                    Double timeout      : Retry with doubled timeout for ping to wait for a reply                     │
  │                    Change IPv4 address : Change the IPv4 address used for this test                                  │
  │                    Network settings    : Enter dietpi-config network options                                         │
  │                    DietPi-Config       : Edit network, APT/NTP mirror settings etc                                   │
  │                    Open subshell       : Open a subshell to investigate or solve the issue                           │
  │                    Send report         : Upload bug report including system info to DietPi                           │
  │                    Print report        : Print bug report template for GitHub or forum                               │
  │                                        ●─ Devs only ───────────────────────────────────────────●                     │
  │                    Change command      : Adjust and rerun the command                                                │
  │                                                                                                                      │
  │                                                                                                                      │
  │                                  <Select>                                  <Exit>                                    │
  │                                                                                                                      │
  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
StarFive VisionFive 2 (riscv64) | IP: 192.168.137.102




  ┌──────────────────────────────────────────────────┤ DietPi-Update ├───────────────────────────────────────────────────┐
  │ Please enter/alter the command to be executed.                                                                       │
  │                                                                                                                      │
  │ NB: Please only use this solution if you know for sure that it will not cause follow up issues from the originating  │
  │ script. It will e.g. allow you to continue a certain software install, but if you edit the download link, the        │
  │ originating script might expect files which are not present.                                                         │
  │                                                                                                                      │
  │ Use this with caution!                                                                                               │
  │                                                                                                                      │
  │ ping -4nc 1 -W 10 8.8.8.8___________________________________________________________________________________________ │
  │                                  <Ok>                                      <Cancel>                                  │
  │                                                                                                                      │
  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


[ INFO ] DietPi-Update | Executing alternative command: ping -4nc 1 -W 10 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=112 time=29.1 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 29.087/29.087/29.087/0.000 ms
[  OK  ] Alternative command execution | Completed
[  OK  ] DietPi-Update | Checking DNS resolver
[  OK  ] DietPi-TimeSync | systemctl stop systemd-timesyncd
[  OK  ] DietPi-TimeSync | mkdir -p /run/systemd/timesync
[ INFO ] DietPi-Update | Getting latest version from: https://raw.githubusercontent.com/MichaIng/DietPi/master/.update/version

[  OK  ] DietPi-Update | Got valid latest version: 9.12.1
[  OK  ] DietPi-Update | eval echo 1 > /boot/dietpi/.install_stage
[  OK  ] DietPi-Update | No update required, your DietPi installation is already up to date:
[ INFO ] DietPi-Update | Current version : v9.12.1
[ INFO ] DietPi-Update | Latest version  : v9.12.1
[ INFO ] DietPi-Update | Checking for new available live patches
[ INFO ] DietPi-Update | APT update, please wait...


[  OK  ] DietPi-Survey | Setting in /boot/dietpi.txt adjusted: SURVEY_OPTED_IN=0
[  OK  ] DietPi-Survey | Purging survey data
[ SUB1 ] DietPi-Services > restart
[  OK  ] DietPi-Services | restart : cron
 ─────────────────────────────────────────────────────
 DietPi v9.12.1 : 17:49 - Sun 05/25/25
 ─────────────────────────────────────────────────────
 - Device model : StarFive VisionFive 2 (riscv64)
 - CPU temp : 58 °C / 136 °F : Running warm, but safe
 - LAN IP : 192.168.137.102 (eth0)
 - MOTD : Open Beta v9.13 | Please help testing our upcoming release:
          https://github.com/MichaIng/DietPi/issues/7539
 ─────────────────────────────────────────────────────

 DietPi Team     : https://github.com/MichaIng/DietPi#the-dietpi-project-team
 Patreon Legends : Chris Gelatt, ADSB.im
 Website         : https://dietpi.com/ | https://x.com/DietPi_ | Bsky: @dietpi.com
 Contribute      : https://dietpi.com/contribute.html
 Web Hosting by  : https://myvirtualserver.com

 dietpi-launcher : All the DietPi programs in one place
 dietpi-config   : Feature rich configuration tool for your device
 dietpi-software : Select optimised software for installation
 htop            : Resource monitor
 cpu             : Shows CPU information and stats

root@DietPi:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.0
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

root@DietPi:~# uname -a
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:02:10 UTC 2024 riscv64 GNU/Linux

root@DietPi:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
