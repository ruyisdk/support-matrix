---
sys: ubuntu
sys_ver: "24.04.01"
sys_var: LTS

status: good
last_update: 2025-05-22
---

# Ubuntu 24.04.01 LTS OrangePi RV2 Test Report

## Test Environment

### Hardware Information

- Development Board: OrangePi RV2 (8GB RAM)
- Other Hardware:
  - A USB power adapter and A USB-A to C or C to C cable
  - A microSD card
  - A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
  - A HDMI cable, A USB Mouse and A USB Keyboard (optional)

### Operating System Information

- OS Version: Ubuntu 24.04.01 LTS
- Download link: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>
- Reference Installation Document: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>

## Installation Steps

### Flashing the Image

Use `7z` to decompress the image.
Use `dd` command or use the `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdX` corresponds to the storage device.

```bash
7z x Orangepirv2_1.0.0_ubuntu_noble_desktop_gnome_linux6.6.63.7z

sudo dd if=Orangepirv2_1.0.0_ubuntu_noble_desktop_gnome_linux6.6.63.img of=/dev/sdX bs=1M status=progress

sync
```

### Logging into the System

Logging into the system via the serial port.

Default username: `orangepi` (automatic login)

Default password: `orangepi`

or

username: `root`

password: `orangepi`

## Expected Results

The system should boot normally, allowing login via the onboard serial port. After connect HDMI to the display screen can normally display the login image, and supports USB mouse and USB keyboard.

## Actual Results

The system booted successfully, and the output was successfully viewed via the serial port. After connect HDMI to the display screen can normally display the login image, and supports USB mouse and USB keyboard.

### Boot Information

```log
Starting kernel ...

[    0.000000] Linux version 6.6.63-ky (root@test) (riscv64-unknown-linux-gnu-gcc (g09b62c20e09) 13.2.1 20240423, GNU ld (GNU Binutils) 2.42) #1.0.0 SMP PREEMPT Wed Mar 12 09:04:00 CST 2025
[    0.000000] Machine model: ky x1 orangepi-rv2 board
[    0.000000] SBI specification v1.0 detected
[    0.000000] SBI implementation ID=0x1 Version=0x10003
[    0.000000] SBI IPI extension detected
[    0.000000] SBI RFENCE extension detected
[    0.000000] earlycon: sbi0 at I/O port 0x0 (options '')
[    0.000000] printk: bootconsole [sbi0] enabled

orangepirv2 login: orangepi (automatic login)

  ___  ____  _   ______     ______
 / _ \|  _ \(_) |  _ \ \   / /___ \
| | | | |_) | | | |_) \ \ / /  __) |
| |_| |  __/| | |  _ < \ V /  / __/
 \___/|_|   |_| |_| \_\ \_/  |_____|

Welcome to Orange Pi 1.0.0 Noble with Linux 6.6.63-ky

System load:   62%              Up time:       0 min
Memory usage:  4% of 7.65G      IP:            172.17.0.1 192.168.137.75
CPU temp:      48°C             Usage of /:    16% of 29G

orangepi@orangepirv2:~$ uname -a
Linux orangepirv2 6.6.63-ky #1.0.0 SMP PREEMPT Wed Mar 12 09:04:00 CST 2025 riscv64 riscv64 riscv64 GNU/Linux

orangepi@orangepirv2:~$ cat /etc/os-release
PRETTY_NAME="Orange Pi 1.0.0 Noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo

orangepi@orangepirv2:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

orangepi@orangepirv2:~$ sensors
cluster0_thermal-virtual-0
Adapter: Virtual device
temp1:        +58.0°C

cluster1_thermal-virtual-0
Adapter: Virtual device
temp1:        +58.0°C

orangepi@orangepirv2:~$
```

GUI for desktop:

![GUI for desktop](./image_desktop.jpg)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
