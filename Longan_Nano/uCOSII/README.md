---
sys: ucosii
sys_ver: null
sys_var: null

status: basic
last_update: 2025-02-24
---

# μC/OS-II TTGO T-Display-GD32 Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/Nuclei-Software/nuclei-sdk
- Reference Installation Document: https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_t_display.html
- Download Links:
    - SDK: https://github.com/Nuclei-Software/nuclei-sdk
    - Toolchain: https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
    - OpenOCD: https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz

### Hardware Information

- TTGO T-Display-GD32
- A USB to UART Debugger
- **JTAG Debugger**
- A Type-C Cable

## Installation Steps

### Configure Environment

Download and extract the toolchain and OpenOCD, then set the toolchain directory:
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
tar -xjvf nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
wget https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz
tar -xzvf nuclei-openocd-2024.02.28-linux-x64.tgz
export NUCLEI_TOOL_ROOT=$(pwd)
```

Download the SDK:
```bash
git clone https://github.com/Nuclei-Software/nuclei-sdk.git
cd nuclei-sdk
echo "NUCLEI_TOOL_ROOT=$(echo $NUCLEI_TOOL_ROOT)" > setup_config.sh

source setup.sh
```

### Compile Code

Compile μC/OS-II:
```bash
cd application/ucosii/demo/
make SOC=gd32vf103 BOARD=gd32vf103c_t_display clean
make SOC=gd32vf103 BOARD=gd32vf103c_t_display all
```

### Flash Image

Connect to the development board via your JTAG debugger. Note that the board should be powered on while flashing.

Make sure your debugger and OpenOCD binary is supported by the build system.
For the former, consider editing relevant settings in `../../../SoC/gd32vf103/Board/gd32vf103c_t_display/openocd_gd32vf103.cfg` to match your JTAG debugger.
e.g. with Sipeed SLogic Combo 8 debugger at DAP-Link mode:
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

Also adding an udev rule if necessary (refer to https://github.com/arduino/OpenOCD/blob/master/contrib/60-openocd.rules)
For the latter, make sure your OpenOCD version is up to date with support for your debugger; a known usable version is at https://github.com/xpack-dev-tools/openocd-xpack/releases/tag/v0.12.0-4

When all set, flash the binary with:
```bash
make SOC=gd32vf103 BOARD=gd32vf103c_t_display upload
```

### Start System

Connect to the development board via serial port.

## Expected Results

The system should boot normally and provide information via the onboard serial port.

## Actual Results

The system booted up normally, and information are viewable via the onboard serial port.

### Boot Log

```log
Nuclei SDK Build Time: Feb 24 2025, 16:20:57
Download Mode: FLASHXIP
CPU Frequency 108000000 Hz
Start ucosii...
create start task success
start all task...
task3 is running... 1
task2 is running... 1
task1 is running... 1
task3 is running... 2
task2 is running... 2
task1 is running... 2
task3 is running... 3
task2 is running... 3
task3 is running... 4
task2 is running... 4
task1 is running... 3
task3 is running... 5
task2 is running... 5
task3 is running... 6
task2 is running... 6
task1 is running... 4
task3 is running... 7
task2 is running... 7
task3 is running... 8
task2 is running... 8
task1 is running... 5
task3 is running... 9
task2 is running... 9
task3 is running... 10
task2 is running... 10
task1 is running... 6
task3 is running... 11
task2 is running... 11
task3 is running... 12
task2 is running... 12
task1 is running... 7
task3 is running... 13
task2 is running... 13
task3 is running... 14
task2 is running... 14
task1 is running... 8
task3 is running... 15
task2 is running... 15
task3 is running... 16
task2 is running... 16
task1 is running... 9
task3 is running... 17
task2 is running... 17
task3 is running... 18
task2 is running... 18
task1 is running... 10
task3 is running... 19
task2 is running... 19
task3 is running... 20
task2 is running... 20

(truncated)
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
