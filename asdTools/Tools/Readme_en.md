[Readme (中文)](Readme.md)

[Readme (English by LLMs)](Readme_en.md)

# Tool Support

[toc]

#### Introduction

* Includes the following:
  1. Out-of-the-box tools.
  2. Tools designed for shortcuts.
  3. External call examples.
* Logging:
  1. Supports logging, and all outputs will be saved by default to ./Logs under the calling path.
  2. Add the parameter `log_dir="./OtherLogDir"` during initialization to modify the save folder.
  3. Add the parameter `log_file="otherLogFile.txt"` during initialization to modify the saved log name.
  4. Example: `GPUMonitor(log_dir="/root/logs", log_file="GPUMonitor.log")`

#### AI Tool Support

1. GPUMonitor - Call example
   * Get the ID of available GPUs.

#### API Tool Support

1. Chat_LLMs - Out-of-the-box
   * Call the ChatGLM local API for chatting.

#### Image Tool Support

1. ImageResizer_256x144 - Shortcut
   * Scale images to 256x144.
