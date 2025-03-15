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
- postmarketOS
  - 下载链接（pmbootstrap）: https://wiki.postmarketos.org/wiki/Pmbootstrap
  - 参考安装文档：https://wiki.postmarketos.org/index.php?title=MangoPi_MQ-Pro_(mangopi-mq-pro)&direction=prev&oldid=46021
- FreeBSD
  - 下载链接：https://github.com/freebsd-d1/freebsd-d1
  - 参考安装文档：https://github.com/freebsd-d1/freebsd-d1
### 硬件开发板信息

- DongshanPI-哪吒 STU 开发板

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告） |
| ----------------------- | -------- | -------------------- |
| Tina-Linux 镜像启动     | N/A      | [成功][Tina]         |
| OpenWrt 镜像启动        | N/A      | [成功][OpenWrt]      |
| Debian 镜像启动         | N/A      | [成功][Debian]       |
| Arch Linux 镜像启动     | N/A      | [CFT][Arch]          |
| BuildRoot 镜像启动      | N/A      | [CFI][BuildRoot]     |
| postmarketOS 编译和启动 | N/A      | [成功][pmOS]         |
| FreeBSD 镜像编译和启动  | N/A      | [成功][FreeBSD]      |

[Tina]: ./TinaLinux/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Arch]: ./ArchLinux/README_zh.md
[pmOS]: ./postmarketOS/README_zh.md
[FreeBSD]: ./FreeBSD/README_zh.md