# openEuler RISC-V 24.03 LTS Pioneer 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler RISC-V 24.03 LTS (Image, Legacy 启动)
- 下载链接：[openEuler 官网](https://www.openeuler.org/en/download/archive/detail/?version=openEuler%2024.03%20LTS) (Choose: riscv64 -> 嵌入式 -> SG2042 -> 选择镜像仓)
- 参考安装文档：[Installing on Pioneer Box - openEuler Docs](https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-Pioneer1.3.html)

### 硬件信息

- Milk-V Pioneer Box v1.3
- microSD 卡一张（或 NVMe SSD + NVMe SSD 转 USB 硬盘盒）
- USB Type-C 线缆一条（用来连接板载串口）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡或 NVMe SSD

下载系统镜像，解压，使用 `dd` 烧录至 microSD 卡或者 NVMe SSD。

如果您在使用 Windows，推荐使用 Rufus 或 Etcher 这类工具进行烧写。

将下面的 `/dev/sda` 替换成真实硬盘位置。

```shell
unzip openEuler-24.03-LTS-riscv64-sg2042.img.zip
sudo wipefs -af /dev/sda
sudo dd if=openEuler-24.03-LTS-riscv64-sg2042.img of=/dev/sda bs=1M status=progress
sudo eject /dev/sda
```

### 登录系统

在 openEuler Docs 中写到：

> `Image` 版本使用者：
> 
> 由于当前出厂固件的局限性，设备启动时 `RISC-V` 串口回显并不完整，操作系统未加载完成时串口输出即会关闭。需将显卡插入 `PCIe` 槽位并连接显示器才能观察到完整的启动过程。

因此，我们将使用 SSH 而不是串口登录系统。

可在路由器上检查机器 IP。

或者也可以连接显示器、键盘、鼠标，直接在机器上登录。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，可通过 SSH 登录。

## 实际结果

系统正常启动，成功通过 SSH 登录。

### 启动信息

```log
Authorized users only. All activities may be monitored and reported.


Welcome to 6.6.0-27.0.0.31.oe2403.riscv64

System information as of time:  Mon Jul  8 14:30:48 CST 2024

System load:    1.30
Memory used:    .6%
Swap used:      0.0%
Usage On:       14%
IP address:     10.0.0.12
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="24.03 (LTS)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS)"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ cat /etc/o
openEuler-latest     openEuler_security/  opensc-riscv64.conf  os-release           
openEuler-release    openldap/            opt/                 
[openeuler@openeuler-riscv64 ~]$ cat /etc/openEuler-release 
openEuler release 24.03 (LTS)
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.6.0-27.0.0.31.oe2403.riscv64 #1 SMP Fri May 24 21:52:58 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo 
processor       : 0
hart            : 3
isa             : rv64imafdcv_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

...

[openeuler@openeuler-riscv64 ~]$
```

asciinema 录屏（从启动时串口输出到 SSH 登录）：

[![asciicast](https://asciinema.org/a/ffNh01g1dltQqIOwGRl4Re9ri.svg)](https://asciinema.org/a/ffNh01g1dltQqIOwGRl4Re9ri)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。