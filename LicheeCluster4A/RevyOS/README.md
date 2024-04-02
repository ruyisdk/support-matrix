# RevyOS Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS (w/mainline kernel)
- 下载链接
  - 系统镜像：[root-lpi4amain-20240127_105111.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/root-lpi4amain-20240127_105111.ext4.zst)
  - boot 镜像：[boot-lpi4amain-20240127_105111.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/boot-lpi4amain-20240127_105111.ext4.zst)
  - u-boot 镜像（8G RAM）：[u-boot-with-spl-lc4a-main.bin](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/u-boot-with-spl-lc4a-main.bin)
  - u-boot 镜像（16G RAM）：[u-boot-with-spl-lc4a-16g-main.bin](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/u-boot-with-spl-lc4a-16g-main.bin)
- 参考安装文档：https://revyos.github.io/

### 硬件信息

- Lichee Cluster 4A 8G / 16G

## 安装步骤

### 使用 `fastboot` 刷写镜像到板载 eMMC

```bash
zstd -dk root-lpi4amain-20240127_105111.ext4.zst
zstd -dk boot-lpi4amain-20240127_105111.ext4.zst
fastboot flash ram u-boot-with-spl-lc4a-main.bin  # 8GB RAM ver.
# fastboot flash ram u-boot-with-spl-lc4a-16g-main.bin  # 16GB RAM ver.
fastboot reboot
fastboot flash uboot u-boot-with-spl-lc4a-main.bin  # 8GB RAM ver.
# fastboot flash uboot u-boot-with-spl-lc4a-16g-main.bin  # 16GB RAM ver.
fastboot flash boot boot-lpi4amain-20240127_105111.ext4
fastboot flash root root-lpi4amain-20240127_105111.ext4
```

### 登录系统

通过串口或图形界面登录系统。

默认用户名：`debian`
默认密码：`debian`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

CFT

### 启动信息


```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT