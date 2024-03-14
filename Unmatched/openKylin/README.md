# openKylin 1.0 HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openKylin 1.0
- 下载链接：https://www.openkylin.top/downloads
- 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）或图形界面登录系统。

默认用户名：`openkylin`
默认密码：`openkylin`

## 预期结果

系统正常启动，能够通过板载串口或图形界面登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to openKylin 1.0 (GNU/Linux 5.11.0-1030-generic riscv64)                                                      
                                                                                                                      
 * Support:        https://openkylin.top                                                                              
                                                                                                                      
The programs included with the openKylin system are free software;                                                    
the exact distribution terms for each program are described in the                                                    
individual files in /usr/share/doc/*/copyright.                                                                       
                                                                                                                      
openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by                                               
applicable law.                                                                                                       
                                                                                                                      
To run a command as administrator (user "root"), use "sudo <command>".                                                
See "man sudo_root" for details.                                                                                      
                                                                                                                      
openkylin@openkylin:~$                                                                                                
openkylin@openkylin:~$ cat /etc/os-release                                                                            
NAME="openKylin"                                                                                                      
FULL_NAME="openKylin"                                                                                                 
VERSION="1.0 (yangtze)"                                                                                               
VERSION_US="1.0 (yangtze)"                                                                                            
ID=openkylin                                                                                                          
PRETTY_NAME="openKylin 1.0"                                                                                           
VERSION_ID="1.0"                                                                                                      
HOME_URL="https://www.openkylin.top/"                                                                                 
VERSION_CODENAME=yangtze                                                                                              
PRODUCT_FEATURES=3                                                                                                    
openkylin@openkylin:~$ cat /proc/cpuinfo                                                                              
processor       : 0                                                                                                   
hart            : 4                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 1                                                                                                   
hart            : 1                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 2                                                                                                   
hart            : 2                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 3                                                                                                   
hart            : 3                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
openkylin@openkylin:~$ 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/Wgz7wgCph6BhEQpEskH4LDMd4.svg)](https://asciinema.org/a/Wgz7wgCph6BhEQpEskH4LDMd4)