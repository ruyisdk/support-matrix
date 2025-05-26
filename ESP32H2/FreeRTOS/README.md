---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-19
---

# FreeRTOS ESP32-h2 Test Report

## Test Environment
### Operating System Information

- Source Code Link: https://github.com/espressif/esp-idf/tree/v5.4/examples/system/freertos/real_time_stats
- Reference Documents:
  - ESP32-h2: https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32h2/

### Hardware Information

- ESP32-H2-DevKitM-1

## Installation Steps

### Install ESP-IDF

The environment installation for ESP-IDF can mainly refer to the official website link:
https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32h2/get-started/index.html#get-started-how-to-get-esp-idf
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

After confirming the connection to esp32h2, flash the image.
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
ESP-ROM:esp32h2-20221101
Build:Nov  1 2022
rst:0x1 (POWERON),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x408460e0,len:0x1674
load:0x4083cad0,len:0xf04
load:0x4083efd0,len:0x2e98
entry 0x4083cada
I (23) boot: ESP-IDF v5.4-dirty 2nd stage bootloader
I (24) boot: compile time May 16 2025 16:27:13
I (25) boot: chip revision: v0.1
I (25) boot: efuse block revision: v0.3
I (28) boot.esp32h2: SPI Speed      : 64MHz
I (31) boot.esp32h2: SPI Mode       : DIO
I (35) boot.esp32h2: SPI Flash Size : 2MB
I (39) boot: Enabling RNG early entropy source...
I (43) boot: Partition Table:
I (46) boot: ## Label            Usage          Type ST Offset   Length
I (52) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (59) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (65) boot:  2 factory          factory app      00 00 00010000 00100000
I (72) boot: End of partition table
I (75) esp_image: segment 0: paddr=00010020 vaddr=42020020 size=09660h ( 38496) map
I (94) esp_image: segment 1: paddr=00019688 vaddr=40800000 size=06990h ( 27024) load
I (103) esp_image: segment 2: paddr=00020020 vaddr=42000020 size=1b220h (111136) map
I (135) esp_image: segment 3: paddr=0003b248 vaddr=40806990 size=03a70h ( 14960) load
I (141) esp_image: segment 4: paddr=0003ecc0 vaddr=4080a400 size=01634h (  5684) load
I (147) boot: Loaded app from partition at offset 0x10000
I (147) boot: Disabling RNG early entropy source...
I (161) cpu_start: Unicore app
I (169) cpu_start: Pro cpu start user code
I (170) cpu_start: cpu freq: 96000000 Hz
I (170) app_init: Application information:
I (170) app_init: Project name:     real_time_stats
I (174) app_init: App version:      1
I (177) app_init: Compile time:     May 16 2025 16:26:55
I (182) app_init: ELF file SHA256:  6a17f07bf...
I (187) app_init: ESP-IDF:          v5.4-dirty
I (191) efuse_init: Min chip rev:     v0.0
I (195) efuse_init: Max chip rev:     v0.99 
I (199) efuse_init: Chip rev:         v0.1
I (203) heap_init: Initializing. RAM available for dynamic allocation:
I (209) heap_init: At 4080CB60 len 00040820 (258 KiB): RAM
I (214) heap_init: At 4084D380 len 00002B60 (10 KiB): RAM
I (219) heap_init: At 50000000 len 00000FE8 (3 KiB): RTCRAM
I (226) spi_flash: detected chip: generic
I (228) spi_flash: flash io: dio
W (231) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (244) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (250) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (257) main_task: Started on CPU0
I (267) main_task: Calling app_main()


Getting real time stats over 100 ticks
I (517) main_task: Returned from app_main()
| Task | Run Time | Percentage
| stats | 926 | 0%
| spin1 | 154402 | 15%
| spin2 | 134395 | 13%
| spin3 | 156560 | 15%
| spin4 | 144374 | 14%
| spin5 | 130492 | 13%
| spin0 | 130509 | 13%
| IDLE | 147381 | 14%
| main | Deleted
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 750 | 0%
| spin1 | 162738 | 16%
| spin2 | 164868 | 16%
| spin4 | 178770 | 17%
| IDLE | 0 | 0%
| spin0 | 156613 | 15%
| spin3 | 156597 | 15%
| spin5 | 179665 | 17%
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 743 | 0%
| spin3 | 160800 | 16%
| spin2 | 171714 | 17%
| spin0 | 172691 | 17%
| IDLE | 3083 | 0%
| spin5 | 167766 | 16%
| spin4 | 156602 | 15%
| spin1 | 166601 | 16%
Real time stats obtained


```

## Test Criteria

Test Success: The actual result matches the expected result.

Test Failure: The actual result does not match the expected result.

## Test Conclusion

Test Success
