# FreeRTOS Longan Nano Test Report

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

### Configure Environment

Download and extract the toolchain and OpenOCD, then set the toolchain directory:
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
wget https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz
tar -xzvf nuclei-openocd-2024.02.28-linux-x64.tgz
export NUCLEI_TOOL_ROOT=$(pwd)
```

Download the SDK:
```bash
git clone https://github.com/Nuclei-Software/nuclei-sdk.git
cd nuclei-sdk
cat << EOF > setup_config.sh
NUCLEI_TOOL_ROOT=$(echo $NUCLEI_TOOL_ROOT)
EOF
source setup.sh
```

### Compile Code

Compile FreeRTOS:
```bash
cd application/freertos/demo/
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano clean
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano all
```

### Flash Image

```bash
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano upload
```

### Start System

Connect to the development board via serial port.

## Expected Results

The system should boot normally and provide information via the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from compilation to startup):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
