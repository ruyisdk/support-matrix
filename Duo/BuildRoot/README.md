---
sys: buildroot
sys_ver: v2.0.0
sys_var: null

status: basic
last_update: 2025-01-08
---

# BuildRoot Milk-V Duo Test Report

## Test Environment

### Operating System Information

<<<<<<< HEAD
- System Version: Duo-V2.0.0
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk-v2
=======
- System Version: Duo-V1.1.4
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
>>>>>>> fc083e5 (Duo/Buildroot: Bump to v1.1.4)

### Hardware Information

- Milk-V Duo 64M
- A USB-A to C or USB C to C cable
- A microSD card

## Installation Steps

<<<<<<< HEAD
### Using `dd` to Flash the Image to the microSD Card

```shell
sudo dd if=milkv-duo-musl-riscv64-sd_v2.0.0.img  of=/path/to/your/device bs=4M status=progress
```

### Using `ruyi` CLI to Flash the Image to the microSD Card
=======
### Download Duo Image
>>>>>>> fc083e5 (Duo/Buildroot: Bump to v1.1.4)

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip
unzip milkv-duo-sd-v1.1.4.img.zip
```

### Flashing the Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=milkv-duo-sd-v1.1.4.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via serial port or SSH.

Default username: `root`
Default password: `milkv`

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
<<<<<<< HEAD
[    2.892411] vi_core_probe:206(): irq(33) for isp get from platform driver.
[    2.901240] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.906979] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.913081] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.919041] sync_task_init:177(): sync_task_init vi_pipe 3
[    2.924997] sync_task_init:177(): sync_task_init vi_pipe 4
[    2.931494] vi_core_probe:242(): isp registered as cvi-vi
[    2.986778] vpss_start_handler:5134(): handler for dev(0) started
[    2.986970] vpss_start_handler:5134(): handler for dev(1) started
[    3.027421] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    3.040112] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    3.048032] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    3.055656] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    3.063401] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    3.093205] [INFO] Register SBM IRQ ###################################
[    3.093235] [INFO] pvctx->s_sbm_irq = 38
[    3.108700] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.121295] end jpu_init result = 0x0
[    3.206886] cvi_vc_drv_init result = 0x0
[    3.220299] sh (163): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Dec 9 10:07:12 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=-g2b4e5fdbc
ID=buildroot
VERSION_ID=2024.02.3
PRETTY_NAME="Buildroot 2024.02.3"
[root@milkv-duo]~# 
```

=======
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri Nov 22 11:31:04 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=20241122-1139
ID=buildroot
VERSION_ID=2021.05
PRETTY_NAME="Buildroot 2021.05"
```

Screen recording (from flashing the image to system login):

[![asciicast](https://asciinema.org/a/pendFyzvbk51Sf8uaeozKjYRb.svg)](https://asciinema.org/a/pendFyzvbk51Sf8uaeozKjYRb)

>>>>>>> fc083e5 (Duo/Buildroot: Bump to v1.1.4)
## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
