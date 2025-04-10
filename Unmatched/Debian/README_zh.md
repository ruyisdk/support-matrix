# Debian trixie/sid HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian trixie/sid
- 下载链接：https://github.com/yuzibo/Unmatched-Debian-image/releases/tag/0.0.5-beta
- 参考安装文档
    - https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched
    - https://github.com/yuzibo/Unmatched-Debian-image

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张
- M.2 NVMe SSD 一个
    - M.2 转 USB 硬盘盒，用于镜像刷写

## 安装步骤

根据 [软件参考手册](https://www.sifive.cn/document-file/hifive-unmatched-software-reference-manual)，HiFive Unmatched 有多种启动方式。

针对此 Debian 镜像，我们有两种方式：
- 使用 GitHub release 页提供的 U-Boot 镜像，刷写至 microSD 卡，DIP 开关设置为 `MSEL[3:0]=1011`（出厂默认）
- 手动编译主线 U-Boot，刷写至 SPI Flash，并将 DIP 开关设置为 `MSEL[3:0]=0110`
    - 需要开发板上有可以运行并能够刷写 SPI Flash 的系统
    - 请参考此处的 U-Boot 文档：https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### U-Boot 烧录至 microSD 卡

`/dev/sdc` 为 microSD 卡所在位置，`/dev/sdY` 为 M.2 NVMe SSD，请根据实际情况更改。

```bash
wget https://github.com/yuzibo/Unmatched-Debian-image/releases/download/0.0.5-beta/sd-uboot.img.xz \
     https://github.com/yuzibo/Unmatched-Debian-image/releases/download/0.0.5-beta/nvme-rootfs.img.xz
xz -dkv sd-uboot.img.xz
xz -dkv nvme-rootfs.img.xz
sudo dd if=sd-uboot.img of=/dev/sdX bs=1M status=progress
sudo dd if=nvme-rootfs.img of=/dev/sdY bs=1M status=progress
sync
sudo eject /dev/sdX; sudo eject /dev/sdY
```

现在可将 microSD 卡和 NVMe SSD 都安装到开发板上。

确保 DIP 开关设置正确：`MSEL[3:0]=1011`

### U-Boot 烧录至 SPI Flash

需要在 Unmatched 上已经有能运行的操作系统。

您将需要手动编译 U-Boot。

#### 编译 U-Boot

下方仅为粗略步骤：您将需要安装所需软件包，并配置工具链（交叉编译或原生编译均可）。

完整文档请见 U-Boot 官网：https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

```shell
git clone https://github.com/riscv/opensbi.git
pushd opensbi
make PLATFORM=generic -j$(nproc)
popd
wget https://github.com/u-boot/u-boot/archive/refs/tags/v2025.04.tar.gz
tar xvf v2025.04.tar.gz
cd u-boot-2025.04
export OPENSBI=../opensbi/build/platform/generic/firmware/fw_dynamic.bin
make sifive_unmatched_defconfig
make -j$(nproc)
```

#### 烧录镜像

以下步骤参考 U-Boot 文档。

```shell
sgdisk --clear -a 1 \
    --new=1:40:2087     --change-name=1:spl   --typecode=1:5B193300-FC78-40CD-8002-E86C45580B47 \
    --new=2:2088:10279  --change-name=2:uboot --typecode=2:2E54B353-1271-4842-806F-E436D6AF6985 \
    --new=3:10280:10535 --change-name=3:env   --typecode=3:3DE21764-95BD-54BD-A5C3-4ABE786F38A8 \
    /dev/mtdblock0
dd if=spl/u-boot-spl.bin of=/dev/mtdblock0 bs=4096 seek=5 conv=sync
dd if=u-boot.itb  of=/dev/mtdblock0 bs=4096 seek=261 conv=sync
```

在另一台计算机上刷写 Debian 镜像到 NVMe SSD：

```shell
wget https://github.com/yuzibo/Unmatched-Debian-image/releases/download/0.0.5-beta/nvme-rootfs.img.xz
xz -dkv nvme-rootfs.img.xz
sudo dd if=nvme-rootfs.img of=/dev/sdY bs=1M status=progress
sync
sudo eject /dev/sdX; sudo eject /dev/sdY
```

现在可以关闭开发板电源，安装烧录好 Debian 镜像的 SSD，并将拨码开关设置为 `MSEL[3:0]=0110`，然后启动开发板。

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`rv`
默认密码：`rv`

#### 调整分区大小

root 分区默认没有自动扩容，参考如下步骤手动扩容：

```log
rv@unmatched:~$ sudo fdisk /dev/nvme0n1

Welcome to fdisk (util-linux 2.40.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

GPT PMBR size mismatch (6291455 != 250069679) will be corrected by write.
This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.


Command (m for help): e
Partition number (1-4, default 4): 4

New <size>{K,M,G,T,P} in bytes or <size>S in sectors (default 118.8G): <Enter>

Partition 4 has been resized.

Command (m for help): w
The partition table has been altered.
Syncing disks.

rv@unmatched:~$ sudo resize2fs /dev/nvme0n1p4
[  178.683726] EXT4-fs (nvme0n1p4): resizing filesystem from 681979 to 31154257 blocks
resize2fs 1.47.2 (1-Jan-2025)
Filesystem at /dev/nvme0n1p4 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 15
[  179.016304] EXT4-fs (nvme0n1p4): resized filesystem to 31154257
The filesystem on /dev/nvme0n1p4 is now 31154257 (4k) blocks long.

rv@unmatched:~$ df -hT
Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  7.8G     0  7.8G   0% /dev
tmpfs          tmpfs     1.6G  376K  1.6G   1% /run
/dev/nvme0n1p4 ext4      117G  541M  112G   1% /
tmpfs          tmpfs     7.9G     0  7.9G   0% /dev/shm
tmpfs          tmpfs     5.0M     0  5.0M   0% /run/lock
tmpfs          tmpfs     7.9G     0  7.9G   0% /tmp
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
/dev/nvme0n1p3 ext4      358M   69M  266M  21% /boot
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/getty@tty1.service
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/serial-getty@ttySIF0.service
tmpfs          tmpfs     1.6G  4.0K  1.6G   1% /run/user/1000
rv@unmatched:~$ 
```

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid unmatched ttySIF0

unmatched login: rv
Password:
Linux unmatched 6.12.17-riscv64 #1 SMP Debian 6.12.17-1 (2025-03-01) riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
rv@unmatched:~$ fastfetch
        _,met$$$$$gg.          rv@unmatched
     ,g$$$$$$$$$$$$$$$P.       ------------
   ,g$$P""       """Y$$.".     OS: Debian GNU/Linux trixie/sid riscv64
  ,$$P'              `$$$.     Host: SiFive HiFive Unmatched A00
',$$P       ,ggs.     `$$b:    Kernel: Linux 6.12.17-riscv64
`d$$'     ,$P"'   .    $$$     Uptime: 50 seconds
 $$P      d$'     ,    $$P     Packages: 186 (dpkg)
 $$:      $$.   -    ,d$$'     Shell: bash 5.2.37
 $$;      Y$b._   _,d$P'       Terminal: vt220
 Y$$.    `.`"Y$$$$P"'          CPU: fu740-c000 (4)
 `$$b      "-.__               Memory: 294.54 MiB / 15.60 GiB (2%)
  `Y$$b                        Swap: Disabled
   `Y$$.                       Disk (/): 545.80 MiB / 2.49 GiB (21%) - ext4
     `$$b.                     Local IP (end0): 10.0.0.117/24
       `Y$$b.                  Locale: C
         `"Y$b._
             `""""

rv@unmatched:~$ uname -a
Linux unmatched 6.12.17-riscv64 #1 SMP Debian 6.12.17-1 (2025-03-01) riscv64 GNU/Linux
rv@unmatched:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

rv@unmatched:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
rv@unmatched:~$ cat /etc/deb
debconf.conf    debian_version
rv@unmatched:~$ cat /etc/debian_version
trixie/sid
```

屏幕录像：

U-Boot 烧录至 SPI Flash：

[![asciicast](https://asciinema.org/a/xmS1RmYMMmQXyhUF0a0xnVK2I.svg)](https://asciinema.org/a/xmS1RmYMMmQXyhUF0a0xnVK2I)

U-Boot 烧录至 microSD：

[![asciicast](https://asciinema.org/a/348eO3lu9rQqsZyMyZvFzAA4U.svg)](https://asciinema.org/a/348eO3lu9rQqsZyMyZvFzAA4U)

> [!NOTE]
> 尽管本测试报告仅测试了 CLI 且标记为 `basic` 支持，但这仅仅是因为我们没有安装独立显卡。
> 如果您安装了一块系统支持的显卡（例如 AMD 显卡），显示输出很有可能正常工作。
> 当然，需要您安装好桌面和 GPU 相关的软件包。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。