# OpenWrt Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/draftbottle/VizOS
- 参考安装文档：https://community.milkv.io/t/milk-v-duo-openwrt/2399

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤
### 环境配置

安装一些必要的包:

```shell
sudo apt update && sudo apt install -y ack antlr3 aria2 asciidoc autoconf automake autopoint binutils bison build-essential bzip2 ccache cmake cpio curl device-tree-compiler fastjar flex gawk gettext gcc-multilib g++-multilib git gperf haveged help2man intltool libc6-dev-i386 libelf-dev libglib2.0-dev libgmp3-dev libltdl-dev libmpc-dev libmpfr-dev libncurses5-dev libncursesw5-dev libreadline-dev libssl-dev libtool lrzsz mkisofs msmtp nano ninja-build p7zip p7zip-full patch pkgconf python3 python3-pip libpython3-dev qemu-utils rsync rename scons squashfs-tools subversion swig texinfo uglifyjs upx-ucl unzip vim wget xmlto xxd zlib1g-dev genimage libconfuse2 genext2fs
```

`genimage` 包在 Ubuntu 24 以后的版本中才有，如果你使用更早的版本，可以从[这里下载](http://archive.ubuntu.com/ubuntu/pool/universe/g/genimage/genimage_17-2_amd64.deb)后手动安装。

安装host tools:

```shell
wget https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz
tar -xzf host-tools.tar.gz
sudo mv host-tools /opt
```

### 下载和编译

```shell
# 拉取源码
git clone -b vizos --single-branch --depth=1 https://github.com/draftbottle/VizOS.git feeds-vizos
git clone https://github.com/draftbottle/istoreos.git --single-branch --depth=1

# 把feeds-vizos链接到openwrt
echo "src-link  vizos  ${PWD}/feeds-vizos" >> istoreos/feeds.conf.default
cd istoreos
cat feeds.conf.default

# 安装依赖
./scripts/feeds update  -a
./scripts/feeds install -a
./scripts/feeds install -f sophgo
./scripts/feeds install -f uboot-sophgo

# 开始编译
cp ../feeds-vizos/configs/cv180x-config .config
make -j$(nproc) || make package/feeds/vizos/uboot-sophgo/compile V=s
make -j$(nproc) V=s
```

如果成功编译，你可以在在 `istoreos/bin/targets/sophgo/cv180x/` 目录中找到 `milkv-duo.img` 镜像

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
cp ./istoreos/bin/targets/sophgo/cv180x/milkv-duo.img ./
dd if=milkv-duo.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
BusyBox v1.36.1 (2024-09-01 11:40:10 UTC) built-in shell (ash)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Powered by OpenWRT                                                                                                                                         -------------------------------------------------------                                                                                                                                     iStoreOS 23.05-SNAPSHOT, r0-5737568                                                                                                                                                         -------------------------------------------------------                                                                                                                                     执行. ./root/network-init.sh一键网络配置(非必须)                                                                                                                                                       -------------------------------------------------------                                                                                                                                    root@iStoreOS:/# uname -a                                                                                                                                                                   Linux iStoreOS 5.10.4 #0 Sun Sep 1 11:40:10 2024 riscv64 GNU/Linux                                                                                                                          root@iStoreOS:/# cat /proc/cpuinfo                                                                                                                                                          processor       : 0                                                                                                                                                                         hart            : 0                                                                                                                                                                         isa             : rv64imafdvcsu                                                                                                                                                             mmu             : sv39
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/lclF60XCCBMahHCGwIJVxJ6vh.svg)](https://asciinema.org/a/lclF60XCCBMahHCGwIJVxJ6vh)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。