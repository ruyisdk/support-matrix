# NuttX Star64 Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/apache/nuttx
- Reference Installation Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
- Toolchain:
    - Boot Image: https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
    - DTB: https://github.com/starfive-tech/VisionFive2/releases
    - Toolchain: https://github.com/sifive/freedom-tools/releases
    - kflash: https://github.com/kendryte/kflash.py

### Hardware Information

- Development Board: Star64
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Preparing Source and Environment

Get the toolchain:
```bash
wget https://static.dev.sifive.com/dev-tools/freedom-tools/v2020.12/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
tar -xvzf riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

Clone the repository and configure:
```bash
mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```

### Building NuttX

Compile nuttx.bin:
```bash
cd nuttx
make distclean
./tools/configure.sh star64:nsh
make -j$(nproc)
riscv64-unknown-elf-objcopy -O binary nuttx nuttx.bin
```

Build the file system:
```bash
make export
pushd ../apps
tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make import
popd
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"
```

Write the dtb file:
- Download the dtb:
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/jh7110-visionfive-v2.dtb
```
- In the nuttx directory:
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

Ensure you have u-boot-tools installed on your system:
```bash
# sudo apt install u-boot-tools
# sudo pacman -S uboot-tools
# sudo dnf install u-boot-tools
```

Create the fit:
```bash
mkimage -f nuttx.its -A riscv -O linux -T flat_dt starfiveu.fit
```

### Building the Image

Download the SD card image and flash:
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

### Flashing the Image

Flash the SBI environment onto the SD card:
```bash
unxz -k canmv230-sdcard.img.xz
sudo dd if=canmv230-sdcard.img of=/dev/your/sdcard bs=1M status=progress
```

Replace the fit file:
```bash
mkdir mnt
sudo mount /dev/your/sdcard/p3 mnt
sudo cp starfiveu.fit mnt/
sudo umount mnt
rm -r mnt
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The development board outputting boot information normally.

## Actual Results

CFT

### Boot Log

Screen recording (from image flashing to boot):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT