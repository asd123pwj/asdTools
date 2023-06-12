from asdTools.Classes.Base.BaseModel import BaseModel
from PIL import Image
import numpy as np


class ImageBase(BaseModel):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def convert_img_to_arr(self, img:Image.Image) -> np.ndarray:
        img_array = np.array(img)
        return img_array
    
    def convert_arr_to_img(self, arr:np.ndarray) -> Image.Image:
        img = Image.fromarray(arr.astype(np.uint8))
        return img

    def convert_RGB_to_gray(self, img:Image.Image, need3Channel:bool=False) -> Image.Image:
        gray_img = img.convert('L')
        if need3Channel:
            gray_img = gray_img.convert('RGB')
        return gray_img

    def count_img_color(self, img:Image.Image) -> set:
        img = self.read_img(img)
        unique_color = img.getcolors(img.size[0] * img.size[1])
        return unique_color

    def count_imgs_color(self, imgs:list) -> dict:
        unique_res = {}
        for img in imgs:
            unique_img = self.count_img_color(img)
            for color in unique_img:
                self.count_in_dict(unique_res, color[1], color[0])
        return unique_res

    def get_img_info(self, img_path:str):
        img = self.read_img(img_path)
        img_array = self.read_img(img, output_type="array")
        img_info = {}
        img_info["path"] = str(img_path)
        img_info["shape"] = img_array.shape
        return img_info
    
    def generate_image(self, mode:str, size:tuple, **kwargs):
        img = Image.new(mode, size, **kwargs)
        return img

    def resize_image(self, 
                     img:Image.Image, 
                     size:tuple=(224, 224)) -> Image.Image:
        img = self.read_img(img)
        img = img.resize(size)
        return img

    def read_img(self, path, output_type="Image"):
        if isinstance(path, str):
            with Image.open(path) as f:
                img = f
                img.load()
        elif isinstance(path, Image.Image):
            img = path
        elif isinstance(path, np.ndarray):
            img = self.convert_arr_to_img(path)
        
        if output_type == "Image":
            return img
        elif output_type == "array":
            img_array = self.convert_img_to_arr(img)
            return img_array

    def save_image(self, img:Image.Image, output_dir:str="", output_file:str="xxx_resized.png") -> str:
        img = self.read_img(img)
        output_path = self.generate_output_path(output_dir=output_dir, output_file=output_file)
        img.save(output_path)
        return output_path



if __name__ == "__main__":
    img_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\train\gt"
    img_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\train\vl"
    img_analyzer = ImageBase()
    imgs_path = img_analyzer.get_paths_from_dir(img_dir)
    unique_color = img_analyzer.count_imgs_color(imgs_path)
    pass