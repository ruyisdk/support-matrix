---
sys: buildroot
sys_ver: null
sys_var: null

status: cfi
last_update: 2025-03-15
---

# BuildRoot DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/DongshanPI/buildroot_dongshannezhastu
- Reference Installation Document: https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/

### Hardware Information

- DongshanPI-Nezha STU
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Compiling SDK

Download the SDK:
```bash
git clone  https://github.com/DongshanPI/buildroot_dongshannezhastu
cd buildroot_dshannezhastu
git submodule update --init --recursive
git submodule update --recursive --remote
```

Compile the SD card image:
```bash
cd buildroot-awol/
make  BR2_EXTERNAL="../br2lvgl  ../br2qt5 ../br2nezhastu"  dongshannezhastu_sdcard_core_defconfig
make -j$(nproc)
```

Notes: 1. Set `BR2_TOOLCHAIN_EXTERNAL_URL` of `./output/build/buildroot-config/autoconf.h` to `https://github.com/YuzukiHD/sunxi-bsp-toolchains/releases/download/1.0.0/riscv64-glibc-gcc-thead_20200702.tar.xz`。

2. On errors like this:

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
Comment out relevant `#ifndef HAVE_PIDFS_SEND_SIGNAL` and `#ifndef HAVE_PIDFD_OPEN` sections in `./output/build/host-util-linux-2.37.4/include/pidfd-utils.h`; see https://github.com/milkv-duo/duo-buildroot-sdk/issues/74


### Flashing Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=dongshannezhastu-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

Unable to fetch necessary resources during compilation:

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

### Boot Log

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFI
