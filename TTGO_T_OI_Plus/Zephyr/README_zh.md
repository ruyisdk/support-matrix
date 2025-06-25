# Zephyr TTGO T-OI-Plus 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
- 参考安装文档：https://docs.zephyrproject.org/latest/boards/lilygo/ttgo_toiplus/doc/index.html

### 硬件信息

- TTGO T-OI-Plus
- USB to UART 调试器一个
- Type-C 线一根

## 安装步骤

### 安装 Zephyr

创建虚拟环境：

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

获取 Zephyr：
```bash
west init ~/zephyrproject
cd ~/zephyrproject
west update
```

配置环境：
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

### 编译代码

使用 west 编译代码：
```bash
west build -p always -b ttgo_toiplus samples/hello_world
```

### 烧写镜像

```bash
west flash --esp-device /dev/ttyACM0 --esp-baud-rate 115200
```

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
ESP-ROM:esp32c3-api1-20210207
Build:Feb  7 2021
rst:0x1 (POWERON),boot:0xd (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fc87b20,len:0xe40
load:0x3fc88960,len:0x68c
load:0x40380000,len:0x7b10
SHA-256 comparison failed:
Calculated: 3499b2a5624bd64a6eb6f4d4b265ad490310cf854d30c21c0cb430077a50a49c
Expected: 00000000e06f0000000000000000000000000000000000000000000000000000
Attempting to boot anyway...
entry 0x40381296
I (54) soc_init: ESP Simple boot
I (54) soc_init: compile time Feb 28 2025 22:02:17
I (54) soc_init: chip revision: v0.4
I (54) flash_init: SPI Speed      : 80MHz
I (57) flash_init: SPI Mode       : DIO
I (61) flash_init: SPI Flash Size : 4MB
I (64) boot: DRAM: lma 0x00000020 vma 0x3fc87b20 len 0xe40    (3648)
I (70) boot: DRAM: lma 0x00000e68 vma 0x3fc88960 len 0x68c    (1676)
I (76) boot: IRAM: lma 0x000014fc vma 0x40380000 len 0x7b10   (31504)
I (83) boot: IRAM: lma 0x00009018 vma 0x00000000 len 0x6fe0   (28640)
I (89) boot: IMAP: lma 0x00010000 vma 0x42000000 len 0x2a34   (10804)
I (95) boot: IRAM: lma 0x00012a3c vma 0x00000000 len 0xd5bc   (54716)
I (101) boot: DMAP: lma 0x00020000 vma 0x3c010000 len 0x548    (1352)
I (107) boot: Image with 7 segments
I (110) boot: IROM segment: paddr=00010000h, vaddr=42000000h, size=02A32h ( 10802) map
I (118) boot: DROM segment: paddr=00020000h, vaddr=3c010000h, size=00550h (  1360) map
I (137) boot: libc heap size 258 kB.
I (137) spi_flash: detected chip: winbond
I (137) spi_flash: flash io: dio
*** Booting Zephyr OS build v4.1.0-rc2-119-gb74b092f22ea ***
Hello World! ttgo_toiplus/esp32c3
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。