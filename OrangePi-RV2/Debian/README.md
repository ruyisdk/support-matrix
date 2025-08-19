---
sys: debian
sys_ver: "13"
sys_var: null

status: basic
last_update: 2025-08-19
---

# Debian OrangePi RV2 Test Report

## Test Environment

### Operating System Information
- OS Version: [Debian Trixie](https://www.debian.org/)
- Download URL: <https://dl.romanrm.net/risc-v/Orangepirv2_1.0.0_debian_trixie_minimal_linux6.6.63.img.bz2>
- Installation Reference: <http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-RV2.html>

### Hardware Information
- OrangePi RV2
- USB to UART debugger
- Three DuPont wires
- microSD card

## Installation Steps

### Download and Extract Image
Download the desired image from the [download link](https://dl.romanrm.net/risc-v/Orangepirv2_1.0.0_debian_trixie_minimal_linux6.6.63.img.bz2).
**Extract files:**
```bash
bzip2 -dk Orangepirv2_1.0.0_debian_trixie_minimal_linux6.6.63.img.bz2 
```

### Writing System Image to microSD Card
You can used the `dd` command:
```bash
sudo dd if=Orangepirv2_1.0.0_debian_trixie_minimal_linux6.6.63.img of=/dev/mmcblkX bs=1M
```

Log:
```log
输入了 1252+0 块记录
输出了 1252+0 块记录
1312817152 字节 (1.3 GB, 1.2 GiB) 已复制，51.3371 s，25.6 MB/s
```

## Logging into the System
Insert the microSD card into OrangePi RV2 and reboot.
Use a serial connection to log in; e.g. `minicom`.
```bash
minicom -D /dev/ttyACM0 -c on
```

Default username: `root`
Default password: `orangepi`

## Expected Results
System boots normally and allows login via onboard serial port.
If network is connected, SSH login should also work.

## Actual Results
System booted successfully and allowed login via serial.

```log
orangepirv2 login: orangepi (automatic login)

error: could not load font standard
Welcome to Orange Pi 1.0.0 Trixie with Linux 6.6.63-ky

System load:   28%              Up time:       0 min
Memory usage:  8% of 1.91G      IP:
CPU temp:      44°C             Usage of /:    4% of 29G

[ Menu-driven system configuration (beta): sudo dpkg -i orangepi-config.deb ]

orangepi@orangepirv2:~$ uname -a
Linux orangepirv2 6.6.63-ky #4 SMP PREEMPT Sun Aug 17 04:28:51 +05 2025 riscv64 GNU/Linux
orangepi@orangepirv2:~$ cat /etc/os-release
PRETTY_NAME="Orange Pi 1.0.0 Trixie"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.0
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
orangepi@orangepirv2:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchidZ for hel: 0x8000000058000001 | Minicom 2.9 | VT102 | 脱机 | ttyACM0                                                                                                                    mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Ky(R) X1
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf
_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : ky,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
```

## Test Criteria
Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion
Test successful.
