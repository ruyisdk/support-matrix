# openSUSE Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openSUSE Tumbleweed 20250527
- 下载链接：<https://downloadcontent.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw.xz>
- 参考安装文档：
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://en.opensuse.org/HCL:VisionFive2>

### 硬件信息

- Milk-V Mars (8GB RAM)
- USB 电源适配器和USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 解压并刷写镜像到 microSD 卡

使用 `xz` 解压镜像，并使用 `dd` 命令或者 `balenaEtcher` 软件将镜像写入 microSD 卡。（假定/dev/sdX为microSD 卡设备）

```bash
xz -d openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw.xz

sudo dd if=openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw of=/dev/sdX bs=1M status=progress

sync
```

### 引导模式选择

Milk-V Mars 在硬件版本V1.2后提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 openSUSE 镜像，选择 microSD card 启动模式（即：`GPIO_0 = 1`, `GPIO_1 = 0`）。

### 登录系统

通过串口登录系统。

默认用户名: `root`

默认密码: `linux`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
Welcome to openSUSE Tumbleweed 20250527 - Kernel 6.15.0-112-default (ttyS0).

end0: 192.168.137.233 fe80::490c:948d:eb6e:60bf
wlP1p1s0:


localhost login: root
Password:
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.15.0-112-default #1 SMP PREEMPT_DYNAMIC Mon May 26 04:54:06 UTC 2025 (ed9faca) riscv64 riscv64 riscv64 GNU/Linux

localhost:~ # cat /etc/os-release
NAME="openSUSE Tumbleweed"
# VERSION="20250527"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20250527"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
# CPE 2.3 format, boo#1217921
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20250527:*:*:*:*:*:*:*"
#CPE 2.2 format
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20250527"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"

localhost:~ # cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

localhost:~ #
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
