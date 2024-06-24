# FreeRTOS Demo M0P Dock 测试报告

## 测试环境

### 操作系统信息

- 构建系统：Ubuntu 22.04.4 LTS
- 源码链接：https://github.com/sipeed/M0P_BL618_examples
- 参考安装文档：https://github.com/sipeed/M0P_BL618_examples
    - 环境配置：
        - https://github.com/bouffalolab/bouffalo_sdk#environment-setup
        - https://bl-mcu-sdk.readthedocs.io/zh_CN/latest/get_started/get_started.html
- 工具链：https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux

### 硬件信息

- Sipeed M0P Dock (BL618)
- USB A to C 或 C to C 线缆一根

## 安装步骤

### 准备构建环境

```shell
git clone https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux --depth=1
export PATH=$PWD/toolchain_gcc_t-head_linux/bin:$PATH
sudo apt install ninja-build make
git clone https://github.com/sipeed/M0P_BL618_examples.git
cd M0P_BL618_examples
git submodule update --init
cd bouffalo_sdk
# git config --global user.name user
# git config --global user.email user@example.com
git am ../sipeed_support/fixes/m0pdock/*.patch && cd -
cd sipeed_support/examples/m0pdock
# Replace ttyACMx with your actual device name
make flash COMX=/dev/ttyACM0
```

### 构建 FreeRTOS Demo

```shell
cd M0P_BL618_examples
git submodule update --init
cd bouffalo_sdk
# git config --global user.name user
# git config --global user.email user@example.com
git am ../sipeed_support/fixes/m0pdock/*.patch && cd -
cd sipeed_support/examples/m0pdock/wifi_screen
make # Or: make ninja
```

### 烧录镜像

```shell
make flash COMX=/dev/ttyACM0 # Replace ttyACMx with your actual device name
```

### 在开发板上启动 UDP Server

此处参考：https://github.com/sipeed/M0P_BL618_examples/tree/main/sipeed_support/examples/m0pdock/wifi_screen

### 启动信息

```shell
bouffalolab />wifi_sta_connect SIPEED_TEST 12345678
bouffalolab />wifi_udp_server
bouffalolab />udp server task start ...
wifi_udp_server [port]
         port: local listen port, default port 5001
udp bind success!
Server ip Address : 0.0.0.0:5001
Press CTRL-C to exit.
recv[2/204800] from 172.49.14.160
recv[10240/204798] from 172.49.14.160
recv[10240/194558] from 172.49.14.160
recv[10240/184318] from 172.49.14.160
recv[10240/174078] from 172.49.14.160
recv[10240/163838] from 172.49.14.160
```



## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。