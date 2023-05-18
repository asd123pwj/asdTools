![asdTools](asdTools.png "asdTools")

> [Github - Code and README](https://github.com/asd123pwj/asdTools)
>
> [Blog - Describtion of tools](https://mwhls.top/project/asdtools)

[ReadMe (中文)](README.md)
[ReadMe (English by LLMs)](README_EN.md)

# AsdTools

[toc]

#### Usage

- Method 1: Install to use

  - Download and extract this repository.
  - Run `pip install .` in the extracted directory.
  - Choose and use the tool in the asdTools/Tools directory.
- Method 2: Only call

  - Download and extract this repository.
  - Run `pip install -r requirements.txt`.
  - Choose and use the tool in the asdTools/Tools directory.

## Features

- For detailed information, please see [README](asdTools/Tools/README.md).

1. ImageResizer_256x144 - Resize images to 256x144.
2. GPUMonitor - Get the ID of the currently available GPU.
3. Chat_LLMs - Call ChatGLM API for chatting.
4. ConvertGT2MMSeg - Convert GT images to the image format required by MMSegmentation. It can handle RGB images and grayscale images.
5. RandomDatasetSplitter_SemanticSegmentation - Randomly split two folders with the same internal file names, such as RGB images and GT (Ground Truth) images in semantic segmentation.

## Update History

#### Refactoring

- 2023/05/03 - V0.0.1: Test push.
- 2023/05/05 - V0.0.2: Implement image quick adjustment to 256x144 and add to the right-click menu.
- 2023/05/14 - V0.0.3: Implement GPU monitoring, LLMs chatting, add poster girl, and support installation.
- 2023/05/17 - V0.0.4: Implement GT2MMSeg converter.
- 2023/05/17 - V0.0.5: Implement the simultaneous random split of images in two folders and fix the bug preventing import.

#### Old Version Code

- The old version code can be found in the branch: [asd123pwj/asdTools at ShitCode_deprecated](https://github.com/asd123pwj/asdTools/tree/ShitCode_deprecated)
- Thirty-two files were written, but they were often written temporarily for a certain purpose, the time was rushed, the readability was poor, and there were not many comments, so they were all deleted. The new version was refactored and the comments will be done by GPT.
