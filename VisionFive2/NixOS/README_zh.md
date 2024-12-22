# NixOS VisionFive 2 测试报告

## 测试环境

### 操作系统信息

- 系统版本：25.05.20241121
- 源码链接: https://github.com/NickCao/nixos-riscv
- 参考安装文档: https://github.com/NickCao/nixos-riscv/README.md

### 硬件信息

- StarFive VisionFive 2
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- microSD 读卡器一个
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 编译镜像

如果主机运行 NixOS, 使用 `nix build ".#hydraJobs.visionfive2"` 编译镜像即可。
对于其他发行版，不建议直接安装并使用 `nix` 包管理器，推荐使用 Nix 的官方 Docker 镜像： 
```shell
docker run -ti -v .:/work ghcr.io/nixos/nix
```

在 Docker 容器中：

```shell
echo "max-jobs = auto" >> /etc/nix/nix.conf # 使用多核编译
echo "substituters = https://mirrors.tuna.tsinghua.edu.cn/nix-channels/store https://cache.nixos.org/" >> /etc/nix/nix.conf # 更换镜像源
cd /work
nix build ".#hydraJobs.visionfive2" --extra-experimental-features nix-command --extra-experimental-features flakes
```

生成的镜像位于 `./result/sd-image/` 目录下，文件名形如 `nixos-sd-image-25.05.20241121.0039986-riscv64-linux-starfive-visionfive2.img.zst`。

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

无密码,初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
<<< Welcome to NixOS 25.05.20241121.0039986 (riscv64) - ttyS0 >>>
The "nixos" and "root" accounts have empty passwords.

To log in over ssh you must set a password for either "nixos" or "root"
with `passwd` (prefix with `sudo` for "root"), or add your public key to
/home/nixos/.ssh/authorized_keys or /root/.ssh/authorized_keys.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)


[nixos@nixos:~]$ uname -a
Linux nixos 6.12.0 #1-NixOS SMP Sun Nov 17 22:15:08 UTC 2024 riscv64 GNU/Linux

[nixos@nixos:~]$ cat /etc/os-release 
ANSI_COLOR="1;34"
BUG_REPORT_URL="https://github.com/NixOS/nixpkgs/issues"
BUILD_ID="25.05.20241121.0039986"
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
SUPPORT_END="2025-06-30"
SUPPORT_URL="https://nixos.org/community.html"
VARIANT=""
VARIANT_ID=installer
VENDOR_NAME=NixOS
VENDOR_URL="https://nixos.org/"
VERSION="25.05 (Warbler)"
VERSION_CODENAME=warbler
VERSION_ID="25.05"

[nixos@nixos:~]$ cat /proc/cpuinfo
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

[nixos@nixos:~]$
```

实测 USB 驱动也可正常使用：
```log
[nixos@nixos:~]$ [  681.045954] usb 2-4: new SuperSpeed USB device number 2 using xhci_hcd
[  681.068527] usb-storage 2-4:1.0: USB Mass Storage device detected
[  681.079456] scsi host0: usb-storage 2-4:1.0
[  682.110860] scsi 0:0:0:0: Direct-Access      USB      SanDisk 3.2Gen1 1.00 PQ: 0 ANSI: 6
[  682.124874] sd 0:0:0:0: [sda] 60088320 512-byte logical blocks: (30.8 GB/28.7 GiB)
[  682.133356] sd 0:0:0:0: [sda] Write Protect is off
[  682.138907] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[  682.182460]  sda: sda1
[  682.185238] sd 0:0:0:0: [sda] Attached SCSI removable disk
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
