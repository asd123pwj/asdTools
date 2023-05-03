from base_model import BaseModel
from PIL import Image
import numpy as np
import json


class SortColor(BaseModel):
    """
    Get files resolution and Statistical them. 
    No description, just test in a dir which has photos.
    """
    def __init__(self):
        # In code, I name resolution as size.
        super().__init__()

    def sort_image_color_by_index(self, path, colors_dict):
        img = Image.open(path)
        img_array = np.array(img)
        for k, v in colors_dict.items():
            img_array[img_array==int(k)] = v
        return img_array
        

    def run(self):
        """
        Main process
        """
        self.help()
        # path = input("input_path:")
        imgs_path = r"F:\0_DATA\1_DATA\Datasets\RainyWCity\annotations\origin\all"
        json_path = r"F:\0_DATA\1_DATA\CODE\PYTHON\202207_Tools\asdTools\log\StatisticalColor\1677067493.853984\statistical_color.json"
        with open(json_path, 'r') as json_file:
            colors_dict = json.load(json_file)
        files_path = self.get_path_content(imgs_path)
        for i, file_path in enumerate(files_path):
            img_array = self.sort_image_color_by_index(file_path, colors_dict)
            save_name = self.path2name(file_path, keep_ext=True)
            save_path = self.save_array_as_img(img_array, save_name, mode='imageio')
            self.log(f"{i+1}: {save_path} has generated")
        self.log("done")


if __name__ == "__main__":
    SortColor().run()