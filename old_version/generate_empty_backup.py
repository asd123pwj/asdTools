import os
import os.path as osp
from base_model import *


class Generate_empty_backup():
    """
    Generate backup files which have the same name but empty.
    Project tree:
    root
    └─ QuickRename
        ├─ build
        │  └─ main
        │      └─ main.exe.manifest     # 2kb
        ├─ 009_dist
        │  └─ QuickRename v1.0.0.exe    # 6756kb
        ├─ main.py                       # 1kb
        └─ test1

    Project tree after adding prefix:
    root
    ├─ QuickRename
    │  ├─ build
    │  │  └─ main
    │  │      └─ main.exe.manifest     # 2kb
    │  ├─ 009_dist
    │  │  └─ QuickRename v1.0.0.exe    # 6756kb
    │  ├─ main.py                       # 1kb
    │  └─ test1
    └─ QuickRename_empty
        ├─ build
        │  └─ main
        │      └─ main.exe.manifest     # 0kb
        ├─ 009_dist
        │  └─ QuickRename v1.0.0.exe    # 0kb
        ├─ main.py                       # 0kb
        └─ test1
    """
    def __init__(self):
        pass

    def save_file_empty(self, save_path):
        # save empty file.
        dir = osp.split(save_path)[0]
        if not osp.exists(dir):
            os.makedirs(dir)
        
        with open(save_path, 'w'):
            pass

    def rename_content(self, root, root_content):
        root_backup_content = []
        for content in root_content:
            content = content[:len(root)] + '_empty' + content[len(root):]
            root_backup_content.append(content)
        return root_backup_content
        
    def help(self): 
        """ Help function
        Print the help message
        """
        self.log(self.__doc__)

    def run(self):
        self.help()

        root = input("Input path:")
        root_content = get_path_content(root)
        root_backup_content = self.rename_content(root, root_content)
        for path in root_backup_content:
            self.save_file_empty(path)
        self.log("Completed.")
