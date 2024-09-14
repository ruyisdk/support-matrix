# Armbian 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 下载链接：https://mirrors.tuna.tsinghua.edu.cn/armbian-releases/bananapif3/archive/Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz
- 参考安装文档：https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -kd Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz
sudo dd if=/path/to/Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

首次启动创建用户

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/aZN2jn6DdEN0clVNhLDFG5Ann.svg)](https://asciinema.org/a/aZN2jn6DdEN0clVNhLDFG5Ann)

```log
uname -a&& echo zE5YXe0d 
uname -a&& echo zE5YXe0d 

Linux bananapif3 6.1.15-legacy-spacemit #1 SMP Fri Aug  2 07:47:59 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
zE5YXe0d
root@bananapif3:~# cat /etc/os-release&& echo Sqndhdce 
cat /etc/os-release&& echo Sqndhdce 

PRETTY_NAME="Armbian 24.8.1 noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://github.com/armbian/build"
SUPPORT_URL="https://community.armbian.com/"
BUG_REPORT_URL="https://github.com/armbian/community/issues"
PRIVACY_POLICY_URL="https://duckduckgo.com/"
UBUNTU_CODENAME=noble
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian 24.8.1 noble"
Sqndhdce
root@bananapif3:~# cat /proc/cpuinfo&& echo W8tQXFQR 
cat /proc/cpuinfo&& echo W8tQXFQR 

processor	: 0
hart		: 0
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 1
hart		: 1
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 2
hart		: 2
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 3
hart		: 3
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 4
hart		: 4
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 5
hart		: 5
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 6
hart		: 6
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 7
hart		: 7
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

W8tQXFQR
root@bananapif3:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
