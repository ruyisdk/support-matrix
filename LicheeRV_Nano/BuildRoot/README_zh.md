# BuildRoot LicheeRV Nano 测试报告

## 测试环境

### 操作系统信息

- 系统版本：20250319
- 下载链接：https://github.com/sipeed/LicheeRV-Nano-Build/releases
- 参考安装文档：https://github.com/sipeed/LicheeRV-Nano-Build

### 硬件信息

- LicheeRV Nano
- type-c 电源线一根
- UART 转 USB 调试器一个

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

下载镜像后进行解压和刷写：

```shell
wget https://github.com/sipeed/LicheeRV-Nano-Build/releases/download/20250319/2025-03-19-15-13-e4e133.img.xz
xz -d 2025-03-19-15-13-e4e133.img.xz
sudo dd if=2025-03-19-15-13-e4e133.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`root`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
Starting kernel ...

[    0.000000] Linux version 5.10.4-tag- (neucrack@neucrack-desktop) (riscv64-unknown-linux-musl-gcc (Xuantie-900 linux-5.10.4 musl gcc Toolchain V2.6.1 B-20220906) 10.2.0, GNU ld (GNU Binutils) 2.35) #19 PREEMPT Wed Mar 19 15:08:48 CST 2025
[    0.000000] earlycon: sbi0 at I/O port 0x0 (options '')
[    0.000000] printk: bootconsole [sbi0] enabled
+ mkdir -p /dev
+ mount -t devtmpfs devtmpfs /dev
+ mkdir -p /proc
+ mount -t proc proc /proc
+ mkdir -p /sys
+ mount -t sysfs sysfs /sys
+ mount -t configfs configfs /sys/kernel/config
+ mount -t debugfs debugfs /sys/kernel/debug
+ mkdir -p /boot
+ mount -o ro /dev/mmcblk0p1 /boot
+ msc=0
+ '[' -e /boot/rec ]
+ umount /dev/mmcblk0p1
+ grep lo
+ grep 'User Key'
+ wc -l
+ cat /sys/kernel/debug/gpio
+ flashkey0=0
+ sleep 0.5
+ grep lo
+ wc -l
+ grep 'User Key'
+ cat /sys/kernel/debug/gpio
+ flashkey1=0
+ '[' 0 -ne 0 ]
+ mkdir /realroot
+ mount -o rw /dev/mmcblk0p2 /realroot
+ mfail=0
+ '[' 0 -ne 0 ]
+ mount -t proc proc /realroot/proc
+ mount -t sysfs sysfs /realroot/sys
+ mount -t devtmpfs devtmpfs /realroot/dev
+ exec switch_root /realroot /sbin/init
INIT: version  booting
INIT: No inittab.d directory found
INIT: Entering runlevel: 3
load kernel module: OK
i2cget: read failed: Remote I/O error
mounting filesystem : OK
Saving 2048 bits of non-creditable seed for next boot
Starting syslogd: OK
copy config file from /boot:  beta OK
Starting klogd: OK
Running sysctl: OK
usb mode: device
sh: write error: Invalid argument
load gt9xx touchscreen driver
Populating /dev using udev: done
hostname: licheervnano-6681
ethernet mac address: 48:da:35:6f:66:81
Starting haveged: haveged: command socket is listening at fd 3
OK
load wifi kernel module: OK
Starting system message bus: done
start ethernet: OK
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
rndis mac address: 48:da:35:6f:66:81
RNDIS DHCP OK
ncm mac address: 48:da:35:6e:66:81
CDC NCM DHCP OK
wifi mode: sta
Successfully initialized wpa_supplicant
nl80211: kernel reports: Registration to specific type not supported
udhcpc: started, v1.36.1
Starting iptables: OK
Starting bluetoothd: OK
udhcpc: broadcasting discover
Starting network: OK
Starting ntpd: udhcpc: broadcasting discover
OK
Starting ssdpd: OK
ssh-keygen: generating new host keys: RSA udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
ECDSA ED25519
Starting sshd: OK
Starting audtest: OK
Starting camtest: Starting ednctest: OK
Starting input-event-daemon: input-event-daemon: fopen(/etc/input-event-daemon.conf): No such file or directory
done
Starting ivetest: OK
udhcpc: broadcasting discover
Starting lcdtest: OK
Starting loadtest: OK
Starting modeltest: OK
HELLO WORLD
Starting nettest: OK
Starting nntest: OK
Warning: Partition /dev/mmcblk0p2 is being used. Are you sure you want to continue?
udhcpc: broadcasting discover
Warning: Partition /dev/mmcblk0p2 is being used. Are you sure you want to continue?
Yes/No? yes
Information: You may need to update /etc/fstab.

Starting temptest: OK
resize2fs 1.47.0 (5-Feb-2023)

Welcome to Linux
licheervnano-6681 login: Filesystem at /dev/mmcblk0p2 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 2
udhcpc: broadcasting discover
udhcpc: broadcasting discover
The filesystem on /dev/mmcblk0p2 is now 7787647 (4k) blocks long.

udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: broadcasting discover
udhcpc: no lease, forking to background
udhcpc: no lease, forking to background

Welcome to Linux
licheervnano-6681 login: root
licheervnano-6681 login: root
Password:
# uname -a
Linux licheervnano-6681 5.10.4-tag- #19 PREEMPT Wed Mar 19 15:08:48 CST 2025 riscv64 GNU/Linux
# cat /etc/os-release
NAME=Buildroot
VERSION=-ge4e133f3d
ID=buildroot
VERSION_ID=2023.11.2
PRETTY_NAME="Buildroot 2023.11.2"
INIT: Id "acm" respawning too fast: disabled for 5 minutes

# lscpu
-sh: lscpu: not found
# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。