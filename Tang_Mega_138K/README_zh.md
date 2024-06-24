# Tang Mega 138K Pro

## 测试环境

### 操作系统信息

- RT-Thread
    - 源码链接：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - 参考安装文档：https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - 参考设计文档：https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - 工具链：
        - 高云云源软件：http://www.gowinsemi.com.cn/faq.aspx
        - RiscV AE350 SOC RDS 软件：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_RDS_V1.1_win.zip
        - Andes-Development-Kit：https://github.com/andestech/Andes-Development-Kit
- Zephyr
    - 源码链接：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - 参考安装文档：https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - 参考设计文档：https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - 工具链：
        - 高云云源软件：http://www.gowinsemi.com.cn/faq.aspx
        - RiscV AE350 SOC RDS 软件：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_RDS_V1.1_win.zip
        - Andes-Development-Kit：https://github.com/andestech/Andes-Development-Kit
- FreeRTOS
    - 源码链接：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - 参考安装文档：https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - 参考设计文档：https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
    - 工具链：
        - 高云云源软件：http://www.gowinsemi.com.cn/faq.aspx
        - RiscV AE350 SOC RDS 软件：https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_RDS_V1.1_win.zip
        - Andes-Development-Kit：https://github.com/andestech/Andes-Development-Kit

### 硬件开发板信息

- Tang Mega 138K Pro Dock

## 测试结果

| 软件分类                      | 软件包名 | 测试结果（测试报告）     |
| ----------------------------- | -------- | --------------------- |
| FreeRTOS 镜像构建及启动       | N/A      | [Basic][FreeRTOS]      |
| RT-Thread nano 镜像构建及启动 | N/A      | [Basic][RT-Thread-nano]|
| RT-Thread std 镜像构建及启动  | N/A      | [Basic][RT-Thread-std] |
| Zephyr 镜像构建及启动         | N/A      | [CFH][Zephyr]          |

[FreeRTOS]: ./FreeRTOS/README_zh.md
[RT-Thread-std]: ./RT-Thread/README_zh.md
[RT-Thread-nano]: ./RT-Thread/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md