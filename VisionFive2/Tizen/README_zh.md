# Tizen Snapshot VisionFive 2 测试报告

## 测试环境

### 系统信息

- 系统版本：Tizen-Unified-X riscv64 Snapshot 20250917
- 下载链接：
  - boot 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-vf2/tizen-unified-x_20250917.211322_tizen-boot-riscv64-vf2.tar.gz
  - platform 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
- 参考安装文档：https://docs.tizen.org/platform/developing/flashing-rpi/

### 硬件信息

- StarFive VisionFive2
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

下载 boot 和 platform 镜像：

```bash
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-vf2/tizen-unified-x_20250917.211322_tizen-boot-riscv64-vf2.tar.gz
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
# or use headed image instead of headless:
# wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headed-riscv64/tizen-unified-x_20250918.035403_tizen-headed-riscv64.tar.gz

```

插入 SD 卡，运行刷写脚本：(`/dev/mmcblk0` 请替换为你的 SD 卡设备名)
```bash
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -t vf2 --format
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -b tizen-unified-x_20250917.211322_tizen-boot-riscv64-vf2.tar.gz  tizen-unified-x_20250917.211322_tizen-headless-riscv64.tar.gz  -t vf2
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置，可参考 StarFive [官方文档](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html)。

开发板本体上亦有丝印标注。

为了启动 Tizen，选择 SDIO3.0 模式（即：`RGPIO_0 = 1`, `RGPIO_1 = 0`）。

### 登录系统

通过串口登录系统。

用户名：`root`

密码：`tizen`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[   20.335661] file system registered
[   20.374657] read descriptors
[   20.390855] read strings
[   20.439559] read descriptors
[   20.445429] read strings

localhost login: root
Password:
[   78.562452] kauditd_printk_skb: 32 callbacks suppressed
[   78.562461] audit: type=1006 audit(978307277.740:16): pid=396 uid=0 subj=User::Shell old-auid=4294967295 auid=0 tty=ttyS0 old-ses=4294967295 ses=3 res=1
Welcome to Tizen[   78.581412] audit: type=1300 audit(978307277.740:16): arch=c00000f3 syscall=64 success=yes exit=1 a0=4 a1=3fd51276e0 a2=1 a3=0 items=0 ppid=1 pid=396 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=ttyS0 ses=3 comm="login" exe="/usr/bin/login" subj=User::Shell key=(null)

[   78.608409] audit: type=1327 audit(978307277.740:16): proctitle=2F62696E2F6C6F67696E002D70002D2D
root:~> cat /etc/os-release
NAME=Tizen
VERSION="10.0.0 (Tizen10.0/Unified)"
ID=tizen
VERSION_ID=10.0.0
PRETTY_NAME="Tizen 10.0.0 (Tizen10.0/Unified)"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:10.0.0"
BUILD_ID=tizen-unified-x_20250917.211322_tizen-headless-riscv64
root:~> uname -a
Linux localhost 6.6.17-riscv-visionfive2 #1 SMP Wed Sep 17 22:13:06 UTC 2025 riscv64 GNU/Linux

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。