[Readme (中文)](Readme.md)
[Readme (English)](Readme_en.md)

# 添加脚本至右键菜单

#### 介绍

- 为可直接作用于文件或文件夹的脚本，添加右键菜单选项。
- 暂时只支持添加脚本，不支持删除。
  - 删除可以使用开源软件：[ContextMenuManager](https://github.com/BluePointLilac/ContextMenuManager)

#### 运行

1. 选择你需要的脚本，例如 ImageResizer_256x144。
2. 编辑该目录下的 Bat_ImageResizer_256x144.bat
   1. 设置 python 路径
   2. （可选）修改选项名称。
3. 以管理员权限运行 Bat_ImageResizer_256x144.bat

- 修改前：

```bat
@REM 请设置Python路径。Please set the Python path。
set "python_path="

@REM 请设置选项名称。Please set the option name.
 set "menu_name=ScriptName"
```

- 修改后：

```bat
@REM 请设置Python路径。Please set the Python path
set "python_path=F:\0_DATA\2_CODE\Anaconda\envs\asdTools\python.exe"

@REM 请设置选项名称。Please set the option name
set "menu_name=ResizeImageTo256x144"

```

#### ImageResizer_256x144

- 支持单张图像的自动缩放，使用Pillow包实现。
