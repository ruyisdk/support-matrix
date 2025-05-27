# Alpine Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Alpine Linux 3.20.0_alpha20231219 (edge)
- 下载链接：<https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz>
- 参考安装文档：
  1. <https://milkv.io/zh/docs/mars/getting-started/boot>
  2. <https://arvanta.net/alpine/alpine-on-visionfive>

### 硬件信息

- Milk-V Mars (8GB RAM)
- USB 电源适配器和USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 解压并刷写镜像到 microSD 卡

使用 `xz` 解压镜像，并使用 `dd` 命令或者 `balenaEtcher` 软件将镜像写入 microSD 卡。（假定/dev/sdc为microSD 卡设备）

```bash
wget https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz

xz -d visionfive-v2-mmc.img.xz

sudo dd if=visionfive-v2-mmc.img of=/dev/sdc bs=1M status=progress

sync
```

### 登录系统

通过串口登录系统。

默认用户名：`root` （自动登入），没有密码

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
Welcome to Alpine Linux 3.20.0_alpha20231219 (edge)
Kernel 6.7.4-0-starfive on an riscv64 (ttyS0)

[press ENTER to login]
localhost login: root (automatic login)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

localhost:~# cat /etc/os-release
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.0_alpha20231219
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"

localhost:~# uname -a
Linux localhost 6.7.4-0-starfive #1-Alpine SMP PREEMPT_DYNAMIC Tue, 06 Feb 2024 12:21:03 +0000 riscv64 Linux

localhost:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

localhost:~#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
