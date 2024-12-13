# RT-Thread M0sense 测试报告

## 测试环境

### 操作系统信息
- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/master/bsp/bouffalo_lab/README.md
- 工具链：https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### 硬件信息

- Sipeed M0sense (BL702)
- USB A to C 或 C to C 线缆一根
- 杜邦线一根

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
cd rt-thread/bsp/bouffalo_lab/bl70x
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
```
生成的固件文件位于 `./rtthread.bin`。


### 烧写固件

将 M0sense 上的 BOOT 引脚与 3V 引脚用杜邦线短接，上电即进入烧写模式。同时连接串口以便观察输出。
烧写固件至开发板（板载有串口设备）：
```shell
cd ../
sudo ./bouffalo_flash_cube.sh bl702 /dev/ttyACM0
```

（该脚本会自动检测并下载 `bouffalo_flash_cube` 工具至编译目录）

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

注意 `msh` 输出可能不立即回显，属正常现象。
```log
Now can [init] goio set o[rgbled_task] start loop

Now: command not found.
bouffalolab />
bouffalolab />help
shell commands list:
memtrace
help

bouffalolab />memtrace
write memory: 0x42000000 0xabcd 10
read memory: 0x42000000 10
bouffalolab />hello
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。