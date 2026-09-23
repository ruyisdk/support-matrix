# BuildRoot K510 测试报告

## 测试环境

### 操作系统信息

- 构建系统环境：Ubuntu 20.04.4 LTS in Docker
- 系统版本：Buildroot 2020.02.11
- 参考安装文档：https://github.com/kendryte/k510_buildroot

### 硬件信息

- Canaan K510 CRB-V1.2 KIT
- USB 电源适配器一个
- USB-A to C 两条（开发板已附带，一条用作供电，另一条用作 USB-UART 以及辅助供电）
- microSD 卡一张（容量 ≥ 1GiB 即可，默认生成的镜像大小为 512MiB）

## 安装步骤

### 构建系统镜像

#### 安装 Docker 

请参考各发行版的文档，或者 Docker 官网文档进行安装。

确认 Docker 可正常使用：

```
docker --version
```

#### 拉取源码仓库

```shell
git clone --depth=1 https://github.com/kendryte/k510_buildroot
```

#### 开始构建

进入 Docker 构建环境：

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
# 在容器内执行：
make dl
make
# 构建完成后退出容器：
exit
```

注意，默认为单线程编译，耗时较久，请确保网络连接正常。

查找生成的系统镜像：

```shell
find k510_buildroot/k510_crb_lp3_v1_2_defconfig \
-name "sysimage-sdcard.img" -type f
```

本次实际生成的镜像为：

```shell
k510_buildroot/k510_crb_lp3_v1_2_defconfig/images/sysimage-sdcard.img
```

#### 使用 dd 烧录镜像

注意，`/dev/sdX` 为 microSD 卡对应的设备，请根据实际设备路径修改。

```shell
sudo dd if=k510_buildroot/k510_crb_lp3_v1_2_defconfig/images/sysimage-sdcard.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

插入 microSD 卡，确保板载 SW1 开关处于 microSD 卡启动位置：

| BOOT1  | BOOT0  | 启动方式   |
| ------ | ------ | ---------- |
| 0(ON)  | 0(ON)  | 串口       |
| 0(ON)  | 1(OFF) | microSD    |
| 1(OFF) | 0(ON)  | NAND Flash |
| 1(OFF) | 1(OFF) | eMMC       |

连接开发板：

- `DC:5V`：供电
- `UART`：USB-UART 串口

确认串口设备，例如：

```
/dev/ttyUSB0
```

首次使用 minicom 时配置串口：

```
sudo minicom -s
```

设置：

```
Serial Device          : /dev/ttyUSB0
Bps/Par/Bits            : 115200 8N1
Hardware Flow Control   : No
```

打开串口：

```
sudo minicom
```

将电源开关 `K1` 拨至 `ON`，等待系统启动。

登录信息：

```
用户名：root
密码：空，直接回车
```

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[root@canaan ~ ]$ uname -a
Linux canaan 4.17.0 #1 SMP PREEMPT Tue Jul 14 18:27:09 CST 2026 riscv64 GNU/Linx
[root@canaan ~ ]$ cat /etc/os-release
NAME=Buildroot
VERSION=-g2ce01d0
ID=buildroot
VERSION_ID=2020.02.11
PRETTY_NAME="Buildroot 2020.02.11"
[root@canaan ~ ]$ cat /proc/cpuinfo
hart    : 0
isa     : rv64i2p0m2p0a2p0f2p0d2p0c2p0xv5-0p0
mmu     : sv39

hart    : 1
isa     : rv64i2p0m2p0a2p0f2p0d2p0c2p0xv5-0p0
mmu     : sv39

[root@canaan ~ ]$
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/1264225.svg)](https://asciinema.org/a/1264225)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
