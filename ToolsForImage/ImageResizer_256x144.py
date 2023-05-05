import sys
import os
# 写了几年python，我还是没搞懂怎么让他正常导入上级文件，所以这里写的很丑。
# I’ve been writing Python for several years, but I still haven’t figured out how to import files from the parent directory properly. That’s why the code here looks ugly.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ClassesBase.ImageBase import ImageBase


if __name__ == "__main__":
    try:
        img_path = sys.argv[1]
        img_path = img_path.strip('"')
        size = (256, 144)
        Resizer = ImageBase(name=f"ImageResizer_{size[0]}x{size[1]}")
        output_dir = Resizer.convert_path2dir(img_path)
        output_dir = Resizer.join_path(output_dir, f"{size[0]}x{size[1]}")
        output_path = Resizer.resize_image(img_path, size, output_dir=output_dir)
        # if you need log, use the following code.
        Resizer.log(f"Resized {img_path} to {size[0]}x{size[1]}, saved to {output_path}.")
    except Exception as e:
        print(e)
        input("Press Enter to exit.")