---
sys: archlinux
sys_ver: null
sys_var: null

status: basic
last_update: 2025-04-16
---

# Arch Linux DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Packaging Script: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- DongshanPI-Nezha ST
- A Type-C power cable
- A UART to USB debugger
- An SD card

## Installation Steps

### Using Packaging Script

### Install Dependencies

Use Arch Linux to install dependencies as follows:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

### Select dtb File

Download the source and modify consts.sh:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
vim consts.sh
```

Select dtb:
```shell
export DEVICE_TREE=sun20i-d1-dongshan-nezha-stu
```

Also modify `1_compile.sh` to address an issue similar to https://github.com/The-OpenROAD-Project/OpenROAD/issues/6451:

```diff
diff --git a/1_compile.sh b/1_compile.sh
index 4fcbc7c..bf62caf 100755
--- a/1_compile.sh
+++ b/1_compile.sh
@@ -80,6 +80,7 @@ if [ ! -f "${OUT_DIR}/u-boot-sunxi-with-spl.bin" ]; then
     clean_dir ${DIR}

     git clone --depth 1 "${SOURCE_UBOOT}" -b "${TAG_UBOOT}"
+    sed -i 's/SWIG_Python_AppendOutput/SWIG_AppendOutput/g' u-boot/scripts/dtc/pylibfdt/libfdt.i_shipped
     cd ${DIR}
     pin_commit "${COMMIT_UBOOT}"
```

### Generate Image

Run `1_compile.sh`:
```bash
./1_compile.sh
```

### Flash Image

Run `2_create_sd.sh`:

```bash
2_create_sd.sh /dev/your/device
```

**If `USE_CHROOT` is enabled (default is enabled), it will automatically chroot into the image for configuration. It's recommended to install basic applications like vim at this step.**

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `archriscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted up normally and login via the onboard serial port is also successful.

### Boot Log

```log
Arch Linux 6.8.0 (ttyS0)

licheerv login: root
Password:

[root@licheerv ~]# uname -a
Linux licheerv 6.8.0 #1 SMP Wed Apr 16 14:52:24 CST 2025 riscv64 GNU/Linux
[root@licheerv ~]# cat /etc/os-release
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo
[root@licheerv ~]# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

[root@licheerv ~]#

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
