# Yocto HiFive Premier P550 测试报告

## 测试环境

### 硬件信息

- 开发板: HiFive Premier P550
- 其他硬件:
  - MicroSD 卡一张
  - USB Type C to A 线缆一条

### 操作系统信息

- 操纵系统版本：Yocto 2024.11.00-HFP550 (SiFive 官方支持)
- 下载链接：<https://github.com/sifiveinc/freedom-u-sdk/releases/tag/2024.11.00-HFP550>
- 参考安装文档：<https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- 软件参考文档：<https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## 安装步骤

1. 下载操作系统镜像和bootloader文件并解压。

    ```bash
    wget https://github.com/sifiveinc/freedom-u-sdk/releases/download/2024.11.00-HFP550/demo-coreip-xfce4-hifive-premier-p550.rootfs.ext4.xz
    
    wget https://github.com/sifiveinc/freedom-u-sdk/releases/download/2024.11.00-HFP550/boot.vfat

    wget https://github.com/sifiveinc/freedom-u-sdk/releases/download/2024.11.00-HFP550/bootloader_ddr5_secboot.bin

    unxz -d demo-coreip-xfce4-hifive-premier-p550.rootfs.ext4.xz
    ```

2. 挂载MicroSD卡，并使用 `cp` 命令拷贝镜像文件至MicroSD卡。(假设 `/dev/sdc` 为MicroSD卡设备)

    ```bash
    sudo mount /dev/sdc /mnt/sd
    
    sudo cp ./demo-coreip-xfce4-hifive-premier-p550.rootfs.ext4 ./boot.vfat ./bootloader_ddr5_secboot.bin /mnt/sd

    sync

    sudo umount /mnt/sd
    ```

3. 插入MicroSD卡，连接开发板串口，启动开发板并进入SPI Flash中的U-Boot。
    - 确保拨码开关为SPI Flash的启动模式：`DIP_SW1[3:0] = 0100`。(SW的ON = 0, OFF = 1)
    - 在串口终端中出现 `Hit any key to stop autoboot` 时迅速按下回车键，进入 U-boot 命令行终端。

4. 使用定制的U-Boot命令烧录镜像。

    - 确认MicroSD卡状态

        ```bash
        => ls mmc 1
        ```

    - 如果需要的话，烧录新的bootloader。

        ```bash
        => ext4load mmc 1 0x90000000 bootloader_ddr5_secboot.bin

        => es_burn write 0x90000000 flash
        ```

    - 烧录系统镜像

        ```bash
        => es_fs update mmc 1 boot.vfat mmc 0#boot
        => es_fs update mmc 1 demo-coreip-xfce4-hifive-premier-p550.rootfs.ext4 mmc 0#root
        ```

5. 重启开发板

## 预期结果

系统应正常启动，并允许通过串口或其他方式登录。

## 实际结果

CFT

### 测试结论

CFT
