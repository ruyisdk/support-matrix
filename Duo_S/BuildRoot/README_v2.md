---
sys: buildroot
sys_ver: v2.0.1
sys_var: v2

status: basic
last_update: 2025-07-03
---

# BuildRoot (v2) Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: DuoS-V2.0.1 (musl riscv64 version)
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk-v2

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB Power Adapter
- A USB-A to C or USB C to C Cable for powering the development board
- A microSD Card
- A USB Card Reader
- A USB to UART Debugger (e.g., CP2102, FT2232, etc. Be aware that WCH CH340/341 series will cause garbled text output, DO NOT USE)

## Installation Steps

### Download DuoS Image and extract

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duos-musl-riscv64-sd_v2.0.1.img.zip
unzip milkv-duos-musl-riscv64-sd_v2.0.1.img.zip
```

### Flashing the Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=milkv-duos-musl-riscv64-sd_v2.0.1.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port and ssh.

## Actual Results

The system booted successfully and login via the onboard serial port and ssh was also successful.

### Boot Information

> The aic8800 insmod failure occurred because the Duo S used in the test does not have a Wi-Fi chip.
>
> This is normal.

```log
[    3.465078] vpss_start_handler:5143(): handler for dev(1) started
[    3.512876] cvi-mipi-tx mipi_tx: IRQ index 0 not found
[    3.524770] cvi-mipi-tx mipi_tx: vbat irq(-6)
[    3.529815] cvi-mipi-tx mipi_tx: reset gpio pin(354) active(0)
[    3.536143] cvi-mipi-tx mipi_tx: power ctrl gpio pin(353) active(1)
[    3.542892] cvi-mipi-tx mipi_tx: pwm gpio pin(352) active(1)
[    3.569852] cv181x-cooling cv181x_cooling: elems of dev-freqs=6
[    3.576099] cv181x-cooling cv181x_cooling: dev_freqs[0]: 850000000 500000000
[    3.583900] cv181x-cooling cv181x_cooling: dev_freqs[1]: 425000000 375000000
[    3.591486] cv181x-cooling cv181x_cooling: dev_freqs[2]: 425000000 300000000
[    3.599164] cv181x-cooling cv181x_cooling: Cooling device registered: cv181x_cooling
[    3.628687] [INFO] Register SBM IRQ ###################################
[    3.628715] [INFO] pvctx->s_sbm_irq = 37
[    3.643789] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.655437] end jpu_init result = 0x0
[    3.750599] cvi_vc_drv_init result = 0x0
[    3.821737] sh (192): drop_caches: 3
Starting app...
insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri May 30 14:51:54 CST 2025 riscv64 GNU/Linux
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39
```

Screen recording:

[![asciicast](https://asciinema.org/a/MRJsh4hLcH9HsXDixX6lJzdZx.svg)](https://asciinema.org/a/MRJsh4hLcH9HsXDixX6lJzdZx)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
