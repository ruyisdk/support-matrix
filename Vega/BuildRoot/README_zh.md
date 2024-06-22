# Milk-V Vega BuildRoot 构建测试报告

## 测试环境

### 操作系统信息

- Host: Ubuntu 22.04.4 LTS x86_64 (in Docker)
- Milk-V Vega Switch
- 参考文档：https://milkv.io/zh/docs/vega/getting-started/buildroot-sdk
- Issue/CFH: https://github.com/milkv-vega/vega-buildroot-sdk/issues/1
  - BuildRoot 构建失败

## 操作步骤

### 构建依赖包安装

```bash
sudo apt install -y make git gcc g++ bison flex device-tree-compiler mtd-utils zip unzip lz4
```

### 获取 SDK

```bash
git clone --depth=1 https://github.com/milkv-vega/vega-buildroot-sdk
```

> [!TIP]
> 目前官方仓库构建会失败，需要手动更新 `m4`, `fakeroot` 和 `autoconf`
> 已经有社区开发者修复了这一问题，在官方合并 PR 或修复之前请先使用此仓库：
> `git clone --depth=1 https://github.com/michaelfuckner/vega-buildroot-sdk`

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

使用来自官方仓库的源码构建失败。

<details>
<summary>日志如下。</summary>

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
</details>

使用社区开发者更新了部分包之后的源码成功构建。

```log
make -C /home/mx/vega-buildroot-sdk/freeloader ARCH=rv64gc ABI=lp64d CROSS_COMPILE=/home/mx/vega-buildroot-sdk/work/buildroot_initramfs/host/bin/riscv-nuclei-linux-gnu- \                      FW_JUMP_BIN=/home/mx/vega-buildroot-sdk/work/opensbi/platform/nuclei/ux600/firmware/fw_jump.bin UBOOT_BIN=/home/mx/vega-buildroot-sdk/work/u-boot/u-boot.bin DTB=/home/mx/vega-buildroot-sdk/work/nuclei_ux600fd.dtb                                                                                                                                                    make[1]: Entering directory '/home/mx/vega-buildroot-sdk/freeloader_rootfs'                                                                                                             cp /home/mx/vega-buildroot-sdk/work/u-boot/u-boot.bin .                                                                                                                                 cp /home/mx/vega-buildroot-sdk/work/opensbi/platform/nuclei/ux600/firmware/fw_jump.bin .                                                                                                cp ../work/boot/uImage.lz4 ./kernel.bin                                                                                                                                                 cp ../work/boot/uInitrd.lz4 ./initrd.bin                                                                                                                                                cp /home/mx/vega-buildroot-sdk/work/nuclei_ux600fd.dtb ./fdt.dtb                                                                                                                        /home/mx/vega-buildroot-sdk/work/buildroot_initramfs/host/bin/riscv-nuclei-linux-gnu-gcc -g -march=rv64gc -mabi=lp64d freeloader.S -o freeloader.elf -nostartfiles -Tlinker.lds         /home/mx/vega-buildroot-sdk/work/buildroot_initramfs/host/bin/riscv-nuclei-linux-gnu-objcopy freeloader.elf -O binary freeloader.bin                                                    /home/mx/vega-buildroot-sdk/work/buildroot_initramfs/host/bin/riscv-nuclei-linux-gnu-objdump -d freeloader.elf > freeloader.dis                                                         make[1]: Leaving directory '/home/mx/vega-buildroot-sdk/freeloader_rootfs'                  
freeloader is generated in /home/mx/vega-buildroot-sdk/freeloader/freeloader.elf                                                                                                        
You can download this elf into development board using make upload_freeloader               
or using openocd and gdb to achieve it                                                                                                                                                  
copy lib and usr/sbin and www                                                               
copy etc files                                                                                                                                                                          
copy files to install                                                                                                                                                                   
create file system                                                                                                                                                                      
~/vega-buildroot-sdk/install ~/vega-buildroot-sdk                                                                                                                                       
###Generating rootfs###                                                                                                                                                                 
rootfs: ubifs web                                                                                                                                                                       
1.gen sh                                                                                                                                                                                
2.clean /root and /dev of rootfs                                                                                                                                                        
3.cp file to rootfs                                                                                                                                                                     
4.add ssh & scp to rootfs                                                                                                                                                               
  etc/dropbear already exists                                                                                                                                                           
5.generating ubifs rootfs                                                                                                                                                               
done! rootfs is work/ubifs.img                                                                                                                                                          
~/vega-buildroot-sdk ~/vega-buildroot-sdk/work                                                                                                                                          
copy images to out                                                                                                                                                                      
Image generation was successful in the 'out' directory.
mx@7427944a6e87:~/vega-buildroot-sdk$ ls -alh out
total 24M
drwxrwxr-x 1 mx mx   66 Apr 16 09:55 .
drwxrwxr-x 1 mx mx  336 Apr 16 09:55 ..
-rwxrwxr-x 1 mx mx 1.1M Apr 16 09:55 freeloader.bin
-rw-rw-r-- 1 mx mx 3.5M Apr 16 09:55 kernel.bin
-rw-rw-r-- 1 mx mx  20M Apr 16 09:55 ubifs.img
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
