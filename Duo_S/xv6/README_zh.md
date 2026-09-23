# xv6 Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- 参考安装文档：https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### 硬件信息

- Milk-V Duo S
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个
- 杜邦线三根

## 安装步骤

### 准备官方 Buildroot SDK 镜像
```bash
wget https://gh-proxy.com/https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duos-musl-riscv64-sd_v2.0.1.img.zip
unzip milkv-duos-musl-riscv64-sd_v2.0.1.img.zip

```

提取 fip.bin
```bash
LOOP_DEV=$(sudo losetup -fP --show milkv-duos-musl-riscv64-sd_v2.0.1.img)
sudo mkdir -p /mnt/duo_official
sudo mount "${LOOP_DEV}p1" /mnt/duo_official
cp /mnt/duo_official/fip.bin /tmp/fip_official.bin
sudo umount /mnt/duo_official
sudo losetup -d "$LOOP_DEV"

```

### 下载 xv6 镜像并替换 fip.bin

```bash
wget https://gh-proxy.com/https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/raw/riscv/duo-imgtools/milkv-duo_sdcard.img -O milkv-duo_sdcard.img

LOOP_DEV=$(sudo losetup -fP --show milkv-duo_sdcard.img)

sudo mkdir -p /mnt/duo_xv6
sudo mount "${LOOP_DEV}p1" /mnt/duo_xv6

# 备份原 fip.bin
sudo cp /mnt/duo_xv6/fip.bin /tmp/fip_xv6_original.bin

# 替换为官方版本
sudo cp /tmp/fip_official.bin /mnt/duo_xv6/fip.bin

```

### 重新打包 boot.sd

> 原 `boot.sd` 的 FIT 配置节点名为 `config-cv1800b_milkv_duo_sd`，与 U-Boot `sdboot` 命令期望的 `config-sg2000_milkv_duos_musl_riscv64_sd` 不匹配，导致 `Could not find configuration node`。需要重新打包 FIT 镜像，修改配置节点名。

```bash
# 解出内核和设备树
dumpimage -T flat_dt -p 0 -o /tmp/kernel.bin /mnt/duo_xv6/boot.sd
dumpimage -T flat_dt -p 1 -o /tmp/fdt.dtb /mnt/duo_xv6/boot.sd

```

```bash
# 创建 .its 文件
cat > /tmp/xv6.its << 'EOF'
/dts-v1/;

/ {
    description = "Milk-V Duo S xv6";
    #address-cells = <1>;

    images {
        kernel-1 {
            description = "xv6 kernel";
            data = /incbin/("/tmp/kernel.bin");
            type = "kernel";
            arch = "riscv";
            os = "linux";
            compression = "none";
            load = <0x80200000>;
            entry = <0x80200000>;
            hash-1 {
                algo = "crc32";
            };
        };
        fdt-1 {
            description = "xv6 fdt";
            data = /incbin/("/tmp/fdt.dtb");
            type = "flat_dt";
            arch = "riscv";
            compression = "none";
            hash-1 {
                algo = "sha256";
            };
        };
    };

    configurations {
        default = "config-sg2000_milkv_duos_musl_riscv64_sd";
        config-sg2000_milkv_duos_musl_riscv64_sd {
            description = "xv6 on Milk-V Duo S";
            kernel = "kernel-1";
            fdt = "fdt-1";
        };
    };
};
EOF

```

```bash
# 重新打包
mkimage -f /tmp/xv6.its /tmp/boot.sd.new

# 替换镜像中的 boot.sd
sudo cp /tmp/boot.sd.new /mnt/duo_xv6/boot.sd

# 卸载并断开 loop 设备
sudo umount /mnt/duo_xv6
sudo losetup -d "$LOOP_DEV"

```

### 刷写

```shell
sudo dd if=milkv-duo_sdcard.img of=/dev/your/device bs=1M status=progress
sync

```

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
## Loading fdt from FIT Image at 81800000 ...
   Using 'config-sg2000_milkv_duos_musl_riscv64_sd' configuration
   Trying 'fdt-1' fdt subimage
     Description:  xv6 fdt
     Type:         Flat Device Tree
     Compression:  uncompressed
     Data Start:   0x81983194
     Data Size:    3956 Bytes = 3.9 KiB
     Architecture: RISC-V
     Hash algo:    sha256
     Hash value:   6121854a8ee59c80da70f5d5ad8d054b2be713a2a8605de8275f03a3cca78e0b
   Verifying Hash Integrity ... sha256+ OK
   Booting using the fdt blob at 0x81983194
   Loading Kernel Image
   Decompressing 1585152 bytes used 1ms
   Loading Device Tree to 0000000094260000, end 0000000094263f73 ... OK

Starting kernel ...


xv6 kernel is booting

SBI specification v0.3 detected
SBI TIME extension detected
SBI IPI extension detected
SBI RFNC extension detected
SBI HSM extension detected

init: starting sh
                 $

```

屏幕录像：

[![asciicast](https://asciinema.org/a/U9m9CTLSUmNo757l.svg)](https://asciinema.org/a/U9m9CTLSUmNo757l)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
