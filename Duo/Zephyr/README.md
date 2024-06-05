# Zephyr MilkV Duo Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/zephyrproject-rtos/zephyr/tree/main
- Reference Installation Document:
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- MilkV Duo
- One USB to UART debugger
- SD card

## Installation Steps

### Create and Compile BuildRoot

Follow the official tutorial to fetch the source code:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

Modify `build/boards/cv180x/cv1800b_milkv_duo_sd/u-boot/cvi_board_init.c` to remove pre-mapped pins:
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

Then use Docker for compilation:
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo"
```

Next, flash the source code to the SD card:
```bash 
sudo dd if=out/milkv-duo-yyyymmdd-hhmm.img of=/dev/your/device bs=1M status=progress
```

### Install Zephyr

Create a virtual environment:

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

Note: Since the changes are not yet merged into the mainline, use the specific repository when fetching Zephyr:
```bash
west init ~/zephyrproject -m https://github.com/plctlab/rvspoc-p2307-zephyr.git
cd ~/zephyrproject
west update
```

Configure the environment:
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

### Code Compliation

Compile the code using west:
```bash
west build -p always -b milkv_duo samples/hello_world
```

### Merge fip.bin

Mount the SD card with the BuildRoot image flashed and merge fip:
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

Copy to the SD card:
```bash
sudo cp ./fsbl/build/cv1800b_milkv_duo_sd/fip.bin /path/to/sdcard
```

### Connect Serial Port

The core used by Zephyr utilizes UART1 (GP1: TX, GP2: RX, GP3: GND)

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

The system booted successfully, and information could be viewed through the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/7ax1STNgh7W6wKFH9mMKLfiHV.svg)](https://asciinema.org/a/7ax1STNgh7W6wKFH9mMKLfiHV)

```log
Hello World! milkv_duo/cv1800b
Hello World! milkv_duo/cv1800b
Hello World! milkv_duo/cv1800b
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

