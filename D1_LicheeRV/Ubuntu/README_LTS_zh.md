# Ubuntu 24.04.1 LTS D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04.1 LTS
- 下载链接：https://ubuntu.com/download/risc-v
    - 或者镜像站：[Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.04.1/release/ubuntu-24.04.1-preinstalled-server-riscv64%2Bnezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.04.1/release/ubuntu-24.04.1-preinstalled-server-riscv64%2Blicheerv.img.xz)

- 参考安装文档：https://wiki.ubuntu.com/RISC-V/LicheeRV

### 硬件信息

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 将镜像写入至 microSD 卡。

### 登录系统

通过串口登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
ubuntu login: ubuntu
Password: 
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password: 
New password: 
Retype new password: 
The password has not been changed.
New password: 
Retype new password: 
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-41-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Aug 27 15:32:33 UTC 2024

  System load:    1.15      Processes:             27
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   5%        IPv4 address for eth0: 10.10.10.2
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
Linux ubuntu 6.8.0-41-generic #41.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 13 09:58:43 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

ubuntu@ubuntu:~$ 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
