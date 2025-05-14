# Nuclei RV-STAR

## 测试环境

### 操作系统信息

- FreeRTOS/RT-Thread/ThreadX/μCOS-II
    - 源码链接：https://github.com/Nuclei-Software/nuclei-sdk
    - 参考文档：https://doc.nucleisys.com/nuclei_sdk/quickstart.html#build-run-and-debug-sample-application
- LiteOS
    - 源码链接：https://github.com/riscv-mcu/kernel_liteos_m
    - 参考文档：https://github.com/riscv-mcu/kernel_liteos_m/blob/nuclei/OpenHarmony-3.0-LTS/targets/riscv_nuclei_gd32vf103_soc_gcc/README.md

### 硬件开发板信息

- RV-STAR 开发板（GD32VF103VBT6）

## 测试结果

| 软件分类  | 软件包名 | 测试结果（测试报告） |
| --------- | -------- | -------------------- |
| FreeRTOS  | N/A      | [成功][FreeRTOS]     |
| RT-Thread | N/A      | [成功][RT-Thread]    |
| ThreadX   | N/A      | [成功][RT-Thread]    |
| μC/OS-II  | N/A      | [成功][uCOSII]       |
| LiteOS    | N/A      | [成功][LiteOS]       |

[FreeRTOS]: ./FreeRTOS/README_zh.md
[LiteOS]: ./LiteOS/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[ThreadX]: ./ThreadX/README_zh.md
[uCOSII]: ./uCOSII/README_zh.md
