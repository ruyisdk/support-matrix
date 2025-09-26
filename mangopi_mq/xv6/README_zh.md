# xv6 MangoPi MQ 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/michaelengel/xv6-d1
- 参考安装文档：https://github.com/michaelengel/xv6-d1

### 硬件信息

- MangoPi MQ
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

### 编译内核

拉取源码：
```shell
dd if=milkv-duo_sdcard.img of=/dev/your/device bs=1M status=progress
```

修改 `Makefile` 以避免编译错误：
```make
diff --git a/Makefile b/Makefile
index 57875f1..bc65d72 100644
--- a/Makefile
+++ b/Makefile
@@ -60,7 +60,7 @@ LD = $(TOOLPREFIX)ld
 OBJCOPY = $(TOOLPREFIX)objcopy
 OBJDUMP = $(TOOLPREFIX)objdump

-CFLAGS = -Wall -Werror -O -fno-omit-frame-pointer -ggdb
+CFLAGS = -Wall -O -fno-omit-frame-pointer -ggdb
 CFLAGS += -MD
 CFLAGS += -mcmodel=medany
 CFLAGS += -ffreestanding -fno-common -nostdlib -mno-relax
```

编译内核：
```shell
make fs.img
make
```

### 通过 FEL 刷写固件

安装 [xfel](https://github.com/xboot/xfel). 如在 Arch Linux 下可通过 AUR 获取：`paru -S xfel`

通过 USB-C 线连接到开发板的 OTG 接口。

使用 `xfel` 发送固件：
```shell
xfel ddr f133
xfel write 0x40000000 kernel/kernel.bin
xfel exec 0x40000000
```

观察串口输出。

TX, RX 分别为板子底部 (P3) 第7, 8号引脚。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

输出卡在 `xv6 kernel is booting`， 无法进入 shell。

### 启动信息

```log
ZQ value = 0x2f***********
get_pmu_exist() = 4294967295
ddr_efuse_type: 0xb
[AUTO DEBUG] single rank and full DQ!
ddr_efuse_type: 0xb
[AUTO DEBUG] rank 0 row = 13
[AUTO DEBUG] rank 0 bank = 4
[AUTO DEBUG] rank 0 page size = 2 KB
DRAM BOOT DRIVE INFO: %s
DRAM CLK = 528 MHz
DRAM Type = 2 (2:DDR2,3:DDR3)
DRAMC read ODT  off.
DRAM ODT off.
ddr_efuse_type: 0xb
DRAM SIZE =64 M
DRAM simple test OK.

xv6 kernel is booting


```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。