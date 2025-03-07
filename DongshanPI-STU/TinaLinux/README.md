---
sys: tina
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-06
---

# Tina Linux DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: [Link](https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7) Password: qcw7
- Reference Installation Document: [Link](https://d1.docs.aw-ol.com/study/study_1tina/)

### Hardware Information

- DongshanPI-Nezha STU
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Compiling SDK

After downloading, you can find the SDK under DongshanNezhaSTU-TinaV2.0-SDK.
Merge and extract the SDK:
```bash
cat tina-d1-h.tar.bz2.* | tar -zxv
```

Compile and package:
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### Flashing Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=tina_d1-h.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the onboard serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted up normally and login via the onboard serial port is also successful.

### Boot Log

Screen recording (From flashing image to login):

```log
kmodloader done
[   21.737966] sunxi-mmc 4021000.sdmmc: smc 1 p1 err, cmd 5, RTO !!
[   21.745840] sunxi-mmc 4021000.sdmmc: smc 1 p1 err, cmd 5, RTO !!
[   21.753436] sunxi-mmc 4021000.sdmmc: smc 1 p1 err, cmd 5, RTO !!
[   21.801755] sunxi-mmc 4021000.sdmmc: smc 1 p1 err, cmd 5, RTO !!
[   21.811462] sunxi-mmc 4021000.sdmmc: sdc set ios:clk 0Hz bm PP pm OFF vdd 0 width 1 timing LEGACY(SDR12) dt B
[   24.528045] libphy: 4500000.eth: probed
[   24.552037] sunxi-gmac 4500000.eth eth0: eth0: Type(8) PHY ID 001cc916 at 0 IRQ poll (4500000.eth-0:00)
[   24.663487] br-lan: port 1(eth0) entered blocking state
[   24.669315] br-lan: port 1(eth0) entered disabled state
[   24.701700] device eth0 entered promiscuous mode
[   24.708268] br-lan: port 1(eth0) entered blocking state
[   24.714139] br-lan: port 1(eth0) entered forwarding state
Trying to connect to SWUpdate...
[   25.441810] br-lan: port 1(eth0) entered disabled state
[   25.978830] [SNDCODEC][sunxi_card_hw_params][620]:stream_flag: 0
[   35.681434] usb1-vbus: disabling
[  238.501416] HDMI cable is disconnected
[  242.101413] hdmi_hpd_sys_config_release
[  248.371415] HDMI cable is connected
[  249.291638] error: invalid cea_vic code:0
[  249.296230] [HDMI2 error]: sink do not support this mode:0



BusyBox v1.27.2 () built-in shell (ash)

 _____  _              __     _
|_   _||_| ___  _ _   |  |   |_| ___  _ _  _ _
  | |   _ |   ||   |  |  |__ | ||   || | ||_'_|
  | |  | || | || _ |  |_____||_||_|_||___||_,_|
  |_|  |_||_|_||_|_|  Tina is Based on OpenWrt!
 ----------------------------------------------
 Tina Linux (Neptune, 61CC0487)
 ----------------------------------------------
root@TinaLinux:/# uname -a
Linux TinaLinux 5.4.61 #5 PREEMPT Fri Jul 22 03:07:57 UTC 2022 riscv64 GNU/Linux
root@TinaLinux:/# lscpu
/bin/ash: lscpu: not found
root@TinaLinux:/# opkg --version
opkg version 0.1.8
root@TinaLinux:/# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
