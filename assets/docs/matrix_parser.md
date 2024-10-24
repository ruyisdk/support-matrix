## matrix parser

用于解析 metadata 的工具。
整个支持矩阵，其可以被分为如下结构：

```plaintext
支持矩阵
 |
 |--- 开发板
    |
    |--- README.md # 开发板的说明文档，开发板的基本metadata包含其中
    |
    |--- 各个系统
    |    |
    |    |--- README.md # 该系统主变体的说明文档，系统的基本metadata包含其中
    |    |
    |    |--- README_变体.md # 该系统的其他变体的说明文档，变体的metadata包含其中
    |    |
    |    |--- README(_变体)_lang.yaml # 各种语言的翻译， **不包含metadata！**
    |
    |--- others.yml # 没有文档的系统的metadata
```

则根据上述结构，解析完的数据结构如下：
- `class Systems`：整个项目，包含一系列的开发板（`classs Board`）
- `class Board`：开发板，包含该开发板的 metadata，和一系列的系统（`class System`）
- `class System`：系统，该系统的 id，和一系列的变体（`class SystemVar`）
- `class SystemVar`：变体，该变体的 metadata

通过向 `Systems` 传入项目的根目录，即可解析整个项目的 metadata。
