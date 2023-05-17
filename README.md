![asdTools](asdTools.png "asdTools")

> [Github - 开源代码及Readme](https://github.com/asd123pwj/asdTools)
>
> [Blog - 工具介绍](https://mwhls.top/project/asdtools)

[ReadMe (中文)](Readme.md)
[ReadMe (English by LLMs)](Readme_en.md)

# AsdTools

[toc]

#### 使用方式

- 方式1：安装以使用

  - 下载本仓库并解压。
  - 在解压目录执行 `pip install .`
  - 在 asdTools/Tools 路径下选择并使用工具。
- 方式2：仅调用

  - 下载本仓库并解压。
  - 运行 `pip install -r requirements.txt`
  - 在 asdTools/Tools 路径下选择并使用工具。

## 功能介绍

- 具体介绍见 [Readme](asdTools/Tools/Readme.md)。

1. ImageResizer_256x144 - 调整图片的分辨率至256x144，提供了Windows右键菜单快捷方式。
2. GPUMonitor - 获取当前可用GPU的id。
3. Chat_LLMs - 用于和LLMs聊天，示例为与ChatGLM本地部署的API通信。
4. ConvertGT2MMSeg - 将GT图片转为MMSegmentation所需的图片格式。支持处理RGB图与灰度图。
5. RandomDatasetSplitter_SemanticSegmentation - 对内部文件名相同的两个文件夹进行随机划分，如语义分割中的RGB图与GT图。

## 更新历史

#### 重构

- 2023/05/03 - V0.0.1: 测试推送。
- 2023/05/05 - V0.0.2: 实现图像快捷调整至256x144，可添加至右键菜单。
- 2023/05/14 - V0.0.3: 实现GPU监控，LLMs聊天，增加看板娘，支持安装。
- 2023/05/17 - V0.0.4: 实现GT转MMSeg格式。
- 2023/05/17 - V0.0.5: 实现同时随机划分两文件夹的图片，修复安装无法import的bug。

#### 旧版代码

- 旧版代码见分支：[asd123pwj/asdTools at ShitCode_deprecated](https://github.com/asd123pwj/asdTools/tree/ShitCode_deprecated)
- 写了三十二个文件，但是经常是出于某个目的临时写的，时间赶，可读性很差，也没有多少注释，所以都删了，新版本重构，注释会让GPT帮忙。
