# Zephyr MilkV DuoS 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Zephyr 4.1.99 
- 源码链接：https://github.com/xingrz/zephyr/tree/milkv-duo/hwmv2/dev
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

修改 `build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c` ，删除所有预映射的引脚，只保留 UART1 (A19/A18) 配置：
```c
int cvi_board_init(void)
{
        PINMUX_CONFIG(JTAG_CPU_TMS, UART1_TX);  // A19
        PINMUX_CONFIG(JTAG_CPU_TCK, UART1_RX);  // A18

        set_rtc_register_for_power();

        return 0;
}

```

确认 SDK 自带 RISC-V 工具链存在：
```bash
ls ~/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-gcc

```

编译 U-Boot：
```bash 
cd ~/duo-buildroot-sdk/u-boot-2021.10

make O=build/cv1813h_milkv_duos_sd \
    CROSS_COMPILE=$HOME/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl- \
    ARCH=riscv \
    CHIP=cv1813h \
    CVIBOARD=milkv_duos_sd \
    -j$(nproc)

```

编译完成后，手动生成：
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

创建虚拟环境：

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

注：当前还未合入主线，获取 Zephyr 时需要使用特定仓库：
```bash
west init ~/zephyrproject -m https://github.com/xingrz/zephyr.git
cd ~/zephyrproject
west update
```

配置环境：
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

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
