---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-19
---

# FreeRTOS ESP32-C6 Test Report

## Test Environment
### Operating System Information

- Source Code Link: https://github.com/espressif/esp-idf/tree/v5.4/examples/system/freertos/real_time_stats
- Reference Documents:
  - ESP32-C6: https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32c6/

### Hardware Information

- ESP32-C6-DevKitC-1

## Installation Steps

### Install ESP-IDF

The environment installation for ESP-IDF can mainly refer to the official website link:
https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32c6/get-started/index.html#get-started-how-to-get-esp-idf
Both graphical interface and command line development have good results.

### Prepare Project Repository

```bash
git clone https://github.com/espressif/esp-idf
```

### Compile Code

```bash
cd esp-idf/examples/system/freertos/real_time_stats
idf.py menuconfig
idf.py build
```

Adjust parameters in menuconfig according to the board used.

### Flash Image

After confirming the connection to esp32C6, flash the image.
In a Linux development environment, you may need to add and apply udev rules in advance (the GROUP may need to be changed depending on the distribution).

```bash
idf.py -p PORT flash monitor
```

(Replace PORT with the name of the serial port you want to use.)

(To exit the serial monitor, type Ctrl-].)

For the complete steps to configure and use ESP-IDF to build projects, refer to the Getting Started Guide.

### Observe Log

Connect the development board via serial port.

## Expected Result

The system starts normally, and information can be viewed through the onboard serial port .

## Actual Result

The system starts normally, and information can be viewed through the onboard serial port .

### Startup Information

Screen recording (from compilation to startup):


```log
ESP-ROM:esp32c6-20220919
Build:Sep 19 2022
rst:0x1 (POWERON),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:2
load:0x40875720,len:0x16b8
load:0x4086c110,len:0xe84
load:0x4086e610,len:0x304c
entry 0x4086c11a
I (23) boot: ESP-IDF v5.4-dirty 2nd stage bootloader
I (24) boot: compile time May 16 2025 16:34:35
I (24) boot: chip revision: v0.0
I (24) boot: efuse block revision: v0.2
I (27) boot.esp32c6: SPI Speed      : 80MHz
I (31) boot.esp32c6: SPI Mode       : DIO
I (35) boot.esp32c6: SPI Flash Size : 2MB
I (39) boot: Enabling RNG early entropy source...
I (43) boot: Partition Table:
I (46) boot: ## Label            Usage          Type ST Offset   Length
I (52) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (59) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (65) boot:  2 factory          factory app      00 00 00010000 00100000
I (72) boot: End of partition table
I (75) esp_image: segment 0: paddr=00010020 vaddr=42018020 size=089d8h ( 35288) map
I (89) esp_image: segment 1: paddr=00018a00 vaddr=40800000 size=07618h ( 30232) load
I (96) esp_image: segment 2: paddr=00020020 vaddr=42000020 size=11778h ( 71544) map
I (110) esp_image: segment 3: paddr=000317a0 vaddr=40807618 size=03b8ch ( 15244) load
I (114) esp_image: segment 4: paddr=00035334 vaddr=4080b1b0 size=01760h (  5984) load
I (119) boot: Loaded app from partition at offset 0x10000
I (119) boot: Disabling RNG early entropy source...
I (136) cpu_start: Unicore app
I (144) cpu_start: Pro cpu start user code
I (144) cpu_start: cpu freq: 160000000 Hz
I (145) app_init: Application information:
I (145) app_init: Project name:     real_time_stats
I (149) app_init: App version:      1
I (152) app_init: Compile time:     May 16 2025 16:34:10
I (157) app_init: ELF file SHA256:  387ce8e7e...
I (162) app_init: ESP-IDF:          v5.4-dirty
I (166) efuse_init: Min chip rev:     v0.0
I (170) efuse_init: Max chip rev:     v0.99 
I (174) efuse_init: Chip rev:         v0.0
I (178) heap_init: Initializing. RAM available for dynamic allocation:
I (184) heap_init: At 4080D8E0 len 0006ED30 (443 KiB): RAM
I (189) heap_init: At 4087C610 len 00002F54 (11 KiB): RAM
I (194) heap_init: At 50000000 len 00003FE8 (15 KiB): RTCRAM
I (200) spi_flash: detected chip: generic
I (203) spi_flash: flash io: dio
W (206) spi_flash: Detected size(8192k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (219) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (225) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (231) coexist: coex firmware version: 49a8cdc
I (250) coexist: coexist rom version 5b8dcfa
I (250) main_task: Started on CPU0
I (250) main_task: Calling app_main()


Getting real time stats over 100 ticks
I (440) main_task: Returned from app_main()
| Task | Run Time | Percentage
| stats | 681 | 0%
| spin1 | 119517 | 11%
| spin2 | 109538 | 10%
| spin3 | 109542 | 10%
| spin4 | 119510 | 11%
| spin5 | 109530 | 10%
| spin0 | 109545 | 10%
| IDLE | 321671 | 32%
| esp_timer | 0 | 0%
| main | Deleted
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 579 | 0%
| spin1 | 130826 | 13%
| IDLE | 228407 | 22%
| spin4 | 125172 | 12%
| spin3 | 125152 | 12%
| spin0 | 125176 | 12%
| spin5 | 125181 | 12%
| spin2 | 139507 | 13%
| esp_timer | 0 | 0%
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 579 | 0%
| spin5 | 140819 | 14%
| spin3 | 140799 | 14%
| IDLE | 217144 | 21%
| spin1 | 125182 | 12%
| spin2 | 125165 | 12%
| spin4 | 125158 | 12%
| spin0 | 125153 | 12%
| esp_timer | 0 | 0%
Real time stats obtained


```

## Test Criteria

Test Success: The actual result matches the expected result.

Test Failure: The actual result does not match the expected result.

## Test Conclusion

Test Success
