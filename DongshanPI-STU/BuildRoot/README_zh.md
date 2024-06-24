# BuildRoot DongshanPI-哪吒 STU 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/DongshanPI/buildroot_dongshannezhastu
- 参考安装文档：https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/

### 硬件信息

- DongshanPI-哪吒 STU
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

CFT

### 启动信息


屏幕录像（从刷写镜像到登录系统）：

```log
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT