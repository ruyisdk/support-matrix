# Arch Linux LPi4A 测试报告

## 测试环境

### 系统信息

- 下载链接：https://mirror.iscas.ac.cn/archriscv/images/
- u-boot 与 boot 下载（采用 revyos 的）：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 创建 rootfs

由于 Arch Linux 提供的并非打包好的镜像，而是 rootfs，我们需要自行打包镜像。

- 创建块设备，并创建文件系统
```bash
sudo dd if=/dev/zero of=rootfs.ext4 bs=1M count=6144 # 创建 6GB rootfs
sudo mkfs.ext4 rootfs.ext4
mkdir mnt
sudo mount ./rootfs.ext4 ./mnt
```

- 将 rootfs 解压到根目录中
```bash
sudo tar -I zstd -xvf archriscv-2024-09-22.tar.zst -C mnt/
```

- 获取该 fs 的 UUID
```bash
lsblk -o NAME,UUID
```

- 到 rootfs 中进行必要的更新，包安装与调整
```bash
sudo systemd-nspawn -D ./mnt --machine=archriscv

# 接下来是在 rootfs 中进行的
pacman -Syu
# 在此处安装你需要的包，如 vim 等。
echo "UUID=<UUID> /  ext4  defaults  1  1 " >> /etc/fstab # 此处的 <UUID> 是之前获得的
passwd # 请设置你的 root 密码！
exit
```

- umount rootfs
```bash
sudo umount ./mnt
```

### 刷写 bootloader

解压安装套件。
刷入 u-boot 与 boot。

*根据你的硬件版本选择是否需要 8g u-boot*

```bash
zstd -d boot-lpi4a-20250110_151339.ext4.zst 
sudo fastboot flash ram u-boot-with-spl-lpi4a-16g-main.bin 
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot flash boot boot-lpi4a-20250110_151339.ext4
```

### 刷写镜像

将 root 分区刷入 eMMC 中。

```bash
sudo fastboot flash root rootfs.ext4
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码：此处为你之前自行设置的密码或使用默认密码 `archriscv`。

### 安装图形环境

以 xfce 为例:

```
pacman -S xorg xfce4 ligthdm lightdm-gtk-greeter
systemctl enable --now ligthdm
```


## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

![xfce](./xfce.png)

屏幕录像（从创建 rootfs 到登录系统）：

[![asciicast](https://asciinema.org/a/7Ywwvlg1kdyAyTa9hiUOnv4yN.svg)](https://asciinema.org/a/7Ywwvlg1kdyAyTa9hiUOnv4yN)

```log
Arch Linux 6.6.66-th1520 (ttyS0)

archlinux login: root
Password: 
Last login: Thu Jan  9 03:54:09 on ttyS0
[root@archlinux ~]# uname -a
Linux archlinux 6.6.66-th1520 #2025.01.10.02.53+1c6721ec2 SMP Fri Jan 10 03:09:24 UTC 2025 riscv64 GNU/Linux
[root@archlinux ~]# cat /etc/os-release 
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo
[root@archlinux ~]# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
[root@archlinux ~]# fastfetch 
                  -`                     root@archlinux
                 .o+`                    --------------
                `ooo/                    OS: Arch Linux riscv64
               `+oooo:                   Host: Sipeed Lichee Pi 4A 16G
              `+oooooo:                  Kernel: Linux 6.6.66-th1520
              -+oooooo+:                 Uptime: 12 mins
            `/:-:++oooo+:                Packages: 131 (pacman)
           `/++++/+++++++:               Shell: bash 5.2.37
          `/++++++++++++++:              Terminal: vt220
         `/+++ooooooooooooo/`            CPU: thead,c910 rv64gc (4) @ 1.85 GHz
        ./ooosssso++osssssso+`           Memory: 232.95 MiB / 15.44 GiB (1%)
       .oossssso-````/ossssss+`          Swap: 0 B / 4.00 GiB (0%)
      -osssssso.      :ssssssso.         Disk (/): 999.02 MiB / 5.82 GiB (17%) - ext4
     :osssssss/        osssso+++.        Locale: C.UTF-8
    /ossssssss/        +ssssooo/-
  `/ossssso+/:-        -:/+osssso+-                              
 `+sso+:-`                 `.-/+oso:                             
`++:.                           `-/+/
.`                                 `/
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
