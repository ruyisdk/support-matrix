---
sys: openeuler
sys_ver: "23.09"
sys_var: null

status: basic
last_update: 2024-10-29
---

# openEuler Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System Version: openEuler-23.09-V1

You need to build this image on your own.

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 256M
- A USB-A to C or USB C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Build Steps

### Build Buildroot

See [milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk).

After the first build of target `milkv_duo256m_sd` is completed, modify `build/boards/cv181x/cv1812cp_milkv_duo256m_sd/linux/cvitek_cv1812cp_milkv_duo256m_sd_defconfig` and add the following lines.

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

Then start build again and get image `out/milkv-duo256m-sd-20240924-2106.img`.

### Update rootfs

Consider use root to avoid permission issues.

#### Download rootfs

Get rootfs from [ISCAS Mirror](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/).

```
wget https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/openeuler-rootfs.tar.gz
```

#### Modify rootfs

```
sudo losetup -f
```

Output is `/dev/loop0`.

Add extra space to your image.

```
qemu-img resize out/milkv-duo256m-sd-20240924-2106.img +10G
```

Mount the image on the loop device.

```
losetup -P loop0 out/milkv-duo256m-sd-20240924-2106.img
```

Expand your image.

```
sudo fdisk /dev/loop0

# 以下在 fdisk 中
d
2
n
p
2
# keep default for start sector.
# keep default for end sector.
w

# 以下应回到bash
sudo mkfs.ext4 /dev/loop0p2
```

Mount disk to `/mnt/duo-rootfs`.

```
mkdir /mnt/duo-rootfs
cd /mnt/duo-rootfs
mount /dev/loop0p2 /mnt/duo-rootfs
```

Remove everything.

```
rm -rf ./*
```

Unzip new rootfs.

```
tar -xvf openeuler-rootfs.tar.gz -C .
```

### Unmount Image

```
umount /dev/loop0p2
losetup -d /dev/loop0
```

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card 

```shell
dd if=milkv-duo256m-sd-20240924-2106.img of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Password: `openEuler12#$`

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

```
openEuler 23.09
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
Password: 


Welcome to 5.10.4-tag-

System information as of time:  Mon Sep 18 08:01:13 CST 2023

System load:    3.04
Processes:      70
Memory used:    43.4%
Swap used:      0.0%
Usage On:       19%
Users online:   1

[root@openeuler-riscv64 ~]# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
