# DongshanPI-哪吒 STU

## 测试环境

### 操作系统信息

- Tina Linux
  - 下载链接：https://pan.baidu.com/s/13uKlqDXImmMl9cgKc41tZg?pwd=qcw7
  - 参考安装文档：https://d1.docs.aw-ol.com/study/study_1tina/
- Debian
  - 下载链接：https://github.com/DongshanPI/NezhaSTU-ReleaseLinux
  - 参考安装文档：https://github.com/DongshanPI/NezhaSTU-ReleaseLinux
- OpenWrt
  - 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=dongshan_nezha_stu
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- BuildRoot:
  - 下载链接：https://github.com/DongshanPI/buildroot_dongshannezhastu
  - 参考安装文档：https://dongshanpi.com/DongshanNezhaSTU/07-Buildroot-SDK_DevelopmentGuide/
- Arch Linux
  - 打包脚本：https://github.com/sehraf/d1-riscv-arch-image-builder

### 硬件开发板信息

- DongshanPI-哪吒 STU 开发板

## 测试结果

| 软件分类                       | 软件包名     | 测试结果（测试报告）        |
|----------------------------|--------------|---------------------------|
| Tina-Linux 镜像启动            | N/A          | [CFT][Tina]       |
| OpenWrt 镜像启动               | N/A          | [CFT][OpenWrt]         |
| Debian 镜像启动                | N/A          | [CFT][Debian]          |
| Arch Linux 镜像启动            | N/A          | [CFT][Arch]            |
| BuildRoot 镜像启动             | N/A          | [CFT][BuildRoot]       |

[Tina]: ./TinaLinux/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Arch]: ./ArchLinux/README_zh.md