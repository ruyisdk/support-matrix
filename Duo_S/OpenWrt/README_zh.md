# OpenWrt Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenWrt(iStoreOS) 23.05
- 下载链接：https://github.com/draftbottle/Milkv-duo-openwrt/releases/download/v4.0/milkv-duos.img
- 参考安装文档：
  - https://community.milkv.io/t/milk-v-duo-openwrt/2399/10
  - https://github.com/draftbottle/VizOS

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个
    - 仅推荐使用 CP210x 系列如 CP2102/CP2104，注意不可使用 CH340/341 系列，会输出乱码；FT232/CH343P 等其他串口调试器在启动至 U-Boot 之前也会出现乱码，启动后可正常使用，这是预期结果，如果持续只能得到乱码输出请尝试更换使用 CP210x 系列芯片的调试器
- 杜邦线三根

## 安装步骤

### 使用 Docker 构建镜像

配置 Docker 环境：
```bash
docker pull ubuntu:24.04
sudo docker run -itd --name openwrt -v $(pwd):/home/openwrt ubuntu:24.04 /bin/bash
```

在 Docker 中执行以下命令：
```bash
cd openwrt

sudo apt install ack antlr3 aria2 asciidoc autoconf automake autopoint binutils bison build-essential bzip2 ccache cmake cpio curl device-tree-compiler fastjar flex gawk gettext gcc-multilib g++-multilib git gperf haveged help2man intltool libc6-dev-i386 libelf-dev libglib2.0-dev libgmp3-dev libltdl-dev libmpc-dev libmpfr-dev libncurses5-dev libncursesw5-dev libreadline-dev libssl-dev libtool lrzsz mkisofs msmtp nano ninja-build p7zip p7zip-full patch pkgconf python3 python3-pip libpython3-dev qemu-utils rsync rename scons squashfs-tools subversion swig texinfo uglifyjs upx-ucl unzip vim wget xmlto xxd zlib1g-dev libconfuse2 genext2fs

wget https://mirrors.united.cd/ubuntu/pool/universe/g/genimage/genimage_16-2_amd64.deb
sudo dpkg -i genimage_16-2_amd64.deb
rm genimage_16-2_amd64.deb

echo 'export FORCE_UNSAFE_CONFIGURE=1' >> ~/.bashrc
source ~/.bashrc

git clone https://github.com/draftbottle/istoreos.git --single-branch
cd istoreos && ./build.sh
```

构建完成的镜像在 `~/openwrt/istoreos/bin/targets/sophgo/` 目录中。

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
sudo dd if=milkv-duo.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```bash
[   11.248443] dwmac1000: Master AXI performs any burst length
[   11.254253] bm-dwmac 4070000.ethernet eth0: No Safety Features support found
[   11.261585] bm-dwmac 4070000.ethernet eth0: IEEE 1588-2002 Timestamp supported
[   11.269076] bm-dwmac 4070000.ethernet eth0: configuring for phy/rmii link mode
[   11.358823] br-lan: port 1(eth0) entered blocking state
[   11.364231] br-lan: port 1(eth0) entered disabled state
[   11.369935] device eth0 entered promiscuous mode



BusyBox v1.36.1 (2024-09-01 11:40:10 UTC) built-in shell (ash)


   ▀     ▄▄▄▄    ▄                          ▄▄▄▄   ▄▄▄▄
 ▄▄▄    █▀   ▀ ▄▄█▄▄   ▄▄▄    ▄ ▄▄   ▄▄▄   ▄▀  ▀▄ █▀   ▀
   █    ▀█▄▄▄    █    █▀ ▀█   █▀  ▀ █▀  █  █    █ ▀█▄▄▄
   █        ▀█   █    █   █   █     █▀▀▀▀  █    █     ▀█
 ▄▄█▄▄  ▀▄▄▄█▀   ▀▄▄  ▀█▄█▀   █     ▀█▄▄▀   █▄▄█  ▀▄▄▄█▀

                                  Powered by OpenWRT
 -------------------------------------------------------
 iStoreOS 23.05-SNAPSHOT, r23457-57375689ae
 -------------------------------------------------------
 执行. ./root/network-init.sh一键网络配置(非必须)
 -------------------------------------------------------
root@iStoreOS:/# uname -a
Linux iStoreOS 5.10.4 #0 Sun Sep 1 11:40:10 2024 riscv64 GNU/Linux
```

屏幕录像：

[![asciicast](https://asciinema.org/a/xbuOGmH4NF3lM1qaHKFjxcxEV.svg)](https://asciinema.org/a/xbuOGmH4NF3lM1qaHKFjxcxEV)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
