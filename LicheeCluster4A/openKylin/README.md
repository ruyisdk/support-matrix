# openKylin Lichee Cluster 4A Test Report

## Test Environment

### System Information

- System Version: openKylin 2.0 alpha
- Download Link: [https://www.openkylin.top/downloads/index-cn.html](https://www.openkylin.top/downloads/index-cn.html)
- Reference Installation Documentation: [https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A baseboard
- Network and Ethernet cable (ensure connection to BMC instead of a switch)

## Installation Steps

*The following steps are based on flashing to the first board of the cluster.*

### Connect the Corresponding SOM

Use an A to A cable to connect the SOM.

### Flashing the Bootloader

Extract the installation kit.
Navigate to the directory of the fastboot tool.
Flash u-boot and boot.

```bash
tar -xvf openKylin-2.0-alpha-licheepi4a.tar.xz
cd openkylin-2.0-alpha-licheepi4a/fastboot/linux
sudo ./fastboot flash ram ../../images/$(ram_size)/u-boot-nonsec-2020.10-r0-noswap.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot ../../images/$(ram_size)/u-boot-nonsec-2020.10-r0-noswap.bin
sudo ./fastboot flash boot ../../images/$(ram_size)/boot.ext4
```

### Flashing the Image

Flash the root partition into the eMMC.

```bash
sudo ./fastboot flash root ../../images/openkylin-2.0-alpha-licheepi4a-riscv64.ext4
```

### Logging into the System

Login to the system via SOL (Serial Over LAN).

BMC default username: `root`

BMC default password: `0penBmc` **Note that it is `0`, not `O`**

Connect with `ssh -p 2301 root@lichee-rv.local`

Default username: `openkylin`
Default password: `openkylin`

### Common Issues

If USB is not working, it may require patching the Linux device tree. [Download the patch](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

If you prefer not to compile the dtb manually, you can extract the dtb (light-lpi4a.dtb) from the [pre-compiled image](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin) and replace the corresponding file under boot.

## Expected Results

The system starts successfully and allows login via SOL (Serial Over LAN).

## Actual Results

The system starts successfully and allows login via SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/d4d3yatzsx13CRtcdqV0RF7Td.svg)](https://asciinema.org/a/d4d3yatzsx13CRtcdqV0RF7Td)

```log
openKylin 2.0 openkylin ttyS0

openkylin login: openkylin
输入密码
Welcome to openKylin 2.0 (GNU/Linux 5.10.113-yocto-standard riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

openkylin@openkylin:~$ uname -a
Linux openkylin 5.10.113-yocto-standard #1 SMP PREEMPT Tue Dec 26 12:49:40 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
