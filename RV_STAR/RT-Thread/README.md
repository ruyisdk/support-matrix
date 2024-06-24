# RT-Thread RV-STAR Test Report

## Test Environment

### Operating System Information

- Source Code Link: [https://github.com/Nuclei-Software/nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk)
- Reference Installation Document:
    - PlatformIO Core: [https://docs.platformio.org/en/latest/core/installation/index.html](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO ch32v: [https://pio-ch32v.readthedocs.io/en/latest/installation.html](https://pio-ch32v.readthedocs.io/en/latest/installation.html)
- Download Links:
    - SDK: [https://github.com/Nuclei-Software/nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk)
    - Toolchain: [https://www.nucleisys.com/download.php](https://www.nucleisys.com/download.php)
        - [https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2](https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2)
    - OpenOCD: [https://www.nucleisys.com/download.php](https://www.nucleisys.com/download.php)
        - [https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz](https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz)

### Hardware Information

- RV-STAR Development Board (GD32VF103VBT6)

## Installation Steps

### Configure the Environment

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

### Compiling the Code

Compile FreeRTOS:
```bash
cd application/rtthread/demo
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar clean
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar all
```

### Flashing the Image

```bash
make SOC=gd32vf103 BOARD=gd32vf103v_rvstar upload
```

### Booting the System

Connect to the development board via serial port.

## Expected Results

The system should boot normally and display information through the onboard serial port.

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
