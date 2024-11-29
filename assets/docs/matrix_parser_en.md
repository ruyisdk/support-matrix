## Matrix Parser

A tool used for parsing metadata. The support_matrix repo can be divided into the following structure:

```plaintext
Support Matrix
 |
 |--- Board
    |
    |--- README.md # Documentation for the board, containing the basic metadata of the board
    |
    |--- Various Systems
    |    |
    |    |--- README.md # Documentation for the main variant of the system, containing the basic metadata of the system
    |    |
    |    |--- README_Variant.md # Documentation for other variants of the system, containing the metadata of the variant
    |    |
    |    |--- README(_Variant)_lang.yaml # Translations in various languages, **does not include metadata!**
    |
    |--- others.yml # Metadata for systems that do not have documentation
```

Based on the structure above, the data structure are:
- `class Systems`: The entire project, containing a series of development boards (`class Board`)
- `class Board`: A development board, containing the board's metadata and a series of systems (`class System`)
- `class System`: A system, with the system's ID and a series of variants (`class SystemVar`)
- `class SystemVar`: A variant, containing the metadata of the variant

By passing the project's root directory to `Systems`, you can parse the metadata of the entire project.