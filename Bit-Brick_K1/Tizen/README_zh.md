# Tizen Snapshot Bit-Brick K1 测试报告

## 测试环境

### 系统信息

- 系统版本：Tizen-Unified-X riscv64 Snapshot 
- 下载链接：
  - boot 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-bpif3/
  - platform 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/
- 参考安装文档：https://docs.tizen.org/platform/developing/flashing-rpi/

### 硬件信息

- Bit-Brick K1
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

下载 boot 和 platform 镜像，无需解压

插入 SD 卡，运行刷写脚本：(`/dev/sdX` 请替换为你的 SD 卡设备名)
```bash
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/sdX -t bpif3 --format
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/sdX -b tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz  tizen-unified-x_20250917.211322_tizen-headless-riscv64.tar.gz  -t bpif3
```

### 登录系统

通过串口登录系统。

用户名：`root`

密码：`tizen`


## 实际结果

### 启动信息

### Boot Log

``` log
localhost login: root
Password:
[   84.026360] kauditd_printk_skb: 32 callbacks suppressed
[   84.026382] audit: type=1006 audit(946684929.212:16): pid=514 uid=0 subj=User::Shell old-auid=4294967295 auid=0 tty=ttyS0 old-ses=4294967295 ses=3 res=1
[   84.045883] audit: type=1300 audit(946684929.212:16): arch=c00000f3 syscall=64 success=yes exit=1 a0=4 a1=3ffb46d6e0 a2=1 a3=0 items=0 ppid=1 pid=514 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=ttyS0 ses=3 comm="login" exe="/usr/bin/login" subj=User::Shell key=(null)
[   84.072304] audit: type=1327 audit(946684929.212:16): proctitle=2F62696E2F6C6F67696E002D70002D2D
Welcome to Tizen
root:~> uname -a
Linux localhost 6.6.88-riscv-bpif3 #1 SMP PREEMPT Thu Sep 18 15:01:10 UTC 2025 riscv64 GNU/Linux
root:~> cat /etc/os-release
NAME=Tizen
VERSION="10.0.0 (Tizen10.0/Unified)"
ID=tizen
VERSION_ID=10.0.0
PRETTY_NAME="Tizen 10.0.0 (Tizen10.0/Unified)"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:10.0.0"
BUILD_ID=tizen-unified-x_20250918.035403_tizen-headless-riscv64
root:~> cat /proc/cpuinfo
processor       : 0
hart            : 0
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

root:~>
```

## 测试结论

系统正常启动，能够通过板载串口登录

