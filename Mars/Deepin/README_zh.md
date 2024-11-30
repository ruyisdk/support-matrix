# Debian Milk-V Mars 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Deepin preview
- 下载链接：https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-milkv-mars-20240613-123442.tar.xz
- 参考安装文档：https://milkv.io/zh/docs/mars/getting-started/boot

### 硬件信息

- Milk-V Mars
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

使用 `tar` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。


```bash
tar -xvf deepin-23-beige-preview-riscv64-milkv-mars-20240613-123442.tar.xz
sudo dd if=deepin-milkv-mars-riscv64-stable-desktop-installer.img of=/dev/sda bs=4M status=progress
```


### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`deepin`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
root@deepin-riscv64-jh7110:/etc# cat /etc/os-release                            
PRETTY_NAME="Deepin 23"                                                         
NAME="Deepin"                                                                
VERSION_ID="23"                                                                 
VERSION="23"                                                                    
ID=deepin                                                                       
HOME_URL="https://www.deepin.org/"                                              
BUG_REPORT_URL="https://bbs.deepin.org"                                         
VERSION_CODENAME=beige   
```

屏幕录像（从刷写镜像到登录系统）：
[![asciinema](https://asciinema.org/a/47e6PqDygxjmg19rxBMepkECt)](https://asciinema.org/a/47e6PqDygxjmg19rxBMepkECt)
## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT
