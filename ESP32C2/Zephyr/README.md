---
sys: zephyr
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-19
---

# Zephyr ESP32-C2 Test Report

## Test Environment
### Operating System Information

- Source Code Link:  
  https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/sys_heap  
  https://docs.zephyrproject.org/latest/boards/espressif/esp8684_devkitm/doc/index.html
- Reference Documents:  
    - ESP32-C2: https://www.espressif.com/en/support/documents/technical-documents?keys=esp32-C2

### Hardware Information

- ESP8684-DevKitM-1

## Installation Steps

### Install Zephyr

Configure the Zephyr environment according to the Zephyr documentation:  
https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### Prepare Project Repository

```bash
cd zephyr
```

### Compile Code

```bash
west build -p always -b esp8684_devkitm samples/basic/sys_heap
```

### Flash Image

After confirming the connection to ESP32-C2, flash the image.  
In a Linux development environment, you may need to add and apply udev rules in advance (the GROUP may need to be changed depending on the distribution).

```bash
west flash
west espressif monitor
```
(To exit the serial monitor, type Ctrl-].)

### Observe Log

Connect the development board via serial port.

## Expected Result

The system starts normally, and information can be viewed through the onboard serial port.

## Actual Result

Basic

### Startup Information

```log
ESP-ROM:esp8684-api2-20220127
Build:Jan 27 2022
rst:0x1 (POWERON),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fca7720,len:0x13dc
load:0x40380000,len:0x7710
SHA-256 comparison failed:
Calculated: 42e4a16fbf8afad01330ea77f9eff92df79321c3f2fd687b1e3caca3fa862e5b
Expected: 00000000d0740000000000000000000000000000000000000000000000000000
Attempting to boot anyway...
entry 0x403812ba
I (57) soc_init: ESP Simple boot
I (57) soc_init: compile time May 19 2025 14:07:10
I (57) soc_init: chip revision: v1.0
I (57) soc_flash_init: MMU Page Size  : 64K
I (62) soc_flash_init: SPI Speed      : 60MHz
I (68) soc_flash_init: SPI Mode       : DIO
I (74) soc_flash_init: SPI Flash Size : 4MB
I (80) boot: DRAM: lma 0x00000020 vma 0x3fca7720 len 0x13dc   (5084)
I (89) boot: IRAM: lma 0x00001404 vma 0x40380000 len 0x7710   (30480)
I (98) boot: IRAM: lma 0x00008b28 vma 0x00000000 len 0x74d0   (29904)
I (107) boot: IMAP: lma 0x00010000 vma 0x42000000 len 0x2e18   (11800)
I (117) boot: IRAM: lma 0x00012e20 vma 0x00000000 len 0xd1d8   (53720)
I (126) boot: DMAP: lma 0x00020000 vma 0x3c010000 len 0x590    (1424)
I (135) boot: Image with 6 segments
I (140) boot: IROM segment: paddr=00010000h, vaddr=42000000h, size=02E18h ( 11800) map
I (152) boot: DROM segment: paddr=00020000h, vaddr=3c010000h, size=00590h (  1424) map
I (180) boot: libc heap size 198 kB.
I (180) spi_flash: detected chip: gd
I (180) spi_flash: flash io: dio
*** Booting Zephyr OS build v4.1.0-3070-g91dfa23f80ee ***
System heap sample
allocated 0, free 196, max allocated 0, heap size 256
allocated 156, free 36, max allocated 156, heap size 256
allocated 100, free 92, max allocated 156, heap size 256
allocated 0, free 196, max allocated 156, heap size 256
There are 3 heaps allocated:
	0 - address 0x3fca8ae8 allocated 40, free 3968, max allocated 52, heap size 256
	1 - address 0x3fcab1bc allocated 0, free 203020, max allocated 0, heap size 256
	2 - address 0x3fcaaf40 allocated 0, free 196, max allocated 156, heap size 256

```

## Test Criteria

- Test Success: The actual result matches the expected result.
- Test Failure: The actual result does not match the expected result.

## Test Conclusion

Test Success