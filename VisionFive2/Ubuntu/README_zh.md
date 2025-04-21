# Ubuntu 25.04 VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 25.04
- 下载链接：https://ubuntu.com/download/risc-v
- 参考安装文档：https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```bash
xzcat ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz | sudo dd bs=1M conv=fsync of=/dev/<your-device>
```

### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置，可参考 StarFive [官方文档](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html)。

开发板本体上亦有丝印标注。

为了启动 Ubuntu 镜像，选择 SDIO3.0 模式（即：`RGPIO_0 = 1`, `RGPIO_1 = 0`）。

### 首次启动

插入 SD 卡并给开发板上电。当看到“Hit any key to stop autoboot:”消息时按 Enter 键进入 U-Boot 控制台以重置环境：

```
env default -f -a
env save
```

对电路板重新通电,第一次启动时，请等待直到看到输出类似为:
```log
[   42.864196] cloud-init[648]: Cloud-init v. 24.4~3+really24.3.1-0ubuntu4 finished at Fri, 04 Oct 2024 15:38:08 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net].  Up 42.85 seconds
```
确认 cloud-init 已完成。 Cloud init 负责生成 SSH 密钥并设置默认密码。

### 登录系统

通过串口登录系统。

默认用户名：`ubuntu`
默认密码：`ubuntu`

初次登录时，会提示更改默认密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

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
ubuntu@ubuntu:~$ lscpu
Architecture:             riscv64
  Byte Order:             Little Endian
CPU(s):                   4
  On-line CPU(s) list:    0-3
Vendor ID:                0x489
  Model name:             sifive,u74-mc
    CPU family:           0x8000000000000007
    Model:                0x4210427
    Thread(s) per core:   1
    Core(s) per socket:   4
    Socket(s):            1
    CPU(s) scaling MHz:   100%
    CPU max MHz:          1500.0000
    CPU min MHz:          375.0000
Caches (sum of all):
  L1d:                    128 KiB (4 instances)
  L1i:                    128 KiB (4 instances)
  L2:                     2 MiB (1 instance)
NUMA:
  NUMA node(s):           1
  NUMA node0 CPU(s):      0-3
Vulnerabilities:
  Gather data sampling:   Not affected
  Ghostwrite:             Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Not affected
  Spectre v1:             Not affected
  Spectre v2:             Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 3
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
