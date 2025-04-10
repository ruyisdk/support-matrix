# Guix System VisionFive 2 测试报告

## 测试环境

### 操作系统信息

- 源码链接: https://git.savannah.gnu.org/cgit/guix.git/tree/gnu/system/images/visionfive2.scm
- 下载链接: https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image

### 硬件信息

- StarFive VisionFive 2
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- microSD 读卡器一个
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

用户名：root
无密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT
