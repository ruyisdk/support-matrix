# openCloudOS-Stream 23 Pioneer 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openCloudOS-Stream 23
- 下载链接：[https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/](https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/)
  - 固件: [https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20241230/](https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20241230/)

### 硬件信息

- Milk-V Pioneer Box v1.3
- microSD 卡一张
- USB Type-C 数据线一根（用于连接板载串口）

## 安装步骤

### 刷写镜像

请下载uefi版本的镜像：[ocs_developer_sdcard-uefi.img.xz](https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/ocs_developer_sdcard-uefi.img.xz)

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -d ocs_developer_sdcard-uefi.img.xz
dd if=ocs_developer_sdcard-uefi.img of=/dev/yout-device bs=4M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`riscv666!`

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

*注：uefi的grub启动可能较慢，需要耐心等待*

```log
User 'riscv' with password 'riscv666!' in 'wheel' and 'mock' groups
is provided.
To install new packages use 'dnf install ...'
To upgrade disk image use 'dnf upgrade --best'
If DNS isn’t working, try editing ‘/etc/yum.repos.d/OpenCloudOS-Stream.repo’.
riscv64 login: riscv
Password:
[riscv@riscv64 ~]$ cat /etc/os-release
NAME="OpenCloudOS Stream"
VERSION="23"
RELEASE="2410"
ID="opencloudos"
ID_LIKE="opencloudos"
VERSION_ID="23"
PLATFORM_ID="platform:ocs23"
PRETTY_NAME="OpenCloudOS Stream 23"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:opencloudos:opencloudos:23"
HOME_URL="https://www.opencloudos.org/"
BUG_REPORT_URL="https://bugs.opencloudos.tech/"
[riscv@riscv64 ~]$ uname -a
Linux riscv64.developer.ocs23 6.6.68 #1 SMP Thu Apr 10 17:26:47 CST 2025 riscv64 riscv64 riscv64 GNU/Linux
[riscv@riscv64 ~]$ lscpu
Architecture:          riscv64
Byte Order:          Little Endian
CPU(s):                64
On-line CPU(s) list: 0-63
NUMA:
NUMA node(s):        4
NUMA node0 CPU(s):   0-7,16-23
NUMA node1 CPU(s):   8-15,24-31
NUMA node2 CPU(s):   32-39,48-55
NUMA node3 CPU(s):   40-47,56-63         
```

串口日志（从刷写系统到启动系统）：

[![asciicast](https://asciinema.org/a/GWK8TtUXpzK4IsTvCNY4Vng9X.svg)](https://asciinema.org/a/GWK8TtUXpzK4IsTvCNY4Vng9X)

## 测试结论

测试成功。