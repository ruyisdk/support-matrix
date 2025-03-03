---
sys: openkylin
sys_ver: "2.0-SP1"
sys_var: null

status: good
last_update: 2025-03-03
---

# openKylin 2.0-SP1 RISC-V Test Report

## Test Environment

- System Version: openKylin 2.0-SP1 RISC-V
- Download Link: [https://mirror.iscas.ac.cn/openkylin-cdimage/2.0-SP1/openKylin-Embedded-V2.0-SP1-milk-v-pioneer-riscv64.img.xz](https://mirror.iscas.ac.cn/openkylin-cdimage/2.0-SP1/openKylin-Embedded-V2.0-SP1-milk-v-pioneer-riscv64.img.xz)
- Reference Installation Document: [https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8Sophgo_sg2042%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8Sophgo_sg2042%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)


### Hardware Information

- Milk-V Pioneer Box v1.3
- A microSD card
- HDMI cable + Monitor

## Installation Steps

### Flashing Image

Use `unxz` to extract the image.
Use `dd` to flash the image to the microSD card.

```bash
wget https://mirror.iscas.ac.cn/openkylin-cdimage/2.0-SP1/openKylin-Embedded-V2.0-SP1-milk-v-pioneer-riscv64.img.xz
unxz /path/to/openKylin-Embedded-V2.0-SP1-milk-v-pioneer-riscv64.img.xz
sudo dd if=/path/to/openKylin-Embedded-V2.0-SP1-milk-v-pioneer-riscv64.img.xz of=/dev/your_device bs=4M status=progress
```

### Logging into the System

Logging to the system through the graphical interface.

Default username: `openKylin`
Default password: `openkylin`

## Expected Results

The system boots up normally and allows login through the graphical interface.

## Actual Results

The system boots up normally and login through the graphical interface is successful.

### Boot Log

![desktop](./desktop.png)

```log
openkylin@192.168.36.39's password: 
Welcome to openKylin 2.0 (GNU/Linux 6.1.22 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

You do not have any new mail.
openkylin@openkylin:~$ uname -a
Linux openkylin 6.1.22 #11 SMP Mon Apr 10 10:16:05 CST 2023 riscv64 riscv64 riscv64 GNU/Linux
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
openkylin@openkylin:~$ 
```

Serial port logs (from flashing image to system boot):
[![asciicast](https://asciinema.org/a/Cgn1K3yizCBB40x4rVbYeZMj3.svg)](https://asciinema.org/a/Cgn1K3yizCBB40x4rVbYeZMj3)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
