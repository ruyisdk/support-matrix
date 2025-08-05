---
sys: eweos
sys_ver: 6.13.8
sys_var: null
provider: panglars
status: basic
last_update: 2025-03-28
---

# eweOS Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: eweOS
- Download Link: <https://github.com/panglars/eweos-vf2-mainline>
- Reference Installation Document: <https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md>
- eweOS Website: <https://os.ewe.moe/>

### Hardware Information

- Milk-V Mars (V1.21)
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Build Image

- Change `CROSS_COMPILE` in `build.sh` according to your local RISC-V toolchain prefix

- Change eweOS mirror link `${WGET} https://os-repo-lu.ewe.moe/eweos-images/eweos-riscv64-tarball.tar.xz` in `build.sh` to `${WGET} https://os-repo-auto.ewe.moe/eweos-images/eweos-riscv64-tarball.tar.xz` (Source of link: <https://os-wiki.ewe.moe/guides/qemu-boot-isoimage>)

``` bash
chmod +x ./build.sh
sudo ./build.sh
```

the resulting image is `ewe-vf2.img`.

### Flashing Image to microSD Card

```bash
sudo dd if=ewe-vf2.img of=/dev/<your-device> bs=1M status=progress
```

> [!Note]
> The build process will mount the image and perform the `chroot` operation, and the network will download the software package, so the image can only be successfully built automatically on a RISC-V HOST machine with a network connection.

### Logging into the System

Logging into the system via the serial port.

Default username: `ewe`

Default password: `ewe`

Root password: `ewe`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
eweOS 6.13.8 (/dev/ttyS0)


eweos-diskimage login: ewe
Password:

Welcome to eweOS!

 * Mainpage: https://os.ewe.moe
 * Wiki:     https://os-wiki.ewe.moe
 * Packages: https://os.ewe.moe/pkglist

[ewe@eweos-diskimage ~]$ cat /etc/os-release
NAME="eweOS"
ID=ewe
PRETTY_NAME="eweOS"
BUILD_ID=rolling
ANSI_COLOR="0;36"
HOME_URL="https://os.ewe.moe"
SUPPORT_URL="https://os.ewe.moe"
BUG_REPORT_URL="https://os.ewe.moe"
LOGO=eweos-logo
[ewe@eweos-diskimage ~]$ uname -a
Linux eweos-diskimage 6.13.8 #1 SMP Wed Mar 26 17:04:22 UTC 2025 riscv64 GNU/Linux
[ewe@eweos-diskimage ~]$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test Successful.
