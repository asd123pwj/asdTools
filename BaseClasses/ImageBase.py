from PIL import Image
from BaseClasses.IOBase import IOBase


class ImageBase(IOBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def resize_image(self, 
                     path:str, 
                     size:tuple, 
                     output_dir:str="", 
                     output_file:str="") -> str:
        if output_dir == "":
            output_dir = self.log_dir
        self.mkdir(output_dir)
        if output_file == "":
            output_file = self.convert_path2name(path, True)
        output_path = self.join_path(output_dir, output_file)
        with Image.open(path) as img:
            img.thumbnail(size)
            img.save(output_path)
        return output_path