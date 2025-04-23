# Arch Linux DongshanPI-Nezha STU 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Initial Release
- 打包脚本：https://github.com/sehraf/d1-riscv-arch-image-builder

### 硬件信息

- DongshanPI-Nezha STU
- Type-C 电源线一根
- UART 转 USB 调试器一个
- SD 卡

## 安装步骤

### 安装依赖

使用 Arch Linux 安装依赖如下：
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

### 编译设置

下载源码后，更改 consts.sh:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
vim consts.sh
```

选择 dtb：
```shell
export DEVICE_TREE=sun20i-d1-dongshan-nezha-stu
```

同时修改 `1_compile.sh` 以修复类似 https://github.com/The-OpenROAD-Project/OpenROAD/issues/6451 的问题：
```diff
diff --git a/1_compile.sh b/1_compile.sh
index 4fcbc7c..bf62caf 100755
--- a/1_compile.sh
+++ b/1_compile.sh
@@ -80,6 +80,7 @@ if [ ! -f "${OUT_DIR}/u-boot-sunxi-with-spl.bin" ]; then
     clean_dir ${DIR}

     git clone --depth 1 "${SOURCE_UBOOT}" -b "${TAG_UBOOT}"
+    sed -i 's/SWIG_Python_AppendOutput/SWIG_AppendOutput/g' u-boot/scripts/dtc/pylibfdt/libfdt.i_shipped
     cd ${DIR}
     pin_commit "${COMMIT_UBOOT}"
```

### 生成镜像

运行 `1_compile.sh`：
```bash
./1_compile.sh
```

### 刷写镜像

运行 `2_create_sd.sh`：

```bash
2_create_sd.sh /dev/your/device
```

**若开启了 USE_CHROOT（默认开启），其会之后自动 chroot 进镜像等待配置。建议这步安装如 vim 等基本应用。**


### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`archriscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
Arch Linux 6.8.0 (ttyS0)

licheerv login: root
Password:

[root@licheerv ~]# uname -a
Linux licheerv 6.8.0 #1 SMP Wed Apr 16 14:52:24 CST 2025 riscv64 GNU/Linux
[root@licheerv ~]# cat /etc/os-release
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo
[root@licheerv ~]# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

[root@licheerv ~]#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。