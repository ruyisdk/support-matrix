# NuttX VisionFive 2 测试报告

## 测试环境

### 操作系统信息

- 源码链接：https://github.com/apache/nuttx
- 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
- 工具链：
    - 启动镜像：https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
    - DTB：https://github.com/starfive-tech/VisionFive2/releases
    - toolchain: https://github.com/sifive/freedom-tools/releases
    - kflash：https://github.com/kendryte/kflash.py

### 硬件信息

- 开发板：VisionFive 2
- USB A to C / USB C to C 线缆
- SD 卡

## 安装步骤

### 准备源码及环境

获取工具链：
```bash
wget https://static.dev.sifive.com/dev-tools/freedom-tools/v2020.12/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
tar -xvzf riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

clone 仓库并进行配置：
```bash
mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```
### 构建 NuttX

编译 nuttx.bin：
```bash
cd nuttx
make distclean
./tools/configure.sh star64:nsh
make -j$(nproc)
riscv64-unknown-elf-objcopy -O binary nuttx nuttx.bin
```

构建文件系统：
```bash
make export
pushd ../apps
tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make import
popd
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"
```

编写 dtb 文件：
- 下载 dtb：
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/jh7110-visionfive-v2.dtb
```
- 在 nuttx 文件夹下进行：
```bash
cat << EOF > nuttx.its
/dts-v1/;

/ {
  description = "NuttX FIT image";
  #address-cells = <2>;

  images {
    vmlinux {
      description = "vmlinux";
      data = /incbin/("./nuttx.bin");
      type = "kernel";
      arch = "riscv";
      os = "linux";
      load = <0x0 0x40200000>;
      entry = <0x0 0x40200000>;
      compression = "none";
    };

    ramdisk {
      description = "buildroot initramfs";
      data = /incbin/("./initrd");
      type = "ramdisk";
      arch = "riscv";
      os = "linux";
      load = <0x0 0x46100000>;
      compression = "none";
      hash-1 {
        algo = "sha256";
      };
    };

    fdt {
      data = /incbin/("./jh7110-visionfive-v2.dtb");
      type = "flat_dt";
      arch = "riscv";
      load = <0x0 0x46000000>;
      compression = "none";
      hash-1 {
        algo = "sha256";
      };
    };
  };

  configurations {
    default = "nuttx";

    nuttx {
      description = "NuttX";
      kernel = "vmlinux";
      fdt = "fdt";
      loadables = "ramdisk";
    };
  };
};
EOF
```

确认你系统上安装了 u-boot-tools：
```bash
# sudo apt install u-boot-tools
# sudo pacman -S uboot-tools
# sudo dnf install u-boot-tools
```

创建 fit：
```bash
mkimage -f nuttx.its -A riscv -O linux -T flat_dt starfiveu.fit
```

### 构建镜像

下载 sd 卡镜像并烧写：
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

### 烧写镜像

在 SD 卡上烧写 SBI 环境：
```bash
unxz -k canmv230-sdcard.img.xz
sudo dd if=canmv230-sdcard.img of=/dev/your/sdcard bs=1M status=progress
```

替换 fit 文件：
```bash
mkdir mnt
sudo mount /dev/your/sdcard/p3 mnt
sudo cp starfiveu.fit mnt/
sudo umount mnt
rm -r mnt
```

### 登录系统

通过串口连接开发板。

## 预期结果

构建成功，开发板正常输出启动信息。

## 实际结果

构建成功，开发板正常输出启动信息。

### 启动信息

屏幕录像（从刷写系统到启动）：
[![asciicast](https://asciinema.org/a/boXeQ4xPfJgGjsJPZeT00uMH0.svg)](https://asciinema.org/a/boXeQ4xPfJgGjsJPZeT00uMH0)

```log
ABC                                                                       
NuttShell (NSH) NuttX-12.5.1                                              
nsh> cat /proc/version                                                    
NuttX version 12.5.1 6e941aed8b May  7 2024 11:25:17 star64:nsh           
nsh> 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功