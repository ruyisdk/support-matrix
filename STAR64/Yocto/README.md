---
sys: yocto
sys_ver: null
sys_var: null

status: basic
last_update: 2025-07-13
---

# Yocto Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
- Reference Installation Document: https://github.com/Fishwaldo/meta-pine64

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flashing Image

After downloading, extract and flash the image (Plasma version as an example):
```bash
wget https://github.com/Fishwaldo/meta-pine64/releases/download/v2.1/star64-image-plasma-star64.wic.bz2
bzip2 -kd star64-image-plasma-star64.wic.bz2
sudo dd if=star64-image-plasma-star64.wic of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port or via GUI.

## Expected Results

The development board outputs boot information normally.

## Actual Results

The development board outputs boot information normally.

### Boot Log

```log
Starting kernel ...

clk u2_dw_i2c_clk_core already disabled
clk u2_dw_i2c_clk_apb already disabled
clk u5_dw_i2c_clk_core already disabled
clk u5_dw_i2c_clk_apb already disabled
[    0.091531] Initramfs unpacking failed: invalid magic at start of compressed archive
[    0.244231] L2CACHE: DataError @ 0x00000000.08040270
[    0.249128] L2CACHE: DataFail @ 0x00000000.08040074
[    0.822920] jh7110-sec 16000000.crypto: Unable to request sec_m dma channel in DMA channel
[    0.831143] jh7110-sec 16000000.crypto: Cannot initial dma chan
[    0.874439] debugfs: Directory '16008000.sec_dma' with parent 'dmaengine' already present!
[    0.888560] rtc-hym8563 2-0051: hctosys: unable to read the hardware clock
�[    1.398847] starfive-i2s 120b0000.i2stx_4ch0: designware: i2s master mode supported
[    1.407277] cdns-dsi 295d0000.mipi: starfive dsi bind end
[    6.711817] mailbox_test mailbox_client: invalid resource
[    6.717238] mailbox_test mailbox_client: invalid resource


PinIx 2.1 star64 hvc0

star64 login: PinIx 2.1 star64 ttyS0

star64 login: root
Password:
root@star64:~# uname -a
Linux star64 5.15.131 #1 SMP Thu Sep 21 04:12:12 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
root@star64:~# cat /etc/os-release
ID=pinix
NAME="PinIx"
VERSION="2.1 (pinix)"
VERSION_ID=2.1
PRETTY_NAME="PinIx 2.1 (pinix)"
DISTRO_CODENAME="pinix"
root@star64:~#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
