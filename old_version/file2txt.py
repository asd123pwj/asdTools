from base_model import BaseModel
import os


class File2txt(BaseModel):
    r"""
    A tools for custom datasets.

    
    data path:
    F:.
    │  0 (1).py
    │  0 (2).py
    │  0 (3).py
    │  0 (4).py
    │  0 (5).py
    └─test1
        │  0 (6).py
        │  0 (7).py
        │  0 (8).py
        │  0 (9).py
        └─test2
                main.py

    ./path_label.txt (relative path, label=1)
    0 (1).py 1
    0 (2).py 1
    0 (3).py 1
    0 (4).py 1
    0 (5).py 1
    test1\0 (6).py 1
    test1\0 (7).py 1
    test1\0 (8).py 1
    test1\0 (9).py 1
    test1\test2\main.py 1

    """
    def __init__(self):
        super(File2txt, self).__init__()
        pass

    def run(self):
        root = input("Input path:")
        content = self.get_path_content(root)
        content = self.sort_list(content)
        label = input("Input label:")
        mode = input("Absolute path (0) or relative path (1, default):") or '1'
        path_label = []
        for path in content:
            if mode == '1':
                path = path.replace(root, '')[1:]
            path_label.append(f"{path} {label}\n")
        path_label[-1] = path_label[-1][:-1]
        tip = f"""
The first 3 lines in path_label.txt:
{path_label[:3]}
Want to add prefix to path? 
For example: 
cat.png 0
---> add prefix "animals/" --->
animals/cat.png 0
prefix (Blank to skip):
"""
        prefix = input(tip)
        if prefix != "":
            for i, line in enumerate(path_label):
                path_label[i] = prefix + line
        
        # save_path = input(f"Input save path (Default: {self.log_dir}/path_label.txt):") or f'{self.log_dir}/path_label.txt'
        # with open(save_path, 'w') as f:
        #     path_label = "".join(path_label)
        #     f.write(path_label)
        self.log2file(path_label, "path_label.txt")
        self.log("done")


if __name__ == "__main__":
    File2txt().run()