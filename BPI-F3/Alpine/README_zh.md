# Alpine 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 下载链接：https://dev.alpinelinux.org/~mps/riscv64/
- 参考安装文档：https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -kd bpi-f3-mmc.img.xz
sudo dd if=/path/to/bpi-f3-mmc.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

显示：[press ENTER to login] 后按回车登录进入root用户

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/g8t5bdrkncNvAKxkhTEP95W5b.svg)](https://asciinema.org/a/g8t5bdrkncNvAKxkhTEP95W5b)

```log
Welcome to Alpine Linux 3.21.0_alpha20240807 (edge)
Kernel 6.6.36-2-bpi-f3 on an riscv64 (ttyS0)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

localhost:~# uname -a
Linux localhost 6.6.36-2-bpi-f3 #3-Alpine SMP Wed, 18 Sep 2024 13:41:15 +0000 riscv64 Linux

localhost:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.21.0_alpha20240807
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"

localhost:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

localhost:~# setup-alpine 


 ALPINE LINUX INSTALL
----------------------

 Hostname
----------
Enter system hostname (fully qualified form, e.g. 'foo.example.org') [localhost] 

 Interface
-----------
Available interfaces are: eth0 eth1 ip6tnl0 sit0 tunl0.
Enter '?' for help on bridges, bonding and vlans.
Which one do you want to initialize? (or '?' or 'done') [eth0] 
Ip address for eth0? (or 'dhcp', 'none', '?') [dhcp] 
Available interfaces are: eth1 ip6tnl0 sit0 tunl0.
Enter '?' for help on bridges, bonding and vlans.
Which one do you want to initialize? (or '?' or 'done') [eth1] done
Do you want to do any manual network configuration? (y/n) [n] 
[  182.914702] priv phy_interface = 9
[  183.008444] emac_phy_connect:  eth0: attached to PHY (UID 0x1cc916) Link = 0
[  183.035905] k1x_emac cac80000.ethernet eth0: registered PTP clock
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting discover
[  187.145641] k1x_emac cac80000.ethernet eth0: Link is Up - 1Gbps/Full - flow control off
udhcpc: broadcasting discover
udhcpc: broadcasting select for 192.168.5.221, server 192.168.5.1
udhcpc: lease of 192.168.5.221 obtained from 192.168.5.1, lease time 43200

 Root Password
---------------
Changing password for root
New password: 
Bad password: too short
Retype password: 
passwd: password for root changed by root

 Timezone
----------
Africa/            Egypt              Iran               Poland
America/           Eire               Israel             Portugal
Antarctica/        Etc/               Jamaica            ROC
Arctic/            Europe/            Japan              ROK
Asia/              Factory            Kwajalein          Singapore
Atlantic/          GB                 Libya              Turkey
Australia/         GB-Eire            MET                UCT
Brazil/            GMT                MST                US/
CET                GMT+0              MST7MDT            UTC
CST6CDT            GMT-0              Mexico/            Universal
Canada/            GMT0               NZ                 W-SU
Chile/             Greenwich          NZ-CHAT            WET
Cuba               HST                Navajo             Zulu
EET                Hongkong           PRC                leap-seconds.list
EST                Iceland            PST8PDT            posixrules
EST5EDT            Indian/            Pacific/

Which timezone are you in? [UTC] 

 * WARNING: clock skew detected!
 * Stopping local ...                                                     [ ok ]
 * Stopping System Message Bus ...                                        [ ok ]
 * Seeding random number generator ...
 * Saving 256 bits of creditable seed for next boot                       [ ok ]
 * WARNING: clock skew detected!
 * Starting busybox acpid ...                                             [ ok ]
 * Starting chronyd ...                                                   [ ok ]
 * Setting system clock using the hardware clock [UTC] ...                [ ok ]
 * Starting busybox syslog ...                                            [ ok ]
 * Starting busybox crond ...                                             [ ok ]
 * Starting System Message Bus ...                                        [ ok ]
 * Starting local ...                                                     [ ok ]

 Proxy
-------
HTTP/FTP proxy URL? (e.g. 'http://proxy:8080', or 'none') [none] 

 Network Time Protocol
-----------------------
Sat Jan  1 00:03:24 UTC 2000
Which NTP client to run? ('busybox', 'openntpd', 'chrony' or 'none') [chrony] 
 * rc-update: chronyd already installed in runlevel `default'; skipping
 * WARNING: chronyd has already been started

 APK Mirror
------------
 (f)    Find and use fastest mirror
 (s)    Show mirrorlist
 (r)    Use random mirror
 (e)    Edit /etc/apk/repositories with text editor
 (c)    Community repo enable
 (skip) Skip setting up apk repositories

Enter mirror number or URL: [1] 

 (f)    Find and use fastest mirror
 (s)    Show mirrorlist
 (r)    Use random mirror
 (e)    Edit /etc/apk/repositories with text editor
 (c)    Community repo enable
 (skip) Skip setting up apk repositories

Enter mirror number or URL: [1] skip


 User
------
Setup a user? (enter a lower-case loginname, or 'no') [no] 
Which ssh server? ('openssh', 'dropbear' or 'none') [openssh] 
Allow root ssh login? ('?' for help) [prohibit-password] 
Enter ssh key or URL for root (or 'none') [none] 
 * service sshd added to runlevel default
ssh-keygen: generating new host keys: RSA ECDSA ED25519 
 * Starting sshd ...                                                      [ ok ]

 Disk & Install
----------------
Available disks are:
  mmcblk2       (15.6 GB  )

Which disk(s) would you like to use? (or '?' for help or 'none') [none] 
findfs: unable to resolve 'LABEL=APKOVL'
Enter where to store configs ('floppy', 'usb' or 'none') [none] 
Enter apk cache directory (or '?' or 'none') [/var/cache/apk] 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
