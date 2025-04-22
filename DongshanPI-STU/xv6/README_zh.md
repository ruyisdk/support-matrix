# xv6 DongshanPI-Nezha STU 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/michaelengel/xv6-d1
- 参考安装文档：https://github.com/michaelengel/xv6-d1

### 硬件信息

- DongshanPI-Nezha STU
- 两根 USB-C 数据线

## 安装步骤

### 编译内核

拉取源码：
```shell
git clone https://github.com/michaelengel/xv6-d1.git
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

在不插入 SD 卡的情况下，按住开发板上的 FEL 按键，通过两根 USB-C 线同时连接到开发板的 OTG 接口和 DEBUG 接口。

使用 `xfel` 发送固件：
```shell
xfel ddr d1
xfel write 0x40000000 kernel/kernel.bin
xfel exec 0x40000000
```

观察串口输出。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

串口输出可能明显错位，属正常现象。

```log
DRAM only have internal ZQ!!
get_pmu_exist() = 4294967295
ddr_efuse_type: 0x0
[AUTO DEBUG] single rank and full DQ!
ddr_efuse_type: 0x0
[AUTO DEBUG] rank 0 row = 15
[AUTO DEBUG] rank 0 bank = 8
[AUTO DEBUG] rank 0 page size = 2 KB
DRAM BOOT DRIVE INFO: %s
DRAM CLK = 792 MHz
DRAM Type = 3 (2:DDR2,3:DDR3)
DRAMC ZQ value: 0x7b7bfb
DRAM ODT value: 0x42.
ddr_efuse_type: 0x0
DRAM SIZE =512 M
DRAM simple test OK.

xv6 kernel is booting

                     init: starting sh
                                      $ ls
                                          .              1 1 1024
                                                                 ..             1 1 1024
                   README         2 2 2059
                                          cat            2 3 21232
                                                                  echo           2 4 20152
                     forktest       2 5 12232
                                             grep           2 6 23736
init           2 7 21016
                        kill           2 8 20032
                                                ln             2 9 19944
   ls             2 10 23480
                            mkdir          2 11 20136
                                                     rm             2 12 20120
         sh             2 13 36184
                                  stressfs       2 14 21168
                                                           usertests      2 15 135512
                grind          2 16 34352
                                         wc             2 17 21848
                                                                  zombie         2 18 19560
                      console        3 19 0
                                           $ echo Hello xv6 from DongShanPiSTU D1!
             "ello xv6 from DongShanPiSTU D1!
                                             $

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。