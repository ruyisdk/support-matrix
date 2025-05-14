# ThreadX RV-STAR 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/Nuclei-Software/nuclei-sdk
- 参考文档：https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103v_rvstar.html
- 下载链接：
    - SDK：https://github.com/Nuclei-Software/nuclei-sdk
    - toolchain：https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
    - OpenOCD：https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz

### 硬件信息

- RV-STAR 开发板（GD32VF103VBT6）
- USB to UART 调试器一个
- **JTAG 调试器**
- Type-C 线一根

## 安装步骤

### 配置环境

下载工具链和 OpenOCD 并解压，设置工具链目录：
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
tar -xzvf nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
wget https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz
tar -xzvf nuclei-openocd-2024.02.28-linux-x64.tgz
export NUCLEI_TOOL_ROOT=$(pwd)
```

下载 SDK：
```bash
git clone https://github.com/Nuclei-Software/nuclei-sdk.git
cd nuclei-sdk
cat << EOF > setup_config.sh
NUCLEI_TOOL_ROOT=$(echo $NUCLEI_TOOL_ROOT)
EOF
source setup.sh
```

### 连接开发板

按下图所示连接开发板至 JTAG 调试器：

![](pinout.jpg)

注意图中的 3V3 pin 和 Type-C 接口均需连接/上电。

### 编译代码

编译 ThreadX:
```bash
cd application/threadx/demo/
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar clean
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar all
```

### 烧写镜像

请确保所使用的调试器和 OpenOCD 版本和编译系统兼容。对于前者，可在 `../../../SoC/gd32vf103/Board/gd32vf103v_rvstar/openocd_gd32vf103.cfg` 参考所使用的调试器种类编辑相应的 OpenOCD 参数。
例如，使用 Sipeed SLogic Combo 8 调试器 （DAP-Link 模式）时:
```diff
diff --git a/SoC/gd32vf103/Board/gd32vf103v_rvstar/openocd_gd32vf103.cfg b/SoC/gd32vf103/Board/gd32vf103v_rvstar/openocd_gd32vf103.cfg
index 019218da..66895b18 100644
--- a/SoC/gd32vf103/Board/gd32vf103v_rvstar/openocd_gd32vf103.cfg
+++ b/SoC/gd32vf103/Board/gd32vf103v_rvstar/openocd_gd32vf103.cfg
@@ -2,8 +2,8 @@ adapter speed     5000
 reset_config    srst_only
 adapter srst pulse_width 100

-adapter driver ftdigd32vf103v_rvstar
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
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar upload
```

### 启动系统

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

系统正常启动，能够通过板载串口查看信息。

### 启动信息

```log
Nuclei SDK Build Time: May 13 2025, 23:44:33
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
...
(truncated)
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。