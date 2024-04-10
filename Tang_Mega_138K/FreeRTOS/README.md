# FreeRTOS Tang Mega 138K Pro 测试报告

## 测试环境

### 操作系统信息

- 构建系统：Linux
- FreeRTOS
- 源码下载链接：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
- 参考安装文档：https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
- 参考设计文档：https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf

### 硬件信息

- Tang Mega 138K Pro Dock

## 安装步骤

**以下以 Linux 系统下的构建为例，Windows 下请安装 AE350 SOC RDS，并在附带的 cygwin 环境下进行除注明外相同的操作**

*若不需要 IDE 功能，Windows 下构建不需要 RDS License*

### 拷贝并 patch 代码

FreeRTOS 代码位于源码压缩包内，ref_design/MCU_RefDesign/ae350_freertos 路径下。将其解压到您的工作区。


若为 Linux：patch Debug/makefile:
替换以下内容：
```diff
diff --git a/Debug/makefile b/Debug/makefile
index eb97e6d..232a162 100644
--- a/Debug/makefile
+++ b/Debug/makefile
@@ -117,7 +117,7 @@ $(SECONDARY_OUTPUT_PATH)/.PHONY.size: $(LINKER_OUTPUTS)
 
 $(SECONDARY_OUTPUT_PATH)/ae350-ddr.ld: $(SAG_SRCS)
 	@echo 'Invoking: LdSaG Tool'
-	nds_ldsag --version=v5 -t "$(ANDESIGHT_ROOT)/utils/nds32_template_v5.txt" "$(SAG_FILE)" -o $(LDSAG_OUT)
+	cp ../src/bsp/sag/ae350-ddr.ld $(LDSAG_OUT)
 	@echo 'Finished building: $@'
 	@echo ' '
 

```
失败请注意换行符应为 CRLF

替换工作路径：
```bash
find -name "*.mk" -exec sed -i "s|/cygdrive/E/RDS5/workspace/ae350_freertos|$(pwd)|g" {} \;
```

### 编译代码

#### Linux
解包交叉编译工具链，此处建议使用 nds32le-elf-mculib-v5。其位置以下记为 `$(nds32_path)`

编译目标文件：
```bash
cd Debug
make CROSS_COMPILE=$(nds32_path)/bin/riscv32-elf-
```

#### Windows
打开 RDS 自带的 cygwin 环境：
运行 RDS 安装目录下的 cygwin/Cygwin.bat

cd 到源码文件夹（磁盘在 `/cygdrive/$(盘符)` 下）

编译目标文件，以下 RDS_ROOT 应被替换为您 RDS 的安装路径：
```bash
cd Debug
make ANDESIGHT_ROOT=<RDS_ROOT> CROSS_COMPILE=<RDS_ROOT>/toolchains/nds32le-elf-mculib-v5/bin/riscv32-elf-
```

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