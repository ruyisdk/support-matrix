# FreeBSD 14.2 HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：FreeBSD 14.2
- 下载链接（USTC Mirror）：https://download.freebsd.org/releases/riscv/riscv64/ISO-IMAGES/14.2/FreeBSD-14.2-RELEASE-riscv-riscv64-mini-memstick.img.xz
- 参考安装文档：https://wiki.freebsd.org/riscv/HiFiveUnmatched

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张，提前刷入 Freedom U SDK
- U 盘一个

## 安装步骤

根据 [软件参考手册](https://www.sifive.cn/document-file/hifive-unmatched-software-reference-manual)，HiFive Unmatched 有多种启动方式。

针对 FreeBSD 镜像，我们有两种方式：
- 使用自带了 U-Boot 的镜像（如 Freedom U SDK），刷写至 microSD 卡，DIP 开关设置为 `MSEL[3:0]=1011`（出厂默认）
- 手动编译主线 U-Boot，刷写至 SPI Flash，并将 DIP 开关设置为 `MSEL[3:0]=0110`
    - 需要开发板上有可以运行并能够刷写 SPI Flash 的系统
    - 请参考此处的 U-Boot 文档：https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### U-Boot 烧录至 microSD

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

#### 刷写 Freedom U SDK

从 [此处](https://github.com/sifive/freedom-u-sdk/releases/latest) 获取 demo-coreip-cli-unmatched.rootfs.wic.xz 镜像。

解压并将镜像写入 microSD 卡。其中 `/dev/sdc` 为 microSD 卡所在位置。

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdc status=progress
```

### U-Boot 烧录至 SPI Flash

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

#### 烧录 U-Boot 到 SPI

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

### 烧录镜像到 U 盘

解压镜像，并使用 `dd` 命令写入镜像到 U 盘。

`/dev/sdX` 为 U 盘位置。

```shell
xz -dk FreeBSD-14.2-RELEASE-riscv-riscv64-mini-memstick.img.xz
sudo dd if=FreeBSD-14.2-RELEASE-riscv-riscv64-mini-memstick.img of=/dev/sdX status=progress
```

## 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名为 `root`，无密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
login: root
Apr 11 07:19:47  login[881]: ROOT LOGIN (root) ON ttyu0
FreeBSD 14.2-RELEASE (GENERIC) releng/14.2-n269506-c8918d6c7412

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List:        https://www.FreeBSD.org/lists/questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

To change this login announcement, see motd(5).
root@:~ # uname -a
FreeBSD  14.2-RELEASE FreeBSD 14.2-RELEASE releng/14.2-n269506-c8918d6c7412 GENERIC riscv
root@:~ # cat /etc/os-release
NAME=FreeBSD
VERSION="14.2-RELEASE"
VERSION_ID="14.2"
ID=freebsd
ANSI_COLOR="0;31"
PRETTY_NAME="FreeBSD 14.2-RELEASE"
CPE_NAME="cpe:/o:freebsd:freebsd:14.2"
HOME_URL="https://FreeBSD.org/"
BUG_REPORT_URL="https://bugs.FreeBSD.org/"
root@:~ # 
```

屏幕录像：

[![asciicast](https://asciinema.org/a/5dxQalniYzBi2YWpozwhs4jdv.svg)](https://asciinema.org/a/5dxQalniYzBi2YWpozwhs4jdv)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。