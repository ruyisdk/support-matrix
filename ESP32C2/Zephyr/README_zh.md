# Zephyr ESP32-C2 测试报告

## 测试环境
### 操作系统信息

- 源码链接：  
  https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/sys_heap  
  https://docs.zephyrproject.org/latest/boards/espressif/esp8684_devkitm/doc/index.html
- 参考文档：  
  - ESP32-C2：https://www.espressif.com/en/support/documents/technical-documents?keys=esp32-C2

### 硬件信息

- ESP8684-DevKitM-1

## 安装步骤

### 安装 Zephyr

根据 Zephyr 文档配置 Zephyr 环境，参考链接：  
https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### 准备工程仓库

```bash
cd zephyr
```

### 编译代码

```bash
west build -p always -b esp8684_devkitm samples/basic/sys_heap
```

### 烧写镜像

确认连接到 ESP32-C2 后，烧写镜像。  
在 Linux 开发环境中，可能需要提前添加 udev 规则并应用（根据发行版不同可能需要更改 GROUP）。

```bash
west flash
west espressif monitor
```
（要退出串行监视器，请键入 Ctrl-]）

### 观察日志

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

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

## 测试判定标准

- 测试成功：实际结果与预期结果相符。
- 测试失败：实际结果与预期结果不符。

## 测试结论

测试成功