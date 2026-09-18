# Ubuntu 24.04.5 VisionFive 2 Lite 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04.5 LTS 
- 系统镜像：`ubuntu-24.04.5-preinstalled-server-riscv64+jh7110.img.xz`
- 下载链接：[Download Canonical-built Ubuntu for RISC-V Platforms | Ubuntu](https://ubuntu.com/download/risc-v/canonical-built#starfive-visionfive-2-lite)
- 参考安装文档：https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/starfive-visionfive-2/

### 硬件信息

- StarFive VisionFive 2 Lite
- Type-C 电源适配器
- Type-C 数据线
- USB 转 TTL 串口模块
- 杜邦线三根

## 安装步骤

### 解压系统镜像

下载系统镜像：

```
ubuntu-24.04.5-preinstalled-server-riscv64+jh7110.img.xz
```

解压得到对应的 `.img` 镜像文件，用于后续 eMMC 烧录。

### 连接串口并进入 Fastboot

下载并解压 SFFB Tool：

```
https://files.waveshare.net/wiki/VisionFive2/SFFB_Tool_V1.0.7z
```

准备 Tera Term 串口工具。

使用 USB 转 TTL 串口模块连接 VisionFive 2 Lite 40Pin 上对应的串口引脚。

开发板一侧：

```
GND    TX    RX
```

分别连接串口模块：

```
GND    RX    TX
```

将串口模块连接电脑 USB 口，打开 Tera Term，将波特率设置为：

```
115200
```

给开发板上电，同时在串口窗口中按任意键打断自动启动，进入 U-Boot 命令行。

执行：

```
fastboot usb 0
```

进入 Fastboot 模式。

### 安装驱动并烧录镜像

打开 Windows 设备管理器，确认出现：

```
USB Download Gadget
```

选择：

```
更新驱动程序
→ 浏览我的电脑以查找驱动程序
```

驱动目录选择：

```
SFFB_Tool_V1.0\usb_driver
```

完成驱动安装。

打开 SFFB Tool，选择解压后的系统镜像，然后点击：

```
Start All
```

或：

```
Action → Run
```

开始烧录镜像。

等待镜像传输完成后给开发板断电。

### 首次启动

重新给 VisionFive 2 Lite 上电，通过串口观察启动过程，等待系统进入 Ubuntu 登录界面。

### 登录系统

通过串口登录系统。

默认用户名：

```
ubuntu
```

初始密码：

```
ubuntu
```

首次登录时，系统会强制要求修改初始密码，请按提示设置自己的新密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```
Ubuntu 24.04.5 LTS ubuntu ttyS0 

ubuntu login: ubuntu                                                            
Password:                           
Welcome to Ubuntu 24.04.5 LTS (GNU/Linux 7.0.0-31-generic riscv64)              
                                                                                
 * Documentation:  https://help.ubuntu.com                                      
 * Management:     https://landscape.canonical.com                              
 * Support:        https://ubuntu.com/pro                                       
                                                                                
 System information as of Tue Sep  8 03:00:04 UTC 2026                          
                                                                                
  System load:    1.04      Processes:             21                           
  Usage of /home: unknown   Users logged in:       0                            
  Memory usage:   3%        IPv4 address for eth0: 10.10.10.2                   
  Swap usage:     0%                                                            
                                                                                
Expanded Security Maintenance for Applications is not enabled.                  
                                                                                
0 updates can be applied immediately.                                           
                                                                                
Enable ESM Apps to receive additional future security updates.                  
See https://ubuntu.com/esm or run: sudo pro status                              
                                                                                
                                                                                
                                                                                
The programs included with the Ubuntu system are free software;                 
the exact distribution terms for each program are described in the              
individual files in /usr/share/doc/*/copyright.                                 
                                                                                
Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by            
applicable law.                                                                 
                                                                                
To run a command as administrator (user "root"), use "sudo <command>".          
See "man sudo_root" for details.                                                
                                                                                
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 7.0.0-31-generic #31.1~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 25 15:43:59 UTC riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ lscpu
Architecture:                riscv64
  Byte Order:                Little Endian
CPU(s):                      4
  On-line CPU(s) list:       0-3
NUMA:                        
  NUMA node(s):              1
  NUMA node0 CPU(s):         0-3
Vulnerabilities:             
  Gather data sampling:      Not affected
  Ghostwrite:                Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Old microcode:             Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Not affected
  Spectre v1:                Not affected
  Spectre v2:                Not affected
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
  Vmscape:                   Not affected
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39                                                                                                                                                                  uarchA Z for hel: sifive,u74-mc| NOR | Minicom 2.9 | VT102 | 脱机 | ttyUSB0                                                                                                             mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

ubuntu@ubuntu:~$ 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
