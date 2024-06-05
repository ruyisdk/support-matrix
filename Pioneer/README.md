
# Milk-V Pioneer

## Test Environment

### Operating System Information

- openEuler RISC-V 23.09 Preview
    - Download link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/SG2042/
    - Reference Installation Document: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/SG2042/README.sg2042.txt
- RevyOS
    - Download link: https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/
    - Reference Installation Document: https://revyos.github.io/docs/
- Fedora
    - Download link: https://milkv.io/docs/pioneer/getting-started/download
    - Reference Installation Document: https://milkv.io/zh/docs/pioneer/getting-started/InstallOS
- openKylin
    - Download link: https://www.openkylin.top/downloads
    - Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### Hardware Information

- Milk-V Pioneer (v1.3)

## Test Results

| Software Category         | Package Name | Test Results (Test Report)                                   |
| ------------------------- | ------------ | ------------------------------------------------------------ |
| openEuler/Base Image Boot | N/A          | [Success][oERV] (Flashed using `ruyi` CLI)                   |
| openEuler/Xfce Image Boot | N/A          | [Success][oERV] (Flashed using `ruyi` CLI)                   |
| RevyOS Image Boot         | N/A          | [Success][RevyOS] (Official support)                         |
| openKylin Image Boot      | N/A          | [Success][oK] (Official support)                             |
| Fedora Image Boot         | N/A          | [Success][Fedora] (Official support & Factory pre-installed) |

[oERV]: ./openEuler/README.md
[RevyOS]: https://docs.revyos.dev/
[oK]: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
[Fedora]: https://milkv.io/zh/docs/pioneer/getting-started/InstallOS

