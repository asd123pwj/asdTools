from asdTools.Classes.Image.ImageBase import ImageBase


class ColorImgWithGT(ImageBase):
    """
    使用彩色分割GT为原图上色。示例见 Sample\ColorImgWithGT 
    注：可使用asdTools\Tools\Image\ColorGT.py为GT上色
    Colorize the image with the colorful segmentation GT. Examples can be found in the "Sample\ColorImgWithGT" folder.
    Note: You can use the "asdTools\Tools\Image\ColorGT.py" script to colorize the GT. 
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(multipleFiles=True, **kwargs)

    def __call__(self, imgs_dir:str, GTs_dir:str) -> str:
        self.run(imgs_dir, GTs_dir)
        
    def map_paths_to_fullPaths(self, files_dir:str, files_path:list):
        res = {}
        for file_path in files_path:
            fullPath = file_path
            path = fullPath[len(files_dir)+1:]
            res[path] = fullPath
        return res

    def run(self, imgs_dir:str, GTs_dir:str) -> str:
        imgs_path = self.get_paths_from_dir(imgs_dir)
        imgs_path = self.filter_ext(imgs_path, ["png", "jpg", "jpeg"])
        imgs_path_mapping = self.map_paths_to_fullPaths(imgs_dir, imgs_path)
        GTs_path = self.get_paths_from_dir(GTs_dir)
        GTs_path = self.filter_ext(GTs_path, ["png", "jpg", "jpeg"])
        GTs_path_mapping = self.map_paths_to_fullPaths(GTs_dir, GTs_path)
        for i, (img_path, img_fullPath) in enumerate(imgs_path_mapping.items()):
            try:
                GT_fullPath = GTs_path_mapping[img_path]
            except:
                self.warning(f"{i+1}: GT is not found: {img_path}")
                continue
            img_res = self.blend(img_fullPath, GT_fullPath, 0.25)
            img_dir = self.get_dir_of_file(img_path)
            img_name = self.get_name_of_file(img_path, True)
            self.save_image(img_res, output_middle_dir=img_dir, output_file=img_name)
            self.log(f"{i+1}: Img has been colored: {img_path}")
        self.done()


if __name__ == "__main__":
    imgs_dir = r"Sample\ColorImgWithGT\Before\Images"
    GTs_dir = r"Sample\ColorImgWithGT\Before\Annotations"
    Converter = ColorImgWithGT()
    Converter(imgs_dir, GTs_dir)
