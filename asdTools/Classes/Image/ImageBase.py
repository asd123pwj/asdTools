from asdTools.Classes.Base.BaseModel import BaseModel
from PIL import Image


class ImageBase(BaseModel):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def resize_image(self, 
                     path:str, 
                     size:tuple=(224, 224), 
                     output_path:str="./Logs/resized.png") -> str:
        with Image.open(path) as img:
            img.thumbnail(size)
            output_dir = self.get_dir_of_file(output_path)
            self.mkdir(output_dir)
            img.save(output_path)
        return output_path