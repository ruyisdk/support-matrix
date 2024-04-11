# RevyOS Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS (w/mainline kernel)
- 下载链接
  - 系统镜像：[root-lpi4amain-20240127_105111.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/root-lpi4amain-20240127_105111.ext4.zst)
  - boot 镜像：[boot-lpi4amain-20240127_105111.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/boot-lpi4amain-20240127_105111.ext4.zst)
  - u-boot 镜像（8G RAM）：[u-boot-with-spl-lc4a-main.bin](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/u-boot-with-spl-lc4a-main.bin)
  - u-boot 镜像（16G RAM）：[u-boot-with-spl-lc4a-16g-main.bin](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/u-boot-with-spl-lc4a-16g-main.bin)
- 参考安装文档：https://revyos.github.io/

### 硬件信息

- Lichee Cluster 4A 8G / 16G
- DC 12V 电源
- USB-A to A
    - 或 LPi4A 底板
- 网络和网线（注意连接到 BMC 而非交换机）

## 安装步骤

*以下以刷写到集群中一号板为例*

### 连接对应 SOM

使用 A to A 线缆连接 SOM。

### 刷写镜像

使用 `zstd` 解压镜像。

```bash
zstd -d boot-lpi4amain-20240127_105111.ext4.zst
zstd -d root-lpi4amain-20240127_105111.ext4.zst
```

使用 `fastboot` 刷写镜像
```bash
sudo ./fastboot flash ram u-boot-with-spl-lc4a-main.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot u-boot-with-spl-lc4a-main.bin
sudo ./fastboot flash boot boot-lpi4amain-20240127_105111.ext4
sudo ./fastboot flash root root-lpi4amain-20240127_105111.ext4
```

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc`  **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

默认用户名：`debian`
默认密码：`debian`

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/TVYy7DGHQR3O71I9BGJL0bECY.svg)](https://asciinema.org/a/TVYy7DGHQR3O71I9BGJL0bECY)

```log
Debian GNU/Linux 12 lpi4amain ttyS0

lpi4amain login: [   25.687999] platform aon:soc_lcd0_vdd18_en: deferred probe pending
[   25.694254] platform aon:soc_avdd28_rgb: deferred probe pending
[   25.700242] platform aon:soc_dovdd18_rgb: deferred probe pending
[   25.706303] platform aon:soc_avdd25_ir: deferred probe pending
[   25.712189] platform aon:soc_dovdd18_ir: deferred probe pending
[   25.718180] platform aon:soc_dvdd12_ir: deferred probe pending
[   25.724063] platform aon:soc_cam2_avdd25_ir: deferred probe pending
[   25.730376] platform aon:soc_cam2_dvdd12_ir: deferred probe pending
[   25.736694] platform aon:soc_cam2_dovdd18_ir: deferred probe pending
[   25.743102] platform aon:soc_dvdd12_rgb: deferred probe pending
[   25.749071] platform aon:soc_lcd0_vdd33_en: deferred probe pending
         Starting ssh.service - OpenBSD Secure Shell server...
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[FAILED] Failed to listen on ssh.so…penBSD Secure Shell server socket.
See 'systemctl status ssh.socket' for details.
[  OK  ] Finished firstboot.service - FirstBoot.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.
         Starting systemd-update-ut… Record Runlevel Change in UTMP...
[  OK  ] Finished systemd-update-ut… - Record Runlevel Change in UTMP.

lpi4amain login: [   40.022409] soc_dovdd18_scan: disabling
[   40.026957] soc_dvdd12_scan: disabling
[   40.031410] soc_avdd28_scan_en: disabling

lpi4amain login: debian
Password: 

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 6.7.1-lpi4a)

Linux lpi4amain 6.7.1-lpi4a #1 SMP Mon Jan 22 16:37:48 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
debian@lpi4amain:~$ uname -a
Linux lpi4amain 6.7.1-lpi4a #1 SMP Mon Jan 22 16:37:48 UTC 2024 riscv64 GNU/Linux
debian@lpi4amain:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lpi4amain:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。