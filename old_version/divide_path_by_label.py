from base_model import BaseModel
import os


class Divide_path_by_label(BaseModel):
    """
    A tools for divide datasets by label.

    class_all.txt:
        0 (1).py 0
        0 (2).py 1
        0 (3).py 2
        0 (4).py 2
        0 (5).py 1
    -->
    class_0.txt:
        0 (1).py 0
    class_1.txt:
        0 (2).py 1
        0 (5).py 1
    class_2.txt:
        0 (3).py 2
        0 (4).py 2
    """
    def __init__(self):
        super(Divide_path_by_label, self).__init__()

    def run(self):
        root = input("Input path:")
        with open(root, 'r') as f:
            path_label_list = f.readlines()
            path_label_list_sort = self.sort_by_label(path_label_list)
        for i, label in enumerate(path_label_list_sort[0]):
            path = f"class_{label}.txt"
            label_list = path_label_list_sort[i+1]
            self.log2file(label_list, log_path=path, show=True)
        self.log('done')
        


if __name__ == "__main__":
    Divide_path_by_label().run()