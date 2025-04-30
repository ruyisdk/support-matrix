# Alpine Linux Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：3.21.3
- 下载链接：
  - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/riscv64/alpine-minirootfs-3.21.3-riscv64.tar.gz)
  - 官方 Buildroot 镜像: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip)
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

### 下载 Alpine minirootfs 和 Buildroot 镜像

```bash
wget https://dl-cdn.alpinelinux.org/alpine/v3.21/releases/riscv64/alpine-minirootfs-3.21.3-riscv64.tar.gz
tar -xvf alpine-minirootfs-3.21.3-riscv64.tar.gz --one-top-level
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip
unzip milkv-duo-sd-v1.1.4.img.zip
```

### 准备 rootfs
Alpine 官方提供的 riscv64 发行仅是一个 "minirootfs", 缺少 OpenRC 等必要的系统组件。要在实体硬件上启动，我们需要使用 `apk` 在该 minirootfs 中安装 Alpine 基础包。 

#### 安装 Alpine 包管理器 `apk`
如果宿主机已经在使用 Alpine 系发行版，则跳过此步

```bash
wget https://gitlab.alpinelinux.org/api/v4/projects/5/packages/generic/v2.14.10/x86_64/apk.static
chmod +x apk.static
mv apk.static /usr/bin/apk
```

#### 在 minirootfs 中安装 Alpine 基础包 `alpine-base`

(注：无需 `chroot`)

```bash
cd alpine-minirootfs-3.20.3-riscv64
sudo apk add -p . --initdb -U --arch riscv64 --allow-untrusted alpine-base
```

#### 额外设置

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

### 刷入 Buildroot 镜像

```bash
cd ..
sudo dd if=milkv-duo-sd-v1.1.3-2024-0930.img of=/dev/your/device bs=4M status=progress
```

你的设备应该能识别到 SD 卡上的 `rootfs` 和 `boot` 两个分区。挂载 `rootfs` 分区。

### 替换 SD 卡上根目录为 Alpine rootfs
```bash
rm -rf /path/to/your/mnt/root/*
cp -r /path/to/your/alpine-minirootfs-3.20.3-riscv64/* /path/to/your/mnt/root/
```

### 启动并登录系统

将 SD 卡插入开发板并启动。
通过 `/dev/ttyUSB0` 上的串口登录系统 （baudrate 115200）。

用户名: `root`
密码: 无

### 安装后设置
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

```log
   OpenRC 0.55.1 is starting up Linux 5.10.4-tag- (riscv64)

 * Mounting /proc ... [ ok ]
 * Mounting /run ... [ ok ]
 * /run/openrc: creating directory
 * /run/lock: creating directory
 * /run/lock: correcting owner
 * Caching service dependencies ... [ ok ]
 * Clock skew detected with `/etc/init.d'
 * Adjusting mtime of `/run/openrc/deptree' to Wed Apr 30 19:42:03 2025

 * WARNING: clock skew detected!
 * WARNING: clock skew detected!
 * WARNING: clock skew detected!

Welcome to Alpine Linux 3.21
Kernel 5.10.4-tag- on an riscv64 (/dev/ttyS0)

(none) login: root
Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

login[206]: root login on 'ttyS0'
(none):~# uname -a
Linux (none) 5.10.4-tag- #1 PREEMPT Fri Nov 22 11:31:04 CST 2024 riscv64 Linux
(none):~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.21.3
PRETTY_NAME="Alpine Linux v3.21"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
(none):~# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
