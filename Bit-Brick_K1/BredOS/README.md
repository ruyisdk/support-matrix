---
sys: bredos
sys_ver: 2025-07-16
sys_var: null
status: basic
last_update: 2025-08-13
---

# Bredos Bit-Brick K1 Test Report

## Test Environment

### System Information

- Download Link: https://bredos.org/download.html
- Reference Installation Document: https://wiki.bredos.org/en/installation

### Hardware Information

- BIT-BRICK K1
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
xz -d BredOS-riscv64-MILK-V-JUPITER-2025-07-16.img.xz
dd if=BredOS-riscv64-MILK-V-JUPITER-2025-07-16.img of=/dev/sdX bs=1M status=progress
```

### Add Device Tree

Download the [Bianbu](https://archive.spacemit.com/image/k1/version/bianbu/) image. Extract its `k1-x_bit-brick.dtb` file,and place it in `/dtb/linux-spacemit-k1/`.

``` log
unzip bianbu-24.04-desktop-k1-v2.1.1-release-20250305144026.img.zip
sudo losetup -fP --show bianbu-24.04-desktop-k1-v2.1.1-release-20250305144026.img
sudo mount /dev/loop0p5 /mnt
sudo cp /mnt/spacemit/6.6.63/k1-x_bit-brick.dtb ./

sudo umount /mnt
sudo losetup -d /dev/loop0

sudo mount /dev/sdX2 /mnt
sudo mv ./k1-x_bit-brick.dtb /mnt/dtb/linux-spacemit-k1/
```

### Setup extlinux.conf

Modify the `/mnt/extlinux/extlinux.conf` file

``` log
default l0
menu title BredOS U-Boot menu
prompt 1
timeout 10


label l0
    menu label BredOS linux-spacemit-k1
    linux /vmlinuz-linux-spacemit-k1
    initrd /initramfs-linux-spacemit-k1.img
    fdt /dtb/linux-spacemit-k1/k1-x_bit-brick.dtb
    append root=UUID=24db3d60-df13-4bf2-b4f0-f795e817ff88 console=ttyS0,115200 console=tty1 rootwait rw init=/sbin/init
rootflags=subvol=@ rootfstype=btrfs
```

### Logging into the System

Logging into the system via the serial port.

Default user and password is `bred`.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

```log
Welcome to BredOS (GNU/Linux 6.15.2-spacemit-k1 riscv64)

* Documentation:  https://wiki.bredos.org/
* Support:        https://discord.gg/beSUnWGVH2

        System Info as of Sun 22 @ 20:49:52
Device: spacemit k1-x bit-brick board     Hostname: bredos
Uptime: 3 minutes                         Users logged in: 1
CPU: Spacemit(R) X60 (8c, 8t)             System load: 0.35
Memory: 11.8% of 7894 MB used             Swap usage: 0.0%
Usage of /: 73.5% of 4.8GB

The updates status has not yet refreshed. Check back later.

Failed to fetch news.

System is operating normally.

┌─[bred@bredos]─(~)
└─[20:49]-(^_^)-[$] uname -a
Linux bredos 6.15.2-spacemit-k1 #6 SMP PREEMPT Sun Jul  6 01:25:47 EEST 2025 riscv64 GNU/Linux

┌─[bred@bredos]─(~)
└─[20:50]-(^_^)-[$] cat /etc/os-release
NAME="BredOS"
PRETTY_NAME="BredOS"
ID=bredos
ID_LIKE=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://discord.gg/jwhxuyKXaa"
LOGO=bred
IMAGE_ID=BredOS
IMAGE_VERSION=2022.02.02
┌─[bred@bredos]─(~)
└─[20:50]-(^_^)-[$] cat /proc/cpuinfo
processor       : 0
hart            : 0
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 1
hart            : 1
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 2
hart            : 2
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 3
hart            : 3
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 4
hart            : 4
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 5
hart            : 5
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 6
hart            : 6
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt

processor       : 7
hart            : 7
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
uarch           : spacemit,x60
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200
hart isa        : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zaamo_zalrsc_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
```

## Desktop Environment

This image comes pre-installed with the **GNOME** desktop environment, which starts automatically as a desktop session when a monitor is connected.

![](./gnome.jpeg)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
