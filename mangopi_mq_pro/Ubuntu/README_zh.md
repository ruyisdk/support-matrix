# Ubuntu MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz
- 参考安装文档：https://mangopi.org/mqpro

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -kd /path/to/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz
sudo dd if=/path/to/ubuntu-24.10-preinstalled-server-riscv64+nezha.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
Ubuntu 24.10 ubuntu ttyS0

ubuntu login: ubuntu
Password: 
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password: 
New password: 
Retype new password: 
Welcome to Ubuntu 24.10 (GNU/Linux 6.11.0-8-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Oct  7 18:11:55 UTC 2024

  System load:    1.12      Processes:             26
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   5%        IPv4 address for eth0: 10.10.10.2
  Swap usage:     0%

0 updates can be applied immediately.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.11.0-8-generic #8.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct  1 11:40:56 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.10"
NAME="Ubuntu"
VERSION_ID="24.10"
VERSION="24.10 (Oracular Oriole)"
VERSION_CODENAME=oracular
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=oracular
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ lscpu
Architecture:           riscv64
  Byte Order:           Little Endian
CPU(s):                 1
  On-line CPU(s) list:  0
Vendor ID:              0x5b7
  Model name:           thead,c906
    CPU family:         0x0
    Model:              0x0
    Thread(s) per core: 1
    Core(s) per socket: 1
    Socket(s):          1
    CPU(s) scaling MHz: 100%
    CPU max MHz:        1008.0000
    CPU min MHz:        408.0000
Caches (sum of all):    
  L1d:                  32 KiB (1 instance)
  L1i:                  32 KiB (1 instance)
NUMA:                   
  NUMA node(s):         1
  NUMA node0 CPU(s):    0
ubuntu@ubuntu:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。