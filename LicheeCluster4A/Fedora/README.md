# Fedora 38 Lichee Cluster 4A Test Report

## Test Environment

### System Information

- System Version: Fedora 38
- Download link: [https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/](https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/)
- Reference Installation Document: [https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head](https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head)
- Fastboot links:
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A Dock
- One microSD card
- Network and Ethernet cable (connect to BMC, not a switch)

## Installation Steps

*The following steps are based on flashing to the first board in the cluster*

*Note: Fedora system boots from an SD card, not eMMC, so make sure to insert the card*

### Flashing Image

Use `unxz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
unxz /path/to/fedora.raw.xz
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### Flashing Bootloader

**Note: Fedora's u-boot is in the image. After the previous `dd` step, extract it from the boot partition on the SD card!**
![u-boot](./u-boot.png)

```bash
sudo ./fastboot flash ram ./path/to/your/u-boot-with-spl_lpi4a.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/u-boot-with-spl_lpi4a.bin
```

### Logging into the System

Login to the system using SOL (Serial Over LAN).

BMC default username: `root`

BMC default password: `0penBmc` **Note: it's `0`, not `O`**

Connect via `ssh -p 2301 root@lichee-rv.local`

Default username: `root`
Default password: `riscv`

### Common Issues

If USB cannot be used, it's because the Linux device tree needs patching. [Download the patch](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

## Expected Results

The system should boot up correctly, and you should be able to log in via SOL (Serial Over LAN).

## Actual Results

The system boots up correctly, and you can log in via SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/OTu3SKCoCpADbc4AMNJNOjjoQ.svg)](https://asciinema.org/a/OTu3SKCoCpADbc4AMNJNOjjoQ)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon May 15 18:37:47 UTC 2023

Kernel 5.10.113 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: [   85.830881] systemd-journald[337]: Oldest entry in /var/log/journal/605fc8e09e9a4453ae8bd14351948ca9/system.journal is older than the configured file retention duration (1month), suggesting rotation.
[   85.850848] systemd-journald[337]: /var/log/journal/605fc8e09e9a4453ae8bd14351948ca9/system.journal: Journal header limits reached or header out-of-date, rotating.
root
Password: 
[root@fedora-riscv ~]# neofetch 
             .',;::::;,'.                root@fedora-riscv 
         .';:cccccccccccc:;,.            ----------------- 
      .;cccccccccccccccccccccc;.         OS: Fedora Linux 38 (Xfce) riscv64 
    .:cccccccccccccccccccccccccc:.       Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board 
  .;ccccccccccccc;.:dddl:.;ccccccc;.     Kernel: 5.10.113 
 .:ccccccccccccc;OWMKOOXMWd;ccccccc:.    Uptime: 2 mins 
.:ccccccccccccc;KMMc;cc;xMMc:ccccccc:.   Packages: 2070 (rpm) 
,cccccccccccccc;MMM.;cc;;WW::cccccccc,   Shell: bash 5.2.15 
:cccccccccccccc;MMM.;cccccccccccccccc:   Resolution: 1024x768 
:ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:   Terminal: /dev/ttyS0 
cccccc:0MMKxdd:;MMMkddc.;cccccccccccc;   CPU: (4) 
ccccc:XM0';cccc;MMM.;cccccccccccccccc'   Memory: 185MiB / 7803MiB
ccccc;MMo;ccccc;MMW.;ccccccccccccccc;
ccccc;0MNc.ccc.xMMd:ccccccccccccccc;                             
cccccc;dNMWXXXWM0::cccccccccccccc:,                              
cccccccc;.:odl:.;cccccccccccccc:,.
:cccccccccccccccccccccccccccc:'.
.:cccccccccccccccccccccc:;,..
  '::cccccccccccccc::;,.


```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
