---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-04
---

# FreeRTOS ESP32-C2 Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/espressif/esp-idf/tree/v5.4/examples/system/freertos/real_time_stats
- Reference Documents:
  - ESP32-C2: https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32c2/

### Hardware Information

- ESP32-C2（ESP8684）

## Installation Steps

### Install ESP-IDF

The environment installation for ESP32-IDF can mainly refer to the official website link:
https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32C2/get-started/index.html#get-started-how-to-get-esp-idf
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

After confirming the connection to esp32c2, flash the image.
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
ESP-ROM:esp8684-api2-20220127
Build:Jan 27 2022
rst:0x1 (POWERON),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fcd5c80,len:0x15a4
load:0x403acb70,len:0xbb0
load:0x403aeb70,len:0x29f0
entry 0x403acb7a
I (21) boot: ESP-IDF v5.4-dirty 2nd stage bootloader
I (21) boot: compile time Apr 25 2025 16:09:43
I (21) boot: chip revision: v1.0
I (21) boot: efuse block revision: v0.1
I (25) boot.esp32c2: MMU Page Size  : 32K
I (29) boot.esp32c2: SPI Speed      : 60MHz
I (33) boot.esp32c2: SPI Mode       : DIO
I (36) boot.esp32c2: SPI Flash Size : 2MB
I (40) boot: Enabling RNG early entropy source...
I (45) boot: Partition Table:
I (47) boot: ## Label            Usage          Type ST Offset   Length
I (53) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (60) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (66) boot:  2 factory          factory app      00 00 00010000 00100000
I (73) boot: End of partition table
I (76) esp_image: segment 0: paddr=00010020 vaddr=3c010020 size=07334h ( 29492) map
I (90) esp_image: segment 1: paddr=0001735c vaddr=3fca9fe0 size=00cbch (  3260) load
I (92) esp_image: segment 2: paddr=00018020 vaddr=42000020 size=0be7ch ( 48764) map
I (110) esp_image: segment 3: paddr=00023ea4 vaddr=3fcaac9c size=00654h (  1620) load
I (110) esp_image: segment 4: paddr=00024500 vaddr=40380000 size=09fd8h ( 40920) load
I (126) boot: Loaded app from partition at offset 0x10000
I (127) boot: Disabling RNG early entropy source...
I (137) cpu_start: Unicore app
I (145) cpu_start: Pro cpu start user code
I (145) cpu_start: cpu freq: 120000000 Hz
I (145) app_init: Application information:
I (145) app_init: Project name:     real_time_stats
I (150) app_init: App version:      1
I (153) app_init: Compile time:     Apr 25 2025 16:09:24
I (158) app_init: ELF file SHA256:  d1ce7d251...
I (162) app_init: ESP-IDF:          v5.4-dirty
I (166) efuse_init: Min chip rev:     v1.0
I (170) efuse_init: Max chip rev:     v2.99 
I (174) efuse_init: Chip rev:         v1.0
I (178) heap_init: Initializing. RAM available for dynamic allocation:
I (184) heap_init: At 3FCAC270 len 00030900 (194 KiB): RAM
I (190) heap_init: At 3FCDCB70 len 0000294C (10 KiB): RAM
I (196) spi_flash: detected chip: gd
I (198) spi_flash: flash io: dio
W (201) spi_flash: Detected size(4096k) larger than the size in the binary image header(2048k). Using the size in the binary image header.
I (213) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (219) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (226) main_task: Started on CPU0
I (226) main_task: Calling app_main()


Getting real time stats over 100 ticks
I (496) main_task: Returned from app_main()
| Task | Run Time | Percentage
| stats | 1049 | 0%
| spin1 | 153928 | 15%
| spin2 | 175248 | 17%
| spin3 | 146080 | 14%
| spin4 | 175252 | 17%
| spin5 | 146073 | 14%
| spin0 | 146841 | 14%
| IDLE | 54990 | 5%
| esp_timer | 0 | 0%
| main | Deleted
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 858 | 0%
| spin2 | 165136 | 16%
| spin1 | 175246 | 17%
| spin3 | 170514 | 17%
| spin4 | 175266 | 17%
| IDLE | 0 | 0%
| spin5 | 146109 | 14%
| spin0 | 166870 | 16%
| esp_timer | 0 | 0%
Real time stats obtained

```

## Test Criteria

Test Success: The actual result matches the expected result.

Test Failure: The actual result does not match the expected result.

## Test Conclusion

Test Success
