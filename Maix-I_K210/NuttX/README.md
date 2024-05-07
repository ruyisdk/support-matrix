# NuttX Maix-I K210 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/apache/nuttx
- 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/k210/boards/maix-bit/index.html
- 工具链：
    - toolchain: https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
    - openOCD(若需要进行调试): https://github.com/kendryte/openocd-kendryte 
    - kflash：https://github.com/kendryte/kflash.py

### 硬件信息

- Sipeed Maix-Bit (K210)

## 安装步骤

### 准备源码及环境

获取工具链，下载并解压。
```bash
wget https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
tar -xzvf riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

clone 仓库并进行配置：
```bash

mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```


### 进行编译

```bash
cd nuttx
make distclean
./tools/configure.sh maix-bit:nsh
make V=1
```

### 烧写镜像

使用 k_flash 进行烧写，工具链文档可见：https://github.com/kendryte/kflash.py

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx nuttx.bin
```

### 登录系统

通过串口连接开发板。

## 预期结果

构建成功，开发板正常输出启动信息。

## 实际结果

构建成功，开发板正常输出启动信息。

### 启动信息

屏幕录像（从刷写系统到启动）：
[![asciicast](https://asciinema.org/a/WlWIs9g3WqjlO9zX9t0pq2ZPU.svg)](https://asciinema.org/a/WlWIs9g3WqjlO9zX9t0pq2ZPU)

```log
NuttShell (NSH) NuttX-12.5.1
nsh> cat /proc/version
NuttX version 12.5.1 6e941aed8b-dirty May  7 2024 09:51:35 maix-bit:nsh
nsh>
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功