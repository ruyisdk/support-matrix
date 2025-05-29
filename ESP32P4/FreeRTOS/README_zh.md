# FreeRTOS ESP32-P4 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/espressif/esp-idf/tree/v5.4/examples/system/freertos/real_time_stats
- 参考文档：
  - ESP32-P4：https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4/esp32p4/

### 硬件信息

- ESP32-P4-Function-EV-Board

## 安装步骤

### 安装 ESP-IDF

ESP32-IDF的环境安装可以主要参考官网连接：
https://docs.espressif.com/projects/esp-idf/zh_CN/v5.4/esp32p4/get-started/index.html#get-started-how-to-get-esp-idf
不管是图形化界面还是命令行开发都有不错的效果。

### 准备工程仓库

```bash
git clone https://github.com/espressif/esp-idf
```

### 编译代码

```bash
cd esp-idf/examples/system/freertos/real_time_stats
idf.py menuconfig
idf.py build
```

根据使用的board在menuconfig调整参数

### 烧写镜像

确认连接到ESP32-P4后，烧写镜像。
在linux开发环境中，可能需要提前添加 udev 规则并应用（根据发行版不同可能需要更改 GROUP）

```bash
idf.py -p PORT flash monitor
```

（将 PORT 替换为要使用的串行端口的名称。

（要退出串行监视器，请键入 。Ctrl-]

有关配置和使用 ESP-IDF 构建项目的完整步骤，请参阅入门指南。

### 观察log

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从编译到启动）：

```log
I (26) boot: compile time May 29 2025 23:01:56
I (26) boot: Multicore bootloader
I (27) boot: chip revision: v1.0
I (29) boot: efuse block revision: v0.3
I (33) boot.esp32p4: SPI Speed      : 80MHz
I (36) boot.esp32p4: SPI Mode       : DIO
I (40) boot.esp32p4: SPI Flash Size : 2MB
I (44) boot: Enabling RNG early entropy source...
I (48) boot: Partition Table:
I (51) boot: ## Label            Usage          Type ST Offset   Length
I (57) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (64) boot:  1 phy_init       ESP-ROM:esp32p4-eco2-20240710
Build:Jul 10 2024
rst:0x1 (POWERON),boot:0x30f (SPI_FAST_FLASH_BOOT)
SPI mode:DIO, clock div:1
load:0x4ff33ce0,len:0x162c
load:0x4ff2abd0,len:0xd70
load:0x4ff2cbd0,len:0x32fc
entry 0x4ff2abda
I (25) boot: ESP-IDF v5.4-dirty 2nd stage bootloader
I (26) boot: compile time May 29 2025 23:01:56
I (26) boot: Multicore bootloader
I (27) boot: chip revision: v1.0
I (29) boot: efuse block revision: v0.3
I (33) boot.esp32p4: SPI Speed      : 80MHz
I (36) boot.esp32p4: SPI Mode       : DIO
I (40) boot.esp32p4: SPI Flash Size : 2MB
I (44) boot: Enabling RNG early entropy source...
I (48) boot: Partition Table:
I (51) boot: ## Label            Usage          Type ST Offset   Length
I (57) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (64) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (70) boot:  2 factory          factory app      00 00 00010000 00100000
I (78) boot: End of partition table
I (80) esp_image: segment 0: paddr=00010020 vaddr=40020020 size=0a1b0h ( 41392) map
I (96) esp_image: segment 1: paddr=0001a1d8 vaddr=30100000 size=0000ch (    12) load
I (98) esp_image: segment 2: paddr=0001a1ec vaddr=3010000c size=00038h (    56) load
I (104) esp_image: segment 3: paddr=0001a22c vaddr=4ff00000 size=05dech ( 24044) load
I (116) esp_image: segment 4: paddr=00020020 vaddr=40000020 size=1b88ch (112780) map
I (137) esp_image: segment 5: paddr=0003b8b4 vaddr=4ff05dec size=0859ch ( 34204) load
I (146) esp_image: segment 6: paddr=00043e58 vaddr=4ff0e400 size=01d4ch (  7500) load
I (152) boot: Loaded app from partition at offset 0x10000
I (152) boot: Disabling RNG early entropy source...
I (163) cpu_start: Multicore app
I (173) cpu_start: Pro cpu start user code
I (173) cpu_start: cpu freq: 360000000 Hz
I (173) app_init: Application information:
I (173) app_init: Project name:     real_time_stats
I (178) app_init: App version:      1
I (181) app_init: Compile time:     May 29 2025 23:01:33
I (186) app_init: ELF file SHA256:  eababab9e...
I (190) app_init: ESP-IDF:          v5.4-dirty
I (194) efuse_init: Min chip rev:     v0.1
I (198) efuse_init: Max chip rev:     v1.99 
I (202) efuse_init: Chip rev:         v1.0
I (206) heap_init: Initializing. RAM available for dynamic allocation:
I (212) heap_init: At 4FF11920 len 000296A0 (165 KiB): RAM
I (218) heap_init: At 4FF3AFC0 len 00004BF0 (18 KiB): RAM
I (223) heap_init: At 4FF40000 len 00060000 (384 KiB): RAM
I (228) heap_init: At 50108080 len 00007F80 (31 KiB): RTCRAM
I (233) heap_init: At 30100044 len 00001FBC (7 KiB): TCM
I (239) spi_flash: detected chip: generic
I (242) spi_flash: flash io: dio
W (245) spi_flash: Detected size(16384k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (258) main_task: Started on CPU0
I (298) main_task: Calling app_main()


Getting real time stats over 100 ticks
I (418) main_task: Returned from app_main()
| Task | Run Time | Percentage
| stats | 369 | 0%
| spin1 | 69516 | 3%
| spin2 | 69515 | 3%
| spin3 | 69540 | 3%
| spin4 | 69534 | 3%
| spin5 | 69547 | 3%
| spin0 | 69525 | 3%
| IDLE1 | 913584 | 45%
| IDLE0 | 662921 | 33%
| ipc1 | 0 | 0%
| ipc0 | 0 | 0%
| main | Deleted
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 291 | 0%
| spin0 | 69521 | 3%
| IDLE1 | 1000000 | 50%
| IDLE0 | 582610 | 29%
| spin2 | 69511 | 3%
| spin4 | 69519 | 3%
| spin3 | 69510 | 3%
| spin5 | 69519 | 3%
| spin1 | 69519 | 3%
| ipc1 | 0 | 0%
| ipc0 | 0 | 0%
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 292 | 0%
| spin0 | 69520 | 3%
| IDLE1 | 1000000 | 50%
| IDLE0 | 582623 | 29%
| spin2 | 69511 | 3%
| spin4 | 69512 | 3%
| spin3 | 69510 | 3%
| spin5 | 69512 | 3%
| spin1 | 69520 | 3%
| ipc1 | 0 | 0%
| ipc0 | 0 | 0%
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 291 | 0%
| spin0 | 69521 | 3%
| IDLE1 | 1000000 | 50%
| IDLE0 | 582635 | 29%
| spin2 | 69511 | 3%
| spin4 | 69510 | 3%
| spin3 | 69510 | 3%
| spin5 | 69510 | 3%
| spin1 | 69512 | 3%
| ipc1 | 0 | 0%
| ipc0 | 0 | 0%
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 291 | 0%
| spin0 | 69521 | 3%
| IDLE1 | 1000000 | 50%
| IDLE0 | 582627 | 29%
| spin2 | 69510 | 3%
| spin4 | 69511 | 3%
| spin3 | 69510 | 3%
| spin5 | 69510 | 3%
| spin1 | 69520 | 3%
| ipc1 | 0 | 0%
| ipc0 | 0 | 0%
Real time stats obtained


```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
