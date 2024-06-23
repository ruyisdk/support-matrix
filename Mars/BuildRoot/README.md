# BuildRoot on Milk-V Mars

## Test Environment

### Operating System Information

- BuildRoot
  - Source Link: https://github.com/milkv-mars/mars-buildroot-sdk
  - Reference Installation Document: https://github.com/milkv-mars/mars-buildroot-sdk
- Build System Environment: Ubuntu 22.04.4 LTS in Docker

### Hardware Information

- Milk-V Mars
- A USB to UART Debugger
- Three Dupont Wires
- A USB A to C or C to C Cable
- A USB Power Supply
- Wired Network Connection

## Installation Steps

### Building the Image

Note: Since the provided BuildRoot is quite old, if you encounter SHA errors or 404 issues during the build process, try manually updating the SHA256SUM or the download link. You can find the latest BuildRoot at [buildroot](https://github.com/buildroot/buildroot) and replace the corresponding part under buildroot/package.
(You could also try directly replacing it with the latest BuildRoot.)

Install build dependencies:

```shell
sudo apt update
sudo apt install -y build-essential automake libtool texinfo bison flex gawk \
g++ git xxd curl wget gdisk gperf cpio bc screen texinfo unzip libgmp-dev \
libmpfr-dev libmpc-dev libssl-dev libncurses-dev libglib2.0-dev libpixman-1-dev \
libyaml-dev patchutils python3-pip zlib1g-dev device-tree-compiler dosfstools \
mtools kpartx rsync libcap-dev
```

Pull the source code:

```shell
git clone https://github.com/milkv-mars/mars-buildroot-sdk.git --depth=1
```

Checkout the branch corresponding to your device:

- Mars
  ```
  git checkout dev
  ```

- Mars CM eMMC
  ```
  git checkout dev-mars-cm
  ```

- Mars CM SD Card
  ```
  git checkout dev-mars-cm-sdcard
  ```

Start building:

```shell
make -j$(nproc)
```

**This process is very long, please be patient.**

After compiling, the following images will be generated in the work directory:

```
work/
├── visionfive2_fw_payload.img
├── image.fit
├── initramfs.cpio.gz
├── u-boot-spl.bin.normal.out
├── linux
    ├── arch/riscv/boot
    │   ├── dts
    │   │   └── starfive
    │   │       ├── jh7110-milkv-mars-cm-emmc.dtb
    │   │       ├── jh7110-milkv-mars-cm-sdcard.dtb
    │   │       ├── jh7110-milkv-mars.dtb
    │   │       ├── jh7110-visionfive-v2-ac108.dtb
    │   │       ├── jh7110-visionfive-v2.dtb
    │   │       ├── jh7110-visionfive-v2-wm8960.dtb
    │   │       ├── vf2-overlay
    │   │       │   └── vf2-overlay-uart3-i2c.dtbo
    │   └── Image.gz
    └── vmlinuz-5.15.0
```

### Building the SD Card Image

Continue to build the SD card image:
```bash
make buildroot_rootfs -j$(nproc)
make img
```

Note: If you encounter issues like libfakeroot during the build, replace the related package with a newer one from BuildRoot (including patches).

### Flashing the SD Card

Flash the image you just built to the SD card:
```bash
sudo dd if=work/sdcard.img of=/dev/sdX bs=4096
sync
```

### Logging into the System

If using network boot, after placing the files into TFTP, then:

Connect the serial port and network, then power up the Mars.

When U-Boot prompts `Hit any key to stop autoboot`, press any key to interrupt the boot process and run the TFTP server on your computer.

```
dhcp; setenv serverip xxx.xxx.xxx.xxx;
tftpboot ${fdt_addr_r} jh7110-milkv-mars.dtb;
tftpboot ${kernel_addr_r} Image.gz;
tftpboot ${ramdisk_addr_r} initramfs.cpio.gz;
run chipa_set_linux;run cpu_vol_set;
booti ${kernel_addr_r} ${ramdisk_addr_r}:${filesize} ${fdt_addr_r}
```

Username: `root`

Password: `starfive`

## Expected Results

The image is successfully built, the system boots normally, and login via the onboard serial port is possible.

## Actual Results

The system boots successfully, and login via the onboard serial port is successful.

### Boot Information

Screen Recording:
[![asciicast](https://asciinema.org/a/uweoEDTIkJplZk2LZwK3KVwhn.svg)](https://asciinema.org/a/uweoEDTIkJplZk2LZwK3KVwhn)

```log
Welcome to Buildroot
buildroot login: root
Password: 
# cat /etc/os-
cat: can't open '/etc/os-': No such file or directory
# cat /etc/os-release 
NAME=Buildroot
VERSION=2021.11
ID=buildroot
VERSION_ID=2021.11
PRETTY_NAME="Buildroot 2021.11"
# uname -a
Linux buildroot 5.15.0 #1 SMP Tue May 28 17:36:13 CST 2024 riscv64 GNU/Linux


```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
