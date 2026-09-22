# Fedora 44 Server HiFive Premier P550 测试报告

## 测试环境

### 硬件信息

- 开发板：HiFive Premier P550
- 其他硬件：
  - MicroSD 卡一张
  - USB Type-C 数据线一条

### 操作系统信息

- 操作系统版本：Fedora Linux 44 (Server Edition)（`Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz`）
- Bootchain：`2026.08.00-HFP550`
- 下载链接：
  - <https://dl.fedoraproject.org/pub/alt/risc-v/release/44/Server/riscv64/images/Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz>
- Bootchain：
  - <https://github.com/sifiveinc/freedom-u-sdk/releases/tag/2026.08.00-HFP550>
- 参考安装文档：
  - <https://fedoraproject.org/wiki/Architectures/RISC-V/SiFive/HiFivePremierP550>
  - <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- 软件参考文档：
  - <https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## 安装步骤

1. 下载 Fedora 镜像、校验文件及 P550 Bootchain：

   ```bash
   wget -c https://dl.fedoraproject.org/pub/alt/risc-v/release/44/Server/riscv64/images/Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz
   wget -c https://dl.fedoraproject.org/pub/alt/risc-v/release/44/Server/riscv64/images/Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz.sha256
   wget -c https://github.com/sifiveinc/freedom-u-sdk/releases/download/2026.08.00-HFP550/bootloader_ddr5_secboot.bin
   ```

   校验 Fedora 镜像：

   ```bash
   sha256sum -c Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz.sha256
   ```

   解压镜像：

   ```bash
   unxz Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw.xz
   ```

2. 准备 ext4 格式的 MicroSD 卡，并将 Fedora 镜像和 Bootloader 复制至卡中。

    > 以下假设 MicroSD 卡设备为 `/dev/sdX`，操作前请使用 `lsblk` 确认实际设备。

    ```bash
    sudo umount /dev/sdX* 2>/dev/null
    sudo wipefs -a /dev/sdX
    sudo mkfs.ext4 -F -L P550_INSTALL /dev/sdX

    sudo mkdir -p /mnt/p550
    sudo mount /dev/sdX /mnt/p550

    sudo cp Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw /mnt/p550/
    sudo cp bootloader_ddr5_secboot.bin /mnt/p550/

    sync
    sudo umount /mnt/p550
    ```

3. 将 MicroSD 卡插入开发板，连接串口并启动 P550。

    串口参数：

    ```text
    Baud rate: 115200
    Data bits: 8
    Parity: None
    Stop bits: 1
    Flow control: None
    ```

    将开发板设置为 SPI Flash 启动模式，在出现：

    ```text
    Hit any key to stop autoboot
    ```

    时按键进入 U-Boot。

4. 在 U-Boot 中确认 MicroSD 卡及文件：

    ```bash
    => mmc list
    => ls mmc 1
    ```

    应能够看到：

    ```bash
    bootloader_ddr5_secboot.bin
    Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw
    ```

5. 更新 P550 Bootchain：

    ```bash
    => ext4load mmc 1 0x90000000 bootloader_ddr5_secboot.bin
    => es_burn write 0x90000000 flash
    ```

    等待写入完成后重新启动开发板。

6. 将 Fedora 完整磁盘镜像写入板载 eMMC：

    ```bash
    => es_fs write mmc 1 Fedora-Server-Host-Omni-44-20260731.0.riscv64.raw mmc 0
    ```

    写入完成后关闭开发板并移除 MicroSD 卡。

7. 设置 Fedora 从板载 eMMC 自动启动。

    重新启动并进入 U-Boot：

    ```bash
    => env default -af
    => env set bootdev 'mmc 0'
    => env set bootcmd 'load ${bootdev}:2 ${fdt_addr_r} dtb/${fdtfile}; load ${bootdev}:1 ${kernel_addr_r} EFI/fedora/shimriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r};'
    => env set stdin serial
    => env set stdout serial
    => env set stderr serial
    => env save
    => reset
    ```

    系统随后将自动从 eMMC 启动 Fedora。

8. 系统启动后使用以下账号登录：

    ```bash
    Username: fedora
    Password: linux
    ```

## 预期结果

系统应正常启动，并允许通过串口或其他方式登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```text
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Finished cockpit-issue.service - Cockpit issue updater service.

Fedora Linux 44 (Server Edition)
Kernel 7.1.5-201.0.riscv64.omni.fc44.riscv64 on riscv64 (ttyS0)

Web console: https://localhost:9090/

localhost login: fedora
Password:

[fedora@localhost ~]$ uname -a
Linux localhost.localdomain 7.1.5-201.0.riscv64.omni.fc44.riscv64 #1 SMP PREEMPT_DYNAMIC Wed Jul 29 22:12:49 EDT 2026 riscv64 GNU/Linux
[fedora@localhost ~]$ cat /etc/os-release
NAME="Fedora Linux"
VERSION="44 (Server Edition)"
RELEASE_TYPE=stable
ID=fedora
VERSION_ID=44
PRETTY_NAME="Fedora Linux 44 (Server Edition)"
VARIANT="Server Edition"
VARIANT_ID=server
[fedora@localhost ~]$
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/1264802.svg)]( https://asciinema.org/a/1264802)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。