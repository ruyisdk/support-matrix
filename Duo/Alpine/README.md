---
sys: alpine
sys_ver: null
sys_var: null

status: basic
last_update: 2024-11-12
---

# Alpine Linux Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: 3.19_alpha20230901 / 3.20.3 riscv64
- Download Link: 
  - https://github.com/cwt/duo-buildroot-sdk/releases/download/poc1/MilkV-Duo-alpine.img.xz
  > Note: This image is provided by community developers and is not an official image.

  (Alternatively):
  - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
  - Official Buildroot image: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip)
- Reference Installation Document: 
  - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
  - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
  - [Milk-V forum thread](https://community.milkv.io/t/alpine-linux-on-the-duo/700/18)

### Hardware Information

- Milk-V Duo
- A USB-A to C or USB-C to C cable
- A microSD card
- A microSD card reader
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Method A: Flash community image

Download the prebuilt community image: https://github.com/cwt/duo-buildroot-sdk/releases/download/poc1/MilkV-Duo-alpine.img.xz
Then flash it with
```shell
xz -d MilkV-Duo-alpine.img.xz
sudo dd if=MilkV-Duo-alpine.img of=/dev/your/device bs=1M status=progress
```

### Method B: Build and flash your own rootfs

Alternatively, you can also build your own image by replacing relevant content in existing images for the Duo with Alpine's official rootfs.

#### Download Alpine minirootfs and Buildroot image

```bash
wget https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz
tar -xvf alpine-minirootfs-3.20.3-riscv64.tar.gz --one-top-level
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip
unzip milkv-duo-sd-v1.1.3-2024-0930.img.zip
```

#### Prepare rootfs
Note that the obtained Alpine system is only a "minirootfs" without system packages such as OpenRC. We need to install Alpine's base packages using `apk` inside the rootfs in order to make it bootable.

##### Install Alpine's package manager `apk`
Skip this step if using Alpine-based distributions on host. Otherwise install `apk-tools` on your distribution (e.g. on Arch Linux: `sudo pacman -S apk-tools`).

run `apk --help` to verify installation.

##### Install Alpine's base package `alpine-base` inside minirootfs

(`chroot` is NOT required)

```bash
cd alpine-minirootfs-3.20.3-riscv64
sudo apk add -p . --initdb -U --arch riscv64 --allow-untrusted alpine-base
```

##### Extra setups

1. Edit `./etc/inittab` and add the following line (or uncomment) to enable serial access on `/dev/ttyS0`:
    ```
    ttyS0::respawn:/sbin/getty -L 115200 ttyS0 vt100
    ```
    And comment out the six lines starting with `tty1` - `tty6`.

2. Edit `./etc/passwd`:

    Remove the `x` in `root:x:0:0:root:/root:/bin/sh`.

    (Alternatively, edit `/etc/shadow` and remove the `*` in `root:*::0:::::`). 

3. Enable the OpenRC hostname service (for setting up the hostname correctly)：
   
   ```bash
   ln -s ./etc/init.d/hostname ./etc/runlevels/boot
   ```
   You may enable other OpenRC system services of interest likewise.

#### Flash Buildroot image

```bash
cd ..
sudo dd if=milkv-duo-sd-v1.1.3-2024-0930.img of=/dev/your/device bs=4M status=progress
```

Your device should now be able to detect the `rootfs` and `boot` partitions on the SD card. Mount only the `rootfs` partition.

#### Replace root on SD card with Alpine rootfs
```bash
rm -rf /path/to/your/mnt/root/*
cp -r /path/to/your/alpine-minirootfs-3.20.3-riscv64/* /path/to/your/mnt/root/
```

#### Booting and Logging into the System

Insert SD card onto the board and boot.
Login into the system via serial port at `/dev/ttyUSB0`, baudrate 115200.

Default username: `root`
Default password: none

##### Optional post-installation setups
Setup the password and hostname with `passwd` and `hostname` after login. 

Setup the system time with `date -s`, then install `cronyd`:
```bash
apk add cronyd
rc-update add chronyd default
```

It is recommended to enable the following system OpenRC services (though test results show that the system will still be able to boot nevertheless):

```bash
rc-update add bootmisc boot
rc-update add networking boot # make sure /etc/network/interfaces is present
rc-update add devfs sysinit
rc-update add mdev sysinit
rc-update add acpid default
rc-update add killprocs shutdown
rc-update add mount-ro shutdown
rc-update add savecache shutdown
```

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully, and login through the onboard serial port was also successful.

### Boot Log

#### Method A example

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

#### Method B example

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
