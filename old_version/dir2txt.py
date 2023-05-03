from base_model import BaseModel
import os


class Dir2txt(BaseModel):
    r"""
    A tools for custom datasets.

    
    data path:
    F:.
    │  0 (1).py
    │  0 (2).py
    └─test1
    │  0 (6).py
    │  0 (7).py
    │  0 (8).py
    │  0 (9).py
    └─test2
        main.py

    ./log/dir2txt/0_test1.txt (relative path, label=1)
    0 (6).py 0
    0 (7).py 0
    0 (8).py 0
    0 (9).py 0
    ./log/dir2txt/1_test2.txt (relative path, label=1)
    main.py 1

    """
    def __init__(self):
        super(Dir2txt, self).__init__()
        pass

    def run(self):
        root = input("Input path:")
        content = self.get_path_content(root, mode='dir')
        content = self.sort_list(content)
        save_dir = input(f"Input save dir (Default: {self.log_dir}/dir2txt):") or f"{self.log_dir}/dir2txt"
        self.mkdir(save_dir)
        for path in content:
            cls = path.replace(root, '')[1:]
            label, cls_name = cls.split("_", 1)
            save_path = f"{save_dir}/{cls}.txt"
            cls_content = self.get_path_content(path)
            cls_content = self.sort_list(cls_content)
            file_label = []
            for file in cls_content:
                file = file.replace(root, '')[1:]
                file += f" {label}"
                file_label.append(file)
            with open(save_path, 'w') as f:
                f.write(f"\n".join(file_label))
        self.log("done")


if __name__ == "__main__":
    Dir2txt().run()