# Zephyr MilkV DuoS 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Zephyr 4.1.99 (commit 4788d883d554)
- 源码链接：https://github.com/xingrz/zephyr/commit/4788d883d554d015470eff11883af610aeb6c2cd
- 参考文档：
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- Milk-V Duo S
- USB C to C 线缆一条
- USB to UART 调试器一个
- 杜邦线三根
- SD 卡

## 安装步骤

### 创建并编译 BuildRoot

根据官方教程，获取源码：
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1

```

### 获取 RISC-V 工具链

全新克隆的 SDK 不包含 host-tools/gcc/，需要先运行 SDK 自带的脚本下载：
```bash
cd ~/duo-buildroot-sdk
./build/scripts/download_toolchain.sh

```

下载完成后，检查交叉编译器是否存在：

```bash
ls -lh ~/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-gcc
```

检查工具链是否可以正常运行：

```bash
~/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-gcc --version
```

确认工具链下载成功后，再进行 U-Boot 配置与编译。

### 修改 U-Boot 板级初始化

`build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c`，删除所有预映射的引脚，只保留 UART1 (A19/A18) 配置：
```c
int cvi_board_init(void)
{
        PINMUX_CONFIG(JTAG_CPU_TMS, UART1_TX);  // A19
        PINMUX_CONFIG(JTAG_CPU_TCK, UART1_RX);  // A18

        set_rtc_register_for_power();

        return 0;
}

```

### 将板级配置同步到 U-Boot 源码树

SDK 的构建脚本会把 build/boards/.../u-boot/ 下的板级文件同步到 U-Boot 源码树。手动编译时需要显式完成这一步：
```bash
# 拷贝板级 defconfig 到 u-boot 源码树
cp ~/duo-buildroot-sdk/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvitek_cv1813h_milkv_duos_sd_defconfig \
   ~/duo-buildroot-sdk/u-boot-2021.10/configs/

# 拷贝 cvi_board_init.c 到 U-Boot 的 board 目录
mkdir -p ~/duo-buildroot-sdk/u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/
cp ~/duo-buildroot-sdk/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c \
   ~/duo-buildroot-sdk/u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/

```

检查两个位置的板级初始化文件是否一致：

```bash
diff -u \
  build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c \
  u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.c
```

如果命令没有输出且退出状态为 `0`，说明两个文件内容一致。

### 配置并编译 U-Boot

使用 Duo S 对应的 defconfig 配置 U-Boot：
```bash 
cd ~/duo-buildroot-sdk/u-boot-2021.10

export CROSS_COMPILE="$HOME/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-"

make O=build/cv1813h_milkv_duos_sd \
    ARCH=riscv \
    CROSS_COMPILE="$CROSS_COMPILE" \
    cvitek_cv1813h_milkv_duos_sd_defconfig
```

配置完成后，清除对应的旧目标文件和编译依赖记录，避免将之前的编译结果误认为本次构建结果：

```bash
rm -f build/cv1813h_milkv_duos_sd/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.o

rm -f build/cv1813h_milkv_duos_sd/board/cvitek/cv1813h_milkv_duos_sd/.cvi_board_init.o.cmd
```

编译 U-Boot：
```bash 
make O=build/cv1813h_milkv_duos_sd \
    CROSS_COMPILE="$CROSS_COMPILE" \
    ARCH=riscv \
    CHIP=cv1813h \
    CVIBOARD=milkv_duos_sd \
    -j"$(nproc)"

```

编译完成后，确认 `cvi_board_init.o` 已生成：
```bash
ls -lh build/cv1813h_milkv_duos_sd/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.o

```

同时检查构建依赖，确认本次构建使用了 `cvi_board_init.c`：
```bash
find build/cv1813h_milkv_duos_sd \
    -name '*.cmd' \
    -exec grep -H "cvi_board_init.c" {} \;

```

同时，检查编译输出中对应的源文件路径，确认实际参与编译的文件为：

`u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.c`

### 生成 U-Boot 原始镜像

手动生成 `u-boot-raw.bin` ：
```bash 
cp build/cv1813h_milkv_duos_sd/u-boot.bin \
   build/cv1813h_milkv_duos_sd/u-boot-raw.bin

ls -lh build/cv1813h_milkv_duos_sd/u-boot-raw.bin

```

### 刷写 BuildRoot 镜像

从 Milk-V 官方 Releases 下载标准 BuildRoot 镜像：
```bash 
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duos-sd-v1.1.4.img.zip
unzip milkv-duos-sd-v1.1.4.img.zip

```

刷写：
```bash 
sudo dd if=milkv-duos-sd-v1.1.4.img of=/dev/sdX bs=1M status=progress
sync

```

### 安装 Zephyr

#### 创建虚拟环境

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

#### 获取指定版本的 Zephyr 源码

当前测试使用的 Milk-V DuoS 支持代码尚未合入 Zephyr 主线，因此需要从对应的开发仓库获取源码，并固定到实测提交：

`4788d883d554d015470eff11883af610aeb6c2cd`

初始化工作区并获取依赖：

```bash
west init ~/zephyrproject \
    -m https://github.com/xingrz/zephyr.git \
    --mr 4788d883d554d015470eff11883af610aeb6c2cd

cd ~/zephyrproject
west update

```

确认当前 Zephyr 源码为指定 commit：
```bash
cd ~/zephyrproject/zephyr 
git rev-parse HEAD

```

配置环境：
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt

```

确认输出为 `4788d883d554d015470eff11883af610aeb6c2cd`

### 编译代码

使用 west 编译代码：
```bash
west build -p always -b milkv_duos/sg2000/c906_1 samples/hello_world

```

为了方便观察使 `hello_world` 循环打印，修改 `samples/hello_world/src/main.c`：
```c
#include <zephyr/kernel.h>

int main(void)
{
        while (1) {
                printk("Hello World! %s\n", CONFIG_BOARD_TARGET);
                k_msleep(1000);
        }
        return 0;
}

```

保存后重新编译：
```bash
west build -p always -b milkv_duos/sg2000/c906_1 samples/hello_world

```

编译成功后，确认生成 Zephyr 镜像：

```bash
ls -lh ~/zephyrproject/zephyr/build/zephyr/zephyr.bin
```

### 合并 fip.bin

挂载刷写好 BuildRoot 镜像的 SD 卡，备份原始 fip.bin：
```bash
sudo mount /dev/sdX1 /mnt/sdcard
sudo cp /mnt/sdcard/fip.bin /mnt/sdcard/fip.bin.bak

```

增量替换 U-Boot 和小核固件：
```bash
sudo python3 ~/duo-buildroot-sdk/fsbl/plat/cv181x/fiptool.py \
    -v genfip /mnt/sdcard/fip.bin \
    --OLD_FIP=/mnt/sdcard/fip.bin \
    --LOADER_2ND=$HOME/duo-buildroot-sdk/u-boot-2021.10/build/cv1813h_milkv_duos_sd/u-boot-raw.bin \
    --BLCP_2ND=$HOME/zephyrproject/zephyr/build/zephyr/zephyr.bin

sync
sudo umount /mnt/sdcard

```

### 连接串口

Zephyr 所在的小核使用了 UART1 ：
- A19 (Pin 18) — TX
- A18 (Pin 22) — RX
- GND (Pin 6/14/20/25)

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
*** Booting Zephyr OS build 4788d883d554 ***
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
...

```

屏幕录像：

[![asciicast](https://asciinema.org/a/XN5DravPePYddw20.svg)](https://asciinema.org/a/XN5DravPePYddw20)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
