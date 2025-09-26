---
sys: xv6
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-09-26
---

# xv6 MangoPi MQ Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/michaelengel/xv6-d1
- Reference Installation Document: https://github.com/michaelengel/xv6-d1

### Hardware Information

- MangoPi MQ
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Compile Kernel

Fetch the source code:
```shell
dd if=milkv-duo_sdcard.img of=/dev/your/device bs=1M status=progress
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

### Flash the firmware via FEL

Install [xfel](https://github.com/xboot/xfel). e.g. on Arch Linux via AUR: `paru -S xfel`

Connect to the OTG port on board through USB-C.

Send the payload through `xfel`:

```shell
xfel ddr f133
xfel write 0x40000000 kernel/kernel.bin
xfel exec 0x40000000
```

Check the serial port for outputs.

The board's TX and RX pins are pins 7, 8 on connector P3, respectively.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

Output is stuck at `xv6 kernel is booting`.

### Boot Log

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.

