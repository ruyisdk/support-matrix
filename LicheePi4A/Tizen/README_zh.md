# Tizen Snapshot Lichee Pi 4A 测试报告

## 测试环境

### 系统信息

- 系统版本：Tizen-Unified-X riscv64 Snapshot 20250917
- 下载链接：
  - boot 镜像 (8GB 版本)：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-lpi4a-8g/tizen-unified-x_20250918.035403_tizen-boot-riscv64-lpi4a-8g.tar.gz
  - boot 镜像 (16GB 版本)：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-lpi4a-16g/tizen-unified-x_20250918.035403_tizen-boot-riscv64-lpi4a-16g.tar.gz
  - platform 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
- 参考安装文档：https://docs.tizen.org/platform/developing/flashing-rpi/

### 硬件信息

- Lichee Pi 4A
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

安装 `pv`:

```bash
sudo apt-get install pv
```

获取 SD 卡刷写脚本：

```bash
git clone git://review.tizen.org/git/platform/kernel/tizen-fusing-scripts -b tizen
cd tizen-fusing-scripts
```

下载 boot 和 platform 镜像，无需解压：

```bash
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-lpi4a-8g/tizen-unified-x_20250918.035403_tizen-boot-riscv64-lpi4a-8g.tar.gz
# For 16GB variants:
# http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-lpi4a-16g/tizen-unified-x_20250918.035403_tizen-boot-riscv64-lpi4a-16g.tar.gz
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
# or use headed image instead of headless:
# wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headed-riscv64/tizen-unified-x_20250918.035403_tizen-headed-riscv64.tar.gz

```

插入 SD 卡，运行刷写脚本：(`/dev/sdX` 请替换为你的 SD 卡设备名)
```bash
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/sdX -t lpi4a --format
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/sdX -b tizen-unified-x_20250918.035403_tizen-boot-riscv64-lpi4a-8g.tar.gz  tizen-unified-x_20250917.211322_tizen-headless-riscv64.tar.gz  -t lpi4a
```

### 登录系统

通过串口登录系统。

用户名：`root`

密码：`tizen`

## 实际结果

### 启动信息

```log

root:~> uname -a
Linux localhost 6.6.20-riscv-lpi4a #1 SMP PREEMPT Thu Sep 18 04:42:17 UTC 2025 riscv64 GNU/Linux
root:~> cat /etc[  218.653133] PVR_K:(Error):  5308: PVRSRVDeviceServicesOpen: Driver already in bad state. Device open failed. [487]
/[  219.664122] PVR_K:(Error):  5308: PVRSRVDeviceServicesOpen: Driver already in bad state. Device open failed. [487]
[  219.683642] enlightenment[5308]: unhandled signal 11 code 0x1 at 0x0000000000000008 in libgallium-24.3.4.so[3f8c57a000+de6000]
[  219.695304] CPU: 3 PID: 5308 Comm: enlightenment Tainted: G           O       6.6.20-riscv-lpi4a #1
[  219.704414] Hardware name: Sipeed Lichee Pi 4A (DT)
[  219.709350] epc : 0000003f8c5e1d2c ra : 0000003f8c5e1dc2 sp : 0000003fe1311460
[  219.716627]  gp : 0000002ac7148264 tp : 0000003f95a36780 t0 : ffffffffee50b442
[  219.723886]  t1 : 0000003f8c5dce6c t2 : 0000000050d43f50 s0 : 0000002ac7273460
[  219.731141]  s1 : 0000000000000000 a0 : 0000000000000000 a1 : 0000000000000000
[  219.738398]  a2 : 8080808080808080 a3 : 0000000000000000 a4 : fefeff0001000003
[  219.745678]  a5 : 0000000000000001 a6 : 0000003f8ccc0558 a7 : 00000000000006e2
[  219.752950]  s2 : 0000003f8d3c1179 s3 : 0000000000000000 s4 : 0000002ac7273460
[  219.760211]  s5 : 0000002ac726ee00 s6 : 0000000000000001 s7 : 0000002ac72734f8
[  219.767465]  s8 : 0000000000000000 s9 : 0000002ac726b7b0 s10: 0000000000000000
[  219.774718]  s11: 0000002ae471e540 t3 : 0000003f96ee53e6 t4 : 000000001f440000
[  219.781971]  t5 : ffffffff9e3779b1 t6 : ffffffff85ebca77
[  219.787314] status: 8000000200006020 badaddr: 0000000000000008 cause: 000000000000000d
[  219.795655] audit: type=1701 audit(219.648:70): auid=4294967295 uid=0 gid=0 ses=4294967295 subj=System pid=5308 comm="enlightenment" exe="/usr/bin/enlightenment" sig=11 res=1
os-release
NAME=Tizen
VERSION="10.0.0 (Tizen10.0/Unified)"
ID=tizen
VERSION_ID=10.0.0
PRETTY_NAME="Tizen 10.0.0 (Tizen10.0/Unified)"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:10.0.0"
BUILD_ID=tizen-unified-x_20250918.035403_tizen-headed-riscv64
root:~> cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

```

## 测试结论

系统正常启动，能够通过板载串口登录
