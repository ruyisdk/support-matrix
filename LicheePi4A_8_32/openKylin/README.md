---
sys: openkylin
sys_ver: v2.0-SP1
sys_var: null

status: good
last_update: 2025-04-07
---

# openKylin v2.0 SP1 LicheePi 4A 测试报告

## 测试环境

### 系统信息

- System Version: openKylin v2.0-SP1
- Download Link: https://www.openkylin.top/downloads/download-smp.php?id=86
- Reference Installation Document: https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- 桌面环境: UKUI (Pre-installed)

### 硬件信息

- Lichee Pi 4A (8G RAM + 32GB eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Flashing the Bootloader

Extract the installation suite.

```bash
tar -xvf openKylin-Embedded-V2.0-SP1-licheepi4a-riscv64.tar.xz
cd openKylin-Embedded-V2.0-SP1-licheepi4a-riscv64/
```

The directory should already contain the `fastboot` application and the `thead-image-linux.sh` script file. This script contains the commands for flashing the image.

Connect the LicheePi 4A to your computer using the Type-C connector and press and hold the `boot` key while powering up to enter fastboot mode. Then run the script.

```bash
sudo ./thead-image-linux.sh
```

### Logging into the System

You can see the installation guide after reboot.

Default username: `openkylin`
Default password: `openkylin`

### Expand partition

Expand the root partition to fill the entire eMMC.

```bash
sudo resize2fs /dev/mmcblk0p4
```

## Expected Results

The system should boot successfully, allowing login via the onboard serial console.

## Actual Results

The system booted up correctly, and login via the onboard serial console was successful. 

### Boot Log

```log
openKylin 2.0 SP1 openkylin ttyS0

openkylin login: openkylin
密码： 
Welcome to openKylin 2.0 SP1 (GNU/Linux 5.10.113-th1520 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

load environment: QT_ACCESSIBILITY=1
load environment: PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
openkylin@openkylin:~$ uname -a
Linux openkylin 5.10.113-th1520 #2024.07.20.13.28+d8f77de53 SMP PREEMPT Sat Jul 20 13:29:42 UTC  riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="2.0 SP1 (nile)"
VERSION_US="2.0 SP1 (nile)"
ID=openkylin
PRETTY_NAME="openKylin 2.0 SP1"
VERSION_ID="2.0"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=nile
PRODUCT_FEATURES=3
openkylin@openkylin:~$ lscpu 
架构：            riscv64
  字节序：        Little Endian
CPU:              4
  在线 CPU 列表： 0-3
openkylin@openkylin:~$ 
```

Login Screen：![](image.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test Successful.