from curses.ascii import isdigit
import os
import shutil


class Quick_prefix_dir():
    """
    Quick add a prefix to directory, test in Windows 11, maybe available for linux.

    Project tree:
    QuickRename
    ├─ build
    │  ├─ dist
    │  └─ main
    │     ├─ main.exe.manifest
    ├─ 009_dist
    │  └─ QuickRename v1.0.0.exe
    ├─ main.py
    └─ test1

    Project tree after add prefix:
    QuickRename
    ├─ 010_build
    │  ├─ 001_dist
    │  └─ 002_main
    │     ├─ main.exe.manifest
    ├─ 009_dist
    │  └─ QuickRename v1.0.0.exe
    ├─ main.py
    └─ 011_test1

    """
    def __init__(self):
        self.dir_source = ''    # Dirs in dir_source will be processed
        self.digits = 3         # The digits of index, e.g. 1 -> 001, 54 -> 054
        self.seg = ' '          # Segmentation between prefix and dirname
        self.is_backup = False  
        self.index = 1

    def modify_dir_name(self, dir_source):
        """ Modify dir name recursively
        add a prefix to dir name
        e.g. Dir1 -> 001_Dir1, Dir2 -> 002_Dir2
        """
        for root, dirs, files in os.walk(dir_source):
            index = self.find_max_index(dirs) + 1
            for dir in dirs:
                dir_source = os.path.join(root, dir)
                if self.get_prefix(dir) != -1:
                    self.modify_dir_name(dir_source)
                    continue
                index_dir = str(index).rjust(self.digits, '0') + self.seg
                dir_dest = os.path.join(root, index_dir + dir)
                os.rename(dir_source, dir_dest)
                index += 1
                print(f"{self.index}: {dir} -> {index_dir + dir}, in {root}")
                self.index += 1
                self.modify_dir_name(dir_dest)

    def find_max_index(self, dirs):
        """ Find the max index in dirs
        """
        index_max = 0
        for dir in dirs:
            index_max = max(index_max, self.get_prefix(dir))
        return index_max

    def get_prefix(self, dir):
        """ Get the prefix of dir
        e.g.
            000_dirname: return 0
            0061_dirname: return 61
            _dirname: return -1
            dirname: return -1
        """
        try:
            prefix, _ = dir.split(self.seg, 1)
        except:
            return -1
        if prefix.isdigit():
            return int(prefix)
        else:
            return -1
        
    def backup_dir(self, dir_source):
        """ Backup dir
        copy dir_source to dir_source_backup recursively
        """
        dir_source_backup = dir_source + '_backup'
        shutil.copytree(dir_source, dir_source_backup)

    def help(self):
        """ Help function
        Print the help message
        """
        print(self.__doc__)

    def run(self):
        """ Main function
        """
        self.help()

        digits = input("Input the digits of index, default: 3 (e.g. index=2, dir->002_dir)\n")
        if digits.isdigit():
            self.digits = int(digits)
        elif digits == '':
            pass
        else:
            print("Error Type, digits is set to 3.")

        seg = input("Input the segmentaion between prefix and dirname, default: ' '\n")
        self.seg = seg if seg != '' else self.seg
        
        is_backup = input("Need to backup the dir? [y/N]\n")
        self.is_backup = True if is_backup in ['y', 'Y'] else False

        while True:
            self.dir_source = input("Input the directory path:\n")
            if self.is_backup:
                self.backup_dir(self.dir_source)
            self.index = 1
            self.modify_dir_name(self.dir_source)

