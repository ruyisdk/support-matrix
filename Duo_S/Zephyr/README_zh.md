# Zephyr MilkV DuoS 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
- 参考文档：
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- MilkV DuoS
- USB to UART 调试器一个
- SD 卡

## 安装步骤

### 创建并编译 BuildRoot

根据官方教程，获取源码：
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

修改 `build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c` 以去除预映射的引脚：
```diff
diff --git a/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c b/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c
index 6552f8da3..cbcb91cb6 100644
--- a/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c
+++ b/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c
@@ -6,52 +6,10 @@ static void set_rtc_register_for_power(void)
 
 int cvi_board_init(void)
 {
-       // Camera
-       PINMUX_CONFIG(CAM_MCLK0, CAM_MCLK0);
-       PINMUX_CONFIG(IIC3_SCL, IIC3_SCL);
-       PINMUX_CONFIG(IIC3_SDA, IIC3_SDA);
-       PINMUX_CONFIG(PAD_MIPIRX4P, XGPIOC_3);
-       PINMUX_CONFIG(PAD_MIPIRX4N, XGPIOC_2);
-
-       // I2C2 for Camera2
-       PINMUX_CONFIG(IIC2_SDA, IIC2_SDA);
-       PINMUX_CONFIG(IIC2_SCL, IIC2_SCL);
-
-       // LED
-       PINMUX_CONFIG(IIC0_SDA, XGPIOA_29);
-
-       // I2C4 for TP
-       PINMUX_CONFIG(VIVO_D1, IIC4_SCL);
-       PINMUX_CONFIG(VIVO_D0, IIC4_SDA);
-
-       // SPI3
-       PINMUX_CONFIG(VIVO_D8, SPI3_SDO);
-       PINMUX_CONFIG(VIVO_D7, SPI3_SDI);
-       PINMUX_CONFIG(VIVO_D6, SPI3_SCK);
-       PINMUX_CONFIG(VIVO_D5, SPI3_CS_X);
-
-       // USB
-       PINMUX_CONFIG(USB_VBUS_EN, XGPIOB_5);
-
-       // WIFI/BT
-       PINMUX_CONFIG(CLK32K, PWR_GPIO_10);
-       PINMUX_CONFIG(UART2_RX, UART4_RX);
-       PINMUX_CONFIG(UART2_TX, UART4_TX);
-       PINMUX_CONFIG(UART2_CTS, UART4_CTS);
-       PINMUX_CONFIG(UART2_RTS, UART4_RTS);
-
-       // GPIOs
-       PINMUX_CONFIG(JTAG_CPU_TCK, XGPIOA_18);
-       PINMUX_CONFIG(JTAG_CPU_TMS, XGPIOA_19);
-       PINMUX_CONFIG(JTAG_CPU_TRST, XGPIOA_20);
-       PINMUX_CONFIG(IIC0_SCL, XGPIOA_28);
-
-       // EPHY LEDs
-       PINMUX_CONFIG(PWR_WAKEUP0, EPHY_LNK_LED);
-       PINMUX_CONFIG(PWR_BUTTON1, EPHY_SPD_LED);
+       PINMUX_CONFIG(VIVO_D10, UART2_TX);
+       PINMUX_CONFIG(VIVO_D9, UART2_RX);
 
        set_rtc_register_for_power();
 
        return 0;
 }
-

```



然后使用 docker 进行编译：
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo256m"
```

而后将源码烧写到 SD 卡中：
```bash 
sudo dd if=out/milkv-duo-yyyymmdd-hhmm.img of=/dev/your/device bs=1M status=progress
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
west init ~/zephyrproject -m https://github.com/plctlab/rvspoc-p2307-zephyr.git
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
west build -p always -b milkv_duos samples/hello_world
```

### 合并 fip.bin

挂载刷写好 BuildRoot 镜像的 SD 卡，合并 fip：
```bash
sudo ./fsbl/plat/cv181x/fiptool.py -v genfip \
        './fsbl/build/cv1813h_milkv_duos_sd/fip.bin' \
        --MONITOR_RUNADDR="0x0000000080000000" \
        --BLCP_2ND_RUNADDR="0x000000009fe00000" \
        --CHIP_CONF='./fsbl/build/cv1813h_milkv_duos_sd/chip_conf.bin' \
        --NOR_INFO='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' \
        --NAND_INFO='00000000'\
        --BL2='./fsbl/build/cv1813h_milkv_duos_sd/bl2.bin' \
        --BLCP_IMG_RUNADDR=0x05200200 \
        --BLCP_PARAM_LOADADDR=0 \
        --BLCP=./fsbl/test/empty.bin \
        --DDR_PARAM='./fsbl/test/cv181x/ddr_param.bin' \
        --BLCP_2ND='~/zephyrproject/zephyr/build/zephyr/zephyr.bin' \
        --MONITOR='./opensbi/build/platform/generic/firmware/fw_dynamic.bin' \
        --LOADER_2ND='./u-boot-2021.10/build/cv1813h_milkv_duos_sd/u-boot-raw.bin' \
        --compress='lzma'

```

复制到 SD 卡中：
```bash
sudo cp ./fsbl/build/cv1813h_milkv_duos_sd/fip.bin /path/to/sdcard
```

### 连接串口

Zephyr 所在的小核使用了 UART2 (GP11: TX, GP13: RX, GP9: GND)

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/oxAM8WHrZvcN04yDOWSlSDsKf.svg)](https://asciinema.org/a/oxAM8WHrZvcN04yDOWSlSDsKf)

```log
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000
Hello World! milkv_duos/sg2000

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功