---
sys: archlinux
sys_ver: null
sys_var: null

status: basic
last_update: 2025-08-31
---

# Arch Linux Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: archriscv-2025-06-12

You need to build this image on your own.

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo S
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Build Steps

### Build Buildroot

See [milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk).

After the first build of target `milkv-duos-sd` is completed, modify `build/boards/cv181x/cv1813h_milkv_duos_sd/linux/cvitek_cv1813h_milkv_duos_sd_defconfig` and add the following lines.

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

Then start build again and get image `out/milkv-duos-sd-<your-build-timex>.img`.

### Update rootfs

Consider use root to avoid permission issues.

#### Download rootfs

Get rootfs from [Arch Linux RISC-V](https://archriscv.felixc.at/).

```
wget https://archriscv.felixc.at/images/archriscv-2025-06-12.tar.zst
```

#### Modify rootfs

```
sudo losetup -f
```

Output is `/dev/loop0`.

Mount the image on the loop device.

```
losetup -P loop0 out/milkv-duos-sd_2025-0831-0547.img
```

Mount disk to `/mnt/duo-rootfs`.

```
mkdir /mnt/duo-rootfs
cd /mnt/duo-rootfs
mount /dev/loop0p3 /mnt/duo-rootfs
```

Remove everything.

```
rm -rf ./*
```

Unzip new rootfs.

```
tar -xvf archriscv-2025-06-12.tar.zst -C .
```

#### Download Package for Network.

To use the network, download some packages to the directory for installation.

```
cd /mnt/duo-rootfs/root
wget https://mirror.iscas.ac.cn/archriscv/repo/core/nano-8.2-1-riscv64.pkg.tar.zst
wget https://mirror.iscas.ac.cn/archriscv/repo/extra/dhcpcd-10.0.10-1-riscv64.pkg.tar.zst
```

### Unmount Image

```
umount /dev/loop0p3
losetup -d /dev/loop0
```

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card

```shell
dd if=milkv-duos-sd_2025-0831-0547.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Password: `archriscv`

#### Configure the network

Install these downloaded package.

```
pacman -U ./dhcpcd-10.0.10-1-riscv64.pkg.tar.zst
pacman -U ./nano-8.2-1-riscv64.pkg.tar.zst
```

Then start dhcp service.

```
ip link set end0 up
systemctl start dhcpcd.service
systemctl enable dhcpcd.service
```

If static network needs configuring, use following commands.

```
ip link set end0 up
ip addr add 172.16.0.188/12 broadcast 172.31.255.255 dev end0 #172.16.0.188/12 is your local IP，172.31.255.255 is broadcast IP.
ip route add default via 172.16.0.1 # default gateway
echo -e "nameserver 172.16.0.1" >> /etc/resolv.conf # DNS server
```

A reboot might be needed.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Information

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

Screen recording:

[![asciicast](https://asciinema.org/a/mMXIs8084TXdx8zVAg2scpPWe.svg)](https://asciinema.org/a/mMXIs8084TXdx8zVAg2scpPWe)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
