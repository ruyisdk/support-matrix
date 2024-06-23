# Tina Linux MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：链接：https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol 提取码：awol
- 参考安装文档：https://d1.docs.aw-ol.com/study/study_1tina/

### 硬件信息

- MangoPi MQ Pro
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 编译 SDK

下载并解压 SDK 后，加入新目标：
```bash
git clone https://github.com/Tina-Linux/Tina_d1x_mangopi-sbc.git
cp -r Tina_d1x_mangopi-sbc tina_d1_open_v2_2
```

编译并打包：
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### 烧写镜像

使用 dd 将镜像烧写到 SD 卡：
```bash
sudo dd if=tina_d1-h.img of=/dev/your/device bs=1M status=progress
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