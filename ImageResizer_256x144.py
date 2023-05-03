from BaseClasses.ImageBase import ImageBase


if __name__ == "__main__":
    img_path = r"F:\0_DATA\1_DATA\3blog\Picture\Cover_AI\test.png"
    Resizer = ImageBase()
    img_dir = Resizer.convert_path2dir(img_path)
    img_dir = Resizer.join_path(img_dir, "256x144")
    Resizer.resize_image(img_path, (256, 144), output_dir=img_dir)
    1