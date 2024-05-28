# BuildRoot on Milk-V Mars

## 测试环境

### 操作系统信息

- BuildRoot
  - 源码链接：https://github.com/milkv-mars/mars-buildroot-sdk
  - 参考安装文档：https://github.com/milkv-mars/mars-buildroot-sdk
- 构建系统环境：Ubuntu 22.04.4 LTS in Docker

### 硬件信息

- Milk-V Mars
- USB to UART 调试器一个
- 杜邦线三根
- USB A to C 或 C to C 线缆一根
- USB 电源一个
- 有线网络连接

## 安装步骤

### 构建镜像

安装构建依赖：

```shell
sudo apt update
sudo apt install -y build-essential automake libtool texinfo bison flex gawk \
g++ git xxd curl wget gdisk gperf cpio bc screen texinfo unzip libgmp-dev \
libmpfr-dev libmpc-dev libssl-dev libncurses-dev libglib2.0-dev libpixman-1-dev \
libyaml-dev patchutils python3-pip zlib1g-dev device-tree-compiler dosfstools \
mtools kpartx rsync
```

拉取源码：

```shell
git clone https://github.com/milkv-mars/mars-buildroot-sdk.git --depth=1
```

检出到设备对应分支：

- Mars
  ```
  git checkout dev
  ```

- Mars CM eMMC
  ```
  git checkout dev-mars-cm
  ```

- Mars CM SD Card
  ```
  git checkout dev-mars-cm-sdcard
  ```

开始编译：

```shell
make -j$(nproc)
```

编译完成后会在 work 目录下生成如下镜像：

```
work/
├── visionfive2_fw_payload.img
├── image.fit
├── initramfs.cpio.gz
├── u-boot-spl.bin.normal.out
├── linux
    ├── arch/riscv/boot
    │   ├── dts
    │   │   └── starfive
    │   │       ├── jh7110-milkv-mars-cm-emmc.dtb
    │   │       ├── jh7110-milkv-mars-cm-sdcard.dtb
    │   │       ├── jh7110-milkv-mars.dtb
    │   │       ├── jh7110-visionfive-v2-ac108.dtb
    │   │       ├── jh7110-visionfive-v2.dtb
    │   │       ├── jh7110-visionfive-v2-wm8960.dtb
    │   │       ├── vf2-overlay
    │   │       │   └── vf2-overlay-uart3-i2c.dtbo
    │   └── Image.gz
    └── vmlinuz-5.15.0
```


### 构建 SD 卡镜像

继续构建 SD 卡镜像：
```bash
make buildroot_rootfs -j$(nproc)
make img
```

### 烧写 SD 卡

将刚才构建的镜像烧到 SD 卡中：
```bash
sudo dd if=work/sdcard.img of=/dev/sdX bs=4096
sync
```

### 登录系统

连接串口和有线网络，给 Mars 上电。

在 U-Boot 提示 `Hit any key to stop autoboot` 时按任意键打断启动流程，在计算机上运行 TFTP server。

```
setenv 192.168.xxx.xxx; setenv serverip 192.168.xxx.xxx;
tftpboot ${fdt_addr_r} jh7110-milkv-mars-cm-sdcard.dtb;
tftpboot ${kernel_addr_r} Image.gz;
tftpboot ${ramdisk_addr_r} initramfs.cpio.gz;
run chipa_set_linux;run cpu_vol_set;
booti ${kernel_addr_r} ${ramdisk_addr_r}:${filesize} ${fdt_addr_r}
```

用户名：`root`

密码：`starfive`

## 预期结果

镜像构建成功，系统正常启动，能够通过板载串口登录。能进入安装向导。

## 实际结果

系统构建成功，启动待测试 / CFT