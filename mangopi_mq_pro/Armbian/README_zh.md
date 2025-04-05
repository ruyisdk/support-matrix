# Armbian MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://xogium.performanceservers.nl/archive/mangopi-mq/archive/Armbian_23.8.1_Mangopi-mq_jammy_edge_6.1.0-rc3_xfce_desktop.img.xz
- 参考安装文档：https://mangopi.org/mqpro

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -d https://xogium.performanceservers.nl/archive/mangopi-mq/archive/Armbian_23.8.1_Mangopi-mq_jammy_edge_6.1.0-rc3_xfce_desktop.img.xz
sudo dd if=/path/to/Armbian_23.8.1_Mangopi-mq_jammy_edge_6.1.0-rc3_xfce_desktop.img.xz of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
第一次后会设置密码

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

U-Boot 启动时出错，无法进入系统。

### 启动信息

```log
U-Boot 2022.07-rc3-35470-gafc07cec42-dirty (Jun 26 2022 - 13:03:06 +0300)

CPU:   rv64imafdc
Model: Allwinner D1 Nezha
DRAM:  1 GiB
sunxi_set_gate: (CLK#24) unhandled
Core:  66 devices, 24 uclasses, devicetree: board
WDT:   Started watchdog@6011000 with servicing (16s timeout)
MMC:   mmc@4020000: 0, mmc@4021000: 1
Loading Environment from nowhere... OK
In:    serial@2500000
Out:   serial@2500000
Err:   serial@2500000
Net:   
Warning: ethernet@4500000 (eth0) using random MAC address - 96:1a:8a:62:24:8b
eth0: ethernet@4500000
Hit any key to stop autoboot:  0 
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Found /boot/extlinux/extlinux.conf
Retrieving file: /boot/extlinux/extlinux.conf
1:      Armbian
Retrieving file: /boot/uInitrd
Retrieving file: /boot/Image
append: root=UUID=89038d48-9eef-4730-94fe-e7fe325e67e2 console=ttyS0,115200n8 console=tty0 earlycon=sbi cma=96M rootflags=data=writeback stmmaceth=chain_mode:1 rw rw no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes net.ifnames=0 splash plymouth.ignore-serial-consoles
Retrieving file: /boot/dtb/allwinner/sun20i-d1-nezha.dtb
Moving Image from 0x40040000 to 0x40200000, end=41ae6000
## Loading init Ramdisk from Legacy Image at 41c00000 ...
   Image Name:   uInitrd
   Image Type:   RISC-V Linux RAMDisk Image (gzip compressed)
   Data Size:    19879135 Bytes = 19 MiB
   Load Address: 00000000
   Entry Point:  00000000
   Verifying Checksum ... OK
ERROR: Did not find a cmdline Flattened Device Tree
Could not find a valid device tree
SCRIPT FAILED: continuing...
No EFI system partition
BootOrder not defined
EFI boot manager: Cannot load any image
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

Device 0: unknown device
sun8i_emac_eth_start: Timeout
missing environment variable: pxeuuid
Retrieving file: /boot/extlinux/pxelinux.cfg/01-96-1a-8a-62-24-8b
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/00000000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/0000000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/000000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/00000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/0000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/00
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/0
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default-riscv-sunxi-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default-riscv-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default-riscv
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default
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