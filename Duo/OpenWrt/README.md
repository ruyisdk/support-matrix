---
sys: openwrt
sys_ver: 23.05
sys_var: null

status: basic
last_update: 2025-03-31
---

# OpenWrt Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/draftbottle/VizOS
- Reference Installation Document: https://community.milkv.io/t/milk-v-duo-openwrt/2399

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires
- Milk-V Duo with necessary header pins pre-soldered for debugging
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Environment Setup

Install some necessary packages:

```shell
sudo apt update && sudo apt install -y ack antlr3 aria2 asciidoc autoconf automake autopoint binutils bison build-essential bzip2 ccache cmake cpio curl device-tree-compiler fastjar flex gawk gettext gcc-multilib g++-multilib git gperf haveged help2man intltool libc6-dev-i386 libelf-dev libglib2.0-dev libgmp3-dev libltdl-dev libmpc-dev libmpfr-dev libncurses5-dev libncursesw5-dev libreadline-dev libssl-dev libtool lrzsz mkisofs msmtp nano ninja-build p7zip p7zip-full patch pkgconf python3 python3-pip libpython3-dev qemu-utils rsync rename scons squashfs-tools subversion swig texinfo uglifyjs upx-ucl unzip vim wget xmlto xxd zlib1g-dev genimage libconfuse2 genext2fs
```

The package `genimage` is provided in Ubuntu 24 or later. If you are runnig earlier versions, you can download it [from this URL](http://archive.ubuntu.com/ubuntu/pool/universe/g/genimage/genimage_17-2_amd64.deb) and install it manually.

Install the host tools:

```shell
wget https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz
tar -xzf host-tools.tar.gz
sudo mv host-tools /opt
```

### Download and Compile

```shell
# pull source code
git clone -b vizos --single-branch --depth=1 https://github.com/draftbottle/VizOS.git feeds-vizos
git clone https://github.com/draftbottle/istoreos.git --single-branch --depth=1

# link feeds-vizos to openwrt
echo "src-link  vizos  ${PWD}/feeds-vizos" >> istoreos/feeds.conf.default
cd istoreos
cat feeds.conf.default

# install dependencies
./scripts/feeds update  -a
./scripts/feeds install -a
./scripts/feeds install -f sophgo
./scripts/feeds install -f uboot-sophgo

# start compiling
cp ../feeds-vizos/configs/cv180x-config .config
make -j$(nproc) || make package/feeds/vizos/uboot-sophgo/compile V=s
make -j$(nproc) V=s
```

If built successfully, you can find the image file `milkv-duo.img` in the `istoreos/bin/targets/sophgo/cv180x/` directory.

### Using `dd` to Flash the Image to the microSD Card 

```shell
cp ./istoreos/bin/targets/sophgo/cv180x/milkv-duo.img ./
dd if=milkv-duo.img of=/dev/sdx bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
BusyBox v1.36.1 (2024-09-01 11:40:10 UTC) built-in shell (ash)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Powered by OpenWRT                                                                                                                                         -------------------------------------------------------                                                                                                                                     iStoreOS 23.05-SNAPSHOT, r0-5737568                                                                                                                                                         -------------------------------------------------------                                                                                                                                     执行. ./root/network-init.sh一键网络配置(非必须)                                                                                                                                                       -------------------------------------------------------                                                                                                                                    root@iStoreOS:/# uname -a                                                                                                                                                                   Linux iStoreOS 5.10.4 #0 Sun Sep 1 11:40:10 2024 riscv64 GNU/Linux                                                                                                                          root@iStoreOS:/# cat /proc/cpuinfo                                                                                                                                                          processor       : 0                                                                                                                                                                         hart            : 0                                                                                                                                                                         isa             : rv64imafdvcsu                                                                                                                                                             mmu             : sv39
```

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/lclF60XCCBMahHCGwIJVxJ6vh.svg)](https://asciinema.org/a/lclF60XCCBMahHCGwIJVxJ6vh)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
