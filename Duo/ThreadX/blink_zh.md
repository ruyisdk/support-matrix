# ThreadX Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 构建系统版本：Ubuntu 22.04 LTS x86_64
- 系统版本：[ThreadX-to-RISC-V64](https://github.com/saicogn/ThreadX-to-RISC-V64), commit [53010e6](https://github.com/saicogn/ThreadX-to-RISC-V64/commit/53010e6b5e5916c5e84c4faf4d1a93ad960dd566)
- 源码链接：[ThreadX-to-RISC-V64](https://github.com/saicogn/ThreadX-to-RISC-V64)
- 参考安装文档：[简介](https://github.com/saicogn/ThreadX-to-RISC-V64/blob/main/README_zh.md)

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- TF 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针

## 构建步骤

### 准备系统环境

```bash
sudo apt install -y pkg-config build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils jq python3-distutils scons parallel tree python3-dev python3-pip device-tree-compiler ssh cpio fakeroot libncurses5 flex bison libncurses5-dev genext2fs rsync unzip dosfstools mtools tcl openssh-client cmake expect -y
```

### 下载和构建

```bash
sudo apt-get install wget git make
git clone https://github.com/milkv-duo/duo-examples.git --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

此时会产生 `mailbox_test` 的可执行文件。

如此过程不正常，请参考 [项目简介](https://milkv.io/zh/docs/duo/getting-started/rtoscore) 排除故障。

### 部署可执行文件

将可执行文件拷贝到用户家目录下。

```bash
chmod +x mailbox_test
./mailbox_test
```

在串口中运行输出如下。

```log
[root@milkv-duo]~# ./mailbox_test 
RT: [507.950049]prvQueueISR
RT: [507.952485]recv cmd(19) from C906B, param_ptr [0x00000002]
RT: [507.958306]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x4
RT: [511.965433]prvQueueISR
RT: [511.967867]recv cmd(19) from C906B, param_ptr [0x00000003]
RT: [511.973689]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x3
```

## 预期结果

灯亮起三秒后熄灭。

## 实际结果

灯亮起三秒后熄灭。

录像：

https://github.com/ruyisdk/support-matrix/assets/17025286/c0350c17-5e94-4c07-96f7-a6b3f66c531c

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
