# RT-Thread MangoPi MQ 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/bigmagic123/d1-nezha-rtthread
- 参考安装文档：https://github.com/bigmagic123/d1-nezha-rtthread

### 硬件信息

- MangoPi MQ
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

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
git clone --depth=1 https://github.com/bigmagic123/d1-nezha-rtthread.git
cd d1-nezha-rtthread/bsp/d1-nezha
scons -c
scons -j$(nproc) --verbose
```

生成的固件文件位于 `./rtthread.bin`。

### 通过 FEL 刷写固件

安装 [xfel](https://github.com/xboot/xfel). 如在 Arch Linux 下可通过 AUR 获取：`paru -S xfel`

通过 USB-C 线连接到开发板的 OTG 接口。

使用 `xfel` 发送固件：
```shell
xfel ddr f133
xfel write 0x40000000 rtthread.bin
xfel exec 0x40000000
```

观察串口输出。

TX, RX 分别为板子底部 (P3) 第7, 8号引脚。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

```log
ZQ value = 0x2f***********
get_pmu_exist() = 4294967295
ddr_efuse_type: 0xb
[AUTO DEBUG] single rank and full DQ!
ddr_efuse_type: 0xb
[AUTO DEBUG] rank 0 row = 13
[AUTO DEBUG] rank 0 bank = 4
[AUTO DEBUG] rank 0 page size = 2 KB
DRAM BOOT DRIVE INFO: %s
DRAM CLK = 528 MHz
DRAM Type = 2 (2:DDR2,3:DDR3)
DRAMC read ODT  off.
DRAM ODT off.
ddr_efuse_type: 0xb
DRAM SIZE =64 M
DRAM simple test OK.
[I/I2C] I2C bus [i2c0] registered
heap: [0x403482e1 - 0x435482e1]

 \ | /
- RT -     Thread Operating System
 / | \     4.1.0 build Jun 20 2025 15:28:00
 2006 - 2021 Copyright by rt-thread team
[I/touch] rt_touch init success
[I/gt911] touch device gt911 init success
file system initialization done!
Hello RISC-V!
msh />help
RT-Thread shell commands:
test_i2c         - test i2c
test_lcd         - test lcd
test_thead_custo - test thead custom
reboot           - reboot system...
memcheck         - check memory data
memtrace         - dump memory trace information
list_fd          - list file descriptor
help             - RT - Thread shell help.
ps               - List threads in the system.
free             - Show the memory usage in the system.
ls               - List information about the FILEs.
cp               - Copy SOURCE to DEST.
mv               - Rename SOURCE to DEST.
cat              - Concatenate FILE(s)
rm               - Remove(unlink) the FILE(s).
cd               - Change the shell working directory.
pwd              - Print the name of the current working directory.
mkdir            - Create the DIRECTORY.
mkfs             - format disk with file system
mount            - mount <device> <mountpoint> <fstype>
umount           - Unmount device from file system
df               - disk free
echo             - echo string to file
tail             - print the last N - lines data of the given file
hello            - say hello world
clear            - clear the terminal screen
version          - show RT - Thread version information
list_thread      - list thread
list_sem         - list semaphore in system
list_event       - list event in system
list_mutex       - list mutex in system
list_mailbox     - list mail box in system
list_msgqueue    - list message queue in system
list_mempool     - list memory pool in system
list_timer       - list timer in system
list_device      - list device in system
list             - list all commands in system

msh />test_thead_custom
aa is 3077
msh />ps
thread               pri  status      sp     stack size max used left tick  error
-------------------- ---  ------- ---------- ----------  ------  ---------- ---
tshell                20  running 0x000002f8 0x00002800    18%   0x00000004 000
sys_work              23  suspend 0x00000288 0x00001000    15%   0x0000000a 000
mmcsd_detect          22  suspend 0x000002e8 0x00002800    07%   0x00000014 000
tidle0                31  ready   0x00000620 0x00004000    10%   0x00000015 000
timer                  4  suspend 0x00000278 0x00004000    04%   0x00000009 000
main                  10  suspend 0x000002f8 0x00004000    10%   0x0000000f 000
msh />

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。