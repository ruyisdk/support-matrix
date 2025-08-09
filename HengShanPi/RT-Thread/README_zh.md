# RT-Thread HengShanPi 测试报告

## 测试环境

### 硬件信息

- 开发板：HengShanPi D133EBS
- 其他硬件：
  - USB 电源适配器和USB-A to C 或 C to C 线缆一条
  - microSD 卡一张 (可选)
  - USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

### 操作系统信息

- 操作系统版本：RT-Thread v4.1.1 (ArtInChip Luban-lite SDK)
- 下载链接：<https://gitee.com/lcsc/luban-lite> 或 <https://gitee.com/artinchip/luban-lite>
- 参考安装文档：<https://wiki.lckfb.com/zh-hans/hspi-d133ebs/>

## 安装步骤

### 编译镜像

下载Lunban-lite SDK
> JLC：<https://gitee.com/lcsc/luban-lite>
>
> ArtInChip：<https://gitee.com/artinchip/luban-lite>

```bash
git clone https://gitee.com/lcsc/luban-lite
```

安装依赖

```bash
sudo apt install scons
sudo apt install pip
cd tools/env/local_pkgs/
tar xvf pycryptodomex-3.11.0.tar.gz
cd pycryptodomex-3.11.0
sudo python3 setup.py install
```

配置SDK

```bash
#scons --list-def //查看有多少配置
#scons --apply-def=0 //选择 0 号配置

saicogn@saicogn:~/hengshanpi/lcsc/luban-lite$ scons --list-def
scons: Reading SConscript files ...
Built-in configs:
  0. d12x_demo68-nand_baremetal_bootloader               
  1. d12x_demo68-nand_rt-thread_helloworld               
  2. d12x_demo68-nor_baremetal_bootloader                
  3. d12x_demo68-nor_rt-thread_helloworld                
  4. d12x_hmi-nor_baremetal_bootloader                   
  5. d12x_hmi-nor_rt-thread_helloworld                   
  6. d13x_JLC_baremetal_bootloader                       
  7. d13x_JLC_rt-thread_helloworld                       
  8. d13x_demo68-nor_baremetal_bootloader                
  9. d13x_demo68-nor_rt-thread_helloworld                
 10. d13x_demo88-nand_baremetal_bootloader               
 11. d13x_demo88-nand_rt-thread_helloworld               
 12. d13x_demo88-nor_baremetal_bootloader                
 13. d13x_demo88-nor_rt-thread_helloworld                
 14. d13x_kunlunpi88-nor_baremetal_bootloader            
 15. d13x_kunlunpi88-nor_rt-thread_helloworld            
 16. d21x_d215-demo88-nand_baremetal_bootloader          
 17. d21x_d215-demo88-nand_rt-thread_helloworld          
 18. d21x_d215-demo88-nor_baremetal_bootloader           
 19. d21x_d215-demo88-nor_rt-thread_helloworld           
 20. d21x_demo100-nor_baremetal_bootloader               
 21. d21x_demo100-nor_rt-thread_helloworld               
 22. d21x_demo128-nand_baremetal_bootloader              
 23. d21x_demo128-nand_rt-thread_helloworld              
 24. d21x_demo88-nand_baremetal_bootloader               
 25. d21x_demo88-nor_baremetal_bootloader                
 26. g73x_demo100-nor_baremetal_bootloader               
 27. g73x_demo100-nor_rt-thread_helloworld               
 28. g73x_demo68-nor_baremetal_bootloader                
 29. g73x_demo68-nor_rt-thread_helloworld                


saicogn@saicogn:~/hengshanpi/lcsc/luban-lite$ scons --apply-def=7
scons: Reading SConscript files ...
Load config from target/configs/d13x_JLC_rt-thread_helloworld_defconfig
```

可以在默认配置基础上使用 `menuconfig` 进一步配置

```bash
scons --menuconfig
```

编译

```bash
scons
```

输出镜像 `d13x_JLC_v1.0.0.img` 将保存在 `output/d13x_JLC_rt-thread_helloworld/images` 目录下

```bash
saicogn@saicogn:~/hengshanpi/lcsc/luban-lite/output/d13x_JLC_rt-thread_helloworld/images$ ls -lh
total 53M
-rw-rw-r-- 1 saicogn saicogn 1.2K  5月 16 13:43 bootcfg.txt
-rw-rw-r-- 1 saicogn saicogn 212K  5月 16 13:43 bootloader.aic
-rw-rw-r-- 1 saicogn saicogn 183K  5月 16 13:43 bootloader.bin
-rwxrwxr-x 1 saicogn saicogn 2.1M  5月 16 13:43 d13x.bin
-rw-rw-r-- 1 saicogn saicogn 114K  5月 16 13:43 d13x.detail.csv
-rw-rw-r-- 1 saicogn saicogn  33K  5月 16 13:43 d13x.dironly.csv
-rwxrwxr-x 1 saicogn saicogn  17M  5月 16 13:43 d13x.elf
-rw-rw-r-- 1 saicogn saicogn  11M  5月 16 13:43 d13x_JLC_v1.0.0.img
-rw-rw-r-- 1 saicogn saicogn 4.1M  5月 16 13:43 d13x.map
-rw-rw-r-- 1 saicogn saicogn 2.1M  5月 16 13:43 d13x_os.itb
-rw-rw-r-- 1 saicogn saicogn  438  5月 16 13:43 d13x_os.its
-rw-rw-r-- 1 saicogn saicogn  27K  5月 16 13:43 d13x.pbp
-rw-rw-r-- 1 saicogn saicogn  174  5月 16 13:43 d13x.summary.csv
-rw-rw-r-- 1 saicogn saicogn 1.0M  5月 16 13:43 data.lfs
-rw-rw---- 1 saicogn saicogn 4.0K  5月 16 13:43 env.bin
-rw-rw-r-- 1 saicogn saicogn  233  5月 16 13:43 env.txt
-rw-rw-r-- 1 saicogn saicogn  304  5月 16 13:43 env.txt.part.tmp
-rw-rw-r-- 1 saicogn saicogn 3.6K  5月 16 13:43 image_cfg.json
drwxrwxr-x 2 saicogn saicogn 4.0K  5月 16 00:14 keys
-rw-rw-r-- 1 saicogn saicogn 184K  5月 16 13:43 loader.aic
-rw-rw-r-- 1 saicogn saicogn  102  5月 16 13:43 ota-subimgs.cfg
-rw-rw-r-- 1 saicogn saicogn  140  5月 16 13:42 partition_file_list.h
-rw-rw-r-- 1 saicogn saicogn  122  5月 16 13:42 partition.json
-rw-rw-r-- 1 saicogn saicogn  736  5月 16 13:43 pbp_cfg.bin
-rw-rw-r-- 1 saicogn saicogn 7.5K  5月 16 13:43 pbp_cfg.json
-rw-rw-r-- 1 saicogn saicogn  29K  5月 16 13:43 pbp_ext.aic
-rw-rw-r-- 1 saicogn saicogn 1.5K  5月 16 13:42 post_build.bat
-rw-rw-r-- 1 saicogn saicogn 7.4M  5月 16 13:43 rodata.fatfs
-rw-rw-r-- 1 saicogn saicogn 6.4M  5月 16 13:43 rodata.fatfs.sparse
-rw-rw-r-- 1 saicogn saicogn  16K  5月 16 13:42 rtua.py
-rwxrwxr-x 1 saicogn saicogn 2.1M  5月 16 13:43 seg0.bin
-rw-rw-r-- 1 saicogn saicogn  29K  5月 16 13:43 usbupg-psram-init.aic
```

### 烧录镜像

使用ArtInChip的 [`AiBurn`](https://gitee.com/artinchip/tools/blob/master/AiBurn-1.4.7_Setup.zip) 软件通过USB直接烧录镜像（Windows环境），或使用MicroSD 卡烧录。

> 使用MicroSD卡烧录需要保证编译生成的 `bootloader.aic` 文件小于126 KB, 具体操作见[文档](https://wiki.lckfb.com/zh-hans/hspi-d133ebs/rtos-sdk/user-guide/burn-image.htm)。

### 登录系统

使用串口调试软件，通过串口连接开发板（默认波特率115200）。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
Pre-Boot Program ... (24-08-30 16:16 9ac5e6f)
SPINOR
cs=0, phase=3
cs=1, phase=2
Psram_init done.
goto run SPL

tinySPL [Built on May 16 2025 01:19:43]
Reboot action: Watchdog-Reset, reason: Command-Reboot
[W] usbh_get_connect_id()107 usb 0 port change wait failed.
qspi0 freq (input): 99000000Hz
qspi0 freq ( bus ): 49500000Hz
qspi0 freq ( bus ): 99000000Hz
Start-up from os
Selecting default config 'Luban-lite firmware'
spl read: 2189224 byte, 44828 us -> 47691 KB/s
Failed to get mtd config
 341973 : Run APP

     _         _   ___        ___ _     _
    / \   _ __| |_|_ _|_ __  / __| |__ (_)_ __
   / _ \ | '__| __|| || '_ \| |  | '_ \| | '_ \
  / ___ \| |  | |_ | || | | | |__| | | | | |_) |
 /_/   \_\_|   \__|___|_| |_|\___|_| |_|_| .__/
                                         |_|

Welcome to ArtInChip Luban-Lite 1.1.0 [D13x Inside]
Image version: 1.0.0
Built on May 16 2025 00:13:10
01-01 08:04:19 I/EPWM: ArtInChip EPWM loaded
01-01 08:04:19 I/PWM: ArtInChip PWM loaded
qspi0 freq (input): 99000000Hz
qspi0 freq ( bus ): 49500000Hz
01-01 08:04:19 I/NO_TAG: Flash ID: 0xef4018
01-01 08:04:19 I/NO_TAG: Find a Winbond flash chip. Size is 16777216 bytes.
qspi0 freq (input): 99000000Hz
qspi0 freq ( bus ): 99000000Hz
01-01 08:04:19 I/NO_TAG: norflash0 flash device is initialize success.
01-01 08:04:19 I/NO_TAG: Probe SPI flash norflash0 by SPI device qspi01 success.
01-01 08:04:19 I/touch: rt_touch init success
01-01 08:04:19 I/gt911: touch device gt911 init success
[I] aic_find_panel()94 find panel driver : panel-rgb
[I] aicfb_probe()958 fb0 allocated at 0x4024b1a0
[I] hal_ge_init()342 cmd queue hal, cmdq buffer size = 2048
[I] hal_ge_init()400 dither line phys: 0x402CB200
01-01 08:04:19 I/PSADC: ArtInChip PSADC loaded
[I] aic_sdmc_clk_init()560 SDMC0 sclk: 49500 KHz, parent clk 792000 KHz
01-01 08:04:19 I/SDMC: SDMC0 BW 1, sclk 49500 KHz, clk expt 400 KHz(act 399 KHz), div 2-62

[I] aic_sdmc_probe()683 SDMC0 driver loaded
[I] aic_sdmc_clk_init()560 SDMC1 sclk: 49500 KHz, parent clk 792000 KHz
01-01 08:04:19 I/SDMC: SDMC1 BW 1, sclk 49500 KHz, clk expt 400 KHz(act 399 KHz), div 2-62

[I] aic_sdmc_probe()683 SDMC1 driver loaded
01-01 08:04:19 I/sensor: rt_sensor[temp_tsen_cpu] init success
01-01 08:04:19 I/sensor: rt_sensor[temp_tsen_gpai] init success
01-01 08:04:20 I/WDT: ArtInChip WDT loaded
01-01 08:04:20 E/DFS: mount fs[elm] on /sdcard failed.

info: cmd ring buf size:1920
lvgl is occupying gt911 device
aic /> 01-01 08:04:20 E/gt911: read id failed
id = GT686369
01-01 08:04:20 E/gt911: read info failed
range_x = 1702059880
range_y = 109
point_num = 117
wifi device id == 0xf179
WL0:
    IPv4 Address   : 0.0.0.0
    Default Gateway: 0.0.0.0
    Subnet mask    : 0.0.0.0
    MAC addr       : 00:00:00:00:00:00
01-01 08:04:20 I/SDMC: SDMC0 BW 1, sclk 49500 KHz, clk expt 400 KHz(act 399 KHz), div 2-62

01-01 08:04:20 E/gt911: read info failed
01-01 08:04:20 W/SDIO: Card ocr below the defined voltage rang.
01-01 08:04:20 W/SDIO: Can't support the low voltage SDIO card.
01-01 08:04:20 I/SDMC: SDMC0 BW 1, sclk 49500 KHz, clk expt 49500 KHz(act 49500 KHz), div 1-0

[I] wifi_on()1104 Initializing WIFI ...

RTL871X: dump_drv_version v03 ic: RTL8189FTV libver: 304280ee502e93f4a7812402eaca66f4c700825e

RTL871X: dump_drv_version build time: Mar  8 2024 11:00:14

RTL871X: wlan0 :rltk_wlan_init

RTL871X: RTW: rtw_drv_entry enter

RTL871X: RTW: rtw_drv_entry exit

RTL871X: RTW: rtw_drv_probe line:1704

RTL871X: [gspi_dvobj_init] get wifi_func:30040b44

RTL871X: rtw_set_chip_endian!!

RTL871X: rtl8188fs_interface_configure: 0x04 = 0

RTL871X: rtl8188fs_interface_configure: 0x04 = 80

RTL871X: rtl8188f_read_chip_version RF_Type is 0 TotalTxPath is 1

RTL871X: Chip Version Info: CHIP_8188F_Normal_Chip_SMIC_B_CUT_1T1R_RomVer(0)

RTL871X: EEPROM type is E-FUSE

RTL871X: SetHwReg8188F: hci_sus_state=1

RTL871X: SetHwReg8188F: hci_sus_state=2

RTL871X: PowerOnCheck: val_mix:0x0002063f, res:0x0002063f

RTL871X: PowerOnCheck: 0x100 the result of cmd52 and cmd53 is the same.

RTL871X: PowerOnCheck: 0x1B8 test Pass.

RTL871X: _ReadAdapterInfo8188FS, 0x4e=0x42

RTL871X: hal_EfuseSwitchToBank: Efuse switch bank to 0

RTL871X: hal_ReadEFuse_WiFi: data end at address=98

RTL871X: Efuse Realmap:
29 81 03 CC 00 00 50 00 00 00 04 CC 0A 0C 00 00
24 24 24 24 24 24 28 28 28 28 28 02 FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF 20 17 1C 00 00 00 00 FF
FF 11 00 10 00 FF 00 FF 00 00 FF FF FF FF FF FF
3E 10 01 12 23 FF FF FF 20 04 4C 02 79 F1 21 02
0C 00 22 04 00 08 00 32 FF 21 02 0C 00 22 2A 01
01 00 00 00 00 00 00 00 00 00 00 00 02 00 FF FF
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 EB 00 6E 01 00 00 00 00 FF 28 F5 2B 81 12 F5
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

RTL871X: Hal_EfuseParsePackageType_8188F phy efuse read 0x1FB =3f

RTL871X: PackageType = 0x3

RTL871X: efuse_date_0xF0 = 0xF5

RTL871X: IC Real Version = 0x5

RTL871X: efuse_date_0xFB = 0x3F

RTL871X: IC SupportBW = 0x7

RTL871X: SetHwReg8188F: hci_sus_state=3

RTL871X: SetHwReg8188F: hci_sus_state=0

RTL871X: <==== _ReadAdapterInfo8188FS in 188 ms

RTL871X: rtw_init_sec_priv(): num_wpa_info= 1

RTL871X: rtw_init_sec_priv(): palloc_wpastainfo_buf= 30082260 alloc_wpastainfo_size=808

RTL871X: rtw_init_sec_priv(): wpa_sta_info[0]= 30082264

RTL871X: The driver is for MP

RTL871X: Init_ODM_ComInfo_8188f(): fab_ver=0 cut_ver=5

RTL871X: rtw_macaddr_cfg MAC Address  = 28:f5:2b:81:12:f5

RTL871X: bDriverStopped:1, bSurpriseRemoved:0, bup:0, hw_init_completed:0

RTL871X: wlan0 :dev=3007f540

RTL871X: wlan0 :rltk_wlan_start

RTL871X: +871x_drv - drv_open, bup=0

RTL871X: FW does not exist before power on!!

RTL871X: SetHwReg8188F: hci_sus_state=1

RTL871X: SetHwReg8188F: hci_sus_state=2

RTL871X: PowerOnCheck: val_mix:0x0000063f, res:0x0000063f

RTL871X: PowerOnCheck: 0x100 the result of cmd52 and cmd53 is the same.

RTL871X: PowerOnCheck: 0x1B8 test Pass.

RTL871X: Power on ok!

RTL871X: nic firmware download

RTL871X: rtl8188f_FirmwareDownload: fw_ver=e fw_subver=0000 sig=0x88f1, Month=06, Date=07, Hour=17, Minute=18

RTL871X: rtl8188f_FirmwareDownload(): Shift for fw header!

RTL871X: rtl8188f_FirmwareDownload by IO write!

RTL871X: rtl8188f_FirmwareDownload: 0x80 != 0x07000105,write to 0x07000105

RTL871X: polling_fwdl_chksum: Checksum report OK! (1, 0ms), REG_MCUFWDL:0x07040505

RTL871X: _8051Reset8188: Finish

RTL871X: _FWFreeToGo: Polling FW ready OK! (543, 14ms), REG_MCUFWDL:0x070405c6

RTL871X: rtl8188f_FirmwareDownload: DLFW OK !

RTL871X: rtl8188f_FirmwareDownload success. write_fw:1, 135ms

RTL871X:  <=== rtl8188f_FirmwareDownload()

RTL871X: Set RF Chip ID to RF_6052 and RF type to 0.

RTL871X: MAC Address = 28:f5:2b:81:12:f5
[I] rtt_thread_enter()593 RTKTHREAD xmitThread
[I] rtt_thread_enter()593 RTKTHREAD RTW_CMD_THREAD

RTL871X: -871x_drv - dev_open, bup=1
[I] wifi_on()1124 WIFI initialized
01-01 08:04:21 I/SDMC: SDMC1 BW 1, sclk 49500 KHz, clk expt 400 KHz(act 399 KHz), div 2-62


aic /> version
Welcome to ArtInChip Luban-Lite 1.1.0 [D13x Inside]
Image version: 1.0.0
Built on May 16 2025 00:13:10

aic />
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
