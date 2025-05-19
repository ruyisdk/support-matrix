# Zephyr ESP32-C6 测试报告

## 测试环境
### 操作系统信息

- 源码链接：  
  https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/sys_heap  
  https://docs.zephyrproject.org/latest/boards/espressif/esp32c6_devkitc/doc/index.html
- 参考文档：  
  - ESP32-C6：https://www.espressif.com/en/support/documents/technical-documents?keys=esp32-C6

### 硬件信息

- ESP32-C6-DevKitC-1

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
west build -p always -b esp32c6_devkitc samples/basic/sys_heap
```

### 烧写镜像

确认连接到 ESP32-C6 后，烧写镜像。  
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
ESP-ROM:esp32c6-20220919
Build:Sep 19 2022
rst:0x1 (POWERON),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:2
load:0x40800000,len:0x868c
load:0x408086a0,len:0x181c
SHA-256 comparison failed:
Calculated: 641afa743a4b73640bb3d9d421a45aecaba7d9dfc1f559250c8f980cf1abedf4
Expected: 0000000010610000000000000000000000000000000000000000000000000000
Attempting to boot anyway...
entry 0x40801904
I (46) soc_init: ESP Simple boot
I (47) soc_init: compile time May 16 2025 17:22:37
I (47) soc_init: chip revision: v0.0
I (47) flash_init: SPI Speed      : 80MHz
I (50) flash_init: SPI Mode       : DIO
I (53) flash_init: SPI Flash Size : 8MB
I (57) boot: DRAM: lma 0x00000020 vma 0x40800000 len 0x868c   (34444)
I (63) boot: DRAM: lma 0x000086b4 vma 0x408086a0 len 0x181c   (6172)
I (69) boot: IRAM: lma 0x00009ee8 vma 0x00000000 len 0x6110   (24848)
I (75) boot: IMAP: lma 0x00010000 vma 0x42800000 len 0x740    (1856)
I (81) boot: IRAM: lma 0x00010748 vma 0x00000000 len 0xf8b0   (63664)
I (87) boot: IMAP: lma 0x00020000 vma 0x42000000 len 0x341c   (13340)
I (94) boot: Image with 6 segments
I (97) boot: IROM segment: paddr=00020000h, vaddr=42000000h, size=0341Ch ( 13340) map
I (104) boot: DROM segment: paddr=00010000h, vaddr=42800000h, size=00740h (  1856) map
I (123) boot: libc heap size 448 kB.
I (123) spi_flash: detected chip: gd
I (124) spi_flash: flash io: dio
*** Booting Zephyr OS build v4.1.0-3070-g91dfa23f80ee ***
System heap sample

allocated 0, free 196, max allocated 0, heap size 256
allocated 156, free 36, max allocated 156, heap size 256
allocated 100, free 92, max allocated 156, heap size 256
allocated 0, free 196, max allocated 156, heap size 256
There are 3 heaps allocated:
        0 - address 0x40809ea8 allocated 40, free 3968, max allocated 52, heap size 256
        1 - address 0x4080c59c allocated 0, free 458688, max allocated 0, heap size 256
        2 - address 0x4080c2f8 allocated 0, free 196, max allocated 156, heap size 256
```

## 测试判定标准

- 测试成功：实际结果与预期结果相符。
- 测试失败：实际结果与预期结果不符。

## 测试结论

测试成功