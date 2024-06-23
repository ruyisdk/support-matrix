# Melis TinyVision Test Report

## Test Environment

### Operating System Information

- SDK Link:
    - Baidu Netdisk: Link: https://pan.baidu.com/s/1oIqGjCCtvUe0_k_kgXkusw?pwd=0kdr Access Code: 0kdr
- Reference Installation Documents:
    - https://dongshanpi.com/YuzukiHD-Lizard/01-BoardIntroduction/
    - https://tina.100ask.net/SdkModule/Linux_E907_DevelopmentGuide-01/

### Hardware Information

- TinyVision Development Board

## Installation Steps

### Prepare SDK

After downloading the SDK, merge the compressed packages and extract:
```bash
tar -xzvf tina-v851se.tar.gz
```

Since the default SDK does not support this development board, we need to separately copy the configurations that support this board into the tina-v853-open SDK. First, clone the repository with the board patches, then override the existing files:
```bash
git clone  https://github.com/DongshanPI/TinyVision-v851se_TinaSDK
cp -rfvd  TinyVision-v851se_TinaSDK/* tina-v851/
```

### Configure and Compile the System

After downloading the SDK, configure the environment:
```bash
cd tina-v853-open
source build/envsetup.sh
lunch
```
Choose the appropriate configuration.

**If issues arise, try using bash instead of other shells like zsh.**

Configure E906 to start RTOS:
```bash
cconfigs
cd ../default/
vim boot_package_nor.cfg
```
```diff
--- boot_package_nor.cfg.bak    2024-05-09 15:59:28.706860360 +0800
+++ boot_package_nor.cfg        2024-05-09 16:40:10.476852456 +0800
@@ -4,6 +4,7 @@
 item=optee,                  optee.fex
 item=u-boot,                        u-boot-spinor.fex
 item=dtb,                    sunxi.fex
+item=melis-elf,              riscv.fex
 ;item=logo,                   bootlogo.bmp.lzma
 ;item=shutdowncharge,         bempty.bmp.lzma
 ;item=androidcharge,          battery_charge.bmp.lzma
```
```bash
vim boot_package.cfg
```
```diff
--- boot_package.cfg.bak        2024-05-09 16:39:35.356852125 +0800
+++ boot_package.cfg    2024-05-09 16:40:01.263519036 +0800
@@ -4,6 +4,7 @@
 item=optee,                  optee.fex
 item=u-boot,                 u-boot.fex
 item=dtb,                    sunxi.fex
+item=melis-elf,              riscv.fex
 ;item=logo,                   bootlogo.bmp.lzma
 ;item=shutdowncharge,         bempty.bmp.lzma
 ;item=androidcharge,          battery_charge.bmp.lzma
```

Configure the kernel:
```bash
ckernel
m kernel_menuconfig
```
Include `Device Drivers → Mailbox Hardware Support`;
Include `Device Drivers → Mailbox Hardware Support → sunxi Mailbox` and `sunxi rv32 standby driver`:
```diff
--- .config.old 2024-05-09 16:42:29.690187100 +0800
+++ .config     2024-05-09 16:45:57.840189075 +0800
@@ -3174,7 +3174,12 @@
 # CONFIG_SH_TIMER_MTU2 is not set
 # CONFIG_SH_TIMER_TMU is not set
 # CONFIG_EM_TIMER_STI is not set
-# CONFIG_MAILBOX is not set
+CONFIG_MAILBOX=y
+CONFIG_SUNXI_MBOX=y
+CONFIG_SUNXI_RV32_STANBY=y
+# CONFIG_PLATFORM_MHU is not set
+# CONFIG_ALTERA_MBOX is not set
+# CONFIG_MAILBOX_TEST is not set
 CONFIG_IOMMU_API=y
 CONFIG_IOMMU_SUPPORT=y
 
@@ -3192,6 +3197,7 @@
 # Remoteproc drivers
 #
 # CONFIG_STE_MODEM_RPROC is not set
+# CONFIG_SUNXI_RPROC is not set
 
 #
 # Rpmsg drivers
@@ -3304,6 +3310,7 @@
 # Firmware Drivers
 #
 CONFIG_ARM_PSCI_FW=y
+# CONFIG_ARM_SCPI_PROTOCOL is not set
 # CONFIG_FIRMWARE_MEMMAP is not set
 # CONFIG_FW_CFG_SYSFS is not set
 CONFIG_HAVE_ARM_SMCCC=y
```
```bash
mkernel -j
```

> If the linker reports `yyloc` redefinition:
> This is due to GCC version being higher than 10. Change `YYLTYPE yyloc` in `scripts/dtc/dtc-parser.tab.c` to `extern YYLTYPE yyloc`.

Configure RTOS:
```bash
mmelis menuconfig
```

### Build and Package

```bash
make -j$(nproc)
```

### Logging into the System

Connect UART3 to view the serial output.

## Expected Results

The system should boot normally and display output via the serial port.

## Actual Results

CFT

### Boot Log

Screen recording:

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
