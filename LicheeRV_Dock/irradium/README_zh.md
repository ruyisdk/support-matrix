# Irradium LicheeRV Dock 测试报告

## 测试环境

### 操作系统信息

- 下载链接: https://dl.irradium.org/irradium/images/lichee_rv_dock/
- 参考安装文档: https://dl.irradium.org/irradium/images/lichee_rv_dock/README.TXT

### 硬件信息

- Sipeed Lichee RV Dock
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

```sh
zstd -d  irradium-3.7-riscv64-core-lichee_rv_dock-6.1.120-build-20241217.img.zst 
sudo dd if=irradium-3.7-riscv64-core-lichee_rv_dock-6.1.120-build-20241217.img of=/dev/<your-device> bs=1M status=progress 
```


### 登录系统

通过串口登录系统。

无密码,初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log

irradium  (lichee-rv-dock) (ttyS0)

lichee-rv-dock login: root
You are required to change your password immediately (administrator enforced).
New password: 
Retype new password: 
 _                   _  _             
|_| ___  ___  ___  _| ||_| _ _  _____ 
| ||  _||  _|| .'|| . || || | ||     |
|_||_|  |_|  |__,||___||_||___||_|_|_|
 _  _       _                              _            _   
| ||_| ___ | |_  ___  ___    ___  _ _    _| | ___  ___ | |_ 
| || ||  _||   || -_|| -_|  |  _|| | |  | . || . ||  _|| '_|
|_||_||___||_|_||___||___|  |_|   \_/   |___||___||___||_,_|

# uname -a
Linux lichee-rv-dock 6.1.120 #1 Sun Dec 15 23:35:12 EET 2024 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=irradium
VERSION="3.7"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org/"
BUG_REPORT_URL="https://irradium.org/bugs/"
# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
