---
sys: buildroot
sys_ver: v2.0.0
sys_var: v2

status: basic
last_update: 2025-01-08
---

# BuildRoot Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- System Version: Duo 256M v2.0.0
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk-v2

### Hardware Information

- Milk-V Duo 256M
- A USB-A to C or USB C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Download Duo 256M Image

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.0/milkv-duo256m-musl-riscv64-sd_v2.0.0.img.zip
unzip milkv-duo256m-musl-riscv64-sd_v2.0.0.img.zip
```

### Flashing the Image

Use `dd` to flash the image to the SD card:

```shell
sudo dd if=milkv-duo256m-musl-riscv64-sd_v2.0.0.img  of=/path/to/your/device bs=4M status=progress
```

### Logging into the System

Logging into the system via serial port or SSH.

System will login as root automatically with no password required.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully, and login through the onboard serial port was also successful.

### Boot Log

```log
[    2.955329] vi_core_probe:206(): irq(29) for isp get from platform driver.
[    2.964050] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.969787] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.975960] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.981935] sync_task_init:177(): sync_task_init vi_pipe 3
[    2.987940] sync_task_init:177(): sync_task_init vi_pipe 4
[    2.994496] vi_core_probe:242(): isp registered as cvi-vi
[    3.056104] vpss_start_handler:5134(): handler for dev(0) started
[    3.056305] vpss_start_handler:5134(): handler for dev(1) started
[    3.089343] cvi-mipi-tx mipi_tx: IRQ index 0 not found
[    3.101222] cvi-mipi-tx mipi_tx: vbat irq(-6)
[    3.106349] cvi-mipi-tx mipi_tx: reset gpio pin(495) active(0)
[    3.112718] cvi-mipi-tx mipi_tx: power ctrl gpio pin(499) active(1)
[    3.119504] cvi-mipi-tx mipi_tx: pwm gpio pin(498) active(1)
[    3.152127] cv181x-cooling cv181x_cooling: elems of dev-freqs=6
[    3.158359] cv181x-cooling cv181x_cooling: dev_freqs[0]: 850000000 500000000
[    3.166143] cv181x-cooling cv181x_cooling: dev_freqs[1]: 425000000 375000000
[    3.173798] cv181x-cooling cv181x_cooling: dev_freqs[2]: 425000000 300000000
[    3.181520] cv181x-cooling cv181x_cooling: Cooling device registered: cv181x_cooling
[    3.213990] [INFO] Register SBM IRQ ###################################
[    3.214017] [INFO] pvctx->s_sbm_irq = 35
[    3.231513] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.243330] end jpu_init result = 0x0
[    3.342841] cvi_vc_drv_init result = 0x0
[    3.416924] sh (163): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Dec 9 10:13:49 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=-g2b4e5fdbc
ID=buildroot
VERSION_ID=2024.02.3
PRETTY_NAME="Buildroot 2024.02.3"
[root@milkv-duo]~#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
