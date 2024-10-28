## ruyi index updator

自动更新 ruyi 工具中镜像的索引文件，同步支持矩阵与 ruyi index。

### 使用方法

你需要设置环境变量 `GITHUB_TOKEN`，并且该 token 需要有对应仓库的读写权限和 pr 权限。或者你可以同时允许 fork 仓库的权限，让工具自动 fork 仓库。

**注意！**你直接从设置中获取到的 token 都是 personal token，但是向组织仓库进行 pr 时，该 token 是会被拒绝的。你需要使用一个 OAuth app token。最简单的辨别方法是，personal token 的格式是 `ghp_` 开头，OAuth app token 的格式是 `gho` 开头。若你不知道如何获取 OAuth app token，可以通过 `gh` 命令行工具来获取一个。 **请注意不要泄漏**

默认工具会在临时文件夹中运行，每次可能会下载一大堆镜像文件。你可以设置环境变量 `$CACHE_DIR` 来指定缓存目录，这样工具会将所有的东西都缓存到这个目录中。

renew_ruyi_index.py 里面封装了所有的操作，你可以直接运行这个脚本。各个参数的含义如下：
- `-c` 或 `--config`：配置文件的路径，可以与 nvchecker 共用。主要是要它的 `[vendor-system-variance]` 这个字段。
- `-p` 或 `--path`：support matrix 的路径。
- `-i` 或 `--index`：上传的新 ruyi index 的路径（不包含`ruyi-index`部分）。不指定的话会临时文件夹中 clone 一个新的。
- `--pr`：是否直接提交 pr。不指定的话会在控制台中显示 pr 的内容。**由于 pr 中包含用于识别重复 pr 的字段，请至少包含该 identifier！**

### 插件开发说明

由于镜像映射情况较为复杂（一份报告对应多个文件乃至于对歌 index），且 ruyi index 那边没定好每个镜像如何映射，现阶段为每个镜像写一些插件是必需的。后续可能可以考虑通用插件的开发。

新增一个插件，即在 `ruyi_index_updator/upload_plugin` 中新建一个文件即可。你可以直接引入当前文件夹下的 `prelude` 来获取一些 typing。

文件中，一个`register`函数是必须的，若其返回 Null，则说明该插件不应该被加载（你可以自行加逻辑判断）。否则，返回一个`UploadPluginBase`实例。

`UploadPluginBase`类中你需要实现以下方法：
- `get_name`：static 方法，返回插件的名字。
- `can_handle`：判断是否能处理当前镜像（以 vendor-system-variance 三元组存储，当然包含原报告在`raw_data`中）。
- `is_mapped_ruyi_index`：判断当前的 ruyi index 中的一个镜像是否可以由该报告生成。
- `handle_version`：从镜像版本 map 到 ruyi 使用的语义化版本号。更多定义问 ruyi。
- `handle_report`：使用当前报告，为 index 生成一份新的 image index。

其中包含的一些 helper 函数可自行查看。一份示例是给 lpi4a 中 ruyi 系统的插件，包含了 RevyOS 和两个 u-boot 镜像，RevyOS 镜像中又有多个文件，应该能较好的代表所有情况。