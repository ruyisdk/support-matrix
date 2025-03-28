# Melis YouMuPI(Yuzuki)-Lizard 测试报告

## 测试环境

### 操作系统信息

- SDK 链接：
    - 国外 - Google Drive：https://drive.google.com/drive/folders/1_HAZRddR69hRMZAVrxFrPZXFFQiV3vE0?usp=share_link
    - 国内 - 百度网盘：https://pan.baidu.com/s/115gVK-8Pt-vJi8jn2AWMYw?pwd=7n4q 提取码：7n4q
    - Docker：https://hub.docker.com/r/gloomyghost/yuzukilizard
- 参考文档：
    - https://dongshanpi.com/YuzukiHD-Lizard/01-BoardIntroduction/
    - https://tina.100ask.net/SdkModule/Linux_E907_DevelopmentGuide-01/

### 硬件信息

- Yuzuki Lizard 开发板

## 安装步骤

### 配置编译环境

建议使用 Docker 镜像：

```bash
docker pull gloomyghost/yuzukilizard
docker run -it gloomyghost/yuzukilizard /bin/bash
```

或者参照如下步骤手动下载SDK并配置：

```bash
cat tina-v853-open.tar.gz.* > tina-v853-open.tar.gz
tar -xzvf tina-v853-open.tar.gz
git clone https://github.com/DongshanPI/Yuzukilizard-v851s-TinaSDK
cp -rfvd Yuzukilizard-v851s-TinaSDK/* tina-v853-open/
mv tina-v853-open tina-v853-docker
```


### 配置系统并编译

```bash
cd ~/tina-v853-docker
source build/envsetup.sh
lunch
```
选择对应方案。

**若出现问题，请尝试换用 bash 而非 zsh 等其他 shell 环境**

配置 E907 启动 RTOS：
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

编译和打包大核 Tina-Linux:
```bash
make -j$(nproc)
p
```

> 若出现链接器报告 `yyloc` 重定义：
> 这是由于 GCC 版本高于 10，更改 `scripts/dtc/dtc-parser.tab.c` 下的 `YYLTYPE yyloc` 为 `extern YYLTYPE yyloc`

配置 E907 小核 RTOS：

```bash
cd ~/e907_rtos/rtos/source
source melis-env.sh
lunch
```

编译 RTOS：
```bash
make menuconfig
make
```
生成的 RTOS 固件在 `ekernel/melis30.bin`。

### 登录系统

连接 UART3 查看串口输出。

## 预期结果

系统正常启动，能够通过串口查看输出。

## 实际结果

CFI

官方文档给出的步骤可编译出小核固件，但无法打包进 armv7 大核的 Linux 镜像中，且并未明确说明正常启动小核的方式。

### 启动信息


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFI