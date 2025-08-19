# Ubuntu 24.04.01 LTS HiFive Premier P550 测试报告

## 测试环境

### 硬件信息

- 开发板: HiFive Premier P550
- 其他硬件:
  - MicroSD 卡一张
  - USB Type C to A 线缆一条

### 操作系统信息

- 操作系统版本：Ubuntu 2025.02.00 (基于Ubuntu 24.04.01 LTS) (SiFive 官方支持)
- 下载链接: <https://github.com/sifiveinc/hifive-premier-p550-ubuntu/releases/tag/2025.02.00>
- 参考安装文档：<https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- 软件参考文档：<https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## 安装步骤

1. 下载操作系统镜像文件并解压。

    ```bash
    wget https://github.com/sifiveinc/hifive-premier-p550-ubuntu/releases/download/2025.02.00/ubuntu-24.04-preinstalled-server-riscv64.img.xz

    wget https://github.com/sifiveinc/freedom-u-sdk/releases/download/2024.11.00-HFP550/bootloader_ddr5_secboot.bin

    unxz -d ubuntu-24.04-preinstalled-server-riscv64.img.xz
    ```

2. 挂载MicroSD卡，并使用 `cp` 命令拷贝镜像文件至MicroSD卡。(假设 `/dev/sdX` 为MicroSD卡设备)

    ```bash
    sudo mount /dev/sdX /mnt/sd
    
    sudo cp ./ubuntu-24.04-preinstalled-server-riscv64.img ./bootloader_ddr5_secboot.bin /mnt/sd

    sync

    sudo umount /mnt/sd
    ```

3. 插入MicroSD卡，连接开发板串口，启动开发板并进入SPI Flash中的U-Boot。
    - 确保拨码开关为SPI Flash的启动模式：`DIP_SW1[3:0] = 0100`。(SW的ON = 0, OFF = 1)
    - 在串口终端中出现 `Hit any key to stop autoboot` 时迅速按下回车键，进入 U-boot 命令行终端。

4. 使用定制的U-Boot命令烧录镜像。

    - 确认MicroSD卡状态。

        ```bash
        => ls mmc 1
        ```

    - 如果需要的话，烧录新的bootloadr。

        ```bash
        => ext4load mmc 1 0x90000000 bootloader_ddr5_secboot.bin

        => es_burn write 0x90000000 flash
        ```

    - 烧录系统镜像。

        ```bash
        => es_fs write mmc 1 ubuntu-24.04-preinstalled-server-riscv64.img mmc 0
        ```

5. 重启开发板。

## 预期结果

系统应正常启动，并允许通过串口或其他方式登录。

## 实际结果

CFT

### 测试结论

CFT
