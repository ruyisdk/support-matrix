# ThreadX TTGO T-Display-GD32 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/Nuclei-Software/nuclei-sdk
- 参考文档：https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_t_display.html
- 下载链接：
    - SDK：https://github.com/Nuclei-Software/nuclei-sdk
    - toolchain：https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
    - openocd：https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz

### 硬件信息

- TTGO T-Display-GD32
- USB to UART 调试器一个
- **JTAG 调试器**
- type-c 线一根

## 安装步骤

### 配置环境

下载工具链和 OpenOCD 并解压，设置工具链目录：
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
tar -xjvf nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
wget https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz
tar -xzvf nuclei-openocd-2024.02.28-linux-x64.tgz
export NUCLEI_TOOL_ROOT=$(pwd)
```

下载 SDK：
```bash
git clone https://github.com/Nuclei-Software/nuclei-sdk.git
cd nuclei-sdk
echo "NUCLEI_TOOL_ROOT=$(echo $NUCLEI_TOOL_ROOT)" > setup_config.sh
source setup.sh
```

### 编译代码

编译 ThreadX:
```bash
cd application/threadx/demo
make SOC=gd32vf103 BOARD=gd32vf103c_t_display clean
make SOC=gd32vf103 BOARD=gd32vf103c_t_display all
```

### 烧写镜像

通过 JTAG 调试器连接开发板。注意刷写期间板子需上电。

请确保所使用的调试器和 OpenOCD 版本和编译系统兼容。对于前者，可在 `../../../SoC/gd32vf103/Board/gd32vf103c_t_display/openocd_gd32vf103.cfg` 参考所使用的调试器种类编辑相应的 OpenOCD 参数。
例如，使用 Sipeed SLogic Combo 8 调试器 （DAP-Link 模式）时:
```diff
diff --git a/SoC/gd32vf103/Board/gd32vf103c_t_display/openocd_gd32vf103.cfg b/SoC/gd32vf103/Board/gd32vf103c_t_display/openocd_gd32vf103.cfg
index 019218da..66895b18 100644
--- a/SoC/gd32vf103/Board/gd32vf103c_t_display/openocd_gd32vf103.cfg
+++ b/SoC/gd32vf103/Board/gd32vf103c_t_display/openocd_gd32vf103.cfg
@@ -2,8 +2,8 @@ adapter speed     5000
 reset_config    srst_only
 adapter srst pulse_width 100
 
-adapter driver ftdi
-ftdi vid_pid 0x0403 0x6010
+adapter driver cmsis-dap
+cmsis-dap vid_pid 0xd6e7 0x3507
 
 ## bindto 0.0.0.0 can be used to cover all available interfaces.
 ## Uncomment bindto line to enable remote machine debug
@@ -25,14 +25,14 @@ if { [ info exists JTAGSN ] } {
     adapter serial $JTAGSN
 }
 
-ftdi layout_init 0x0008 0x001b
-ftdi layout_signal nSRST -oe 0x0020 -data 0x0020
+#ftdi layout_init 0x0008 0x001b
+#ftdi layout_signal nSRST -oe 0x0020 -data 0x0020
 # These signals are used for cJTAG escape sequence on initialization only
-ftdi layout_signal TCK -data 0x0001
-ftdi layout_signal TDI -data 0x0002
-ftdi layout_signal TDO -input 0x0004
-ftdi layout_signal TMS -data 0x0008
-ftdi layout_signal JTAG_SEL -data 0x0100 -oe 0x0100
+#ftdi layout_signal TCK -data 0x0001
+#ftdi layout_signal TDI -data 0x0002
+#ftdi layout_signal TDO -input 0x0004
+#ftdi layout_signal TMS -data 0x0008
+#ftdi layout_signal JTAG_SEL -data 0x0100 -oe 0x0100
 transport select jtag
 
 set _CHIPNAME riscv
```
如有必要可添加对应的 udev 规则 （参考 https://github.com/arduino/OpenOCD/blob/master/contrib/60-openocd.rules）。

对于后者，工具链中提供的 OpenOCD 版本可能不兼容某些种类的调试器。一个已知可用的版本在 https://github.com/xpack-dev-tools/openocd-xpack/releases/tag/v0.12.0-4 。

准备就绪后，使用如下命令烧写：

```bash
make SOC=gd32vf103 BOARD=gd32vf103c_t_display upload
```

> 如果还是无法连接到开发板，可尝试重新烧写其固件进DFU。
> 
> 从这里下载固件：https://github.com/Xinyuan-LilyGO/LilyGO-T-DisplayGD32/raw/refs/heads/master/firmware/GD32V_CBT6_20200116.bin
> 
> 按住开发板上的 BOOT 按钮的同时上电，进入 DFU 模式，此时 `lsusb` 应有例如：
> 
> ```shell
> Bus 001 Device 047: ID 28e9:0189 GDMicroelectronics GD32 DFU Bootloader (Longan Nano)
> # 显示 Longan Nano 为正常现象
> ```

> 使用 `gd32-dfu-utils` (https://github.com/riscv-mcu/gd32-dfu-utils) 烧写固件：
> 
> ```shell
> sudo gd32-dfu-util -D GD32V_CBT6_20200116.bin
> ```

### 启动系统

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
Nuclei SDK Build Time: Feb 24 2025, 16:00:38
Download Mode: FLASHXIP
CPU Frequency 108000000 Hz
thread 6_7 is running, current is 6, thread 6 counter 1, thread 7 counter 1
thread 6_7 is running, current is 7, thread 6 counter 2, thread 7 counter 1
thread 6_7 is running, current is 6, thread 6 counter 2, thread 7 counter 2
thread 6_7 is running, current is 7, thread 6 counter 3, thread 7 counter 2
thread 6_7 is running, current is 6, thread 6 counter 3, thread 7 counter 3
thread 6_7 is running, current is 7, thread 6 counter 4, thread 7 counter 3
thread 6_7 is running, current is 6, thread 6 counter 4, thread 7 counter 4
thread 6_7 is running, current is 7, thread 6 counter 5, thread 7 counter 4
thread 6_7 is running, current is 6, thread 6 counter 5, thread 7 counter 5
thread 6_7 is running, current is 7, thread 6 counter 6, thread 7 counter 5
thread 6_7 is running, current is 6, thread 6 counter 6, thread 7 counter 6
thread 6_7 is running, current is 7, thread 6 counter 7, thread 7 counter 6
thread 6_7 is running, current is 6, thread 6 counter 7, thread 7 counter 7
thread 6_7 is running, current is 7, thread 6 counter 8, thread 7 counter 7
thread 6_7 is running, current is 6, thread 6 counter 8, thread 7 counter 8
thread 6_7 is running, current is 7, thread 6 counter 9, thread 7 counter 8
thread 6_7 is running, current is 6, thread 6 counter 9, thread 7 counter 9
thread 6_7 is running, current is 7, thread 6 counter 10, thread 7 counter 9
thread 6_7 is running, current is 6, thread 6 counter 10, thread 7 counter 10
thread 6_7 is running, current is 7, thread 6 counter 11, thread 7 counter 10
thread 6_7 is running, current is 6, thread 6 counter 11, thread 7 counter 11
thread 6_7 is running, current is 7, thread 6 counter 12, thread 7 counter 11
thread 6_7 is running, current is 6, thread 6 counter 12, thread 7 counter 12
thread 6_7 is running, current is 7, thread 6 counter 13, thread 7 counter 12
thread 6_7 is running, current is 6, thread 6 counter 13, thread 7 counter 13
thread 6_7 is running, current is 7, thread 6 counter 14, thread 7 counter 13
thread 6_7 is running, current is 6, thread 6 counter 14, thread 7 counter 14
thread 6_7 is running, current is 7, thread 6 counter 15, thread 7 counter 14
thread 6_7 is running, current is 6, thread 6 counter 15, thread 7 counter 15
thread 6_7 is running, current is 7, thread 6 counter 16, thread 7 counter 15
thread 6_7 is running, current is 6, thread 6 counter 16, thread 7 counter 16
thread 6_7 is running, current is 7, thread 6 counter 17, thread 7 counter 16
thread 6_7 is running, current is 6, thread 6 counter 17, thread 7 counter 17
thread 6_7 is running, current is 7, thread 6 counter 18, thread 7 counter 17
thread 6_7 is running, current is 6, thread 6 counter 18, thread 7 counter 18
thread 6_7 is running, current is 7, thread 6 counter 19, thread 7 counter 18
thread 6_7 is running, current is 6, thread 6 counter 19, thread 7 counter 19
thread 6_7 is running, current is 7, thread 6 counter 20, thread 7 counter 19
thread 6_7 is running, current is 6, thread 6 counter 20, thread 7 counter 20
thread 6_7 is running, current is 7, thread 6 counter 21, thread 7 counter 20
thread 6_7 is running, current is 6, thread 6 counter 21, thread 7 counter 21
thread 6_7 is running, current is 7, thread 6 counter 22, thread 7 counter 21
thread 6_7 is running, current is 6, thread 6 counter 22, thread 7 counter 22
thread 6_7 is running, current is 7, thread 6 counter 23, thread 7 counter 22
thread 6_7 is running, current is 6, thread 6 counter 23, thread 7 counter 23
thread 6_7 is running, current is 7, thread 6 counter 24, thread 7 counter 23
thread 6_7 is running, current is 6, thread 6 counter 24, thread 7 counter 24
thread 6_7 is running, current is 7, thread 6 counter 25, thread 7 counter 24
thread 6_7 is running, current is 6, thread 6 counter 25, thread 7 counter 25
thread 6_7 is running, current is 7, thread 6 counter 26, thread 7 counter 25
thread 6_7 is running, current is 6, thread 6 counter 26, thread 7 counter 26
thread 6_7 is running, current is 7, thread 6 counter 27, thread 7 counter 26
thread 6_7 is running, current is 6, thread 6 counter 27, thread 7 counter 27
thread 6_7 is running, current is 7, thread 6 counter 28, thread 7 counter 27
thread 6_7 is running, current is 6, thread 6 counter 28, thread 7 counter 28
thread 6_7 is running, current is 7, thread 6 counter 29, thread 7 counter 28
thread 6_7 is running, current is 6, thread 6 counter 29, thread 7 counter 29
thread 6_7 is running, current is 7, thread 6 counter 30, thread 7 counter 29
thread 6_7 is running, current is 6, thread 6 counter 30, thread 7 counter 30
thread 6_7 is running, current is 7, thread 6 counter 31, thread 7 counter 30
thread 6_7 is running, current is 6, thread 6 counter 31, thread 7 counter 31
thread 6_7 is running, current is 7, thread 6 counter 32, thread 7 counter 31
thread 6_7 is running, current is 6, thread 6 counter 32, thread 7 counter 32
thread 6_7 is running, current is 7, thread 6 counter 33, thread 7 counter 32
... (truncated)

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。