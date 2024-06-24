# Arch Linux MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：
    - Image Builder: https://github.com/sehraf/d1-riscv-arch-image-builder
    - U-Boot: https://github.com/smaeul/u-boot.git
    - RootFS: https://archriscv.felixc.at
- 参考安装文档：https://github.com/sehraf/d1-riscv-arch-image-builder

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 安装依赖

使用 Arch Linux 安装依赖如下：
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

### 选择 dtb 文件

下载 builder 后，更改 consts.sh:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
vim consts.sh
```

选择 dtb：
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..6fc61d5 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-mangopi-mq-pro
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

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

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`archriscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT