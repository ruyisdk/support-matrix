# Tina Linux LicheePi RV Dock 测试报告

## 测试环境

### 操作系统信息

- 系统版本：LicheeRV_Tina_hdmi_8723ds
- 下载链接：https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html#%E7%83%A7%E5%BD%95%E9%95%9C%E5%83%8F

### 硬件信息

- LicheePi RV Dock
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

1. 打开烧录软件 [PhoenixCard](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/tool)，选择烧录的固件，将内存卡通过读卡器插入电脑中
2. 选择 `启动卡` 选项
3. 选择正确的盘符
4. 点击 `烧卡`
5. 根据状态栏的颜色可以判断烧录结果：红色的话说明烧录失败，建议使用 `SD card Formatter` 格式化后再重新烧录一次

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Please press Enter to activate this console.



BusyBox v1.27.2 () built-in shell (ash)

    __  ___     _        __   _               
   /  |/  /__ _(_)_ __  / /  (_)__  __ ____ __
  / /|_/ / _ `/ /\ \ / / /__/ / _ \/ // /\ \ /
 /_/  /_/\_,_/_//_\_\ /____/_/_//_/\_,_//_\_\ 
 ----------------------------------------------
 Maix Linux (Neptune, 5C1C9C53)
 ----------------------------------------------
Trying to connect to SWUpdate...
root@MaixLinux:/# uname -a
Linux MaixLinux 5.4.61 #189 PREEMPT Thu Dec 23 07:30:37 UTC 2021 riscv64 GNU/Linux
root@MaixLinux:/# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvu
mmu             : sv39

root@MaixLinux:/# 
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
