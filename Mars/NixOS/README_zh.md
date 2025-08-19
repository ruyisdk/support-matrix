# NixOS Milk-V Mars 测试报告

## 测试环境

### 硬件信息

- 开发板：Milk-V Mars (8GB RAM)
- 其他硬件：
  - USB 电源适配器和USB-A to C 或 C to C 线缆一条
  - microSD 卡一张
  - USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

### 操作系统信息

- 操作系统版本：NixOS 25.05 (Warbler) (Build ID: 20250328.2cc0d7f)
- 下载链接：<https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst>
- 参考安装文档：
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://github.com/NickCao/nixos-riscv>

## 安装步骤

### 刷写镜像

使用 `zstd` 命令解压镜像，并使用 `dd` 命令或 `balenaEtcher` 软件将镜像写入 microSD 卡。

其中，`/dev/sdX` 为存储卡对应设备。

```bash
wget https://hydra.nichi.co/build/1426425/download/1/nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst

zstd -d nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img.zst

sudo dd if=nixos-image-sd-card-25.05.20250328.2cc0d7f-riscv64-linux.img of=/dev/sdX bs=1M status=progress

sync
```

### 登录系统

通过串口登录系统。

默认用户名： `nixos` (自动登录)

默认无密码

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

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

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
