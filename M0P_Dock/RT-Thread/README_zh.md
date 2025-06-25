# RT-Thread M0P Dock 测试报告

## 测试环境

### 操作系统信息
- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/master/bsp/bouffalo_lab/README.md
- 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
- 工具链：https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### 硬件信息

- Sipeed M0P Dock (BL618)
- USB to UART 调试器一个
- USB C to C 线缆一根

## 构建步骤

以下步骤在 Arch Linux 上测试通过，但应适用各大主流 Linux 发行版。

### 准备系统环境

获取工具链并配置：
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

自行更改以下路径：
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

获取依赖：
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
# 在 Arch Linux 上为：sudo pacman -S scons dtc ncurses
```

### 拉取源码并编译固件

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/bouffalo_lab/bl61x
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
```

Choose Module 请选择 `M0P Module`。
生成的固件文件位于 `./rtthread.bin`。


### 烧写固件

按住BOOT按钮并上电即进入烧写模式。

下载烧录工具后使用对应系统的工具烧录。请确保所使用的 BLDevCube 版本为 1.8.3。

进入 IOT 页面，按如下所示设置参数：

选中 "Single Download", 地址 `0x0`， 选择 `rtthread.bin`。选择对应的 UART 接口，波特率 2000000。点击 "Create & Download" 进行刷写。

![](iot.png)

### 登录系统

分别连接 Pin 21, 22 到 UART 调试器的 RX, TX。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log

 \ | /
- RT -     Thread Operating System
 / | \     5.2.1 build Jun 20 2025 22:31:12
 2006 - 2024 Copyright by RT-Thread team
Hello, RISC-V!
msh />ps
thread   pri  status      sp     stack size max used left tick   error  tcb addr
-------- ---  ------- ---------- ----------  ------  ---------- ------- ----------
tshell    20  running 0x00000250 0x00001000    25%   0x00000007 OK      0x62fe4160
mmcsd_de  22  suspend 0x00000220 0x00000800    26%   0x00000013 EINTRPT 0x62fe113c
tidle0    31  ready   0x00000130 0x00000800    22%   0x00000004 OK      0x62fe1b18
timer      4  suspend 0x00000210 0x00000800    25%   0x00000006 EINTRPT 0x62fe2600
msh />

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。