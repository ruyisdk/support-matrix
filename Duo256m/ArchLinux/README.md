---
sys: archlinux
sys_ver: null
sys_var: null

status: basic
last_update: 2024-10-09
---

# Arch Linux Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System Version: archriscv-2024-09-22

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

Get rootfs from [Arch Linux RISC-V](https://archriscv.felixc.at/).

```
wget https://archriscv.felixc.at/images/archriscv-2024-09-22.tar.zst
```

#### Modify rootfs

```
sudo losetup -f
```

Output is `/dev/loop0`.

Mount the image on the loop device.

```
losetup -P loop0 out/out/milkv-duo256m-sd-20240924-2106.img
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
tar -xvf archriscv-2024-09-22.tar.zst -C .
```

#### Download Package for Network

To use the network, download some packages to the directory for installation.

```
cd /mnt/duo-rootfs/root
wget https://mirror.iscas.ac.cn/archriscv/repo/core/nano-8.2-1-riscv64.pkg.tar.zst
wget https://mirror.iscas.ac.cn/archriscv/repo/extra/dhcpcd-10.0.10-1-riscv64.pkg.tar.zst
```

### Unmount Image

```
umount /dev/loop0p2
losetup -d /dev/loop0
```

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card 

```shell
dd if=milkv-duo256m-sd-20240924-2106.img of=/dev/sdc bs=1M status=progress
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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
