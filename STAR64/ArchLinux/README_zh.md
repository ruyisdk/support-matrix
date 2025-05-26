# Arch Linux Pine64 Star64 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/yogo1212/arch-linux-star64
- 参考安装文档：https://github.com/yogo1212/arch-linux-star64

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 编译并烧写镜像

拉取源码，编译并烧写镜像（建议在 Arch Linux 主机下）：
```bash
git clone https://github.com/yogo1212/arch-linux-star64.git
cd arch-linux-star64
mkdir build
make
dd if=./build/star64.img of=/dev/your/device bs=1M status=progress
# or:
# make DEV_OR_IMG=/dev/your/device
```

### 登录系统

通过串口连接开发板。

## 预期结果

开发板正常输出启动信息。

## 实际结果

启动过程出现 `Boot failed (err=-14)`, 无法启动。

### 启动信息

```log

U-Boot 2025.07-rc2-00085-g92da174fc636 (May 26 2025 - 16:02:32 +0800)

CPU:   sifive,u74-mc
Model: Pine64 Star64
DRAM:  8 GiB
Core:  160 devices, 29 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
OK
StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : PINE64
Product full SN: STAR64V1-2310-D008E000-00000005
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:75:61
Ethernet MAC1 address: 6c:cf:39:00:75:62
--------EEPROM INFO--------

starfive_7110_pcie pcie@9c0000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
starting USB...
Register 2000820 NbrPorts 2
Starting the controller
USB XHCI 1.00
Bus usb@0: 4 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
Working FDT set to ff71a300
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Cannot persist EFI variables without system partition
** Booting bootflow '<NULL>' with efi_mgr
Loading Boot0000 'mmc 1' failed
EFI boot manager: Cannot load any image
Boot failed (err=-14)
Card did not respond to voltage select! : -110
ethernet@16030000 Waiting for PHY auto negotiation to complete....
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。