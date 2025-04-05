# Longan Nano

## 测试环境

### 操作系统信息

- FreeRTOS/RT-Thread/ThreadX/μCOS-II
    - 源码链接：https://github.com/Nuclei-Software/nuclei-sdk
    - 参考文档：https://doc.nucleisys.com/nuclei_sdk/quickstart.html#build-run-and-debug-sample-application
        - https://doc.nucleisys.com/nuclei_sdk/design/board/gd32vf103c_longan_nano.html
- Zephyr
    - 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
    - 参考文档：https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### 硬件开发板信息

- Longan Nano (GD32VF103CBT6)

## 测试结果

| 软件分类  | 软件包名 | 测试结果（测试报告） |
| --------- | -------- | -------------------- |
| FreeRTOS  | N/A      | [成功][FreeRTOS]     |
| RT-Thread | N/A      | [成功][RT-Thread]    |
| ThreadX   | N/A      | [成功][RT-Thread]    |
| Zephyr    | N/A      | [成功][Zephyr]       |
| μC/OS-II  | N/A      | [成功][uCOSII]       |

[FreeRTOS]: ./FreeRTOS/README_zh.md
[RT-Thread]: ./RT-Thread/README_zh.md
[ThreadX]: ./ThreadX/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[uCOSII]: ./uCOSII/README_zh.md
