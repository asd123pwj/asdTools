from asdTools.Classes.Image.ImageBase import ImageBase


class RGB2Gray3Channel(ImageBase):
    """
    转换RGB图像为三通道灰度图。示例见 Sample\RGB2Gray3Channel
    Convert RGB images into gray images with 3 channels. Example: Sample\RGB2Gray3Channel
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(multipleFiles=True, **kwargs)

    def __call__(self, imgs_dir:str) -> str:
        self.run(imgs_dir)

    def run(self, imgs_dir:str) -> str:
        imgs_path = self.get_paths_from_dir(imgs_dir)
        for i, img_path in enumerate(imgs_path):
            img_rgb = self.read_img(img_path)
            img_gray = self.convert_RGB_to_gray(img_rgb, True)
            img_name = self.get_name_of_file(img_path, keepExt=True)
            self.save_image(img_gray, output_file=img_name)
            self.log(f"{i+1}: {img_name} has converted from rgb to gray img with 3 channels.")
        self.done()


if __name__ == "__main__":
    imgs_dir = r"Sample\ImageResizer_256x144\before"
    Converter = RGB2Gray3Channel()
    Converter(imgs_dir)
