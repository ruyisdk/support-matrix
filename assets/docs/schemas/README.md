# Schema

此处放置了各个文件的 schema 描述，供如 yaml-language-server 等插件读取并给予 lint。

对于可交互式的文档，[json-schema-for-humans](https://coveooss.github.io/json-schema-for-humans/) 给出了一些不错的结果。您可以通过以下方式生成：

```bash
pip install json-schema-for-humans
generate-schema-doc --config template_name=js schemas/config.schema.json
```

并打开生成的文档进行查看。

---

Here, the schema descriptions for various files are provided for plugins such as `yaml-language-server` to read and perform linting.  

For interactive documentation, [json-schema-for-humans](https://coveooss.github.io/json-schema-for-humans/) produces excellent results. You can generate it using the following commands:  

```bash
pip install json-schema-for-humans
generate-schema-doc --config template_name=js schemas/config.schema.json
```  

Then, open the generated document to view it.