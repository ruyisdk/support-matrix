# RT-Thread Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 构建系统版本：Ubuntu 20.04 LTS x86_64
- 系统版本：RT-Thread 5.1.0, commit [3ff4fe5](https://github.com/RT-Thread/rt-thread/commit/3ff4fe5395516eb734b2cead9cc50f35e54f6511)
- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv1800b

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针

## 构建步骤

### 准备系统环境

注意，请使用 Ubuntu 20.04，已知在更新版本的系统上可能出现构建失败。

可以使用 Docker 等容器环境进行构建。

安装依赖包：

```shell
sudo apt update && sudo apt install -y git gcc build-essential scons libncurses5-dev python3 python3-requests curl
```

获取工具链：

```shell
curl -LO https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
tar xvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
export RTT_EXEC_PATH=~/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

### 拉取源码并编译固件

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv1800b
# 生成配置文件
scons --menuconfig
source ~/.env/env.sh
scons -j$(nproc) --verbose
cd ../
bash combine-fip.sh
```

执行结束后，会在 `cvitek` 目录下生成 boot.sd 和 fip.bin 两个文件。

### 准备 microSD 卡

清空 microSD 卡（可使用 `wipefs -af /path/to/your-card`），并创建一个 FAT32 分区。

将构建出的 boot.sd 和 fip.bin 复制进 microSD 卡。至此，存储卡已经可用来在 Duo 上启动 RT-Thread。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Boot from SD ...                                                                                                                    
switch to partitions #0, OK                                                                                                         
mmc0 is current device                                                                                                              
173704 bytes read in 10 ms (16.6 MiB/s)                                                                                             
## Loading kernel from FIT Image at 81400000 ...                                                                                    
   Using 'config-cv1800b_milkv_duo_sd' configuration                                                                                
   Trying 'kernel-1' kernel subimage                                                                                                
   Verifying Hash Integrity ... crc32+ OK                                                                                           
## Loading fdt from FIT Image at 81400000 ...                                                                                       
   Using 'config-cv1800b_milkv_duo_sd' configuration                                                                                
   Trying 'fdt-cv1800b_milkv_duo_sd' fdt subimage                                                                                   
   Verifying Hash Integrity ... sha256+ OK                                                                                          
   Booting using the fdt blob at 0x814255c4                                                                                         
   Uncompressing Kernel Image                                                                                                       
   Decompressing 424720 bytes used 58ms                                                                                             
   Loading Device Tree to 0000000081be5000, end 0000000081becb60 ... OK                                                             
                                                                                                                                    
Starting kernel ...                                                                                                                 
                                                                                                                                    
heap: [0x8029be68 - 0x8129be68]                                                                                                     
                                                                                                                                    
 \ | /                                                                                                                              
- RT -     Thread Smart Operating System                                                                                            
 / | \     5.1.0 build Mar 26 2024 05:52:37                                                                                         
 2006 - 2024 Copyright by RT-Thread team                                                                                            
Hello RT-Smart!                                                                                                                     
msh />  
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl.svg)](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。