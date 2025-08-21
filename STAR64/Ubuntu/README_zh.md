# Ubuntu Pine64 Star64 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 25.04
- 下载链接：https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
- 参考安装文档：https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
xz -d ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
sudo dd if=ubuntu-25.04-preinstalled-server-riscv64+jh7110.img of=/dev/sdX bs=1m status=progress
```

### 登录系统

1. 将 microSD 卡插入开发板

2. 将启动项设为 microSD 卡 (参见 [选择启动项](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection))

3. 使用 USB to UART 调试器连接到开发板上的 GPIO 引脚 (参见 [UART 控制台](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#uart-console))

4. 给开发板上电，当看到 “Hit any key to stop autoboot” 字样时，按下 Enter

5. 使用如下命令将镜像内附带的 U-Boot 刷写至 SPI Flash (开发板出厂自带的 U-Boot 不工作):

```bash
sf probe
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot-spl.bin.normal.out
sf update $kernel_addr_r 0 $filesize
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot.itb
sf update $kernel_addr_r 0x100000 $filesize
```

6. 断电，将启动项设为 SPI Flash (参见 [选择启动项](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection))

7. 给开发板上电，当看到 “Hit any key to stop autoboot” 字样时，按下 Enter

8. 使用如下命令重置 U-Boot 环境:

```bash
env default -f -a
env save
```
9. 断电并重新上电，等待启动完成

10. 使用用户名 `ubuntu` 和默认密码 `ubuntu`登陆

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

```log
ubuntu login: ubuntu
Password:
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password:
New password:
Retype new password:
Welcome to Ubuntu 25.04 (GNU/Linux 6.14.0-13-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Apr 15 02:59:18 UTC 2025

  System load:    1.02      Processes:             27
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   2%        IPv4 address for eth0: 10.10.10.2
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
Linux ubuntu 6.14.0-13-generic #13.2-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr  6 05:26:54 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 25.04"
NAME="Ubuntu"
VERSION_ID="25.04"
VERSION="25.04 (Plucky Puffin)"
VERSION_CODENAME=plucky
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=plucky
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

ubuntu@ubuntu:~$

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。