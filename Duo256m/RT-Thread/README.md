# RT-Thread Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv1800b
   - 工具链：https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 构建步骤

### 拉取源码并编译固件

获取工具链并配置：
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1705395512373/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
tar -xzvf Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1-20240115.tar.gz
```

自行更改以下路径：
```bash
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.1/bin
```

获取依赖：
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
```

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/
# 生成配置文件
scons --menuconfig
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
bash combine-fip.sh
```

请选择 256m 版本

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

```

屏幕录像（从刷写镜像到登录系统）：


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT