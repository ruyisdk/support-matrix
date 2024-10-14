# BuildRoot DongshanPI-哪吒 STU 测试报告

## 测试环境

### 操作系统信息

- 下载链接： https://github.com/zuoyi001/zue_sophpi-huashan
- 参考安装文档： https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1692610610938/%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA-%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.pdf , https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1692610600110/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97-1.%E7%83%A7%E5%BD%95%E5%9B%BA%E4%BB%B6.pdf


### 硬件信息

- 华山派
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 编译 SDK

下载 SDK：
```bash
sudo apt-get update
sudo apt-get install -y build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils android-sdk-ext4-utils jq cmake python3-distutils tclsh scons parallel ssh-client tree python3-dev python3-pip device-tree-compiler ssh cpio fakeroot libncurses5 flex bison

git clone https://github.com/sophgo/sophpi-huashan.git
cd sophpi-huashan
```

编译镜像：
```bash
cd cvi_media_sdk/
source build/cvisetup.sh 
defconfig cv1812h_wevb_0007a_emmc
build_all 
```

### 烧写镜像

格式化 SD 卡：
```bash
sudo mkfs.vfat -F 32 /dev/<your-device>
```

将烧写档案放入 SD 卡中:
```
.
├── fip.bin
├── boot.emmc (minimal Linux image)
├── rootfs.emmc (rootFS)
├── system.emmc (rw 分区)
├── cfg.emmc (config rw)
└── fw_payload_uboot.bin (bootloader + uboot)
``` 

插卡上电开机后，会自动进入升级，升级完成后，会停留在 uboot,拔掉 SD 卡，输入 re 重启进入系统

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
