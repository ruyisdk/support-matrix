# Milk-V Vega BuildRoot 构建测试报告

## 测试环境

### 操作系统信息

- Host: Ubuntu 22.04.3 LTS x86_64
- Milk-V Vega Switch
- 参考文档：https://milkv.io/zh/docs/vega/getting-started/buildroot-sdk
- Issue/CFH: https://github.com/milkv-vega/vega-buildroot-sdk/issues/1
  - BuildRoot 构建失败

## 操作步骤

### 构建依赖包安装

```bash
sudo apt install -y make git gcc g++ bison flex device-tree-compiler mtd-utils
```

### 获取 SDK

```bash
git clone --depth=1 https://github.com/milkv-vega/vega-buildroot-sdk
```

### 构建固件

```bash
cd vega-buildroot-sdk/
./build.sh
```

> 注意：初次构建过程中会连接至 GitHub 自动下载所需的工具链。请确保您的互联网连接正常。

构建成功后会在 `out` 目录输出三个镜像：

```
out/
├── freeloader.bin
├── kernel.bin
└── ubifs.img
```

### 预期结果

构建成功，烧写后可以正常启动。

### 实际结果

固件构建失败，日志如下。

```log
In file included from /usr/include/signal.h:328,
                 from ./signal.h:52,
                 from c-stack.c:49:
c-stack.c:55:26: error: missing binary operator before token "("
   55 | #elif HAVE_LIBSIGSEGV && SIGSTKSZ < 16384
      |                          ^~~~~~~~
  CC       closein.o
make[6]: *** [Makefile:1915: c-stack.o] Error 1
make[6]: *** Waiting for unfinished jobs....
  CC       closeout.o
  CC       dirname.o
make[5]: *** [Makefile:1674: all] Error 2
make[4]: *** [Makefile:1572: all-recursive] Error 1
make[3]: *** [Makefile:1528：all] 错误 2
make[2]: *** [package/pkg-generic.mk:269：/home/mx/vega-buildroot-sdk/work/buildroot_initramfs/build/host-m4-1.4.18/.stamp_built] 错误 2
make[1]: *** [Makefile:84：_all] 错误 2
make[1]: 离开目录“/home/mx/vega-buildroot-sdk/buildroot”
make: *** [Makefile:128：/home/mx/vega-buildroot-sdk/work/buildroot_initramfs/images/rootfs.tar] 错误 2
copy lib and usr/sbin and www
cp: 目标 '/home/mx/vega-buildroot-sdk/work/buildroot_initramfs_sysroot/lib' 不是目录
cp: 目标 '/home/mx/vega-buildroot-sdk/work/buildroot_initramfs_sysroot/usr/sbin' 不是目录
cp: 无法创建目录 '/home/mx/vega-buildroot-sdk/work/buildroot_initramfs_sysroot/usr': 没有那个文件或目录
copy etc files
mkdir: 无法创建目录 "/home/mx/vega-buildroot-sdk/work/buildroot_initramfs_sysroot/usr/etc": 没有那个文件或目录
cp: 目标 '/home/mx/vega-buildroot-sdk/work/buildroot_initramfs_sysroot/usr/etc' 不是目录
copy files to install
create file system
~/vega-buildroot-sdk/install ~/vega-buildroot-sdk
###Generating rootfs###
rootfs: ubifs web
1.gen sh
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/mnt/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/mnt/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/mnt/': 没有那个文件或目录
2.clean /root and /dev of rootfs
3.cp file to rootfs
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/mnt/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/mnt/': 没有那个文件或目录
ln: 无法创建符号链接 '../work/buildroot_initramfs_sysroot/etc/init.d/S40initconfig.sh': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/root/': 没有那个文件或目录
cp: 目标 '../work/buildroot_initramfs_sysroot/root/' 不是目录
cp: 无法创建目录 '../work/buildroot_initramfs_sysroot/dev': 没有那个文件或目录
chmod: 无法访问 '../work/buildroot_initramfs_sysroot/bin/busybox': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/root/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/root/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/root/': 没有那个文件或目录
chmod: 无法访问 '../work/buildroot_initramfs_sysroot/root/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/usr/sbin/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/usr/sbin/': 没有那个文件或目录
chmod: 无法访问 '../work/buildroot_initramfs_sysroot/usr/sbin/i2c_dev_msg_muti': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/root/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/etc/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/usr/bin/': 没有那个文件或目录
./install/cp.sh: 第 146 行： cd: ../work/buildroot_initramfs_sysroot/usr/bin: 没有那个文件或目录
./install/cp.sh: 第 149 行： cd: ../../../../install/: 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/etc/init.d/': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/etc/profile.d/': 没有那个文件或目录
4.add ssh & scp to rootfs
cp: 目标 '../work/buildroot_initramfs_sysroot/usr/bin/' 不是目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/usr/sbin/': 没有那个文件或目录
cp: 目标 '../work/buildroot_initramfs_sysroot/lib/' 不是目录
mkdir: 无法创建目录 "../work/buildroot_initramfs_sysroot/etc/dropbear": 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/etc/dropbear': 没有那个文件或目录
cp: 无法创建普通文件 '../work/buildroot_initramfs_sysroot/etc/dropbear': 没有那个文件或目录
5.generating ubifs rootfs
Error: bad root directory './buildroot_initramfs_sysroot/'
       No such file or directory (error 2)
done! rootfs is work/ubifs.img
~/vega-buildroot-sdk ~/vega-buildroot-sdk/work
copy images to out
cp: 对 'work/ubifs.img' 调用 stat 失败: 没有那个文件或目录
cp: 对 'freeloader_rootfs/freeloader.bin' 调用 stat 失败: 没有那个文件或目录
cp: 对 'freeloader_rootfs/kernel.bin' 调用 stat 失败: 没有那个文件或目录
Image generation was successful in the 'out' directory.
mx @ Phony in ~/vega-buildroot-sdk |16:11:55  |main ✓| 
$ 

```