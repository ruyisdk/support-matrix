# OpenHarmony v5.0.0.71 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 系统版本：OpenHarmony v5.0.0.71
- Repo Manifest: [riscv-sig/manifest](https://gitee.com/riscv-sig/manifest)
- 刷写工具：[TITANTOOLS](https://developer.spacemit.com/documentation?token=O6wlwlXcoiBZUikVNh2cczhin5d)
- 参考安装文档：[spacemit](https://developer.spacemit.com/documentation)

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- USB 转 UART 调试器一个
- USB Type-C 数据线一根

## 安装步骤

### 配置开发环境

目前 OpenHarmony 的 SDK 仅支持 Ubuntu focal 及以上版本。如果你使用的是其他操作系统，可以使用 Docker 镜像。

安装所需的软件包：
```bash
sudo apt-get update

sudo apt-get install binutils git git-lfs gnupg gperf build-essential zip curl zlib1g-dev gcc-multilib lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libxml2-utils xsltproc unzip m4 bc gnutls-bin python3-pip ruby ccache libgl1-mesa-dev g++-multilib libc6-dev-i386 flex bison default-jdk openssl libelf-dev lz4 genext2fs libncurses5 libssl-dev u-boot-tools dosfstools mtools python2 cpio nodejs npm android-tools-adb android-tools-fastboot android-sdk-ext4-utils android-sdk-libsparse-utils mtd-utils scons
```

### 下载源码

源码维护在 gitee 上，所以你需要一个 gitee 账号和一个 ssh 密钥来使用 repo。

设置好 gitee 账号后，克隆 repo：
```bash
mkdir ohos5
cd ohos5
repo init -u git@gitee.com:riscv-sig/manifest.git -b riscv/OpenHarmony-v5.0.0-Release --no-repo-verify --repo-url=https://gerrit-googlesource.lug.ustc.edu.cn/git-repo
repo sync -c
repo forall -c 'git lfs pull'
repo start OpenHarmony-v5.0.0-Release --all
```

### 安装预编译工具链

```bash
build/prebuilts_download.sh
```

### 编译源码

虽然官方列表中没有支持 bpi-f3，但是可以使用 `deb1` 的配置，它有相同的设备树。

建议使用 `ccache` 来加速编译过程。整个编译过程可能需要几个小时。

```bash
./build.sh --product-name deb1 --ccache
```

#### 如果：使用 SD 卡而不是 eMMC

如果你想使用 microSD 卡而不是 eMMC，你需要修改一些配置：

```bash
cd device/board/spacemit/deb1
grep -rl 'd4281000' ./ | xargs sed -i 's/d4281000/d4280000/g'
cd -
```

#### 如果：使用 MIPI DSI 显示而不是 HDMI

默认显示是 HDMI，如果你想使用 MIPI DSI 显示，你需要修改设备树：

```diff
diff --git a/kernel/linux/spacemit_kernel-6.6/arch/riscv/boot/dts/spacemit/k1-x_deb1.dts b/kernel/linux/spacemit_kernel-6.6/arch/riscv/boot/dts/spacemit/k1-x_deb1.dts.new
index 721d351..f34775c 100644
--- a/kernel/linux/spacemit_kernel-6.6/arch/riscv/boot/dts/spacemit/k1-x_deb1.dts
+++ b/kernel/linux/spacemit_kernel-6.6/arch/riscv/boot/dts/spacemit/k1-x_deb1.dts
@@ -208,11 +208,11 @@
        spacemit-dpu-escclk = <76800000>;
        dsi_1v2-supply = <&ldo_5>;
        vin-supply-names = "dsi_1v2";
-       status = "disabled";
+       status = "okay";
 };
 
 &dsi2 {
-       status = "disabled";
+       status = "okay";
 
        panel2: panel2@0 {
                status = "ok";
@@ -228,18 +228,18 @@
 };
 
 &lcds {
-       status = "disabled";
+       status = "okay";
 };
 
 &dpu_online2_hdmi {
        memory-region = <&dpu_resv>;
-       status = "okay";
+       status = "disabled";
 };
 
 &hdmi{
        pinctrl-names = "default";
        pinctrl-0 = <&pinctrl_hdmi_0>;
-       status = "okay";
+       status = "disabled";
 };
 
 &i2c0 {
```

### 生成镜像

```bash
./build/gen_zip.sh deb1
```

生成的镜像为 `out/deb1/packages/phone/images/openharmony-spacemit-deb1.zip`。

### 刷写镜像

刷写镜像需要使用 spacemit 提供的 TITANTOOLS。

它是一个 GUI 工具，以 AppImage 形式提供，所以你需要将其设置为可执行并运行。

```bash
chmod +x titantools_for_linux-2.0.1-Rc.AppImage
./titantools_for_linux-2.0.1-Rc.AppImage
```

#### 刷写镜像（Fastboot）

你可以使用 fastboot 来刷写镜像，使用以下命令：

```bash
sudo fastboot stage factory/FSBL.bin
sudo fastboot continue
sudo fastboot stage u-boot.itb
sudo fastboot continue
sudo fastboot flash gpt partition_universal.json
sudo fastboot flash bootinfo factory/bootinfo_sd.bin
sudo fastboot flash fsbl factory/FSBL.bin
sudo fastboot flash env env.bin
sudo fastboot flash opensbi fw_dynamic.itb
sudo fastboot flash uboot u-boot.itb
sudo fastboot flash boot boot.img
sudo fastboot flash ramdisk ramdisk.img
sudo fastboot flash updater updater.img
sudo fastboot flash sys_prod sys_prod.img
sudo fastboot flash chip_prod chip_prod.img
sudo fastboot flash system system.img
sudo fastboot flash vendor vendor.img
sudo fastboot flash userdata userdata.img
```

### 登录系统

通过串口或 HDMI 显示器登录系统。

## 预期结果

系统正常启动，能够通过板载串口和 HDMI 显示器登录。

## 实际结果

系统正常启动，成功通过板载串口和 HDMI 显示器登录。

### 启动信息

![sysinfo](./sysinfo.png)

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/TgUFTR6rbXmiBNrWaKqHkFv8b.svg)](https://asciinema.org/a/TgUFTR6rbXmiBNrWaKqHkFv8b)

```log
# begetctl dump api
Begin dump syspara
=======================
DeviceType:default
Manufacture:default
Brand:default
MarketName:OpenHarmony 3.2
ProductSeries:default
ProductModel:ohos
SoftwareModel:default
HardwareModel:default
Serial:7320052b95f4
OSFullName:OpenHarmony-5.0.0.71
DisplayVersion:OpenHarmony 5.0.0.71
BootloaderVersion:bootloader
GetSecurityPatchTag:2024/09/01
AbiList:riscv64
IncrementalVersion:default
VersionId:default/default/default/default/OpenHarmony-5.0.0.71/ohos/default/12/default/default
BuildType:default
BuildUser:default
BuildHost:default
BuildTime:default
BuildRootHash:default
GetOsReleaseType:Release
GetHardwareProfile:default
FirstApiVersion:1
GetSerial:7320052b95f4
acl serial:
GetDevUdid:6A9BC9718275333E50F82F6866646BEEFDF5223893CE84B633A7C268BA7EB1A2
Acl devUdid:
Version:5.0.0.71
GetSdkApiVersion:12
GetSystemCommitId:896
=======================
End dump syspara
# uname -a
Linux localhost 6.6.36 #1 SMP PREEMPT Fri Mar 28 01:16:56 CST 2025 riscv64
# cat /proc/cpuinfo                                                            
processor       : 0
hart            : 0
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 1
hart            : 1
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 2
hart            : 2
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 3
hart            : 3
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 4
hart            : 4
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 5
hart            : 5
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 6
hart            : 6
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

processor       : 7
hart            : 7
model name      : Spacemit(R) X60
isa             : rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu             : sv39
mvendorid       : 0x710
marchid         : 0x8000000058000001
mimpid          : 0x1000000049772200

```

### 注意

默认的加载器是 `ld-musl-riscv64.so.1`，你需要自己获取 glibc 加载器来运行基于 glibc 的应用程序。
