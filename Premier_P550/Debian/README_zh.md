# Debian HiFive Premier P550 测试报告

## 测试环境

### 硬件信息

- 开发板: HiFive Premier P550
- 其他硬件:
  - MicroSD 卡一张
  - USB Type C to A 线缆一条

### 操作系统信息

- 操作系统版本：Debian GNU/Linux trixie/sid（ESWIN Debian-v1.0.0-20250730）
- 下载链接：<https://github.com/eswincomputing/eic7x-images/releases/tag/Debian-v1.0.0-20250730>
- 参考安装文档：
  - <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- 软件参考文档：<https://www.sifive.com/document-file/hifive-premier-p550-software-reference-manual>

## 安装步骤

1. 下载并解压操作系统镜像。

    ```bash
    for i in 001 002 003 004; do
        wget -c "https://github.com/eswincomputing/eic7x-images/releases/download/Debian-v1.0.0-20250730/EIC7x_Release_Images_0730.zip.$i"
    done
    ```

    本次 Release 中压缩包实际分卷顺序与编号不一致，需要重新映射后解压：

    ```bash
    mkdir -p fixed-split
    cd fixed-split
    
    ln -s ../EIC7x_Release_Images_0730.zip.002 EIC7x_Release_Images_0730.z01
    ln -s ../EIC7x_Release_Images_0730.zip.003 EIC7x_Release_Images_0730.z02
    ln -s ../EIC7x_Release_Images_0730.zip.004 EIC7x_Release_Images_0730.z03
    ln -s ../EIC7x_Release_Images_0730.zip.001 EIC7x_Release_Images_0730.zip
    
    7z x EIC7x_Release_Images_0730.zip
    cd EIC7x_Release_Images_0730
    ```

2. 将 MicroSD 卡格式化为 ext4，并拷贝 P550 minimal 镜像。（假设 `/dev/sdb` 为 MicroSD 卡设备）

    ```bash
    lsblk
    sudo umount /dev/sdb* 2>/dev/null || true
    sudo wipefs -a /dev/sdb
    sudo mkfs.ext4 -F -L P550_INSTALL /dev/sdb
    
    sudo mkdir -p /mnt/sd
    sudo mount /dev/sdb /mnt/sd
    ```

    将 boot 和 root 镜像使用短文件名复制到 MicroSD：

    ```bash
    sudo cp ./dvb/bootloader_P550.bin /mnt/sd/
    sudo cp ./dvb/minimal/boot-P550-20250904-101110.ext4 /mnt/sd/b
    sudo cp ./dvb/minimal/root-P550-20250904-101110.ext4 /mnt/sd/r
    
    sync
    sudo umount /mnt/sd
    ```

3. 插入MicroSD卡，连接开发板串口，启动开发板并进入SPI Flash中的U-Boot。
    - 确保拨码开关为SPI Flash的启动模式：`DIP_SW1[3:0] = 0100`。(SW的ON = 0, OFF = 1)
    - 在串口终端中出现 `Hit any key to stop autoboot` 时迅速按下回车键，进入 U-boot 命令行终端。
    - 确认 MicroSD 卡中的镜像文件：
    
      ```text
      => ls mmc 1
               4751464 bootloader_P550.bin
            1048576000 r
             104857600 b
      ```
    
4. 使用 U-Boot 命令建立 eMMC 分区并烧录 Debian 镜像。

    ```text
    => run gpt_partition
    Writing GPT: success!
    ```

    烧录 boot 分区：

    ```text
    => es_fs update mmc 1 b mmc 0:1
    ```

    - 输出结果：

      ```
      Write progress: 100%:++++++++++++++++++++++++++++++++++++++++++++++++++
      mmc has been successfully writen in mmc 0:1
      ```

    烧录 root 分区：

    ```text
    => es_fs update mmc 1 r mmc 0:3
    ```

    - 输出结果：

      ```
      Write progress: 100%:++++++++++++++++++++++++++++++++++++++++++++++++++
      mmc has been successfully writen in mmc 0:3
      ```

5. 关闭开发板，拔出 MicroSD 卡后重新上电。

    ```
    => poweroff
    poweroff ...
    eic770x_core_shutdown
    ```

    系统启动后使用以下账号登录：

    ```text
    Username: eswin
    Password: eswin
    ```

## 预期结果

系统应正常启动，并允许通过串口或其他方式登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```text
[ OK ] Reached target graphical.target - Graphical Interface. Starting systemd-update-utmp-runle…- Record Runlevel Change in UTMP... 
[ OK ] Finished systemd-update-utmp-runle…e - Record Runlevel Change in UTMP.

Debian GNU/Linux trixie/sid rockos-eswin ttyS0

rockos-eswin login: eswin
Password:

Linux rockos-eswin 6.6.92-eic7x-2025.07 #2025.09.04.09.57+ SMP Thu Sep  4 09:59:13 CST 2025 riscv64

eswin@rockos-eswin:~$ uname -a
Linux rockos-eswin 6.6.92-eic7x-2025.07 #2025.09.04.09.57+ SMP Thu Sep  4 09:59:13 CST 2025 riscv64 GNU/Linux

eswin@rockos-eswin:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

eswin@rockos-eswin:~$
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/1264770.svg)](https://asciinema.org/a/1264770)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。