![asdTools](https://s2.loli.net/2023/05/14/gyRvM4WHp6hEuxa.png "asdTools")

> [Github - 开源代码及README](https://github.com/asd123pwj/asdTools)
>
> [Blog - 工具介绍](https://mwhls.top/project/asdtools)

[ReadMe (中文)](README.md)
[ReadMe (English)](README_EN.md)

# AsdTools

[toc]

#### 使用方式

- 方式1：安装以使用

  - 下载本仓库并解压。
  - 在解压目录执行 `pip install .`
  - 在 *asdTools/Tools* 路径下选择并使用工具。
- 方式2：仅调用

  - 下载本仓库并解压。
  - 运行 `pip install -r requirements.txt`
  - 在 *asdTools/Tools* 路径下选择并使用工具。

#### 示例

- 部分工具提供文字示例、结果示例，使用示例。
- 文字示例、结果示例见脚本的注释。
- 使用示例见*Sample*文件夹。
  - 注：*Sample*文件夹内包含少量图片，可以直接在游览器上参考，无需下载。

## 功能介绍

- 具体介绍见 [README](asdTools/Tools/README.md)。

1. ImageResizer_256x144 - 调整图片的分辨率至256x144，提供了Windows右键菜单快捷方式。
2. GPUMonitor - 获取当前可用GPU的id。
3. Chat_LLMs - 用于和LLMs聊天，示例为与ChatGLM本地部署的API通信。
4. ConvertGT2MMSeg - 将GT图片转为MMSegmentation所需的图片格式。支持RGB图与灰度图的输入。
5. RandomDatasetSplitter_SemanticSegmentation - 对内部文件名相同的两个文件夹进行随机划分，如语义分割中的RGB图与GT图。
6. SDStylesBeautify - 将 Stable Diffusion Web UI 的 styles.csv 美化（包括排序，加分类头，去除空行）。
7. RGB2Gray3Channel - 转换RGB图像为三通道灰度图。
8. ColorImgWithGT - 使用彩色分割GT为原图上色。
9. ColorGT - 为GT图片上色，支持RGB图与灰度图的输入及输出。
10. WordPressSpiderInMarkdown - 爬取我的博客，以markdown返回。
11. SaveExpData - 排除无用文件，保存实验数据。
12. VisualizeHeatmapOfReID - 可视化热力图。
13. VisualizeRankOfReID - 可视化ReID Rank，极快。
14. VisualizeSegGTDistribution - 可视化语义分割GT分布。

## 更新历史

#### 重构

- 2023/05/03 - V0.0.1: 测试推送。
- 2023/05/05 - V0.0.2: 实现图像快捷调整至256x144，可添加至右键菜单。
- 2023/05/14 - V0.0.3: 实现GPU监控，LLMs聊天，增加看板娘，支持安装。
- 2023/05/17 - V0.0.4: 实现GT转MMSeg格式。
- 2023/05/17 - V0.0.5: 实现同时随机划分两文件夹的图片，修复安装无法import的bug。
- 2023/06/03 - V0.0.6: 实现SDWebUI styles.csv的美化，为快捷方式提供使用示例。
- 2023/06/12 - V0.0.7: 实现RGB转三通道灰度图。
- 2023/06/16 - V0.0.8: 实现彩色分割GT为原图上色。
- 2023/08/20 - V0.0.10: 实现爬取我的博客文章。
- 2023/08/30 - V0.0.11: 实现实验数据保存。
- 2023/09/30 - V0.0.12: 实现热力图可视化。
- 2023/10/08 - V0.0.13: 实现ReID Rank可视化。
- 2024/06/15 - V0.0.14: 实现语义分割GT分布可视化。

#### 旧版代码

- 旧版代码见分支：[asd123pwj/asdTools at ShitCode_deprecated](https://github.com/asd123pwj/asdTools/tree/ShitCode_deprecated)
- 写了三十二个文件，但是经常是出于某个目的临时写的，时间赶，可读性很差，也没有多少注释，所以都删了，新版本重构，注释会让GPT帮忙。
