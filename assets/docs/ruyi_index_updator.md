## ruyi index updator

自动更新 ruyi 工具中镜像的索引文件，同步支持矩阵与 ruyi index。

### 使用方法

你需要设置环境变量 `GITHUB_TOKEN`，并且该 token 需要有对应仓库的读写权限和 pr 权限。或者你可以同时允许 fork 仓库的权限，让工具自动 fork 仓库。

**注意！**你直接从设置中获取到的 token 都是 personal token，但是向组织仓库进行 pr 时，该 token 是会被拒绝的。你需要使用一个 OAuth app token。最简单的辨别方法是，personal token 的格式是 `ghp` 开头，OAuth app token 的格式是 `gho` 开头。

临时测试可以通过 `gh` 命令行工具来获取一个。 **请注意不要泄漏，从 `gh` 工具获得的 token 具有您账号的全部权限。**；创建一个 OAuth app 并使用见下文。

默认工具会在临时文件夹中运行，每次可能会下载一大堆镜像文件。你可以设置环境变量 `CACHE_DIR` 来指定缓存目录，这样工具会将所有的东西都缓存到这个目录中。

renew_ruyi_index.py 里面封装了所有的操作，你可以直接运行这个脚本。各个参数的含义如下：
- `-c` 或 `--config`：配置文件的路径，可以与 nvchecker 共用。主要是要它的 `[vendor-system-variance]` 这个字段。
- `-p` 或 `--path`：support matrix 的路径。
- `-i` 或 `--index`：上传的新 ruyi index 的路径（不包含`ruyi-index`部分）。不指定的话会临时文件夹中 clone 一个新的。
- `--pr`：是否直接提交 pr。不指定的话会在控制台中显示 pr 的内容。**由于 pr 中包含用于识别重复 pr 的字段，请至少包含该 identifier！**

### 配置说明

对于镜像来说，其具有着如下的结构：
```
Device as vendor (eg: LicheePi-4A as sipeed-lpi4a)
    |
    |--- Board Variants as board_var (eg: 4g ver as 4g)
    |       |
    |       |--- System Variant as sys (eg: RevyOS as revyos)
    |       |       |
    |       |       |--- File as file (eg: uboot as uboot)
    |       |       |
    |       |       |--- File (eg: boot)
    |       |       |
    |       |       |--- File (eg: root)
    |       |
    |       |--- System Variant (eg: openKylin)
    |               |
    |               |--- File (eg: uboot)
    |               |
    |               |--- File (eg: boot)
    |               |
    |               |--- File (eg: root)
    |
    |--- Board Variants (eg: 8g ver)
            |
            |--- System Variant (eg: RevyOS)
            |       |
            |       |--- File (eg: uboot)
            |       |
            |       |--- File (eg: boot)
            |       |
            |       |--- File (eg: root)
            |
            |--- System Variant (eg: openKylin)
                    |
                    |--- File (eg: uboot)
                    |
                    |--- File (eg: boot)
                    |
                    |--- File (eg: root)
```

其中，`vendor`，`board_variant`、`system` 和 `system_variant` 被定义在了每个测试报告的 metadata 中，分别指代了板子及其类型（如 Lichee Pi 4A 的 8G 和 16G 两个版本）；系统和系统版本（如 base、xfce 镜像等）。这个四元组确定了一个镜像。

而 file 则是对于一个系统要刷入的所有文件，其可能只有一个大的 img 文件，也可能会有多个文件需要，甚至于需要进行某些预先操作。对于这些行为，ruyi 包管理器采用了如下的组织方式：

```
System Image (eg: lpi4a-8g)
|
|--- Package
|       |
|       |--- File and operation (eg: lpi4a-8g uboot into ram)
|       |
|       |--- File (eg: lpi4a-8g uboot)
|
|--- Package
|       |
|       |--- File and operation (eg: lpi4a-8g boot)
|       |
|       |--- File (eg: lpi4a-8g root)
```

而将上面的 metadata 和各种配置文件的信息转为 ruyi 的配置文件则是该工作的工作。

#### 通用说明

##### 同步方式

对于一个镜像配置，首先要说明其要使用哪种同步方式。目前支持了以下几种方式进行同步：

- doc_only：占位符，只作为去除任何未同步表示
- github_release_simple：从 github release 下载镜像文件（简易版本）
- github_release_std：从 github release 下载镜像文件（标准版本）
- mirrorsite_getter_simple：从镜像源下载镜像文件（简易版本）
- github_release_std：从镜像源下载镜像文件（标准版本）

对于简易版本和标准版本的区别如下：

从上面的结构示意可以看出，其中配置文件的复杂性很大原因是在于其是一种多对多的关系：多个 package 对多个 file。也就是说，如果我们能确定一种简单的对应关系，那会简单不少。

恰巧的，很多系统镜像只有一个文件，板子也只有一个变体。一旦做出如下的假设，能发现 System Image、Package 和 File 立刻变成了一对一的关系，极大量的简化了配置量。

为此，许多的通用同步方式都被分出了简易版和标准版。

##### 使用配置 schema 文件

在该文件夹下有着配置文件的 schemas，若您使用了任何的 yaml 语法工具，可以配置使用 `schemas/config.schema.json`，将会提供自动补全、检查和注释等一系列功能。

##### 配置文件格式

配置文件采用 yaml 格式，目前格式如下：

- util：Any，放置任何用于 yaml 引用的对象
- handler：同步配置
- - plugin：使用哪种同步方式
- - id：*可选* 名称，无除区分外作用
- - vendor：镜像四元组之一，见镜像结构
- - system：镜像四元组之一，见镜像结构
- - variant：镜像四元组之一，见镜像结构
- - **余下见具体同步配置**

###### general definition

一些通用的类格式如下：

filter：过滤

- type：判断方式类型，目前支持 `regex` 和 `lambda` 两种

if type is regex:

- filter：正则表达式，如 `"^Hello, \w*$"`

将会以传入字符串是否 match 该 regex 作为判断条件

elif type is lambda:

- filter：python lambda函数，函数原型如下：
`lambda s: str, info: SystemInfo -> bool`

mapper：映射

- type：映射方式类型，目前支持 `regex` 和 `lambda` 两种

if type is regex:

- regex：正则表达式捕获组，如 `"Hello, (.*)!"`
- mapper：format字符串，传入捕获组，如 `"Goodby, {0}!"`

format字符串见 python 定义

elif type is lambda:

- mapper：python lambda函数，函数原型如下：
`lambda s: str, info: SystemInfo -> str`

generator：生成字符串

*该类型部分重用 mapper 定义*

- type：映射方式类型，目前支持 `regex` 和 `lambda` 两种

if type is regex:

*实际指代 format 字符串*

- mapper：format 字符串，传入一个参数 `info: SystemInfo`，如 `"Hello, {info.version}!"`

format字符串见 python 定义

elif type is lambda:

- mapper：python lambda函数，函数原型如下：
`lambda s: info: SystemInfo -> str`


小技巧：
如果需要使用外部库（如 re）和多语句，lambda 函数中可以如此使用：
```python
lambda str: (re := __import__("re"), m := re.match("Hello, (.*)!"), f"Goodby, {m[1]})")[-1]
```

###### github_release_simple

- - repo：github repo
- - strategy：*默认 dd_v1*，见 ruyi 工具 doc
- - partition_map：*默认 disk*，见 ruyi 工具 doc
- - release_filter：一个 filter，选取 release 用
- - version_mapper：映射 metadata 中的 version 到语义化版本号
- - asset_filter：过滤出你想使用的文件
- - desc_mapper：生成描述

###### mirrorsite_getter_simple

- - url：mapper，映射到镜像 url
- - strategy：*默认 dd_v1*，见 ruyi 工具 doc
- - partition_map：*默认 disk*，见 ruyi 工具 doc
- - file_filter：一个 filter，选取 release 用
- - version_mapper：映射 metadata 中的 version 到语义化版本号
- - asset_filter：过滤出你想使用的文件
- - desc_mapper：生成描述

###### .*_std

对于 std 类工具，有如下几个需要阐述的定义：

files：镜像文件

fileset：文件集

这两者间组成了多对多关系，一个 fileset 包含多个 file，一个 file 也可以存在于多个 fileset 中

fileset：
- id：unique，用于引用 fileset。若为 null 表示被所有文件引用
- perpend：*可选* 添加到文件名前，若非冲突情况一般留空
- append：*可选* 添加到文件名后，若非冲突情况一般留空
- board_variants：该文件集可以用于哪些板子变体，null 表示所有
- desc_mapper：*可选* 生成描述

file：
- id：*可选* 无特殊用途
- fileset：填写 array{fileset.id} 其存在于哪些 fileset 中。null 表示所有
- **余下见具体同步配置**
- partition_map：*默认 disk*，见 ruyi 工具 doc

top：

- board_variants：该配置可以用于哪些板子变体，null 表示所有
- fileset：array(fileset)
- files：array(files)
- strategy：*默认 dd_v1*，见 ruyi 工具 doc
- partition_map：*默认 disk*，见 ruyi 工具 doc
- version_mapper：映射 metadata 中的 version 到语义化版本号

注意更具体层级的相同字段会覆盖高层级字段。若高层级中出现字段，低层级中可不填。

###### github_release_std

top:
- repo：github repo
- release_filter：一个 filter，选取 release 用

file:
- repo：github repo
- release_filter：一个 filter，选取 release 用
- asset_filter：过滤出你想使用的文件
- desc_mapper：生成描述

###### mirrorsite_getter_std

top:
- url：mapper，映射到镜像 url

file:
- url：mapper，映射到镜像 url
- file_filter：一个 filter，选取镜像文件用
- desc_mapper：生成描述

### 插件开发说明

由于镜像映射情况较为复杂（一份报告对应多个文件乃至于多个 index），且版本号存在需要自行处理的问题，现阶段为每个镜像写一些插件是必需的。后续可能可以考虑通用插件的开发。

新增一个插件，即在 `ruyi_index_updator/upload_plugin` 中新建一个文件即可。你可以直接引入当前文件夹下的 `prelude` 来获取一些 typing。

文件中，一个`register`函数是必须的，若其返回 Null，则说明该插件不应该被加载（你可以自行加逻辑判断）。否则，返回一个`UploadPluginBase`实例。

## 如何使用一个 OAuth APP

以下将会介绍如何使用一个 OAuth APP 并获取一个 token。

### 确认您想使用的账户的类型

首先，由于 Github 对权限的处理，所有的权限是 **绑定在用户上的**（包括组织），这也代表着您无法是一个组织有一个 token，而是您的账号有一个 token。因此，对于您授权的 Github 账户，请确认其类型是一个用户账户，而非组织账户。

如果您不想使用您的主账户，请放心的去创建一个新的账户。Github 为 bot 账户提供了特例，不会违反 Github 一人一号的政策：
> User accounts are intended for humans, but you can create accounts to automate activity on GitHub. This type of account is called a machine user. For example, you can create a machine user account to automate continuous integration (CI) workflows.

### 创建一个 OAuth APP

打开您账户的设置，找到 Developer settings：
![1](img/1.png)

进入，并选择 OAuth Apps：
![2](img/2.png)

点击 New OAuth App：
![3](img/3.png)

自行填写信息，其中 Authorization callback URL 可以随便填写，如
 `http://127.0.0.1:12345`, **务必勾选 Enable Device Flow**：
![4](img/4.png)

注册 APP，记录下其中的 Client ID：
![5](img/5.png)

### 使用它

在 `scripts/github_auth.py` 是一个单独的脚本，其用途就是获取一个 token。直接运行它，按照提示输入即可。
```shell
pip install -r requirements_ruyinv.txt
python scripts/github_auth.py
```
