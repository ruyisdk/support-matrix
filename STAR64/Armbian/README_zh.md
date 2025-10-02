# Armbian Star64 测试报告

> [!WARNING]
> Armbian Star64 的 GitHub release 版本已经被移除；最后一个可供下载的存档版本经测试同样无法启动。
> 尽管版本不同，若使用 Ubuntu/Debian 或主线 U-Boot 时，你将会遇到和下面完全一致的 `bootarg overflow 265+0+0+1 > 256` 错误。
> 目前看来 Armbian 对 Star64 的支持已经结束。建议使用其它发行版。

## 测试环境

### 操作系统信息

- 下载链接（已失效/已移除）：https://github.com/armbian/community/releases/download/25.2.0-trunk.124/Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
    - 最后可用的存档版本：https://k-space.ee.armbian.com/archive/star64/archive/
- 参考安装文档：https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429

### 硬件信息

- 开发板：Star64
- USB A to C / USB C to C 线缆
- SD 卡

## 安装步骤

### 烧写镜像

下载后，解压并烧写镜像（以下以 xfce 版为例）：
```bash
unxz -k Armbian_community_25.2.0-trunk.86_Star124_noble_edge_5.15.0_xfce_desktop.img.xz
sudo dd if=Armbian_community_25.2.0-trunk.86_Star124_noble_edge_5.15.0_xfce_desktop.img of=/dev/your/sdcard bs=1M status=progress
```

### 登录系统

通过串口连接开发板。

启动后，系统会要求用户手动配置用户名、密码、时区、语言等。

Xfce 版本需要配置完成后方可进入桌面。

可通过串口配置。若接入了键盘和显示器，亦可通过键盘配置。

## 预期结果

开发板正常输出启动信息。

## 实际结果

启动过程出现 `Boot failed (err=-14)`, 无法启动。

### 启动信息

```log

U-Boot 2025.01-1~0ubuntu2 (Feb 27 2025 - 17:08:21 +0000)

CPU:   sifive,u74-mc
Model: Pine64 Star64
DRAM:  8 GiB
Core:  158 devices, 29 uclasses, devicetree: board
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
No USB controllers found
resetting USB...
No USB controllers found
Working FDT set to ff71ca10
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Cannot persist EFI variables without system partition
** Booting bootflow '<NULL>' with efi_mgr
Loading Boot0000 'mmc 1' failed
EFI boot manager: Cannot load any image
Boot failed (err=-14)
Card did not respond to voltage select! : -110
** Booting bootflow 'mmc@16020000.bootdev.part_1' with extlinux
1:      Armbian_community
Retrieving file: /boot/Image
Retrieving file: /boot/uInitrd
bootarg overflow 265+0+0+1 > 256
Boot failed (err=-14)
No USB controllers found
ethernet@16030000 Waiting for PHY auto negotiation to complete......... TIMEOUT !
phy_startup() failed: -110
FAILED: -110
ethernet@16040000 Waiting for PHY auto negotiation to complete......... TIMEOUT !
phy_startup() failed: -110
FAILED: -110
BOOTP broadcast 1
BOOTP broadcast 2
BOOTP broadcast 3
BOOTP broadcast 4

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。