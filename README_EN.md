![asdTools](https://s2.loli.net/2023/05/14/gyRvM4WHp6hEuxa.png "asdTools")

> [Github - Code and README](https://github.com/asd123pwj/asdTools)
>
> [Blog - Describtion of tools](https://mwhls.top/project/asdtools)

[ReadMe (中文)](README.md)
[ReadMe (English)](README_EN.md)

# AsdTools

[toc]

#### Usage

- Method 1: Install to use

  - Download and extract this repository.
  - Run `pip install .` in the extracted directory.
  - Choose and use the tool in the *asdTools/Tools* directory.
- Method 2: Only call

  - Download and extract this repository.
  - Run `pip install -r requirements.txt`.
  - Choose and use the tool in the *asdTools/Tools* directory.

#### Examples

- Some tools provide text examples, result examples, and usage examples.
- Text examples and result examples can be found in the comments of the scripts.
- Usage examples can be found in the *Sample* folder.
  - Note: The folder *Sample* contains a small number of images that can be referenced directly in the browser, without the need for downloading.

## Features

- For detailed information, please see [README](asdTools/Tools/README.md).

1. ImageResizer_256x144 - Resize images to 256x144.
2. GPUMonitor - Get the ID of the currently available GPU.
3. Chat_LLMs - Call ChatGLM API for chatting.
4. ConvertGT2MMSeg - Convert GT images to the image format required by MMSegmentation. Support input and output RGB images and grayscale images.
5. RandomDatasetSplitter_SemanticSegmentation - Randomly split two folders with the same internal file names, such as RGB images and GT (Ground Truth) images in semantic segmentation.
6. SDStylesBeautify - Beautify the styles.csv of the Stable Diffusion Web UI (including sorting, adding category headers, removing empty lines).
7. RGB2Gray3Channel - Convert RGB images into gray images with 3 channels.
8. ColorImgWithGT - Colorize the image with the colorful segmentation GT.

## Update History

#### Refactoring

- 2023/05/03 - V0.0.1: Test push.
- 2023/05/05 - V0.0.2: Implement image quick adjustment to 256x144 and add to the right-click menu.
- 2023/05/14 - V0.0.3: Implement GPU monitoring, LLMs chatting, add poster girl, and support installation.
- 2023/05/17 - V0.0.4: Implement GT2MMSeg converter.
- 2023/05/17 - V0.0.5: Implement the simultaneous random split of images in two folders and fix the bug preventing import.
- 2023/06/03 - V0.0.6: Implement to beautify SDWebUI styles.csv, provide usage examples for shortcuts.
- 2023/06/12 - V0.0.7: Implement to convert RGB images into gray images with 3 channels.
- 2023/06/16 - V0.0.8: Implement to colorize the image with the colorful segmentation GT.

#### Old Version Code

- The old version code can be found in the branch: [asd123pwj/asdTools at ShitCode_deprecated](https://github.com/asd123pwj/asdTools/tree/ShitCode_deprecated)
- Thirty-two files were written, but they were often written temporarily for a certain purpose, the time was rushed, the readability was poor, and there were not many comments, so they were all deleted. The new version was refactored and the comments will be done by GPT.
