# BuildRoot DongshanPI-Nezha STU 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/DongshanPI/buildroot_dongshannezhastu
- 参考安装文档：https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/

### 硬件信息

- DongshanPI-Nezha STU
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 编译 SDK

下载 SDK：
```bash
git clone  https://github.com/DongshanPI/buildroot_dongshannezhastu
cd buildroot_dshannezhastu
git submodule update --init --recursive
git submodule update --recursive --remote
```

编译 sd 卡镜像：
```bash
cd buildroot-awol/
make  BR2_EXTERNAL="../br2lvgl  ../br2qt5 ../br2nezhastu"  dongshannezhastu_sdcard_core_defconfig
make -j$(nproc)
```

注：1. 修改 `./output/build/buildroot-config/autoconf.h` 中的 `#define BR2_TOOLCHAIN_EXTERNAL_URL` 为 `https://github.com/YuzukiHD/sunxi-bsp-toolchains/releases/download/1.0.0/riscv64-glibc-gcc-thead_20200702.tar.xz`。

2. 如编译过程遇到形如以下报错
```
misc-utils/kill.c: In function ‘kill_with_timeout’:
misc-utils/kill.c:395:20: error: implicit declaration of function ‘pidfd_open’; did you mean ‘fdopen’? [-Wimplicit-function-declaration]
  395 |         if ((pfd = pidfd_open(ctl->pid, 0)) < 0)
      |                    ^~~~~~~~~~
      |                    fdopen
misc-utils/kill.c:395:20: warning: nested extern declaration of ‘pidfd_open’ [-Wnested-externs]
misc-utils/kill.c:400:13: error: implicit declaration of function ‘pidfd_send_signal’; did you mean ‘SYS_pidfd_send_signal’? [-Wimplicit-function-declaration]
  400 |         if (pidfd_send_signal(pfd, ctl->numsig, &info, 0) < 0)
      |             ^~~~~~~~~~~~~~~~~
      |             SYS_pidfd_send_signal
misc-utils/kill.c:400:13: warning: nested extern declaration o
```
请注释掉 `./output/build/host-util-linux-2.37.4/include/pidfd-utils.h` 的 `#ifndef HAVE_PIDFS_SEND_SIGNAL` 和 `#ifndef HAVE_PIDFD_OPEN` 的相应字段；见 https://github.com/milkv-duo/duo-buildroot-sdk/issues/74

### 烧写镜像

使用 dd 将镜像烧写到 SD 卡：
```bash
sudo dd if=dongshannezhastu-sdcard.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

编译时无法获取资源：

```log
GIT_DIR=/path/to/buildroot_dongshannezhastu/buildroot-awol/dl/opensbi/git/.git git clean -ffdx 
ERROR: opensbi-666fa35305c44340e793a21f7bbfac4528756a5f-br1.tar.gz has wrong sha256 hash:
ERROR: expected: 7fa3960547daca44972e2f7767016c7b1fb1735ce1d95c38902ee4a6bec58656
ERROR: got     : 357b8967c5f3ad6931b8ebce9e6707cec7009234dcd32e23307cb82ae0860ebf
ERROR: Incomplete download, or man-in-the-middle (MITM) attack
wget --passive-ftp -nd -t 3 -O '/path/to/buildroot_dongshannezhastu/buildroot-awol/output/build/.opensbi-666fa35305c44340e793a21f7bbfac4528756a5f-br1.tar.gz.cZ2aTx/output' 'http://sources.buildroot.net/opensbi/opensbi-666fa35305c44340e793a21f7bbfac4528756a5f-br1.tar.gz' 
--2025-03-15 14:30:22--  http://sources.buildroot.net/opensbi/opensbi-666fa35305c44340e793a21f7bbfac4528756a5f-br1.tar.gz
Resolving sources.buildroot.net (sources.buildroot.net)... 104.26.1.37, 104.26.0.37, 172.67.72.56, ...
Connecting to sources.buildroot.net (sources.buildroot.net)|104.26.1.37|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2025-03-15 14:30:24 ERROR 404: Not Found.
```

### 启动信息

```log
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFI