from asdTools.Classes.Base.BaseModel import BaseModel
from PIL import Image
import numpy as np


class ImageBase(BaseModel):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def resize_image(self, 
                     img, 
                     size:tuple=(224, 224)):
        if isinstance(img, str):
            img = self.read_img(img)
        img.thumbnail(size)
        return img
        # with Image.open(path) as img:
        #     img.thumbnail(size)
        #     output_dir = self.get_dir_of_file(output_path)
        #     self.mkdir(output_dir)
        #     img.save(output_path)
        # return output_path

    def save_image(self, img, output_dir:str="", output_file:str="xxx_resized.png") -> str:
        if isinstance(img, str):
            img = self.read_img(img)
        if output_dir == "":
            output_dir = self.log_dir
        output_path = self.join(output_dir, output_file)
        img.save(output_path)
        return output_path

    @staticmethod
    def read_img(path:str):
        with Image.open(path) as img:
            return img

    @staticmethod
    def convert_img_to_array(img):
        img_array = np.array(img)
        return img_array
    