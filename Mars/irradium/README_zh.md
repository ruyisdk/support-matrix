# irradium 3.8 Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：irradium 3.8
- 下载链接：<https://mirror.serverion.com/irradium/images/visionfive_2/irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img.zst>
- 参考安装文档：
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://mirror.serverion.com/irradium/images/visionfive_2/README.TXT>

### 硬件信息

- Milk-V Mars (8GB RAM)
- USB 电源适配器和USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 解压并刷写镜像到 microSD 卡

使用 `zstd` 解压镜像，并使用 `dd` 命令或者 `balenaEtcher` 软件将镜像写入 microSD 卡。（假定/dev/sdc为microSD 卡设备）

```bash
zstd -d irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img.zst

sudo dd if=irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img of=/dev/sdX bs=1M status=progress

sync
```

### 引导模式选择

Milk-V Mars 在硬件版本V1.2后提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 irradium 镜像，选择 SPI Flash 启动模式（即：`GPIO_0 = 0`, `GPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件。

### 登录系统

通过串口登录系统。

默认用户名： `root` (自动登录)

默认无密码

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
irradium  (visionfive-2) (ttyS0)

visionfive-2 login: root
You are required to change your password immediately (administrator enforced).
New password:
Retype new password:
 _                   _  _
|_| ___  ___  ___  _| ||_| _ _  _____
| ||  _||  _|| .'|| . || || | ||     |
|_||_|  |_|  |__,||___||_||___||_|_|_|
      _       _            ___  _              ___
 _ _ |_| ___ |_| ___  ___ |  _||_| _ _  ___   |_  |
| | || ||_ -|| || . ||   ||  _|| || | || -_|  |  _|
 \_/ |_||___||_||___||_|_||_|  |_| \_/ |___|  |___|

# uname -a
Linux visionfive-2 6.12.28 #1 SMP PREEMPT Mon May 12 01:22:37 EEST 2025 riscv64 GNU/Linux

# cat /etc/os-release
NAME=irradium
VERSION="3.8"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org/"
BUG_REPORT_URL="https://irradium.org/bugs/"

# cat /proc/cpuinfo
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

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
