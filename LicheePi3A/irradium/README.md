---
sys: irradium
sys_ver: "3.8"
sys_var: null

status: good
last_update: 2025-08-06
---

# irradium LicheePi 3A Test Report

## Test Environment

### Operating System Information
- OS Version: irradium 3.8
- Official Download Links:
  - irradium-core: <https://dl.irradium.org/irradium/images/lichee_pi_3a/irradium-3.8-riscv64-core-lichee_pi_3a-6.16.0-build-20250801.img.zst>
  - irradium-xfce: <https://dl.irradium.org/irradium/images/lichee_pi_3a/irradium-3.8-riscv64-xfce-lichee_pi_3a-6.16.0-build-20250801.img.zst>
  - boot: <https://dl.irradium.org/irradium/images/lichee_pi_3a/boot-20250801.tar.xz>
- Faster Download links:
  - irradium-core: <https://mirrors.dotsrc.org/irradium/images/lichee_pi_3a/irradium-3.8-riscv64-core-lichee_pi_3a-6.15.2-build-20250611.img.zst>
  - irradium-xfce: <https://mirrors.dotsrc.org/irradium/images/lichee_pi_3a/irradium-3.8-riscv64-xfce-lichee_pi_3a-6.15.2-build-20250611.img.zst>
- Installation Reference: <https://dl.irradium.org/irradium/images/lichee_pi_3a/README.TXT>

### Hardware Information
- Lichee Pi 3A
- Power adapter
- USB to UART debugger
- Three DuPont wires
- MicroSD card

## Installation Steps

### Download and Extract Image
Download the desired image and u-boot from the [official download server](https://dl.irradium.org/irradium/images/lichee_pi_3a/).
**Extract files:**
```bash
zstd -d irradium-3.8-riscv64-core-lichee_pi_3a-6.15.2-build-20250611.img.zst
zstd -d irradium-3.8-riscv64-xfce-lichee_pi_3a-6.15.2-build-20250611.img.zst
```

**Result:**
```bash
❯ tree .
.
├── irradium-3.8-riscv64-core-lichee_pi_3a-6.15.2-build-20250510.img
├── irradium-3.8-riscv64-core-lichee_pi_3a-6.15.2-build-20250510.img.zst
├── irradium-3.8-riscv64-xfce-lichee_pi_3a-6.15.2-build-20250510.img
└── irradium-3.8-riscv64-xfce-lichee_pi_3a-6.15.2-build-20250510.img.zst
```

### Writing System Image to MicroSD Card
The author used the `dd` command:
```bash
sudo dd if=irradium-3.8-riscv64-core-lichee_pi_3a-6.15.2-build-20250510.img of=/dev/mmcblk0 bs=1M
```

## Logging into the System
Insert the MicroSD card into LPi3A and reboot.
Use a serial connection to log in; the author used `minicom`.
```bash
minicom -D /dev/ttyACM0 -c on
```
Default username: `root`
Password needs to be set after boot.

## Expected Results
System boots normally and allows login via onboard serial port.
If network is connected, SSH login should also work.

## Actual Results
System booted successfully and allowed login via serial.

```log
# uname -a
Linux lichee-pi-3a 6.15.2 #1 SMP PREEMPT Tue Jun 10 20:02:24 UTC 2025 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=irradium
VERSION="3.8"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org/"
BUG_REPORT_URL="https://irradium.org/bugs/"
```

## Desktop Environment
The official release includes an **XFCE** desktop image. Simply write it to the MicroSD card to use it.
```bash
sudo dd if=irradium-3.8-riscv64-xfce-lichee_pi_3a-6.15.2-build-20250510.img of=/dev/mmcblk0 bs=1M
```

Screenshots of XFCE desktop:
![](Screenshot.png)

## Test Criteria
Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion
Test successful.
