# openKylin 1.0.1 VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openKylin 1.0.1
- 下载链接：https://www.openkylin.top/downloads/index-cn.html
- 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
xz -d openKylin-1.0.1-visionfive2-riscv64.img.xz 
sudo dd if=openKylin-1.0.1-visionfive2-riscv64.img of=/dev/sdc bs=1M status=progress
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动 openKylin 镜像，选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### 登录系统

通过串口登录系统。

默认用户名：`openkylin`
默认密码：`openkylin$`

## 预期结果

系统正常启动，能够通过图形界面登录。

## 实际结果

系统正常启动，成功通过图形界面登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

```log
openkylin@openkylin:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

openkylin@openkylin:~$ uname -a
Linux openkylin 5.15.0 #1 SMP Fri Sep 1 11:22:00 CST 2023 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="1.0.1 (yangtze)"
VERSION_US="1.0.1 (yangtze)"
ID=openkylin
PRETTY_NAME="openKylin 1.0.1"
VERSION_ID="1.0.1"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=yangtze
PRODUCT_FEATURES=3
openkylin@openkylin:~$
```

屏幕录像（从刷写到启动）：

[![asciicast](https://asciinema.org/a/qoDqBWFEJlBPhIBva66HFGzd9.svg)](https://asciinema.org/a/qoDqBWFEJlBPhIBva66HFGzd9)