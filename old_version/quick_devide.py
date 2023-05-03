import os.path as osp
import random
import shutil
from base_model import BaseModel

class Quick_devide(BaseModel):
    """
    Quick devide files into a number of copies
    mode:
        1: random select <num> files
        2: random select <num> files until all files have been select
        3: select <num> files in order
        4: select <num> files in order until all files have been select

    Project tree:
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

    Project tree after deviding (mode = 2, num = 2)
    F:.
    ├─1-2
    │      0 (3).py
    │      0 (5).py
    ├─3-4
    │      0 (1).py
    │      0 (4).py
    ├─5-5
    │      0 (2).py
    └─test1
        │  0 (6).py
        │  0 (7).py
        │  0 (8).py
        │  0 (9).py
        └─test2
                main.py

    """
    def __init__(self):
        super(Quick_devide, self).__init__()
        pass

    def divide(self, content, mode, num):
        """
        mode: 
            random_once: random select <num> files
            random_all:  random select <num> files until all files have been select
            order_once:  select <num> files in order
            order_all:   select <num> files in order until all files have been select
        """
        if 'random' in mode:
            random.shuffle(content)
        result = []
        while True:
            if len(content) > num:
                result.append(content[:num])
                content = content[num:]
            else:
                result.append(content)
                break
            if 'once' in mode:
                break

        return result

    def mode2str(self, mode):
        if mode == '1':
            mode = 'random_once'
        elif mode == '2':
            mode = 'random_all'
        elif mode == '3':
            mode = 'order_once'
        elif mode == '4':
            mode = 'order_all'
        return mode

    def merge_files(self, contents_split):
        start = 1
        end = 0
        for content_split in contents_split:
            end += len(content_split)
            subfolder = str(f"{start}-{end}")
            dir_dest = osp.join(content_split[0][0], subfolder)
            self.mkdir(dir_dest)
            for dir, file in content_split:
                src = osp.join(dir, file)
                dest = osp.join(dir_dest, file)
                shutil.move(src, dest)
            start = end + 1

    def help(self): 
        """ Help function
        Print the help message
        """
        print(self.__doc__)

    def run(self):
        self.help()
        mode = input("Input mode:")
        num = int(input("Input max number of a group:"))
        if not mode in ['1', '2', '3', '4']:
            print("Error mode.")
            return -1 
        path = input("Input path:")
        mode = self.mode2str(mode)
        content = self.get_path_content(path, mode='peer')
        content = self.sort_list(content)
        content = self.divide(content, mode, num)
        contents_split = self.split_content(content)
        self.merge_files(contents_split)
        print("done")


if __name__ == '__main__':
    Quick_devide().run()
        