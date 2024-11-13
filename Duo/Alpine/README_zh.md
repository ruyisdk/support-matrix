# Alpine Linux Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：3.19_alpha20230901 / 3.20.3 riscv64
- 下载链接：
  - https://github.com/cwt/duo-buildroot-sdk/releases/download/poc1/MilkV-Duo-alpine.img.xz
  > Note: 此镜像为社区开发者提供，非官方镜像。

  或者
  - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
  - 官方 Buildroot 镜像: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip)
- 参考安装文档：
  - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
  - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
  - [Milk-V forum thread](https://community.milkv.io/t/alpine-linux-on-the-duo/700/18)

### 硬件信息

- Milk-V Duo
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- microSD 读卡器一个
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 方式一：刷写社区镜像

下载镜像：https://github.com/cwt/duo-buildroot-sdk/releases/download/poc1/MilkV-Duo-alpine.img.xz

之后使用如下命令刷入
```shell
xz -d MilkV-Duo-alpine.img.xz
sudo dd if=MilkV-Duo-alpine.img of=/dev/your/device bs=1M status=progress
```

### 方式二：自行制作 rootfs 刷入
如不能使用上述镜像，也可以自行参考如下步骤通过使用官方 rootfs 替换 buildroot 或其他发行版镜像中对应内容的方式启动。

#### 下载 Alpine minirootfs 和 Buildroot 镜像

```bash
wget https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz
tar -xvf alpine-minirootfs-3.20.3-riscv64.tar.gz --one-top-level
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip
unzip milkv-duo-sd-v1.1.3-2024-0930.img.zip
```

#### 准备 rootfs
Alpine 官方提供的 riscv64 发行仅是一个 "minirootfs", 缺少 OpenRC 等必要的系统组件。要在实体硬件上启动，我们需要使用 `apk` 在该 minirootfs 中安装 Alpine 基础包。 

##### 安装 Alpine 包管理器 `apk`
（如果宿主机已经在使用 Alpine 系发行版则跳过此步）
安装 `apk-tools` （如在 Arch Linux 上： `sudo pacman -S apk-tools`），并运行 `apk --help` 确认安装。

##### 在 minirootfs 中安装 Alpine 基础包 `alpine-base`

(注：无需 `chroot`)

```bash
cd alpine-minirootfs-3.20.3-riscv64
sudo apk add -p . --initdb -U --arch riscv64 --allow-untrusted alpine-base
```

##### 额外设置

1. 编辑 `./etc/inittab`，加入或取消注释下面一行以启用 `/dev/ttyS0` 上的串口访问：
    ```
    ttyS0::respawn:/sbin/getty -L 115200 ttyS0 vt100
    ```
    并注释掉以 `tty1` - `tty6` 开头的六行。

2. 编辑 `./etc/passwd`:

    去掉 `root:x:0:0:root:/root:/bin/sh` 一行中的 `x`。

    （也可以编辑  `/etc/shadow` 并去掉 `root:*::0:::::` 一行中的 `*`）。

3. 启用 OpenRC hostname 服务 （否则主机名无法正确设置）：
   
   ```bash
   ln -s ./etc/init.d/hostname ./etc/runlevels/boot
   ```
   可仿照此步按需启用其他的 OpenRC 系统服务。

#### 刷入 Buildroot 镜像

```bash
cd ..
sudo dd if=milkv-duo-sd-v1.1.3-2024-0930.img of=/dev/your/device bs=4M status=progress
```

你的设备应该能识别到 SD 卡上的 `rootfs` 和 `boot` 两个分区。挂载 `rootfs` 分区。

#### 替换 SD 卡上根目录为 Alpine rootfs
```bash
rm -rf /path/to/your/mnt/root/*
cp -r /path/to/your/alpine-minirootfs-3.20.3-riscv64/* /path/to/your/mnt/root/
```

#### 启动并登录系统

将 SD 卡插入开发板并启动。
通过 `/dev/ttyUSB0` 上的串口登录系统 （baudrate 115200）。

用户名: `root`
密码: 无

##### 安装后设置
登录后分别使用 `passwd` 和 `hostname` 设置密码和主机名。

使用 `date -s` 设置系统时间，再安装 `cronyd`:

```bash
apk add cronyd
rc-update add chronyd default
```

建议同时启用如下的 OpenRC 服务（虽然测试中发现如跳过此步，系统仍然可以正常启动）：

```bash
rc-update add bootmisc boot
rc-update add networking boot # 需要先编辑好 /etc/network/interfaces
rc-update add devfs sysinit
rc-update add mdev sysinit
rc-update add acpid default
rc-update add killprocs shutdown
rc-update add mount-ro shutdown
rc-update add savecache shutdown
```

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

#### 方式一启动示例

```log
   OpenRC 0.51 is starting up Linux 5.10.4-tag- (riscv64)

 * Mounting /proc ... [ ok ]
 * Mounting /run ... [ ok ]
 * /run/openrc: creating directory
 * /run/lock: creating directory
 * /run/lock: correcting owner
[    1.744315] random: fast init done
Service `hwdrivers' needs non existent service `dev'
Service `machine-id' needs non existent service `dev'
 * Caching service dependencies ... [ ok ]
 * Clock skew detected with `/etc/init.d'
 * Adjusting mtime of `/run/openrc/deptree' to Wed Oct 25 12:24:45 2023

 * WARNING: clock skew detected!
 * WARNING: clock skew detected!
[    2.856766] cv180x_pwm: bad vermagic: kernel tainted.
[    2.862103] Disabling lock debugging due to kernel taint
[    2.867650] cv180x_pwm: loading out-of-tree module taints kernel.
 * Loading modules ...[    3.092709] res-reg: start: 0xa0c8000, end: 0xa0c801f, virt-addr(ffffffd0042a1000).
[    3.101162] CVITEK CHIP ID = 22
[    3.122044] cvi_rtos_cmdqu_probe start ---
[    3.126419] name=1900000.rtos_cmdqu
[    3.130321] res-reg: start: 0x1900000, end: 0x1900fff, virt-addr(ffffffd0042b6000).
[    3.138366] cvi_rtos_cmdqu_probe DONE
[    3.142435] [cvi_spinlock_init] success
[    3.366529] RTOS_CMDQU_SEND_WAIT timeout
[    3.370632] SYS_CMD_INFO_LINUX_INIT_DONE fail
[    3.375186] communicate with rtos fail
[    3.400375] cif a0c2000.cif: cam0 clk installed
[    3.405169] cif a0c2000.cif: cam1 clk installed
[    3.409918] cif a0c2000.cif: vip_sys_2 clk installed
[    3.415112] cif a0c2000.cif: clk_mipimpll clk installed (____ptrval____)
[    3.422097] cif a0c2000.cif: clk_disppll clk installed (____ptrval____)
[    3.428994] cif a0c2000.cif: clk_fpll clk installed (____ptrval____)
[    3.435621] cif a0c2000.cif: (0) res-reg: start: 0xa0c2000, end: 0xa0c3fff.
[    3.442851] cif a0c2000.cif:  virt-addr((____ptrval____))
[    3.448476] cif a0c2000.cif: (1) res-reg: start: 0xa0d0000, end: 0xa0d0fff.
[    3.455703] cif a0c2000.cif:  virt-addr((____ptrval____))
[    3.461328] cif a0c2000.cif: (2) res-reg: start: 0xa0c4000, end: 0xa0c5fff.
[    3.468555] cif a0c2000.cif:  virt-addr((____ptrval____))
[    3.474180] cif a0c2000.cif: (3) res-reg: start: 0x3001c30, end: 0x3001c5f.
[    3.481407] cif a0c2000.cif:  virt-addr((____ptrval____))
[    3.487019] cif a0c2000.cif: no pad_ctrl for cif
[    3.491905] cif a0c2000.cif: request irq-26 as cif-irq0
[    3.497417] cif a0c2000.cif: request irq-27 as cif-irq1
[    3.502913] cif a0c2000.cif: rst_pin = 424, pol = 1
[    3.523593] snsr_i2c snsr_i2c: i2c:-------hook 0
[    3.528631] snsr_i2c snsr_i2c: i2c:-------hook 1
[    3.533575] snsr_i2c snsr_i2c: i2c:-------hook 2
[    3.538538] snsr_i2c snsr_i2c: i2c:-------hook 3
[    3.543471] snsr_i2c snsr_i2c: i2c:-------hook 4
[    3.598874] vi_core_probe:203(): res-reg: start: 0xa000000, end: 0xa07ffff, virt-addr(ffffffd004480000).
[    3.608759] vi_core_probe:216(): irq(28) for isp get from platform driver.
[    3.616433] vi_tuning_buf_setup:253(): tuning fe_addr[0]=0x8169f490, be_addr[0]=0x81697290, post_addr[0]=0x81680000
[    3.627370] vi_tuning_buf_setup:253(): tuning fe_addr[1]=0x8165f490, be_addr[1]=0x81657290, post_addr[1]=0x81640000
[    3.638276] vi_tuning_buf_setup:253(): tuning fe_addr[2]=0x8167f490, be_addr[2]=0x81677290, post_addr[2]=0x81660000
[    3.649128] sync_task_init:177(): sync_task_init vi_pipe 0
[    3.654834] sync_task_init:177(): sync_task_init vi_pipe 1
[    3.660530] sync_task_init:177(): sync_task_init vi_pipe 2
[    3.666831] vi_core_probe:252(): isp registered as cvi-vi
[    3.738895] cvi_dwa_probe:487(): done with rc(0).
[    3.796083] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    3.802358] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    3.809710] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    3.817030] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    3.824451] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    3.887420] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.895048] end jpu_init result = 0x0
[    4.010054] cvi_vc_drv_init result = 0x0
 [ ok ]
 * Activating swap devices ...[    4.222544] Adding 65532k swap on /dev/mmcblk0p3.  Priority:-2 extents:1 across:65532k SSDsc
 [ ok ]
 * Checking local filesystems  ... [ ok ]
 * Remounting filesystems ...[    4.659028] EXT4-fs (mmcblk0p2): re-mounted. Opts: discard
 [ ok ]
 * Mounting local filesystems ... [ ok ]
 * Loading zram module...
[    5.196337] zram: Added device: zram0
 [ ok ]
 * Swap->zram0
[    5.307208] zram0: detected capacity change from 0 to 33554432
[    8.358561] Adding 32764k swap on /dev/zram0.  Priority:16383 extents:1 across:32764k SSDsc
 [ ok ]
 * WARNING: clock skew detected!
 * /run/dhcpcd: creating directory
 * Starting dhcpcd ... [ ok ]
[    9.042260] random: dhcpcd: uninitialized urandom read (40 bytes read)
 * Setting hostname ... [ ok ]
[    9.706759] bm-dwmac 4070000.ethernet eth0: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[    9.734618] dwmac1000: Master AXI performs any burst length
[    9.745607] bm-dwmac 4070000.ethernet eth0: No Safety Features support found
[    9.764674] bm-dwmac 4070000.ethernet eth0: IEEE 1588-2002 Timestamp supported
 * Starting networking ...[    9.781062] bm-dwmac 4070000.ethernet eth0: configuring for phy/rmii link mode
 *   lo ... [ ok ]
 *   eth0 ...sending commands to dhcpcd process
 [ ok ]
 * Starting chronyd ...[   15.700583] random: chronyd: uninitialized urandom read (3 bytes read)
[   15.707454] random: chronyd: uninitialized urandom read (1024 bytes read)
 [ ok ]
 * Starting dropbear ... [ ok ]
 * Configuring kernel parameters ...sysctl: error: 'net.ipv4.tcp_syncookies' is an unknown key
sysctl: error: 'kernel.unprivileged_bpf_disabled' is an unknown key
 [ ok ]
0 file(s)
2 in ep
1 out ep
[   16.486902] using random self ethernet address
[   16.491691] using random host ethernet address
1 file(s)
[   16.583275] usb0: HOST MAC 6e:c8:69:3c:9e:af
[   16.590810] usb0: MAC d6:80:67:ff:c9:b9
[   16.598575] dwc2 4340000.usb: bound driver configfs-gadget
[   17.431319] random: dnsmasq: uninitialized urandom read (128 bytes read)
[   17.438507] random: dnsmasq: uninitialized urandom read (48 bytes read)
 * Starting dnsmasq ...[   17.475029] random: dnsmasq: uninitialized urandom read (128 bytes read)
 [ ok ]

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

login[881]: root login on 'console'
milkv-duo:~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Tue Oct 24 10:20:29 UTC 2023 riscv64 Linux
milkv-duo:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.19_alpha20230901
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
milkv-duo:~# 
```

#### 方式二启动示例

```log
   OpenRC 0.54 is starting up Linux 5.10.4-tag- (riscv64)

 * Mounting /proc ... [ ok ]
 * Mounting /run ... [ ok ]
 * /run/openrc: creating directory
 * /run/lock: creating directory
 * /run/lock: correcting owner
[    1.660531] random: fast init done
 * Caching service dependencies ... [ ok ]
 * Caching service dependencies ... [ ok ]
 * Clock skew detected with `/etc/init.d'
 * Adjusting mtime of `/run/openrc/deptree' to Wed Nov  6 12:40:12 2024

 * WARNING: clock skew detected!
 * Remounting devtmpfs on /dev ... [ ok ]
 * Mounting /dev/mqueue ... [ ok ]
 * Mounting /dev/pts ... [ ok ]
 * Mounting /dev/shm ... [ ok ]
 * Mounting /sys ... [ ok ]
 * Mounting debug filesystem ... [ ok ]
 * Mounting config filesystem ... [ ok ]
 * Starting busybox mdev ... [ ok ]
 * Scanning hardware for mdev ... [ ok ]
 * WARNING: clock skew detected!
 * Checking local filesystems  ... [ ok ]
 * Remounting filesystems ... [ ok ]
 * Mounting local filesystems ... [ ok ]
 * Creating user login records ... [ ok ]
 * Cleaning /tmp directory ... [ ok ]
 * Setting hostname ... [ ok ]
 * Starting networking ...ifquery: could not parse /etc/network/interfaces
 * ERROR: networking failed to start
 * WARNING: clock skew detected!
 * Starting networking ...ifquery: could not parse /etc/network/interfaces
 * ERROR: networking failed to start
 * Starting busybox acpid ... [ ok ]

Welcome to Alpine Linux 3.20
Kernel 5.10.4-tag- on an riscv64 (/dev/ttyS0)

localhost login: root
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

login[734]: root login on 'ttyS0'
localhost:~# uname -a
Linux localhost 5.10.4-tag- #1 PREEMPT Mon Sep 30 18:01:49 CST 2024 riscv64 Linux
localhost:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.3
PRETTY_NAME="Alpine Linux v3.20"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
localhost:~# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
