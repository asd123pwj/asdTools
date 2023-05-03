from base_model import BaseModel
import os
import random


class Divide_ClsLabel_file(BaseModel):
    """
    A tools for divide classification label file to get train set and test set.

    class_all.txt:
        0 (1).py 0
        0 (2).py 1
        0 (3).py 2
        0 (4).py 2
        0 (5).py 1
    -->
    train.txt:
        0 (1).py 0
        0 (2).py 1
        0 (4).py 2
    test.txt:
        0 (3).py 2
        0 (5).py 1
    """
    def __init__(self):
        super(Divide_ClsLabel_file, self).__init__()

    def run(self):
        root = input("Input path:")
        prob = float(input("Input probabilty of train set (default: 0.7):") or 0.7)
        with open(root, 'r') as f:
            path_label_list = f.readlines()
        random.shuffle(path_label_list)
        train_set_len = int(len(path_label_list) * prob)
        path_label_list_train = path_label_list[:train_set_len]
        path_label_list_test = path_label_list[train_set_len:]
        path_label_list_train_sort = self.sort_list(path_label_list_train)
        path_label_list_test_sort = self.sort_list(path_label_list_test)
        filename = self.path2name(root)
        self.log2file(path_label_list_train_sort, log_path=f"{filename}_train.txt", show=True)
        self.log2file(path_label_list_test_sort, log_path=f"{filename}_test.txt", show=True)
        self.log('done')
        


if __name__ == "__main__":
    Divide_ClsLabel_file().run()