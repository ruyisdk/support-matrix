# openEuler Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler-23.09-V1

需要自行构建。

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- TF 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 构建步骤

### 构建 Buildroot

请参阅 [milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk)。

在第一次构建完成目标 `milkv_duo256m_sd` 后，修改 `build/boards/cv181x/cv1812cp_milkv_duo256m_sd/linux/cvitek_cv1812cp_milkv_duo256m_sd_defconfig`

增加下列行。

```
CONFIG_CGROUPS=y
CONFIG_CGROUP_FREEZER=y
CONFIG_CGROUP_PIDS=y
CONFIG_CGROUP_DEVICE=y
CONFIG_CPUSETS=y
CONFIG_PROC_PID_CPUSET=y
CONFIG_CGROUP_CPUACCT=y
CONFIG_PAGE_COUNTER=y
CONFIG_MEMCG=y
CONFIG_CGROUP_SCHED=y
CONFIG_NAMESPACES=y
CONFIG_OVERLAY_FS=y
CONFIG_AUTOFS4_FS=y
CONFIG_SIGNALFD=y
CONFIG_TIMERFD=y
CONFIG_EPOLL=y
CONFIG_IPV6=y
CONFIG_FANOTIFY=y
```

然后再构建一次，获得镜像 `out/milkv-duo256m-sd-20240924-2106.img`。

### 更新根文件系统

为了防止权限问题，请考虑切换到根用户操作。

#### 下载根文件系统

先从 [ISCAS Mirror](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/) 下载根文件系统。

```
wget https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/openeuler-rootfs.tar.gz
```

#### 挂载镜像

```
sudo losetup -f
```

输出 `/dev/loop0`，下文请根据情况修改。缺少环设备需要新建。

为镜像扩容。

```
qemu-img resize out/milkv-duo256m-sd-20240924-2106.img +10G
```

挂载镜像到环设备上。

```
losetup -P loop0 out/milkv-duo256m-sd-20240924-2106.img
```

扩容分区。

```
sudo fdisk /dev/loop0

# 以下在 fdisk 中
d
2
n
p
2
# 最开始的扇区，保持默认值
# 最后的一个扇区，保持默认值
w

# 以下应回到bash
sudo mkfs.ext4 /dev/loop0p2
```

挂载分区到目录。

```
mkdir /mnt/duo-rootfs
cd /mnt/duo-rootfs
mount /dev/loop0p2 /mnt/duo-rootfs
```

删除原来的一切。

```
rm -rf ./*
```

将根文件系统解压到此处。

```
tar -xvf openeuler-rootfs.tar.gz -C .
```

### 卸载镜像

```
umount /dev/loop0p2
losetup -d /dev/loop0
```

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
dd if=milkv-duo256m-sd-20240924-2106.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

- 默认账号：`root`
- 默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

```
openEuler 23.09
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
Password: 


Welcome to 5.10.4-tag-

System information as of time:  Mon Sep 18 08:01:13 CST 2023

System load:    3.04
Processes:      70
Memory used:    43.4%
Swap used:      0.0%
Usage On:       19%
Users online:   1

[root@openeuler-riscv64 ~]# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。