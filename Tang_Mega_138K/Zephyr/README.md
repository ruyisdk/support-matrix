# Zephyr Tang Mega 138K Pro 测试报告

## 测试环境

### 操作系统信息

- 构建系统：Linux
- FreeRTOS
- 源码下载链接：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
- 参考安装文档：https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
- 参考设计文档：https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf

### 硬件信息

- FreeRTOS Tang Mega 138K Pro Dock

## 安装步骤

**以下以 Linux 系统下的构建为例，Windows 下请安装 AE350 SOC RDS，并在附带的 cygwin 环境下进行除注明外相同的操作**

*若不需要 IDE 功能，Windows 下构建不需要 RDS License*

### 拷贝代码

Zephyr 代码位于源码压缩包内，ref_design/MCU_RefDesign/ae350_zephyr 路径下。将其解压到您的工作区。

### 编译代码

进入到代码目录下，设置环境变量：
```bash
source zephyr-env.sh
export ZEPHYR_TOOLCHAIN_VARIANT='cross-compile
```

设置交叉编译工具链，此处建议使用 nds32le-elf-mculib-v5：
```bash
export CROSS_COMPILE=path/to/nds32le-elf-mculib-v5/bin/riscv32-elf-
```

Windows 下该文件在 RDS 安装目录下的 toolchains 中。

进入 hello_world 目录：
```bash
cd samples/hello_world
```

准备构建文件：
```bash
mkdir build
cd build
cmake -DBOARD=adp_xc7k_ae350 ../
```

图形化配置构建选项：`make menuconfig`

构建源码：`make`


### 生成 FPGA 码流

**Tang Mega 138K 支持仅在商业版中提供**

FPGA 工程位于位于源码压缩包内，ref_design/FPGA_RefDesign/Tang_MEGA_138K_Pro_Dock/ae350_demo 路径下。

使用高云云源软件，打开该工程后，进行综合、布线布局和生成码流。

### 下载码流

连接 FPGA，使用高云云源软件下载码流。

### 烧录程序

使用 ICEman，将生成的 bin 文件烧录至 flash 中。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT