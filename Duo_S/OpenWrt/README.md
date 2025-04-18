---
sys: openwrt
sys_ver: "23.05"
sys_var: null

status: basic
last_update: 2025-03-24
---

# OpenWrt Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: OpenWrt(iStoreOS) 23.05
- Download Link: https://github.com/draftbottle/Milkv-duo-openwrt/releases/download/v4.0/milkv-duos.img
- Reference Installation Document:
  - https://community.milkv.io/t/milk-v-duo-openwrt/2399/10
  - https://github.com/draftbottle/VizOS

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB power adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger
    - Only CP210x series is recommeneded (e.g. CP2102/CP2104). Be aware you'll only get garbled text output on WCH CH340/341 series; you can still use other USB-UART chips like FT232 and CH343 series, although you might still get garbled output but only before U-Boot loads, this is expected. If UART isn't working at all please consider try another USB-UART adaptor.
- Three DuPont wires

## Installation Steps

### Build in Docker

Setup the environment:
```bash
docker pull ubuntu:24.04
sudo docker run -itd --name openwrt -v $(pwd):/home/openwrt ubuntu:24.04 /bin/bash
```

Inside docker:
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

The built image can be found in `~/openwrt/istoreos/bin/targets/sophgo/`

### Using `dd` to Flash the Image to the microSD Card

```bash
sudo dd if=milkv-duo.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Information

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
Screen recording:

[![asciicast](https://asciinema.org/a/xbuOGmH4NF3lM1qaHKFjxcxEV.svg)](https://asciinema.org/a/xbuOGmH4NF3lM1qaHKFjxcxEV)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
