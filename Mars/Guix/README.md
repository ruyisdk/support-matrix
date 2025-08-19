---
sys: guix
sys_ver: null
sys_var: null

status: basic
last_update: 2025-04-12
---

# Guix Milk-V Mars Test Report

## Test Environment

### Hardware Information

- Development Board: Milk-V Mars (8GB RAM)
- Other Hardware:
  - A USB power adapter and A USB-A to C or C to C cable
  - A microSD card
  - A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

### Operating System Information

- OS Version: Guix (Build ID: 9893288, 8 April 2025)
- Download Link: <https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image>
- Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>

## Installation Steps

### Flashing the Image

Use `dd` command or `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
sudo dd if=0rvywqxwkfn0rk18q71fv5b55bc16ax8-visionfive2-barebones-raw-image of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`

No password by default

## Expected Results

The system should boot normally, allowing login via the onboard serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Information

```log
This is the GNU system.  Welcome.
visionfive2 login: root
This is the GNU operating system, welcome!

root@visionfive2 ~# uname -a
Linux visionfive2 6.13.9-gnu #1 SMP 1 riscv64 GNU/Linux
root@visionfive2 ~# cat /etc/os-release
NAME="Guix System"
ID=guix
PRETTY_NAME="Guix System"
LOGO=guix-icon
HOME_URL="https://guix.gnu.org"
DOCUMENTATION_URL="https://guix.gnu.org/en/manual"
SUPPORT_URL="https://guix.gnu.org/en/help"
BUG_REPORT_URL="https://lists.gnu.org/mailman/listinfo/bug-guix"
root@visionfive2 ~# cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
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

root@visionfive2 ~#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
