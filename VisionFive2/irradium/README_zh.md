# irradium VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：irradium 3.7
- 下载链接：https://dl.irradium.org/irradium/images/visionfive_2/
- 参考安装文档：https://dl.irradium.org/irradium/images/visionfive_2/README.TXT

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```bash
zstd -d irradium-3.7-riscv64-core-visionfive_2-6.13.1-build-20250208.img.zst
sudo dd if=irradium-3.7-riscv64-core-visionfive_2-6.13.1-build-20250208.img of=/dev/<your-device> bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
无密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

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

# 
# uname -a
Linux visionfive-2 6.13.1 #4 SMP PREEMPT Sat Feb  8 00:21:02 EET 2025 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=irradium
VERSION="3.7"
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

# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
