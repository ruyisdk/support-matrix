---
sys: xv6
sys_ver: null
sys_var: null

status: basic
last_update: 2026-09-21
---

# xv6 Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/blob/riscv/duo-imgtools/milkv-duo_sdcard.img
- Reference Installation Document: https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/

### Hardware Information

- Milk-V Duo S
- A USB power adapter
- A USB-A to C or USB C to C cable
- A microSD card
- A USB to UART debugger
- Three Dupont wires

## Installation Steps

### Prepare the Official Buildroot SDK Image
```bash
wget https://gh-proxy.com/https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duos-musl-riscv64-sd_v2.0.1.img.zip
unzip milkv-duos-musl-riscv64-sd_v2.0.1.img.zip

```

Extract `fip.bin`
```bash
LOOP_DEV=$(sudo losetup -fP --show milkv-duos-musl-riscv64-sd_v2.0.1.img)
sudo mkdir -p /mnt/duo_official
sudo mount "${LOOP_DEV}p1" /mnt/duo_official
cp /mnt/duo_official/fip.bin /tmp/fip_official.bin
sudo umount /mnt/duo_official
sudo losetup -d "$LOOP_DEV"

```

### Download the xv6 Image and Replace fip.bin

```bash
wget https://gh-proxy.com/https://github.com/xhackerustc/rvspoc-p2308-xv6-riscv/raw/riscv/duo-imgtools/milkv-duo_sdcard.img -O milkv-duo_sdcard.img

LOOP_DEV=$(sudo losetup -fP --show milkv-duo_sdcard.img)

sudo mkdir -p /mnt/duo_xv6
sudo mount "${LOOP_DEV}p1" /mnt/duo_xv6

# Back up the original fip.bin
sudo cp /mnt/duo_xv6/fip.bin /tmp/fip_xv6_original.bin

# Replace with the official version
sudo cp /tmp/fip_official.bin /mnt/duo_xv6/fip.bin

```

### Repack boot.sd

> The original `boot.sd` uses the FIT configuration node name `config-cv1800b_milkv_duo_sd`, while the U-Boot `sdboot` command expects `config-sg2000_milkv_duos_musl_riscv64_sd`. This mismatch causes `Could not find configuration node`. The FIT image must be repacked with the correct configuration node name.

```bash
# Extract kernel and device tree
dumpimage -T flat_dt -p 0 -o /tmp/kernel.bin /mnt/duo_xv6/boot.sd
dumpimage -T flat_dt -p 1 -o /tmp/fdt.dtb /mnt/duo_xv6/boot.sd

```

```bash
# Create the .its file
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
# Repack
mkimage -f /tmp/xv6.its /tmp/boot.sd.new

# Replace boot.sd in the image
sudo cp /tmp/boot.sd.new /mnt/duo_xv6/boot.sd

# Unmount and detach the loop device
sudo umount /mnt/duo_xv6
sudo losetup -d "$LOOP_DEV"

```

### Flash the Image

```shell
sudo dd if=milkv-duo_sdcard.img of=/dev/your/device bs=1M status=progress
sync

```

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and allows login through the onboard serial port.

### Boot Log

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

Screen recording:

[![asciicast](https://asciinema.org/a/U9m9CTLSUmNo757l.svg)](https://asciinema.org/a/U9m9CTLSUmNo757l)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
