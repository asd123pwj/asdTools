from base_model import BaseModel
from PIL import Image
import numpy as np


class StatisticalColor(BaseModel):
    """
    Get files resolution and Statistical them. 
    No description, just test in a dir which has photos.
    """
    def __init__(self):
        # In code, I name resolution as size.
        super().__init__()

    def get_color_set(self, path):
        """
        Get file size
        """
        img = Image.open(path)
        img_array = np.array(img)
        if len(img_array.shape) == 2:
            # (H, W)
            img_array = img_array.reshape(img_array.shape[0] * img_array.shape[1])
            color_set = set(img_array.tolist())
        elif len(img_array.shape) == 3:
            # (H, W, C)
            # no need, no write.
            pass
        return color_set

    def run(self):
        """
        Main process
        """
        self.help()
        # path = input("input_path:")
        path = r"F:\0_DATA\1_DATA\Datasets\RainyWCity\segmentation_realRain (2)\segmentation_realRain\gtFine"
        path = r"F:\0_DATA\1_DATA\Datasets\RainyWCity\segmentation_realRain (2)\segmentation_realRain\gtFineID"
        colors_set = set()
        files_path = self.get_path_content(path)
        for file_path in files_path:
            color_set = self.get_color_set(file_path)
            colors_set = color_set | colors_set
        colors_list = list(colors_set)
        colors_dict = {colors_list[i]: i for i in range(len(colors_list))}
        colors_num_dict = {colors_list[i]: 0 for i in range(len(colors_list))}

        for file_path in files_path:
            color_set = self.get_color_set(file_path)
            for color in color_set:
                colors_num_dict[color] += 1
            if len(color_set) == len(colors_set):
                self.log_file(f"File has all color: {file_path}")

        self.log(f"color number: {len(colors_set)}")
        self.log(f"{colors_num_dict}")
        self.log2file(colors_dict, log_path="statistical_color.json", show=True)
        self.log("done")


if __name__ == "__main__":
    StatisticalColor().run()