# Arch Linux Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：archriscv-2025-06-12

需要自行构建。

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo S
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- TF 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 构建步骤

### 构建 Buildroot

请参阅 [milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk)。

在第一次构建完成目标 `milkv-duos-sd` 后，修改 `build/boards/cv181x/cv1813h_milkv_duos_sd/linux/cvitek_cv1813h_milkv_duos_sd_defconfig`

增加下列行。

```
CONFIG_CGROUPS=y
CONFIG_CGROUP_FREEZER=y
CONFIG_CGROUP_PIDS=y
CONFIG_CGROUP_DEVICE=y
CONFIG_CPUSETS=y
CONFIG_PROC_PID_CPUSET=y
CONFIG_CGROUP_CPUACCT=y
CONFIG_PAGE_COUNTER=y
CONFIG_MEMCG=y
CONFIG_CGROUP_SCHED=y
CONFIG_NAMESPACES=y
CONFIG_OVERLAY_FS=y
CONFIG_AUTOFS4_FS=y
CONFIG_SIGNALFD=y
CONFIG_TIMERFD=y
CONFIG_EPOLL=y
CONFIG_IPV6=y
CONFIG_FANOTIFY=y
```

然后再构建一次，获得镜像 `out/milkv-duos-sd-<your-build-timex>.img`。

### 更新根文件系统

为了防止权限问题，请考虑切换到根用户操作。

#### 下载根文件系统

先从 [Arch Linux RISC-V](https://archriscv.felixc.at/) 下载根文件系统。

```
wget https://archriscv.felixc.at/images/archriscv-2025-06-12.tar.zst
```

#### 挂载镜像

```
sudo losetup -f
```

输出 `/dev/loop0`，下文请根据情况修改。缺少环设备需要新建。

挂载镜像到环设备上。

```
losetup -P loop0 out/milkv-duos-sd_2025-0831-0547.img
```

挂载分区到目录。

```
mkdir /mnt/duo-rootfs
cd /mnt/duo-rootfs
mount /dev/loop0p3 /mnt/duo-rootfs
```

删除原来的一切。

```
rm -rf ./*
```

将根文件系统解压到此处。

```
tar -xvf archriscv-2025-06-12.tar.zst -C .
```

#### 下载包

为了有网络用，下载一些包到目录中以便安装。

```
cd /mnt/duo-rootfs/root
wget https://mirror.iscas.ac.cn/archriscv/repo/core/nano-8.2-1-riscv64.pkg.tar.zst
wget https://mirror.iscas.ac.cn/archriscv/repo/extra/dhcpcd-10.0.10-1-riscv64.pkg.tar.zst
```

### 卸载镜像

```
umount /dev/loop0p3
losetup -d /dev/loop0
```

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
dd if=milkv-duos-sd_2025-0831-0547.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

- 默认账号：root
- 默认密码：archriscv

#### 配置网络

使用 UART 连接到开发板。

```
pacman -U ./dhcpcd-10.0.10-1-riscv64.pkg.tar.zst
pacman -U ./nano-8.2-1-riscv64.pkg.tar.zst
```

启动网络。

```
ip link set end0 up
systemctl start dhcpcd.service
systemctl enable dhcpcd.service
```

##### 手动配置网络

如果需要手工配置网络，参考如下代码。

```
ip link set end0 up
ip addr add 172.16.0.188/12 broadcast 172.31.255.255 dev end0 #172.16.0.188/12为本机IP，172.31.255.255为广播地址。
ip route add default via 172.16.0.1 #默认网关
echo -e "nameserver 172.16.0.1" >> /etc/resolv.conf #DNS服务器
```

也许需要重新启动。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```bash
         Starting Flush Journal to Persistent Storage...
[    9.174420] systemd-journald[127]: Received client request to flush runtime journal.
[    9.200170] systemd-journald[127]: File /var/log/journal/33bd66794bef4c019a0e3acfdcceb30a/system.journal corrupted or uncleanly shut down, renaming and replacing.
[  OK  ] Finished Flush Journal to Persistent Storage.
[  OK  ] Started User Database Manager.
[  OK  ] Finished Coldplug All udev Devices.
[  OK  ] Finished Create Static Device Nodes in /dev gracefully.
         Starting Create Static Device Nodes in /dev...
[  OK  ] Finished Create Static Device Nodes in /dev.
[  OK  ] Reached target Preparation for Local File Systems.
[  OK  ] Reached target Local File Systems.
[  OK  ] Listening on Boot Entries Service Socket.
[  OK  ] Listening on Disk Image Download Service Socket.
[  OK  ] Listening on System Extension Image Management.
         Starting Create System Files and Directories...
         Starting Rule-based Manager for Device Events and Files...
[   12.700936] random: crng init done
[  OK  ] Finished Load/Save OS Random Seed.
[  OK  ] Finished Create System Files and Directories.
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Started Rule-based Manager for Device Events and Files.
[   13.672405] bm-dwmac 4070000.ethernet end0: renamed from eth0
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
[  OK  ] Reached target Sound Card.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Refresh existing PGP keys of archlinux-keyring regularly.
[  OK  ] Started Daily verification of password and group files.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target Timer Units.
[  OK  ] Reached target Hardware activated USB gadget.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Listening on GnuPG network certifi…ent daemon for /etc/pacman.d/gnupg.
[  OK  ] Listening on GnuPG cryptographic a… browsers) for /etc/pacman.d/gnupg.
[  OK  ] Listening on GnuPG cryptographic a…estricted) for /etc/pacman.d/gnupg.
[  OK  ] Listening on GnuPG cryptographic a…emulation) for /etc/pacman.d/gnupg.
[  OK  ] Listening on GnuPG cryptographic a…rase cache for /etc/pacman.d/gnupg.
[  OK  ] Listening on GnuPG public key mana…nt service for /etc/pacman.d/gnupg.
[  OK  ] Listening on Hostname Service Socket.
[  OK  ] Reached target Socket Units.
[  OK  ] Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
         Starting D-Bus System Message Bus...
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Reached target Basic System.
         Starting User Login Management...
         Starting Permit User Sessions...
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Reached target Login Prompts.
[   16.871684] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/lib/systemd/linger supports timestamps until 2038 (0x7fffffff)
[   16.886837] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
[   16.899137] ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
[   16.925233] ext4 filesystem being remounted at /run/systemd/mount-rootfs/etc supports timestamps until 2038 (0x7fffffff)
[   17.048985] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/lib/systemd/linger supports timestamps until 2038 (0x7fffffff)
[   17.068576] ext4 filesystem being remounted at /run/systemd/mount-rootfs/var/tmp supports timestamps until 2038 (0x7fffffff)
[  OK  ] Started User Login Management.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.

Arch Linux 5.10.4-tag- (ttyS0)

archlinux login: root
Password:
[root@archlinux ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
[root@archlinux ~]#
```

屏幕录像：

[![asciicast](https://asciinema.org/a/mMXIs8084TXdx8zVAg2scpPWe.svg)](https://asciinema.org/a/mMXIs8084TXdx8zVAg2scpPWe)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
