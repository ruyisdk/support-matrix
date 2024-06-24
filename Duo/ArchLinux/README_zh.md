# Arch Linux Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.img
- 下载链接：https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing
- 参考安装文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
unzip milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.zip
dd if=milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`milkv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
[root@archlinux ~]# uname -a                                                                                                        
Linux archlinux 5.10.4-tag- #1 PREEMPT Wed Oct 18 17:20:17 CEST 2023 riscv64 GNU/Linux                                              
[root@archlinux ~]# neofetch                                                                                                        
                   -`                                                                                                               
                  .o+`                   --------------                                                                             
                 `ooo/                   OS: Arch Linux riscv64                                                                     
                `+oooo:                  Host: Cvitek. CV180X ASIC. C906.                                                           
               `+oooooo:                 Kernel: 5.10.4-tag-                                                                        
               -+oooooo+:                Uptime: 54 secs                                                                            
             `/:-:++oooo+:               Packages: 143 (pacman)                                                                     
            `/++++/+++++++:              Shell: bash 5.1.16                                                                         
           `/++++++++++++++:             Terminal: /dev/ttyS0                                                                       
          `/+++ooooooooooooo/`           CPU: (1)                                                                                   
         ./ooosssso++osssssso+`          Memory: 23MiB / 54MiB                                                                      
        .oossssso-````/ossssss+`                                                                                                    
       -osssssso.      :ssssssso.                                                                                                   
      :osssssss/        osssso+++.                                                                                                  
     /ossssssss/        +ssssooo/-                                                                                                  
   `/ossssso+/:-        -:/+osssso+-                                                                                                
  `+sso+:-`                 `.-/+oso:                                                                                               
 `++:.                           `-/+/                                                                                              
 .`                                 `/                                                                                              
                                                                                                                                    
[root@archlinux ~]# 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/GIQOyBNHONziQszZ13HDhs2lP.svg)](https://asciinema.org/a/GIQOyBNHONziQszZ13HDhs2lP)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。