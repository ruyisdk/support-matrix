# ArchLinux LicheeRV / AWOL Nezha D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Initial Release
- 打包脚本：https://github.com/sehraf/d1-riscv-arch-image-builder

### 硬件信息

- Nezha D1
- Type-C 电源线一根
- UART 转 USB 调试器一个
- SD 卡

## 安装步骤

### 使用打包脚本

使用 Archlinux 安装依赖如下：
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```


社区创建了自动打包 ArchLinux 的脚本。您若想使用，可直接跳过以下所有安装过程。

clone 对应仓库：
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
```

根据具体的板子，修改 `consts.sh` 中的 `DEVICE_TREE`，如以下是 Lichee RV 的：
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..0b990ad 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-lichee-rv
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

运行 `1_compile.sh` 编译镜像；
运行 `2_create_sd.sh /dev/your/device` 烧写到 SD 卡。

注：若其自动配置 rootfs，需要：`arch-install-scripts`, `qemu-user-static-bin (AUR)`, `binfmt-qemu-static (AUR)`。不需要此环节可以将 `consts.sh` 中的 `USE_CHROOT` 设为 0。

```bash
./1_compile.sh
./2_create_sd.sh /dev/your/device
```

**若开启了 USE_CHROOT（默认开启），其会之后自动 chroot 进镜像等待配置。建议这步安装如 vim 等基本应用。**

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`archriscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/D86o9kqp6phQBswrEEBt4rwyv.svg)](https://asciinema.org/a/D86o9kqp6phQBswrEEBt4rwyv)

```log
Arch Linux 6.8.0 (ttyS0)

licheerv login: root
Password: 
[root@licheerv ~]# neofetch
                   -`                                                                                                      
                  .o+`                   ------------- 
                 `ooo/                   OS: Arch Linux riscv64 
                `+oooo:                  Host: Allwinner D1 Nezha 
               `+oooooo:                 Kernel: 6.8.0 
               -+oooooo+:                Uptime: 1 min 
             `/:-:++oooo+:               Packages: 119 (pacman) 
            `/++++/+++++++:              Shell: bash 5.2.26 
           `/++++++++++++++:             Terminal: /dev/ttyS0 
          `/+++ooooooooooooo/`           CPU: (1) 
         ./ooosssso++osssssso+`          Memory: 55MiB / 970MiB 
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.                                
      :osssssss/        osssso+++.                               
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/

[root@licheerv ~]# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功