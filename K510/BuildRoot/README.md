# BuildRoot K510 测试报告

## 测试环境

### 操作系统信息

- 构建系统环境：Ubuntu 20.04.4 LTS in Docker
- 系统版本：v1.9
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

#### 拉取源码仓

```shell
git clone --depth=1 https://github.com/kendryte/k510_buildroot
```

#### 开始构建

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
make dl
make
```

注意，默认为单线程编译，耗时较久，请确保网络连接正常。

编译结束后，会在 `k510_buildroot/k510_crb_lp3_v1_2_defconfig/image/` 目录下生成 `sysimage-sdcard.img` 镜像。

#### 使用 dd 烧录镜像

注意，`/dev/sdc` 为存储卡所在位置。请根据实际情况修改。

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

插入 microSD 卡，确保板载 SW1 开关处于 microSD 卡启动位置：

| BOOT1  | BOOT0  | 启动方式   |
|--------|--------|------------|
| 0(ON)  | 0(ON)  | 串口       |
| 0(ON)  | 1(OFF) | microSD    |
| 1(OFF) | 0(ON)  | NAND Flash |
| 1(OFF) | 1(OFF) | eMMC       |

插入 USB Type-C 供电和 USB-UART 串口。接口分别位于开发板两侧，丝印为 `DC:5V` 和 `UART`。

（K510 板载了一颗 CH340 用于 USB-UART，可直接连接使用。UART 接口同时用作 USB 辅助供电，建议连接。）

将电源开关 `K1` 拨到 ON 位置，通过串口连接并登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[root@canaan ~ ]$ uname -a
Linux canaan 4.17.0 #1 SMP PREEMPT Fri Apr 12 18:13:44 CST 2024 riscv64 GNU/Linux
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

[![asciicast](https://asciinema.org/a/wdVYHHOcy5laeXA2tKewkqNRR.svg)](https://asciinema.org/a/wdVYHHOcy5laeXA2tKewkqNRR)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。