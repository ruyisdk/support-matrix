# FreeRTOS Longan Nano 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/Nuclei-Software/nuclei-sdk
- 参考文档：https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html
- 下载链接：
    - SDK：https://github.com/Nuclei-Software/nuclei-sdk
    - toolchain：https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
    - openocd：https://www.nucleisys.com/download.php
        - https://download.nucleisys.com/upload/files/toolchain/openocd/nuclei-openocd-2024.02.28-linux-x64.tgz

### 硬件信息

- Longan Nano
- USB to UART 调试器一个
- **JTAG 调试器**
- type-c 线一根

## 安装步骤

### 配置环境

下载工具链和 OpenOCD 并解压，设置工具链目录：
```bash
wget https://download.nucleisys.com/upload/files/toolchain/gcc/nuclei_riscv_newlibc_prebuilt_linux64_nuclei-2024.tar.bz2
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

### 编译代码

编译 FreeRTOS:
```bash
cd application/freertos/demo/
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano clean
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano all
```

### 烧写镜像

```bash
make SOC=gd32vf103 BOARD=gd32vf103c_longan_nano upload
```

### 启动系统

通过串口连接开发板。

## 预期结果

系统正常启动，能够通过板载串口查看信息。

## 实际结果

CFT

### 启动信息

屏幕录像（从编译到启动）：

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT