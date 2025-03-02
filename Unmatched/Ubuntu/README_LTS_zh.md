# Ubuntu 24.04.2 LTS HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04.2 LTS
- 下载链接：https://ubuntu.com/download/risc-v | [TUNA 镜像站](https://mirrors.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64%2Bunmatched.img.xz)
- 参考安装文档：https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 `dd` 刷写镜像到 microSD 卡

下载并解压镜像。使用 `dd` 刷写至 microSD 卡。

```shell
xzcat ubuntu-24.04.2-preinstalled-server-riscv64+unmatched.img.xz | sudo dd of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

初次登录时，系统会提示更改密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果
<details>
<summary>结果已过时（24.04）</summary>
系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to Ubuntu 24.04 LTS (GNU/Linux 6.8.0-31-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information disabled due to load higher than 1.0

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

ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
ubuntu@ubuntu:~$
```

屏幕录像：

[![asciicast](https://asciinema.org/a/Rh773h5eOalKZlzjQRFrQDnjY.svg)](https://asciinema.org/a/Rh773h5eOalKZlzjQRFrQDnjY)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
</details>
