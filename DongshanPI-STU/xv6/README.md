---
sys: xv6
sys_ver: null
sys_var: null

status: basic
last_update: 2025-04-15
---

# xv6 DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/michaelengel/xv6-d1
- Reference Installation Document: https://github.com/michaelengel/xv6-d1

### Hardware Information

- DongshanPI-Nezha STU
- Two USB-C cables

## Installation Steps

### Compile Kernel

Fetch the source code:
```shell
git clone https://github.com/michaelengel/xv6-d1.git
```

Modify `Makefile` to avoid compilation errors:
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

Compile:
```shell
make fs.img
make
```

### Flash the kernel with `xfel`

Install [xfel](https://github.com/xboot/xfel). e.g. on Arch Linux via AUR: `paru -S xfel`

With no SD card attached, press and hold the FEL button, and connect to both the OTG and DEBUG ports on board through two USB-C cables.

Send the payload through `xfel`:

```shell
xfel ddr d1
xfel write 0x40000000 kernel/kernel.bin
xfel exec 0x40000000
```

Check the serial port for outputs.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is also successful.

### Boot Log

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

