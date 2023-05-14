![asdTools](asdTools.png "asdTools")

> [Github](https://github.com/asd123pwj/QuickRename)
>
> [Blog](https://mwhls.top/3944.html)

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

1. ImageResizer_256x144 - 缩放图片至256x144。
2. GPUMonitor - 获取当前可用GPU的id。
3. Chat_LLMs - 调用 ChatGLM API 进行聊天。

## 更新历史

#### 重构

- 2023/05/03 - V0.0.1: 测试推送。
- 2023/05/05 - V0.0.2: 实现图像快捷调整至256x144，可添加至右键菜单。
- 2023/05/14 - V0.0.3: 实现GPU监控，LLMs聊天，增加看板娘，支持安装。

#### 旧版代码

- 旧版代码见分支：[asd123pwj/asdTools at ShitCode_deprecated](https://github.com/asd123pwj/asdTools/tree/ShitCode_deprecated)
- 写了三十二个文件，但是经常是出于某个目的临时写的，时间赶，可读性很差，也没有多少注释，所以都删了，新版本重构，注释会让GPT帮忙。
