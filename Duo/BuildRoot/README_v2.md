---
sys: buildroot
sys_ver: v2.0.1
sys_var: v2

status: basic
last_update: 2025-08-22
---

# Buildroot (v2) Milk-V Duo Test Report

## Test Environment

### Operating System Information
- System Version: Duo Buildroot V2.0.1
- Download Link: <https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duo-musl-riscv64-sd_v2.0.1.img.zip>
- Reference Installation Document: <https://github.com/milkv-duo/duo-buildroot-sdk-v2>

### Hardware Information
- Milk-V Duo 64M
- USB to UART debugger
- microSD card

## Installation Steps

### Download and Extract Image
Download the desired image from the [download link](https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duo-musl-riscv64-sd_v2.0.1.img.zip).
**Extract files:**
```shell
unzip milkv-duo-musl-riscv64-sd_v2.0.1.img.zip
```

### Using `dd` to Flash the Image to the microSD Card
```shell
sudo dd if=milkv-duo-musl-riscv64-sd_v2.0.1.img of=/dev/mmcblkX bs=1M
```

Log:
```log
输入了 896+1 块记录
输出了 896+1 块记录
939524608 字节 (940 MB, 896 MiB) 已复制，31.3784 s，29.9 MB/s
```

## Logging into the System
Insert the microSD card into Milk-V Duo and reboot.
Use a serial connection to log in; e.g. `minicom`.
```bash
minicom -D /dev/ttyACM0 -c on
```

Default username: `root`
Default password: `milkv`

## Expected Results
System boots normally and allows login via onboard serial port.
If USB NET is connected, SSH login should also work.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
[    2.777741] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.783716] sync_task_init:177(): sync_task_init vi_pipe 3
[    2.789690] sync_task_init:177(): sync_task_init vi_pipe 4
[    2.796187] vi_core_probe:242(): isp registered as cvi-vi
[    2.854730] vpss_start_handler:5143(): handler for dev(0) started
[    2.854911] vpss_start_handler:5143(): handler for dev(1) started
[    2.905199] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    2.917803] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    2.925703] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    2.933317] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    2.941032] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    2.975689] [INFO] Register SBM IRQ ###################################
[    2.975718] [INFO] pvctx->s_sbm_irq = 38
[    2.996176] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.007900] end jpu_init result = 0x0
[    3.101127] cvi_vc_drv_init result = 0x0
[    3.115999] sh (167): drop_caches: 3
Starting app...

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri May 30 14:51:52 CST 2025 riscv64 GNU/Linux
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

[root@milkv-duo]~# cat /etc/os-release
NAME=Buildroot
VERSION=-g6b03c2762-dirty
ID=buildroot
VERSION_ID=2025.02
PRETTY_NAME="Buildroot 2025.02"
[root@milkv-duo]~#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
