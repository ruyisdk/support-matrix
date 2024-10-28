# RevyOS LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS 20240720
- 下载链接：[ISCAS mirror](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
- 参考安装文档：https://revyos.github.io/docs/

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C 电源适配器 / DC 电源一个
- USB-UART 调试器一个

## 安装步骤

### 下载并解压镜像

下载镜像，使用 `zstd` 解压镜像：

```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/boot-lpi4a-20240720_171951.ext4.zst
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/u-boot-with-spl-lpi4a.bin
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/root-lpi4a-20240720_171951.ext4.zst
zstd -d boot-lpi4a-20240720_171951.ext4.zst
zstd -d root-lpi4a-20240720_171951.ext4.zst

```

### 通过 `fastboot` 刷写到板载 eMMC

有两种方式进入 fastboot 模式：

#### 使用 boot 按钮进入 fastboot 模式

按住 **BOOT** 按钮，然后连接 USB-C 线（另一端连接 PC）进入 USB 烧录模式。

#### 使用 u-boot 进入 fastboot 模式

进入 u-boot 控制台后，中断 u-boot，使用以下命令进入 fastboot 模式：

```shell
fastboot usb 0
```

---

在 Linux 中使用 `lsusb` 命令，你会看到一个设备：`ID 2345:7654 T-HEAD USB download gadget`。

使用以下命令刷写镜像。

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a.bin 
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo fastboot flash boot boot-lpi4a-20240720_171951.ext4
sudo fastboot flash root root-lpi4a-20240720_171951.ext4

```

### 登录系统

通过串口或图形界面登录系统。

默认用户名：`debian`
默认密码：`debian`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

屏幕录制（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/GLrnMuapSQwQ1DufMCtaRYnkY.svg)](https://asciinema.org/a/GLrnMuapSQwQ1DufMCtaRYnkY)

```log
revyos-lpi4a login: debian
Password: 
[  300.207430] audit: type=1100 audit(1703432525.400:211): pid=589 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:authen'
[  300.229172] audit: type=1101 audit(1703432525.400:212): pid=589 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:accoun'
[  300.250545] audit: type=1006 audit(1703432525.400:213): pid=589 uid=0 old-auid=4294967295 auid=1000 tty=ttyS0 old-ses=41

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 5.10.113-th1520)

Linux revyos-lpi4a 5.10.113-th1520 #2024.07.20.13.28+d8f77de53 SMP PREEMPT Sat Jul 20 13:29:42 UTC  riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
[  300.586878] audit: type=1130 audit(1703432525.776:214): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=user-runti'
[  300.648819] audit: type=1101 audit(1703432525.840:215): pid=2082 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:accou'
[  300.669416] audit: type=1103 audit(1703432525.840:216): pid=2082 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:setcr'
[  300.689717] audit: type=1006 audit(1703432525.840:217): pid=2082 uid=0 old-auid=4294967295 auid=1000 tty=(none) old-ses1
[  300.806560] audit: type=1105 audit(1703432525.996:218): pid=2082 uid=0 auid=1000 ses=3 msg='op=PAM:session_open grantor'
[  300.850013] audit: type=1334 audit(1703432526.040:219): prog-id=64 op=LOAD
[  300.856980] audit: type=1334 audit(1703432526.040:220): prog-id=64 op=UNLOAD
debian@revyos-lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@revyos-lpi4a:~$ uname -a
Linux revyos-lpi4a 5.10.113-th1520 #2024.07.20.13.28+d8f77de53 SMP PREEMPT Sat Jul 20 13:29:42 UTC  riscv64 GNU/Linux
debian@revyos-lpi4a:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 1
hart            : 1
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 2
hart            : 2
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 3
hart            : 3
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。