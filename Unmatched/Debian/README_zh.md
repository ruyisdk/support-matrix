# Debian bookworm/sid HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian bookworm/sid
- 下载链接：https://people.debian.org/~deiv/riscv/debian-sid-risc-v-sifive-unmatched.tar.xz
- 参考安装文档：https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 解压并烧录镜像到 microSD 卡

`/dev/sdc` 为 microSD 卡所在位置，请根据实际情况更改。

```bash
tar xvf debian-sid-risc-v-sifive-unmatched.tar.xz
sudo dd if=debian-sid-risc-v-sifive-unmatched.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`root`
默认密码：`sifive`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Debian GNU/Linux bookworm/sid unmatched ttySIF0                                                                       
                                                                                                                      
unmatched login: root                                                                                                 
Password:                                                                                                             
Linux unmatched 5.14.0-3-riscv64 #1 SMP Debian 5.14.12-1 (2021-10-14) riscv64                                         
                                                                                                                      
The programs included with the Debian GNU/Linux system are free software;                                             
the exact distribution terms for each program are described in the                                                    
individual files in /usr/share/doc/*/copyright.                                                                       
                                                                                                                      
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent                                                     
permitted by applicable law.                                                                                          
root@unmatched:~# uname -a                                                                                            
Linux unmatched 5.14.0-3-riscv64 #1 SMP Debian 5.14.12-1 (2021-10-14) riscv64 GNU/Linux                               
root@unmatched:~# cat /etc/os-release                                                                                 
PRETTY_NAME="Debian GNU/Linux bookworm/sid"                                                                           
NAME="Debian GNU/Linux"                                                                                               
ID=debian                                                                                                             
HOME_URL="https://www.debian.org/"                                                                                    
SUPPORT_URL="https://www.debian.org/support"                                                                          
BUG_REPORT_URL="https://bugs.debian.org/"                                                                             
root@unmatched:~# cat /proc/cpuinfo                                                                                   
processor       : 0                                                                                                   
hart            : 4                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 1                                                                                                   
hart            : 1                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 2                                                                                                   
hart            : 2                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 3                                                                                                   
hart            : 3                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
root@unmatched:~# 
```

屏幕录像（从刷写镜像到登录系统）

[![asciicast](https://asciinema.org/a/YjvmONomTstvHYU4yLnKVX7Rv.svg)](https://asciinema.org/a/YjvmONomTstvHYU4yLnKVX7Rv)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。