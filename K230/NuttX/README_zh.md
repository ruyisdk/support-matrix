# NuttX CanMV K230 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/apache/nuttx
- 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/k230/boards/canmv230/index.html
- 工具链：
    - SDK: https://github.com/kendryte/k230_sdk
    - 启动镜像：https://gitee.com/yf1972/filexfers/tree/canmv230-tools-for-nuttx-v1.2
    - SBI：https://github.com/yf13/k230osbi
    - toolchain: https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack
    - kflash：https://github.com/kendryte/kflash.py

### 硬件信息

- 开发板：Canaan Kendryte K230
- USB A to C / USB C to C 线缆
- SD 卡
- 网络连接与 TFTP 服务器

## 安装步骤

### 准备源码及环境

获取预构建启动映像：
```bash
wget https://gitee.com/yf1972/filexfers/releases/download/canmv230-tools-for-nuttx-v1.2/canmv230-opensbi-dtb.tar.xz
wget https://gitee.com/yf1972/filexfers/releases/download/canmv230-tools-for-nuttx-v1.2/canmv230-sdcard.img.xz
```

获取工具链：
```bash
wget https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v13.2.0-2/xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz
tar -xvzf xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

clone 仓库并进行配置：
```bash
mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```


### 构建 NuttX

```bash
cd nuttx
make distclean
./tools/configure.sh canmv230:nsh
make -j$(nproc)
```

### 烧写镜像

在 SD 卡上烧写 SBI 环境：
```bash
unxz -k canmv230-sdcard.img.xz
sudo dd if=canmv230-sdcard.img of=/dev/your/device bs=1M status=progress
```

### 启动 NuttX

将构建出的 nuttx.bin 放入 TFTP 服务器中，在 U-boot 控制台中加载并运行（请手动中断 autoboot）：
```bash
k230# usb start
k230# env edit serverip
env: your.tftp.server.ip
k230# dhcp
k230# ping $serverip
k230# tftp 8000000 nuttx.bin
k230# go 8000000
```

### 登录系统

通过串口连接开发板。

## 预期结果

构建成功，开发板正常输出启动信息。

## 实际结果

构建成功，开发板正常输出启动信息。

### 启动信息

屏幕录像（从刷写系统到启动）：
[![asciicast](https://asciinema.org/a/wxzebwRRYH909rIlx69ISi3ar.svg)](https://asciinema.org/a/wxzebwRRYH909rIlx69ISi3ar)

```log
## Starting application at 0x08000000 ...
ABC
NuttShell (NSH) NuttX-12.5.1
nsh> cat /proc/version
NuttX version 12.5.1 6e941aed8b May  7 2024 10:24:29 canmv230:nsh
nsh> 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功