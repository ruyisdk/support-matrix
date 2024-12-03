---
sys: rtthread
sys_ver: null
sys_var: null

status: basic
last_update: 2024-12-03
---

# RT-Thread Longan Nano Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/Nuclei-Software/nuclei-sdk
- Reference Installation Document: https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html
- Download Links:
    - SDK: https://github.com/Nuclei-Software/nuclei-sdk
    - Toolchain: https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
    - OpenOCD: https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz

### Hardware Information

- Longan Nano
- A USB to UART Debugger
- **JTAG Debugger**
- A Type-C Cable

## Installation Steps

### Environment Setup

Download and extract the toolchain and OpenOCD, then set up the toolchain directory:
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

### Compiling the Code

Compile RT-Thread:
```bash
cd application/rtthread/msh
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano clean
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano all
```

### Flashing the Image

Connect to the development board via your JTAG debugger. Note that the board should be powered on while flashing.

Make sure your debugger and OpenOCD binary is supported by the build system.
For the former, consider editing relevant settings in `../../../SoC/gd32vf103/Board/gd32vf103c_longan_nano/openocd_gd32vf103.cfg` to match your JTAG debugger.
e.g. with Sipeed SLogic Combo 8 debugger at DAP-Link mode:
```diff
diff --git a/SoC/gd32vf103/Board/gd32vf103c_longan_nano/openocd_gd32vf103.cfg b/SoC/gd32vf103/Board/gd32vf103c_longan_nano/openocd_gd32vf103.cfg
index 019218da..66895b18 100644
--- a/SoC/gd32vf103/Board/gd32vf103c_longan_nano/openocd_gd32vf103.cfg
+++ b/SoC/gd32vf103/Board/gd32vf103c_longan_nano/openocd_gd32vf103.cfg
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
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano upload
```
### System Startup

Connect to the development board via the serial port.

## Expected Results

The system should boot up normally, and information should be viewable via the onboard serial port.

## Actual Results

The system booted up normally, and information are viewable via the onboard serial port.

### Boot Log

```log
msh >
msh >help
RT-Thread shell commands:
list_timer       - list timer in system
list_mailbox     - list mail box in system
list_sem         - list semaphore in system
list_thread      - list thread
version          - show RT-Thread version information
ps               - List threads in the system.
help             - RT-Thread shell help.
nsdk             - msh nuclei sdk demo

msh >version

 \ | /
- RT -     Thread Operating System
 / | \     3.1.5 build Dec  3 2024
 2006 - 2020 Copyright by rt-thread team
msh >ps
thread   pri  status      sp     stack size max used left tick  error
-------- ---  ------- ---------- ----------  ------  ---------- ---
tshell     6  ready   0x000000d8 0x00001000    09%   0x00000004 000
tidle      7  ready   0x00000078 0x00000200    23%   0x00000020 000
main       2  suspend 0x000000b8 0x00000400    17%   0x00000013 000
msh >nsdk
Hello Nuclei SDK!
msh >

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

