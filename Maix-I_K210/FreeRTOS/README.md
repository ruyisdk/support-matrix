# FreeRTOS Maix-I K210 测试报告

## 测试环境

### 操作系统信息

- 构建系统：Ubuntu 22.04.4 LTS (Docker)
- 源码链接：https://github.com/kendryte/kendryte-freertos-sdk
- 参考安装文档：https://github.com/kendryte/kendryte-freertos-sdk
- 工具链：https://github.com/kendryte/kendryte-gnu-toolchain/releases/tag/v8.2.0-20190409

### 硬件信息

- Sipeed Maix-I (K210)

## 安装步骤

### 创建 Docker 环境

```shell
sudo docker run -it --name ubuntu2204 ubuntu:22.04
```

以下所有操作在 Ubuntu 22.04.4 LTS Docker 的 root shell 中进行。

### 准备构建环境

```shell
apt update
apt install -y cmake git curl bzip2
cd /opt
curl -LO https://github.com/kendryte/kendryte-gnu-toolchain/releases/download/v8.2.0-20190409/kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.bz2
tar xvf kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.bz2
cd
```

### 构建 hello_world

拉取 FreeRTOS 仓到本地并构建。

```shell
git clone --depth=1 https://github.com/kendryte/kendryte-freertos-sdk
cd kendryte-freertos-sdk
mkdir build && cd build
cmake .. -DPROJ=hello_world -DTOOLCHAIN=/opt/kendryte-toolchain/bin
make -j$(nproc)
```

构建结束后，在源码目录下生成 `hello_world` 和 `hello_world.bin` 两个文件。

```log
[100%] Linking C executable hello_world                                             
Generating .bin file ...                                                            
[100%] Built target hello_world                                                     
root@4b1ebf5f94f4:~/kendryte-freertos-sdk/build# file hello_world
hello_world: ELF 64-bit LSB executable, UCB RISC-V, RVC, single-float ABI, version 1 (SYSV), statically linked, with debug_info, not stripped
```

### 烧录镜像

若使用 JLink 来运行或者调试程序，使用 `hello_world`。

若需要直接烧录至开发板，使用 `hello_world.bin`。

### 登录系统

通过串口连接开发板。

## 预期结果

构建成功，开发板正常输出 Hello World 信息。

## 实际结果

构建成功。

### 启动信息

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT