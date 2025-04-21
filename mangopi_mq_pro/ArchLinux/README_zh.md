# Arch Linux MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：
    - Image Builder: https://github.com/sehraf/d1-riscv-arch-image-builder
    - U-Boot: https://github.com/smaeul/u-boot.git
    - RootFS: https://archriscv.felixc.at
- 参考安装文档：https://github.com/sehraf/d1-riscv-arch-image-builder

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 安装依赖

使用 Arch Linux 安装依赖如下：
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

### 编译设置

下载 builder 后，更改 consts.sh:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
vim consts.sh
```

选择 dtb：
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..6fc61d5 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-mangopi-mq-pro

 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

同时修改 `1_compile.sh` 以修复类似 https://github.com/The-OpenROAD-Project/OpenROAD/issues/6451 的问题：
```diff
diff --git a/1_compile.sh b/1_compile.sh
index 4fcbc7c..bf62caf 100755
--- a/1_compile.sh
+++ b/1_compile.sh
@@ -80,6 +80,7 @@ if [ ! -f "${OUT_DIR}/u-boot-sunxi-with-spl.bin" ]; then
     clean_dir ${DIR}

     git clone --depth 1 "${SOURCE_UBOOT}" -b "${TAG_UBOOT}"
+    sed -i 's/SWIG_Python_AppendOutput/SWIG_AppendOutput/g' u-boot/scripts/dtc/pylibfdt/libfdt.i_shipped
     cd ${DIR}
     pin_commit "${COMMIT_UBOOT}"
```

### 生成镜像

运行 `1_compile.sh`：
```bash
./1_compile.sh
```

### 刷写镜像

运行 `2_create_sd.sh`：

```bash
2_create_sd.sh /dev/your/device
```

**若开启了 USE_CHROOT（默认开启），其会之后自动 chroot 进镜像等待配置。建议使用这步安装如 vim 等基本应用。**

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`archriscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

U-Boot 启动时出错，无法进入系统。

### 启动信息

```log
U-Boot 2022.10-dirty (Mar 04 2025 - 12:39:02 +0800) Allwinner Technology

DRAM:  1 GiB
sunxi_set_gate: (CLK#24) unhandled
Core:  54 devices, 20 uclasses, devicetree: separate
WDT:   Started watchdog@6011000 with servicing every 1000ms (16s timeout)
MMC:   mmc@4020000: 0, mmc@4021000: 1
Loading Environment from FAT... PLL reg = 0xf8216300, freq = 1200000000
Unable to use mmc 0:1...
In:    serial@2500000
Out:   serial@2500000
Err:   serial@2500000
Net:
Warning: ethernet@4500000 (eth0) using random MAC address - 52:e9:78:d2:2a:ec
eth0: ethernet@4500000
starting USB...
Bus usb@4101000: USB EHCI 1.00
Bus usb@4101400: USB OHCI 1.0
Bus usb@4200000: USB EHCI 1.00
Bus usb@4200400: USB OHCI 1.0
scanning bus usb@4101000 for devices... 1 USB Device(s) found
scanning bus usb@4101400 for devices... 1 USB Device(s) found
scanning bus usb@4200000 for devices... 1 USB Device(s) found
scanning bus usb@4200400 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
Hit any key to stop autoboot:  0
PLL reg = 0xf8216300, freq = 1200000000
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Card did not respond to voltage select! : -110
** Bad device specification host 0 **
Couldn't find partition host 0:0
Cannot read EFI system partition
BootOrder not defined
EFI boot manager: Cannot load any image

Device 0: unknown device
sun8i_emac_eth_start: Timeout
missing environment variable: pxeuuid
Retrieving file: pxelinux.cfg/01-52-e9-78-d2-2a-ec
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/00000000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/0000000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/000000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/00000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/0000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/00
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/0
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default-riscv-sunxi-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default-riscv-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default-riscv
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default
sun8i_emac_eth_start: Timeout
Config file not found
sun8i_emac_eth_start: Timeout
sun8i_emac_eth_start: Timeout
=>

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。