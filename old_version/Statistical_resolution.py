from base_model import BaseModel
from PIL import Image
import numpy as np


class Statistical_resolution(BaseModel):
    """
    Get files resolution and Statistical them. 
    No description, just test in a dir which has photos.
    """
    def __init__(self):
        # In code, I name resolution as size.
        super().__init__()

    def get_size(self, path):
        """
        Get file size
        """
        try:
            size = Image.open(path).size
            return size
        except:
            return (0, 0)

    def statistical_sizes(self, file_size, section=20):
        """
        Statistical size, get max, min, avg, and so on.
        """
        sizes_info = {}
        files = file_size["files"]
        sizes = file_size["sizes"]
        # area = [size[0] * size[1] for size in sizes]

        sizes_sort_index = np.argsort(sizes, axis=0)
        sizes_sort = np.sort(sizes, axis=0)
        # area_sort = np.argsort(area)

        max_w = [files[sizes_sort_index[-1][0]], self.list2tuple2str(sizes[sizes_sort_index[-1][0]])]
        max_h = [files[sizes_sort_index[-1][1]], self.list2tuple2str(sizes[sizes_sort_index[-1][1]])]
        # max_size = [files[area_sort[-1]], sizes[area_sort[-1]]]

        min_w = [files[sizes_sort_index[0][0]], self.list2tuple2str(sizes[sizes_sort_index[0][0]])]
        min_h = [files[sizes_sort_index[0][1]], self.list2tuple2str(sizes[sizes_sort_index[0][1]])]
        # min_size = [files[area_sort[0]], sizes[area_sort[0]]]
        
        avg_w = np.average(sizes, axis=0)[0]
        avg_h = np.average(sizes, axis=0)[1]
        # avg_area = np.average(area)

        # UGLY code, but I'm a IDIOT.
        step_w = (sizes_sort[-1][0] - sizes_sort[0][0]) // section
        step_h = (sizes_sort[-1][1] - sizes_sort[0][1]) // section
        sizes_section_w = {}
        sizes_section_h = {}
        i = 0
        j = 0
        while j < len(sizes):
            if sizes_sort[j][0] <= sizes_sort[0][0] + step_w * (i + 1):
                key = f"{sizes_sort[0][0] + step_w * i} ~ {sizes_sort[0][0] + step_w * (i + 1)}"
                self.dict_plus(sizes_section_w, key)
            else:
                i += 1
                j -= 1
            j += 1

        i = 0
        j = 0
        while j < len(sizes):
            if sizes_sort[j][1] <= sizes_sort[0][1] + step_h * (i + 1):
                key = f"{sizes_sort[0][1] + step_h * i} ~ {sizes_sort[0][1] + step_h * (i + 1)}"
                self.dict_plus(sizes_section_h, key)
            else:
                i += 1
                j -= 1
            j += 1

        sizes_info["max_w"] = max_w
        sizes_info["max_h"] = max_h
        # sizes_info["max_size"] = max_size
        sizes_info["min_w"] = min_w
        sizes_info["min_h"] = min_h
        # sizes_info["min_size"] = min_size
        sizes_info["avg_w"] = avg_w
        sizes_info["avg_h"] = avg_h
        # sizes_info["avg_area"] = avg_area
        sizes_info["distribution_w"] = sizes_section_w
        sizes_info["distribution_h"] = sizes_section_h

        return sizes_info

    def run(self):
        """
        Main process
        """
        self.help()
        path = input("input_path" + ":")
        section = int(input("input_section" + " (" + "default" + " 50):") or 50)
        file_size = {"files": [], "sizes":[]}
        not_img = 0
        files_path = self.get_path_content(path)
        for file_path in files_path:
            size = self.get_size(file_path)
            if size[0]:
                file_size["files"].append(file_path)
                file_size["sizes"].append(size)
            else:
                not_img += 1
        size_info = self.statistical_sizes(file_size, section)
        size_info["not_img"] = not_img
        self.log2file(size_info, log_path="statistical_resolution.txt", show=True)
        self.log("done")


if __name__ == "__main__":
    Statistical_resolution().run()