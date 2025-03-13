---
sys: armbian
sys_ver: 25.2.1
sys_var: minimal

status: basic
last_update: 2025-03-13
---

# Armbian Bit-Brick K1 Test Report

## Test Environment

### System Information

- System Version: Armbian 25.2.1 Noble Minimal / IOT
- Download Links: https://www.armbian.com/bananapi-f3/

### Hardware Information

- Bit-Brick K1
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
xz -kd Armbian_25.2.1_Bananapif3_noble_current_6.6.76_minimal.img.xz 
sudo dd if=Armbian_25.2.1_Bananapif3_noble_current_6.6.76_minimal.img of=/dev/<your-device> bs=1M status=progress
```

**Warning**: This image loads `bpi-f3`'s device tree file by default, which may cause some peripherals to be unusable, please modify the file `/boot/extlinux/extlinux.conf` in the image after flashing.

```
label Armbian
  kernel /boot/Image
  initrd /boot/uInitrd
  fdt /boot/dtb/spacemit/k1-x_bit-brick.dtb
  append root=UUID=eee55a77-fdd4-44a3-bbb9-07c346297d0c earlycon=sbi console=tty1 console=ttyS0,115200 clk_ignore_unused rw no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes net.ifnames=0 splash plymouth.ignore-serial-consoles
```

### Logging into the System

Logging into the system via the serial port.

At the first boot, Armbian will ask to create a user and password, set the time zone, etc.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

```log
    _             _    _           
   /_\  _ _ _ __ | |__(_)__ _ _ _  
  / _ \| '_| '  \| '_ \ / _` | ' \ 
 /_/ \_\_| |_|_|_|_.__/_\__,_|_||_|
                                   
 v25.2.1 for BananaPi BPI-F3 running Armbian Linux 6.6.76-current-spacemit

 Packages:     Ubuntu stable (noble)
 Support:      DIY (community maintained)
 IP addresses: (LAN) IPv4:  IPv6:  
 Performance:  

 Load:         7%               Up time:       2 min
 Memory usage: 2% of 7.65G  
 CPU temp:     31°C              Usage of /:   4% of 29G    

 Commands: 

 Configuration : armbian-config
 Monitoring    : htop

root@bananapif3:~# uname -a
Linux bananapif3 6.6.76-current-spacemit #1 SMP PREEMPT_DYNAMIC Sat Feb  8 16:27:57 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
root@bananapif3:~# cat /etc/os-release 
PRETTY_NAME="Armbian 25.2.1 noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.armbian.com/"
SUPPORT_URL="https://forum.armbian.com"
BUG_REPORT_URL="https://www.armbian.com/bugs"
PRIVACY_POLICY_URL="https://www.armbian.com"
UBUNTU_CODENAME=noble
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian 25.2.1 noble"
root@bananapif3:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

root@bananapif3:~# cat /sys/firmware/devicetree/base/model 
spacemit k1-x bit-brick board
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
