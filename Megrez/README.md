---
vendor: milkv_megrez
product: Milk-V Megrez
cpu: EIC7700X
cpu_core: SiFive P550
ram: 8G/16G/32G
---

# Milk-V Megrez

## Test Environment

### Operating System Information

- RockOS
    - Project Link: https://github.com/rockos-riscv
    - Reference Installation Document
        - https://milkv.io/zh/docs/megrez/getting-started/boot
        - https://rockos-riscv.github.io/rockos-docs/docs/installation
- Fedora 41
    - Download Link: https://images.fedoravforce.org/Megrez
    - Reference Installation Document: https://milkv.io/zh/docs/megrez/getting-started/boot
- Guix System
    - Download Link: https://github.com/Z572/guix-riscv-channel/releases
    - Reference Installation Document: https://github.com/Z572/guix-riscv-channel#megrez
- Deepin
    - Download Link: https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
    - Reference Installation Document: https://milkv.io/zh/docs/megrez/getting-started/boot

### Hardware Information

- Milk-V Megrez

## Test Results

| Software Category       | Package Name | Test Result (Test Report)       |
|-------------------------|--------------|---------------------------------|
| RockOS Image Boot       | N/A          | [Good][RockOS]                  |
| Fedora Image Boot       | N/A          | [CFT][Fedora]                   |
| Guix System Image Boot  | N/A          | [CFT][Guix]                     |
| deepin Image Boot       | N/A          | [Good][deepin]                  |

[RockOS]: ./RockOS/README.md
[Fedora]: ./Fedora/README.md
[Guix]: ./Guix/README.md
[deepin]: ./deepin/README.md
