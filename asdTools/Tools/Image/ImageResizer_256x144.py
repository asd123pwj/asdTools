from asdTools.Classes.Image.ImageBase import ImageBase
import sys


if __name__ == "__main__":
    try:
        img_path = sys.argv[1]
        img_path = img_path.strip('"')
        size = (256, 144)
        Resizer = ImageBase(name=f"ImageResizer_{size[0]}x{size[1]}")

        output_dir = Resizer.get_dir_of_file(img_path)
        output_dir = Resizer.join(output_dir, f"{size[0]}x{size[1]}")
        output_file = Resizer.get_name_of_file(img_path, True)
        output_file = Resizer.add_suffix(output_file, "_resized")
        output_path = Resizer.join(output_dir, output_file)

        output_path = Resizer.resize_image(img_path, size, output_path=output_path)
        # if you need log, use the following code.
        # Resizer.log(f"Resized {img_path} to {size[0]}x{size[1]}, saved to {output_path}.")
    except Exception as e:
        print(e)
        input("Press Enter to exit.")