# openEuler RISC-V 23.09 VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/VisionFive2/
- 参考安装文档：https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过串口登录系统。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过图形界面登录。

## 实际结果

系统正常启动，成功通过图形界面登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

https://gitee.com/yunxiangluo/ruyisdk-test/blob/master/20240130/videos/VF2.mp4