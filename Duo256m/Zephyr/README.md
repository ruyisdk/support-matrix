# Zephyr MilkV Duo256M Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/zephyrproject-rtos/zephyr/tree/main
- Reference Installation Document:
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- MilkV Duo256M
- USB to UART Debugger 
- SD Card

## Installation Steps

### Create and Compile BuildRoot

Obtain the source code according to the official tutorial:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1
```

Modify `build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c` to remove pre-mapped pins:
```diff
diff --git a/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c b/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
index c9c722236..c388ec0ee 100644
--- a/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
+++ b/build/boards/cv181x/cv1812cp_milkv_duo256m_sd/u-boot/cvi_board_init.c
@@ -1,46 +1,14 @@
 int cvi_board_init(void)
 {
-       // Camera
-       PINMUX_CONFIG(PAD_MIPI_TXM1, IIC2_SDA);    // GP10
-       PINMUX_CONFIG(PAD_MIPI_TXP1, IIC2_SCL);    // GP11
-       PINMUX_CONFIG(PAD_MIPI_TXP0, CAM_MCLK0);   // Sensor MCLK
-       PINMUX_CONFIG(PAD_MIPI_TXP2, XGPIOC_17);   // Sensor RESET
 
        // UART1
        PINMUX_CONFIG(IIC0_SCL, UART1_TX);         // GP0
        PINMUX_CONFIG(IIC0_SDA, UART1_RX);         // GP1
 
-       // PWM
-       PINMUX_CONFIG(JTAG_CPU_TMS, PWM_7);        // GP2
-       PINMUX_CONFIG(JTAG_CPU_TCK, PWM_6);        // GP3
 
-       // I2C1
-       PINMUX_CONFIG(SD1_D2, IIC1_SCL);           // GP4
-       PINMUX_CONFIG(SD1_D1, IIC1_SDA);           // GP5
 
-       // SPI2
-       PINMUX_CONFIG(SD1_CLK, SPI2_SCK);          // GP6
-       PINMUX_CONFIG(SD1_CMD, SPI2_SDO);          // GP7
-       PINMUX_CONFIG(SD1_D0, SPI2_SDI);           // GP8
-       PINMUX_CONFIG(SD1_D3, SPI2_CS_X);          // GP9
 
-       // All default GPIOs
-       PINMUX_CONFIG(SD0_PWR_EN, XGPIOA_14);      // GP14
-       PINMUX_CONFIG(SPK_EN, XGPIOA_15);          // GP15
-       PINMUX_CONFIG(EMMC_CMD, XGPIOA_23);        // GP16
-       PINMUX_CONFIG(EMMC_DAT1, XGPIOA_24);       // GP17
-       PINMUX_CONFIG(EMMC_CLK, XGPIOA_22);        // GP18
-       PINMUX_CONFIG(EMMC_DAT0, XGPIOA_25);       // GP19
-       PINMUX_CONFIG(EMMC_DAT3, XGPIOA_27);       // GP20
-       PINMUX_CONFIG(EMMC_DAT2, XGPIOA_26);       // GP21
-       PINMUX_CONFIG(PWR_SEQ2, PWR_GPIO_4);       // GP22
 
-       // LED
-       PINMUX_CONFIG(PWR_GPIO2, PWR_GPIO_2);      // GP25
-
-       // ADC pins set to GPIO
-       PINMUX_CONFIG(ADC1, XGPIOB_3);             // GP26 (ADC1)
-       PINMUX_CONFIG(USB_VBUS_DET, XGPIOB_6);     // GP27 (ADC2)
 
        return 0;
-}
\ No newline at end of file
+}

```

Then compile using Docker:
```bash
cd duo-buildroot-sdk
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo256m"
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
pip install westcv180x/cv1800b_milkv_duo_sd
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
west build -p always -b milkv_duo256m samples/hello_world
```

### Merge fip.bin

Mount the SD card with the BuildRoot image flashed and merge fip:
```bash
sudo ./fsbl/plat/cv181x/fiptool.py -v genfip \
 './fsbl/build/cv1812cp_milkv_duo256m_sd/fip.bin' \
  --BLCP_2ND_RUNADDR="0x000000008fe00000" \
  --MONITOR_RUNADDR="0x0000000080000000" \
  --CHIP_CONF='./fsbl/build/cv1812cp_milkv_duo256m_sd/chip_conf.bin' \
  --NOR_INFO='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF' \
  --NAND_INFO='00000000'\
  --BL2='./fsbl/build/cv1812cp_milkv_duo256m_sd/bl2.bin' \
  --BLCP_IMG_RUNADDR=0x05200200 \
  --BLCP_PARAM_LOADADDR=0 \
  --BLCP='./fsbl/test/empty.bin' \
  --DDR_PARAM='./fsbl/test/cv181x/ddr_param.bin' \
  --BLCP_2ND='~/zephyrproject/zephyr/build/zephyr/zephyr.bin' \
  --MONITOR='./opensbi/build/platform/generic/firmware/fw_dynamic.bin' \
  --LOADER_2ND='./u-boot-2021.10/build/cv1812cp_milkv_duo256m_sd/u-boot-raw.bin' \
  --compress='lzma'

```

Copy it to the SD card:
```bash
sudo cp ./fsbl/build/cv1812cp_milkv_duo256m_sd/fip.bin /path/to/sdcard
```

### Connecting the serial port

The small core running Zephyr is using UART1 (GP1: TX, GP2: RX, GP3: GND)

## Expected Results

The system boots up normally and allows login through the serial port.


## Actual Results

The system boots up normally and login through the serial port is successful.

### 启动信息

屏幕录像（从编译到启动）：
[![asciicast](https://asciinema.org/a/l8UeZmW5Q6xRS2wBAdL4GFlXp.svg)](https://asciinema.org/a/l8UeZmW5Q6xRS2wBAdL4GFlXp)

```log
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
Hello World! milkv_duo256m/sg2002
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
