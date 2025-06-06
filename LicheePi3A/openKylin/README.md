---
sys: openkylin
sys_ver: 2.0-SP1
sys_var: null

status: good
last_update: 2025-01-20
---

# openKylin v2.0 SP1 Lichee Pi 3A Test Report

## Test Environment

### System Information

- System Version: openKylin v2.0-SP1
- Download Link: [https://www.openkylin.top/downloads/index.html](https://www.openkylin.top/downloads/index.html) **Choose k1 version**
- Reference Installation Document: [https://docs.openkylin.top/en/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8SpacemiT_K1%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/en/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8SpacemiT_K1%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### Hardware Information

- Lichee Pi 3A
- Power Adapter
- A USB to UART Debugger
- A microSD Card

## Installation Steps

### Using `dd` to flash the image to SD card

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
xz -d openKylin-Embedded-V2.0-SP1-spacemit-k1-riscv64.img.xz
sudo dd if=openKylin-Embedded-V2.0-SP1-spacemit-k1-riscv64.img of=/dev/your-device bs=1M status=progress oflag=dsync
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `openkylin`
Default Password: `openkylin`


## Expected Results

The system should boot normally and allow login via the onboard serial port. Screen is accessible via display.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful. Screen is accessible via display.

### Boot Log

Screen recording (from flashing image to login):

[![asciicast](https://asciinema.org/a/pST1HOrfsuWLalTtE47RzzoUO.svg)](https://asciinema.org/a/pST1HOrfsuWLalTtE47RzzoUO)

```log
openKylin 2.0 openkylin ttyS0

openkylin 用户名：openkylin
密码： 
Welcome to openKylin 2.0 (GNU/Linux 6.1.15 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

You do not have any new mail.
load environment: QT_ACCESSIBILITY=1
load environment: PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
load environment: COGL_DRIVER=gles2
load environment: GDK_GL=gles
load environment: XWAYLAND_NO_GLAMOR=1
load environment: SDL_VIDEODRIVER=wayland
load environment: MESA_LOADER_DRIVER_OVERRIDE=pvr
openkylin@openkylin:~$ uname -a
Linux openkylin 6.1.15 #1.0.14.1 SMP PREEMPT Fri Aug 30 18:58:33 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="2.0 (nile)"
VERSION_US="2.0 (nile)"
ID=openkylin
PRETTY_NAME="openKylin 2.0"
VERSION_ID="2.0"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=nile
PRODUCT_FEATURES=3
openkylin@openkylin:~$ lscpu
架构：                riscv64
  字节序：            Little Endian
CPU:                  8
  在线 CPU 列表：     0-7
型号名称：            Spacemit(R) X60
  每个核的线程数：    1
  每个座的核数：      8
  座：                1
  CPU(s) scaling MHz: 100%
  CPU 最大 MHz：      1600.0000
  CPU 最小 MHz：      614.4000
Caches (sum of all):  
  L1d:                256 KiB (8 instances)
  L1i:                256 KiB (8 instances)
  L2:                 1 MiB (2 instances)
openkylin@openkylin:~$ 
```

login screen: ![login](./login.png)
desktop screenshot: ![desktop](./desktop.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
