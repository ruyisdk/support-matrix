# RT-Thread Smart Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 源码链接：
  - https://github.com/RT-Thread/rt-thread
  - https://github.com/RT-Thread/userapps
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
   - 工具链：https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 构建步骤

以下步骤在 Arch Linux 上测试通过，但应适用各大主流 Linux 发行版。

### 拉取源码并编译固件

获取工具链并配置：
```bash
wget https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

tar -xjvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
```

自行更改以下路径：
```bash
export RTT_CC_PREFIX=riscv64-unknown-linux-musl-
export RTT_EXEC_PATH=/opt/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

获取依赖：
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
# 在 Arch Linux 上为：sudo pacman -S scons dtc ncurses
```

```bash
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# 生成配置文件
scons --menuconfig
```

在 `menuconfig` 中，Board Type 请选择 `milkv-duo256m`。进入 `RT-Thread Kernel` 菜单 ---> 选中 `Enable RT-Thread Smart (microkernel on kernel/userland)` 选项以启用 RT-Smart 内核。


```bash
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

执行结束后，会在 `cvitek/output/milkv-duo256m` 目录下生成 boot.sd 和 fip.bin 两个文件。

### 拉取源码并编译 RT-Smart 用户态应用

获取依赖：
```bash
sudo apt install -y unzip xmake
```

编译：
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
source env.sh
cd apps
xmake f -a riscv64gc
xmake -j$(nproc)
```

构建镜像：
```bash
xmake smart-rootfs
xmake smart-image -f ext4 
```
生成的应用镜像位于 `userapps/apps/build/ext4.img`。

### 准备 microSD 卡

清空 microSD 卡，并创建一个 FAT32 分区：
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```
将构建出的 boot.sd 和 fip.bin 复制进 microSD 卡。至此，存储卡已经可用来在 Duo 256M 上启动 RT-Thread。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

要求在 menuconfig 中修改 `The virtural address of kernel start (KERNEL_VADDR_START)` 选项的值为 `0xffffffc000200000`，否则编译时 assert 会失败；进而导致可编译出镜像但内核启动失败，详细启动信息如下

### 启动信息

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

Unhandled Exception 13:Load Page Fault
[E/libcpu.trap] 
-------- [SEVER ERROR] --------
[E/libcpu.trap] Nested trap detected
[E/libcpu.trap] scause:0x000000000000000d,stval:0x0000000000000170,sepc:0xffffffc0002797f8

--------------Dump Registers-----------------
Function Registers:                                                                   
        ra(x1) = 0xffffffc0002797f0     user_sp = 0xffffffc0002a6bc0                  
        gp(x3) = 0xffffffc0002a5a18     tp(x4) = 0x0000000000000000                   
Temporary Registers:                                                                  
        t0(x5) = 0x8000000000000005     t1(x6) = 0x0000000000000008                   
        t2(x7) = 0x0000000000000000
        t3(x28) = 0x0000000000000000    t4(x29) = 0x0000000000000000
        t5(x30) = 0x0000000000000000    t6(x31) = 0x0000000000000000
Saved Registers:
        s0/fp(x8) = 0xffffffc0002a6bf0  s1(x9) = 0x0000000000000000
        s2(x18) = 0x0000000000000000    s3(x19) = 0x0000000000000000
        s4(x20) = 0x0000000000000000    s5(x21) = 0x0000000000000000
        s6(x22) = 0x0000000000000000    s7(x23) = 0x0000000000000000
        s8(x24) = 0x0000000000000000    s9(x25) = 0x0000000000000000
        s10(x26) = 0x0000000000000000   s11(x27) = 0x0000000000000000
Function Arguments Registers:
        a0(x10) = 0xffffffc0002ea208    a1(x11) = 0x0000000000000000
        a2(x12) = 0xffffffc0002631ac    a3(x13) = 0xffffffc0002a6c70
        a4(x14) = 0x0000000000000001    a5(x15) = 0x0000000000000000
        a6(x16) = 0x0000000000000000    a7(x17) = 0x0000000000000001
sstatus = 0x8000000201844100
        Supervisor Interrupt Disabled
        Last Time Supervisor Interrupt Disabled
        Last Privilege is Supervisor Mode
        Permit to Access User Page
        Not Permit to Read Executable-only Page
satp = 0x80000000000802e6
        Current Page Table(Physical) = 0x00000000802e6000
        Current ASID = 0x0000000000000000
        Mode = Page-based 39-bit Virtual Addressing Mode
-----------------Dump OK---------------------
shutdown...
```

可能需要 revert RT-Thread 仓库中的某一个 commit 以解决该问题，详见 [RT-Thread/rt-thread#9608](https://github.com/RT-Thread/rt-thread/issues/9608)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFH