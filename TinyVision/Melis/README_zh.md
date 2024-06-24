# Melis TinyVision 测试报告

## 测试环境

### 操作系统信息

- SDK 链接：
    - 百度网盘：链接：https://pan.baidu.com/s/1oIqGjCCtvUe0_k_kgXkusw?pwd=0kdr 提取码：0kdr
- 参考文档：
    - https://dongshanpi.com/YuzukiHD-Lizard/01-BoardIntroduction/
    - https://tina.100ask.net/SdkModule/Linux_E907_DevelopmentGuide-01/

### 硬件信息

- TinyVision 开发板


## 安装步骤

### 解压 SDK

下载 SDK 后，合并压缩包，并解压：
```bash
tar -xzvf tina-v851se.tar.gz
```

由于默认的 sdk 并未支持此开发板，所以我们需要支持此开发板的配置 单独拷贝增加到 tina-v853-open sdk 内，首先 clone 此开发板补丁仓库，然后单独覆盖：
```bash
git clone  https://github.com/DongshanPI/TinyVision-v851se_TinaSDK
cp -rfvd  TinyVision-v851se_TinaSDK/* tina-v851/
```


### 配置系统并编译

下载 SDK 后，进行配置环境工作：
```bash
cd tina-v853-open
source build/envsetup.sh
lunch
```
选择对应方案。

**若出现问题，请尝试换用 bash 而非 zsh 等其他 shell 环境**

配置 E906 启动 RTOS：
```bash
cconfigs
cd ../default/
vim boot_package_nor.cfg
```
```diff
--- boot_package_nor.cfg.bak    2024-05-09 15:59:28.706860360 +0800
+++ boot_package_nor.cfg        2024-05-09 16:40:10.476852456 +0800
@@ -4,6 +4,7 @@
 item=optee,                  optee.fex
 item=u-boot,                        u-boot-spinor.fex
 item=dtb,                    sunxi.fex
+item=melis-elf,              riscv.fex
 ;item=logo,                   bootlogo.bmp.lzma
 ;item=shutdowncharge,         bempty.bmp.lzma
 ;item=androidcharge,          battery_charge.bmp.lzma
```
```bash
vim boot_package.cfg
```
```diff
--- boot_package.cfg.bak        2024-05-09 16:39:35.356852125 +0800
+++ boot_package.cfg    2024-05-09 16:40:01.263519036 +0800
@@ -4,6 +4,7 @@
 item=optee,                  optee.fex
 item=u-boot,                 u-boot.fex
 item=dtb,                    sunxi.fex
+item=melis-elf,              riscv.fex
 ;item=logo,                   bootlogo.bmp.lzma
 ;item=shutdowncharge,         bempty.bmp.lzma
 ;item=androidcharge,          battery_charge.bmp.lzma
```

配置 kernel：
```bash
ckernel
m kernel_menuconfig
```
Include `Device Drivers` 下的 `Mailbox Hardware Support`；
Include `Device Drivers → Mailbox Hardware Support` 下的 `sunxi Mailbox` 和 `sunxi rv32 standby driver`：
```diff
--- .config.old 2024-05-09 16:42:29.690187100 +0800
+++ .config     2024-05-09 16:45:57.840189075 +0800
@@ -3174,7 +3174,12 @@
 # CONFIG_SH_TIMER_MTU2 is not set
 # CONFIG_SH_TIMER_TMU is not set
 # CONFIG_EM_TIMER_STI is not set
-# CONFIG_MAILBOX is not set
+CONFIG_MAILBOX=y
+CONFIG_SUNXI_MBOX=y
+CONFIG_SUNXI_RV32_STANBY=y
+# CONFIG_PLATFORM_MHU is not set
+# CONFIG_ALTERA_MBOX is not set
+# CONFIG_MAILBOX_TEST is not set
 CONFIG_IOMMU_API=y
 CONFIG_IOMMU_SUPPORT=y
 
@@ -3192,6 +3197,7 @@
 # Remoteproc drivers
 #
 # CONFIG_STE_MODEM_RPROC is not set
+# CONFIG_SUNXI_RPROC is not set
 
 #
 # Rpmsg drivers
@@ -3304,6 +3310,7 @@
 # Firmware Drivers
 #
 CONFIG_ARM_PSCI_FW=y
+# CONFIG_ARM_SCPI_PROTOCOL is not set
 # CONFIG_FIRMWARE_MEMMAP is not set
 # CONFIG_FW_CFG_SYSFS is not set
 CONFIG_HAVE_ARM_SMCCC=y
```
```bash
mkernel -j
```

> 若出现链接器报告 `yyloc` 重定义：
> 这是由于 GCC 版本高于 10，更改 `scripts/dtc/dtc-parser.tab.c` 下的 `YYLTYPE yyloc` 为 `extern YYLTYPE yyloc`

配置 RTOS：
```bash
mmelis menuconfig
```

### 构建并打包

```bash
make -j$(nproc)
```

### 登录系统

连接 UART3 查看串口输出。

## 预期结果

系统正常启动，能够通过串口查看输出。

## 实际结果

CFT

### 启动信息

屏幕录像：

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT