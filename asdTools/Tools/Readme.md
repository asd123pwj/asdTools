[Readme (中文)](Readme.md)

[Readme (English by LLMs)](Readme_en.md)

# 工具支持

[toc]

#### 介绍

- 包括以下内容：

  1. 即开即用的工具。
  2. 为快捷方式设计的工具。
  3. 外部调用示例。
- 日志记录：

  1. 支持日志记录，所有输出将默认保存至调用路径下的 ./Logs 中。
  2. 在初始化时加入参数 `log_dir="./OtherLogDir"` 以修改保存文件夹。
  3. 在初始化时加入参数 `log_file="otherLogFile.txt"` 以修改保存日志名称。
  4. 如 `GPUMonitor(log_dir="/root/logs", log_file="GPUMonitor.log")`

#### AI 工具支持

1. GPUMonitor - 调用示例
   - 获取可用GPU的ID。

#### API 工具支持

1. Chat_LLMs - 即开即用
   - 调用 ChatGLM 本地 API 进行聊天。

#### Image 工具支持

1. ImageResizer_256x144 - 快捷方式
   - 缩放图像至256x144。
