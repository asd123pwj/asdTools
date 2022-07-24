> [Github](https://github.com/asd123pwj/QuickRename)
>
> [Blog](https://mwhls.top/3944.html)

## Update 更新

1. V1.0.0: Add functions: `1. Click to rename a file`, `2. Rename files in directory`.
2. V1.1.0: Add a function: `3. Add prefix to directory `.

## Usage 用法

#### 1. One file rename 单文件重命名

- Click file1 and file2 to rename file2 as follow:
  点击文件1与文件2以重命名文件2：


```c
    Quick rename one file for windows.
    Click file1 and file2 to rename file2 as follow:
    点击文件1与文件2以重命名文件2：
    Step:
        1. Run the script                       运行脚本
        2. Click on the old file.               点击旧文件
        3. Press <q> to copy the file name.     按<q>复制文件名
        4. Click on the new file.               点击新文件
        5. Press <e> to paste the file name.    按<e>粘贴文件名
        6. Press <esc> to exit.                 按<esc>退出
```

#### 2. Directory files rename 文件夹内文件重命名

- Copy the path of dir1 and dir2 to rename files in dir2 as follow:
  复制路径1与路径2以重命名路径2内文件：

```c
    Quick rename files in directory for windows.
    Copy the path of dir1 and dir2 to rename files in dir2 as follow:
    复制路径1与路径2以重命名路径2内文件：
    Step / 步骤:
        1. Run the script                                   运行脚本
        2. Copy the source directory path.                  复制源目录路径
        3. Press <q> to record source directory path.       按<q>记录源目录路径
        4. Copy the destination directory path.             复制目标目录路径
        5. Press <e> to record destination directory path.  按<e>记录目标目录路径
        6. Press <w> to rename destination directory path.  按<w>重命名目标目录路径
        7. Press <esc> to exit.                             按<esc>退出
```

#### 3. Add prefix to directory 文件夹添加前缀

- Support:
  - The digits of index, default: 3.    修改序号位数，默认3
  - The segmentation between prefix and dirname, default: ' '.    修改分隔符，默认空格
  - Index of prefix start from the biggest index.    从已有的最大序号开始对前缀技术。
  - Pass the directory which have prefix.     跳过有前缀的文件夹。
- Example(`digits=3, segmentation='_'`):

```c
Project tree
QuickRename
├─ build
│  ├─ dist
│  └─ main
│     └─ main.exe.manifest
├─ 009_dist
│  └─ QuickRename v1.0.0.exe
├─ main.py
└─ test1

Project tree after add prefix:
QuickRename
├─ 009_dist
│  └─ QuickRename v1.0.0.exe
├─ 010_build
│  ├─ 001_dist
│  └─ 002_main
│     └─ main.exe.manifest
├─ main.py
└─ 011_test1
```

## Download 下载

GitHub: https://github.com/asd123pwj/QuickRename/releases
