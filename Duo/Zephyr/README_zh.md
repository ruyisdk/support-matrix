# Zephyr MilkV Duo 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
- 参考文档：
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- MilkV Duo
- USB to UART 调试器一个
- SD 卡

## 安装步骤

### 创建并编译 BuildRoot

根据官方教程，获取源码：
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

修改 `build/boards/cv180x/cv1800b_milkv_duo_sd/u-boot/cvi_board_init.c` 以去除预映射的引脚：
```diff
diff --git a/build/boards/cv180x/cv1800b_milkv_duo_sd/u-boot/cvi_board_init.c b/build/boards/cv180x/cv1800b_milkv_duo_sd/u-boot/cvi_board_init.c
index 74941cb09..cd1fd6c1d 100644
--- a/build/boards/cv180x/cv1800b_milkv_duo_sd/u-boot/cvi_board_init.c
+++ b/build/boards/cv180x/cv1800b_milkv_duo_sd/u-boot/cvi_board_init.c
@@ -1,45 +1,6 @@
 int cvi_board_init(void)
 {
-       // sensor mclk reset
-       PINMUX_CONFIG(PAD_MIPIRX0P, CAM_MCLK0); // Camera MCLK0
-       PINMUX_CONFIG(PAD_MIPIRX1N, XGPIOC_8);  // Camera Reset
-
-       // all default gpio
-       PINMUX_CONFIG(SD0_PWR_EN, XGPIOA_14);    // Duo Pin 19
-       PINMUX_CONFIG(SPK_EN, XGPIOA_15);        // Duo Pin 20
-       PINMUX_CONFIG(SPINOR_MISO, XGPIOA_23);   // Duo Pin 21
-       PINMUX_CONFIG(SPINOR_CS_X, XGPIOA_24);   // Duo Pin 22
-       PINMUX_CONFIG(SPINOR_SCK, XGPIOA_22);    // Duo Pin 24
-       PINMUX_CONFIG(SPINOR_MOSI, XGPIOA_25);   // Duo Pin 25
-       PINMUX_CONFIG(SPINOR_WP_X, XGPIOA_27);   // Duo Pin 26
-       PINMUX_CONFIG(SPINOR_HOLD_X, XGPIOA_26); // Duo Pin 27
-       PINMUX_CONFIG(PWR_SEQ2, PWR_GPIO_4);     // Duo Pin 29
-
-       // ADC pins set to gpio
-       PINMUX_CONFIG(ADC1, XGPIOB_3);           // ADC1
-       PINMUX_CONFIG(USB_VBUS_DET, XGPIOB_6);   // ADC2
-
-       // I2C0
-       PINMUX_CONFIG(IIC0_SCL, IIC0_SCL);
-       PINMUX_CONFIG(IIC0_SDA, IIC0_SDA);
-
-       // I2C1
-       PINMUX_CONFIG(PAD_MIPIRX1P, IIC1_SDA);
-       PINMUX_CONFIG(PAD_MIPIRX0N, IIC1_SCL);
-
-       // PWM
-       PINMUX_CONFIG(SD1_D2, PWM_5);
-       PINMUX_CONFIG(SD1_D1, PWM_6);
-
-       // UART 4
-       PINMUX_CONFIG(SD1_GPIO1, UART4_TX);
-       PINMUX_CONFIG(SD1_GPIO0, UART4_RX);
-
-       // SPI
-       PINMUX_CONFIG(SD1_CLK, SPI2_SCK);
-       PINMUX_CONFIG(SD1_CMD, SPI2_SDO);
-       PINMUX_CONFIG(SD1_D0, SPI2_SDI);
-       PINMUX_CONFIG(SD1_D3, SPI2_CS_X);
-
+       PINMUX_CONFIG(IIC0_SCL, UART1_TX);
+       PINMUX_CONFIG(IIC0_SDA, UART1_RX);
        return 0;
 }

```



然后使用 docker 进行编译：
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo"
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
west build -p always -b milkv_duo samples/hello_world
```

### 合并 fip.bin

挂载刷写好 BuildRoot 镜像的 SD 卡，合并 fip：
```bash
sudo ./fsbl/plat/cv180x/fiptool.py -v genfip \
 './fsbl/build/cv1800b_milkv_duo_sd/fip.bin' \
  --BLCP_2ND_RUNADDR="0x0000000083f40000" \
  --MONITOR_RUNADDR="0x0000000080000000" \
  --CHIP_CONF='./fsbl/build/cv1800b_milkv_duo_sd/chip_conf.bin' \
  --NOR_INFO='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' \
  --NAND_INFO='00000000'\
  --BL2='./fsbl/build/cv1800b_milkv_duo_sd/bl2.bin' \
  --BLCP_IMG_RUNADDR=0x05200200 \
  --BLCP_PARAM_LOADADDR=0 \
  --BLCP='./fsbl/test/empty.bin' \
  --DDR_PARAM='./fsbl/test/cv181x/ddr_param.bin' \
  --BLCP_2ND='~/zephyrproject/zephyr/build/zephyr/zephyr.bin' \
  --MONITOR='./opensbi/build/platform/generic/firmware/fw_dynamic.bin' \
  --LOADER_2ND='./u-boot-2021.10/build/cv1800b_milkv_duo_sd/u-boot-raw.bin' \
  --compress='lzma'
```

复制到 SD 卡中：
```bash
sudo cp ./fsbl/build/cv1800b_milkv_duo_sd/fip.bin /path/to/sdcard
```

### 连接串口

Zephyr 所在的小核使用了 UART1 (GP1: TX, GP2: RX, GP3: GND)

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/7ax1STNgh7W6wKFH9mMKLfiHV.svg)](https://asciinema.org/a/7ax1STNgh7W6wKFH9mMKLfiHV)

```log
Hello World! milkv_duo/cv1800b
Hello World! milkv_duo/cv1800b
Hello World! milkv_duo/cv1800b
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功