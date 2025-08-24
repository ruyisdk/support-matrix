# Milk-V Megrez OpenCloudOS 测试报告

## 测试环境

### 操作系统信息

- 下载链接: https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/ocs_developer_sdcard-megrez.img.xz

### 硬件信息

- Milk-V Megrez
- USB A to C / USB C to C 线缆
- microSD 卡
- 12V DC 电源/ATX 电源

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

用户名：`root`
默认密码: `riscv666!`

## 实际结果

### 启动信息

[![asciicast](https://asciinema.org/a/YWKSf8oS0nbcdNVny1qE6Czow.svg)](https://asciinema.org/a/YWKSf8oS0nbcdNVny1qE6Czow)

## 测试结论

系统正常启动，能够通过串口登录。
