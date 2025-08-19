# OpenBSD 7.6 HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenBSD 7.6
- 下载链接：https://cdn.openbsd.org/pub/OpenBSD/7.6/riscv64/install76.img
- 参考安装文档：https://cdn.openbsd.org/pub/OpenBSD/7.6/riscv64/INSTALL.riscv64

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张，提前刷入 Freedom U SDK
- U 盘一个

## 安装步骤

根据 [软件参考手册](https://www.sifive.cn/document-file/hifive-unmatched-software-reference-manual)，HiFive Unmatched 有多种启动方式。

针对 OpenBSD 镜像，我们有两种方式：
- 使用自带了 U-Boot 的镜像（如 Freedom U SDK），刷写至 microSD 卡，DIP 开关设置为 `MSEL[3:0]=1011`（出厂默认）
- 手动编译主线 U-Boot，刷写至 SPI Flash，并将 DIP 开关设置为 `MSEL[3:0]=0110`
    - 需要开发板上有可以运行并能够刷写 SPI Flash 的系统
    - 请参考此处的 U-Boot 文档：https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### U-Boot 烧录至 microSD

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

#### 刷写 Freedom U SDK

从 [此处](https://github.com/sifive/freedom-u-sdk/releases/latest) 获取 demo-coreip-cli-unmatched.rootfs.wic.xz 镜像。

解压并将镜像写入 microSD 卡。其中 `/dev/sdX` 为 microSD 卡所在位置。

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdX status=progress
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

### 刷写安装镜像到 U 盘

使用 `dd` 命令写入镜像到 microSD 卡。

`/dev/sdX` 为 U 盘位置。

```bash
sudo dd if=install74.img of=/dev/sdX status=progress
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

[![asciicast](https://asciinema.org/a/Mg53YxiOoNSGNImOs5WMei5uf.svg)](https://asciinema.org/a/Mg53YxiOoNSGNImOs5WMei5uf)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。