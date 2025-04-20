---
sys: nixos
sys_ver: "25.05"
sys_var: null

status: basic
last_update: 2025-04-18
---

# NixOS Milk-V Mars Test Report

## Test Environment

### Hardware Information

- Development Board: Milk-V Mars (8GB RAM)
- Other Hardware:
  - A USB power adapter and A USB-A to C or C to C cable
  - A microSD card
  - A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

### Operating System Information

- OS Version: NixOS 25.05 (Warbler) (Build ID: 20250328.2cc0d7f)
- Download Link: <https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://github.com/NickCao/nixos-riscv>

## Installation Steps

### Flashing the Image

Use `zstd` command to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
wget https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst

zstd -d nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst

sudo dd if=nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img of=/dev/sdc bs=1M status=progress

sync
```

### Logging into the System

Logging into the system via the serial port.

Default username: `nixos` (automatic login)

No password by default

## Expected Results

The system should boot normally, allowing login via the onboard serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Information

```log
<<< Welcome to NixOS sd-card-25.05.20250328.2cc0d7f (riscv64) - ttyS0 >>>
The "nixos" and "root" accounts have empty passwords.

To log in over ssh you must set a password for either "nixos" or "root"
with `passwd` (prefix with `sudo` for "root"), or add your public key to
/home/nixos/.ssh/authorized_keys or /root/.ssh/authorized_keys.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)


[nixos@nixos:~]$ cat /etc/os-release
ANSI_COLOR="0;38;2;126;186;228"
BUG_REPORT_URL="https://github.com/NixOS/nixpkgs/issues"
BUILD_ID="25.05.20250328.2cc0d7f"
CPE_NAME="cpe:/o:nixos:nixos:25.05"
DEFAULT_HOSTNAME=nixos
DOCUMENTATION_URL="https://nixos.org/learn.html"
HOME_URL="https://nixos.org/"
ID=nixos
ID_LIKE=""
IMAGE_ID=""
IMAGE_VERSION=""
LOGO="nix-snowflake"
NAME=NixOS
PRETTY_NAME="NixOS 25.05 (Warbler)"
SUPPORT_URL="https://nixos.org/community.html"
VARIANT=""
VARIANT_ID=installer
VENDOR_NAME=NixOS
VENDOR_URL="https://nixos.org/"
VERSION="25.05 (Warbler)"
VERSION_CODENAME=warbler
VERSION_ID="25.05"

[nixos@nixos:~]$ uname -a
Linux nixos 6.14.0 #1-NixOS SMP Mon Mar 24 14:02:41 UTC 2025 riscv64 GNU/Linux

[nixos@nixos:~]$ cat /proc/cpuinfo
processor       : 0
hart            : 3
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
hart            : 2
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

Test successful.
