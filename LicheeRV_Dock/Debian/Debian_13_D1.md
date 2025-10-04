# Debian 13 D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian 13 Trixie
- 来源：`sudo debootstrap --arch=riscv64 trixie rootfs http://deb.debian.org/debian`

### 硬件信息

- Sipeed Lichee RV Dock
- 电源适配器
- MicroSD 卡
- CH340

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 预期结果

正常刷写与启动。

## 实际结果

正常刷写与启动。

## 测试结论

正常启动。

## 实现步骤

### OpenSBI

```
git clone https://github.com/riscv-software-src/opensbi.git

make CROSS_COMPILE=riscv64-linux-gnu- PLATFORM=generic FW_PIC=y -j$(nproc)
```


### U-Boot

```
git clone https://github.com/smaeul/u-boot.git -b d1-wip

make lichee_rv_dock_defconfig

make CROSS_COMPILE=riscv64-linux-gnu- OPENSBI=../opensbi/build/platform/generic/firmware/fw_dynamic.bin -j$(nproc)
```

### Linux Kernel

```
git clone https://github.com/smaeul/linux.git -b d1/all

从这里搞一个 rv dock 的 config 文件：https://github.com/jamesgraves/licheerv-debian-linux/blob/main/licheerv_linux_defconfig

make ARCH=riscv licheerv_linux_defconfig

make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu- KCFLAGS='-fno-asynchronous-unwind-tables -fno-unwind-tables' -j$(nproc)

```

### extlinux.conf

```
Label Debian
	LINUX /Image
	APPEND root=/dev/mmcblk0p2 rw rootwait console=ttyS0,115200 earlycon=sbi
```

### rootfs

```
mkdir rootfs

sudo debootstrap --arch=riscv64 trixie rootfs http://deb.debian.org/debian
```

然后 chroot 进去设置个密码 装点需要的东西 之类的

### rootfs 镜像

```
dd if=/dev/zero of=rootfs.img bs=1G count=1

sudo mkfs.ext4 rootfs.img

mkdir rootfs_mount

sudo mount rootfs.img rootfs_mount

sudo cp -rfp rootfs/* rootfs_mount

sudo umount rootfs_mount

rm -r rootfs_mount

sudo e2fsck -f rootfs.img

sudo resize2fs -M rootfs.img
```

### 烧录

```
sudo sgdisk /dev/sdb -o 

sudo sgdisk /dev/sdb --new=1:4096:69631 --change-name=1:boot 

sudo sgdisk /dev/sdb --new=2:69632: --change-name=2:rootfs 

-p

sudo mkfs.vfat /dev/sdb1

sudo dd if=./u-boot/u-boot-sunxi-with-spl.bin of=/dev/sdb seek=256

sync

sudo mount /dev/sdb1 /mnt

sudo mkdir /mnt/extlinux

sudo cp ./linux/arch/riscv/boot/Image /mnt/

sudo cp ./extlinux.conf /mnt/extlinux/

sync

sudo umount /mnt

sudo dd if=./rootfs.img of=/dev/sdb2 bs=4096

sync
```

## 基本信息

### 以下是收集的 log

```
root@wdhyb-ThinkPad-X1-Carbon-3rd:~# uname -a
Linux wdhyb-ThinkPad-X1-Carbon-3rd 6.1.0-rc3-443875-gb466df90d48f #1 PREEMPT Sat Oct  4 20:28:29 CST 2025 riscv64 GNU/Linux
root@wdhyb-ThinkPad-X1-Carbon-3rd:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.1
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@wdhyb-ThinkPad-X1-Carbon-3rd:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
```


