# openKylin 0.9.5 VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：openKylin 0.9.5
- 下载链接：[https://www.openkylin.top/downloads/old_releases.html](https://www.openkylin.top/downloads/old_releases.html)
- 参考安装文档：[https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/openKylin.img.xz
sudo dd if=/path/to/openKylin.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `openkylin`
默认密码： `openkylin`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/TgWQuZfKq1nb1CKJYuO4eyr8i.svg)](https://asciinema.org/a/TgWQuZfKq1nb1CKJYuO4eyr8i)

```log
openKylin 0.9.5 openkylin ttyS0

openkylin login: openkylin
密码： 
Welcome to openKylin 0.9.5 (GNU/Linux 5.18.0-rc4-starfive-rc5 riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

openkylin@openkylin:~$ uname -a
Linux openkylin 5.18.0-rc4-starfive-rc5 #1 SMP Wed Apr 27 17:02:33 CST 2022 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="0.9.5 (yangtze)"
VERSION_US="0.9.5 (yangtze)"
ID=openkylin
PRETTY_NAME="openKylin 0.9.5"
VERSION_ID="0.9.5"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=yangtze
PRODUCT_FEATURES=3
openkylin@openkylin:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。