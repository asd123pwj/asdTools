import numpy as np
import os
import os.path as osp
import re
import json
import time
import datetime


class BaseModel():
    """
    BaseModel, call it "utils" is OK.
    """
    def __init__(self, log_dir='', mode='timestamp'):
        if log_dir == '':
            self.log_root = f"./log/{self.__class__.__name__}"
        else:
            self.log_root = log_dir
        self.log_dir = self.log_root
        self.timestamp = time.time()
        self.log_file = f"{self.__class__.__name__}_{self.timestamp}.log"
        self.change_log_path(mode)
        # self.lang_path = "./languages"
        # self.lang_dict = {
        #     "en": "English.json",
        #     "zh": "Chinese.json"
        # }
        # self.lang_encoding = {
        #     "en": "utf-8",
        #     "zh": "gb18030"
        # }
        # self.lang = {}
        # self.parse_from_language("zh")

    def help(self): 
        """ Help function
        Print the help message
        """
        self.log(self.__doc__)

    def change_log_path(self, mode="timestamp"):
        if mode == "timestamp":
            self.log_dir = osp.join(self.log_root, str(self.timestamp))
        elif mode == "root":
            self.log_dir = self.log_root

    def init_log_file(self):
        self.log_file = f"{self.__class__.__name__}_{time.time()}.log"

    def get_path_content(self, path, mode='allfile', output='AbsPath'):
        """
        mode:
            allfile: All files in path, including files in subfolders.
            file: Files in path, only including files in this dir: path
            dir: Dirs in path, only including Dir in this dir: path
        output:
            AbsPath: Return absolute path, e.g. C:\\name.ext
            name_ext: Return name.ext, e.g. name.ext
            name: Return name, e.g. name
        """
        path_content = []
        index = 0
        for root, dirs, files in os.walk(path):
            index += 1
            if mode == 'allfile':
                for file in files:
                    file_path = osp.join(root, file)
                    if output == 'AbsPath':
                        pass
                    elif output == 'name_ext':
                        file_path = self.path2name(file_path, keep_ext=True)
                    elif output == 'name':
                        file_path = self.path2name(file_path, keep_ext=False)
                    path_content.append(file_path)
            if mode == 'file':
                for file in files:
                    file_path = osp.join(root, file)
                    if output == 'AbsPath':
                        pass
                    elif output == 'name_ext':
                        file_path = self.path2name(file_path, keep_ext=True)
                    elif output == 'name':
                        file_path = self.path2name(file_path, keep_ext=False)
                    path_content.append(file_path)
                break
            if mode == 'dir':
                for dir in dirs:
                    dir_path = osp.join(root, dir)
                    path_content.append(dir_path)
                break
                
        return path_content

    def is_file_meet(self, 
                     file_path, 
                     condition={
                         'size_max': '10M', 
                         'size_min': '10M', 
                         'ext_allow': ['pth', 'pt', 't'],
                         'ext_forbid': ['pth', 'pt', 't'],
                         'name_allow': ['epoch_99.t'],
                         'name_forbid': ['epoch_99.t']
                         }):
        meet = True
        for k, v in condition.items():
            if k == 'size_max':
                # file size should <= size_max
                max_value = self.unit_conversion(v, 'B')
                file_size = os.path.getsize(file_path)
                if not file_size <= max_value:
                    meet = False
            elif k == 'size_min':
                # file size should >= size_min
                min_value = self.unit_conversion(v, 'B')
                file_size = os.path.getsize(file_path)
                if not file_size >= min_value:
                    meet = False
            elif k == 'ext_allow':
                # file's extension name should in ext_allow[]
                _, file_name = os.path.split(file_path)
                _, ext = os.path.splitext(file_name)
                ext = ext[1:]
                if not ext in v:
                    meet = False
            elif k == 'ext_forbid':
                # file's extension name shouldn't in ext_forbid[]
                _, file_name = os.path.split(file_path)
                _, ext = os.path.splitext(file_name)
                ext = ext[1:]
                if ext in v:
                    meet = False
            elif k == 'name_allow':
                # file's name should in name_allow[]
                _, file_name = os.path.split(file_path)
                if not file_name in v:
                    meet = False
            elif k == 'name_forbid':
                # file's name shouldn't in name_forbid[]
                _, file_name = os.path.split(file_path)
                if file_name in v:
                    meet = False
        return meet


    def unit_conversion(self, size, output_unit='B'):
        # convert [GB, MB, KB, B] to [GB, MB, KB, B]
        if not isinstance(size, str):
            return size
        # to Byte
        size = size.upper()
        if 'GB' == size[-2:] or 'G' == size[-1]:
            size = size.replace("G", '')
            size = size.replace("B", '')
            size_num = float(size)
            size_num = size_num * 1024 * 1024 * 1024
        elif 'MB' == size[-2:] or 'M' == size[-1]:
            size = size.replace("M", '')
            size = size.replace("B", '')
            size_num = float(size)
            size_num = size_num * 1024 * 1024
        elif 'KB' == size[-2:] or 'K' == size[-1]:
            size = size.replace("K", '')
            size = size.replace("B", '')
            size_num = float(size)
            size_num = size_num * 1024
        elif 'B' == size[-1]:
            size = size.replace("B", '')
            size_num = float(size)
        else:
            raise

        # to output_unit
        if output_unit in ['GB', 'G']:
            size_num = size_num / 1024 / 1024 / 1024
        if output_unit in ['MB', 'M']:
            size_num = size_num / 1024 / 1024
        if output_unit in ['KB', 'K']:
            size_num = size_num / 1024
        if output_unit in ['B']:
            size_num = size_num

        # return
        return size_num

    def mkdir(self, path):
        if not osp.exists(path):
            os.makedirs(path)

    def split_content(self, content):
        if isinstance(content[0], str):
            content_split = []
            for path in content:
                content_split.append(osp.split(path))
            return content_split
        elif isinstance(content[0], list):
            contents_split = []
            for group in content:
                content_split = []
                for path in group:
                    content_split.append(osp.split(path))
                contents_split.append(content_split)
            return contents_split

    def path_to_last_dir(self, path):
        dirname = osp.dirname(path)
        last_dir = osp.basename(dirname)
        return last_dir

    def save_array_as_img(self, array, save_path, toLogDir=True, mode='cv2'):
        if toLogDir:
            save_path = self.log_dir + "/"+ self.path2name(save_path, keep_ext=True)
        if mode == 'cv2':
            import cv2
            cv2.imwrite(save_path, array)
        elif mode == 'scipy':
            from scipy import misc
            misc.imsave(save_path, array)
        elif mode == 'imageio':
            import imageio
            imageio.imwrite(save_path, array.astype(np.uint8))
        elif mode == 'plt':
            import matplotlib.pyplot as plt
            fig = plt.gcf()
            fig.set_size_inches(7.0/3,7.0/3)
            # plt.figure(figsize=(array.shape))
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
            plt.axis('off')
            plt.imshow(array)
            # plt.savefig(save_path, pad_inches=0)
            fig.savefig(save_path, format='png', transparent=True, dpi=300, pad_inches=0, cmap='gray')
            plt.cla()

        return save_path
        
    def path2name(self, path, keep_ext=False):
        _, filename = osp.split(path)
        if keep_ext:
            return filename
        file, _ = osp.splitext(filename)
        return file

    def sort_list(self, list):
        # copy from: https://www.modb.pro/db/162223
        # To make 1, 10, 2, 20, 3, 4, 5 -> 1, 2, 3, 4, 5, 10, 20
        list = sorted(list, key=lambda s: [int(s) if s.isdigit() else s for s in sum(re.findall(r'(\D+)(\d+)', 'a'+s+'0'), ())])
        return list

    def file_last_subtract_1(self, path, mode='-'):
        """
        Just for myself.
        file:
            xxx.png 1
            ccc.png 2
        ---> mode='-' --->
        file:
            xxx.png 0
            ccc.png 1
        """
        with open(path, 'r') as f:
            lines = f.readlines()
        res = []
        for line in lines:
            last = -2 if line[-1] == '\n' else -1
            line1, line2 = line[:last], line[last]
            if mode == '-':
                line2 = str(int(line2) - 1)
            elif mode == '+':
                line2 = str(int(line2) + 1)
            line = line1 + line2 + "\n"
            if last == -1:
                line = line1 + line2
            res.append(line)
        with open(path, 'w') as f:
            f.write("".join(res))

    def log(self, content):
        time_now = datetime.datetime.now()
        content = f"{time_now}: {content}\n"
        self.log2file(content, self.log_file, mode='a')
        print(content, end='')

    def append2file(self, path, text):
        with open(path, 'a') as f:
            f.write(text)

    def log2file(self, content, log_path='log.txt', mode='w', show=False):
        self.mkdir(self.log_dir)
        path = osp.join(self.log_dir, log_path)
        with open(path, mode, encoding='utf8') as f:
            if isinstance(content, list):
                f.write("".join(content))
            elif isinstance(content, str):
                f.write(content)
            elif isinstance(content, dict):
                json.dump(content, f, indent=2, sort_keys=True, ensure_ascii=False)
            else:
                f.write(str(content))
        if show:
            self.log(f"Log save to: {path}")

    def list2tuple2str(self, list):
        return str(tuple(list))

    def dict_plus(self, dict, key, value=1):
        if key in dict.keys():
            dict[key] += value
        else:
            dict[key] = value

    def sort_by_label(self, path_label_list):
        """
        list:[
            "mwhls.jpg 1",                      # path and label
            "mwhls.png 0",                      # path and label
            "mwhls.gif 0"]                      # path and label
        -->
        list:[
            ["0", "1"],                         # label
            ["mwhls.png 0", "mwhls.gif 0"],     # class 0
            ["mwhls.jpg 1"]]                    # class 1
        """
        label_list = []
        for path_label in path_label_list:
            label = path_label.split()[-1]
            label_list.append(label)
        label_set = set(label_list)
        res_list = []
        res_list.append(list(label_set))
        for label in label_set:
            index_equal = []    # why index_equal = label_list == label isn't working?
            for i, lab in enumerate(label_list):
                if lab == label:
                    index_equal.append(i)
            res = [path_label_list[i] for i in index_equal] # why path_label_list[index_equal] isn't working either??
            res_list.append(res)
        return res_list

    def clear_taobao_link(self, text):
        # try:
        link = "https://item.taobao.com/item.htm?"
        try:
            id_index_1 = text.index('&id=') + 1
            id_index = id_index_1
        except:
            pass
        try:
            id_index_2 = text.index('?id=') + 1
            id_index = id_index_2
        except:
            pass
        try:
            id = text[id_index: id_index+15]
            text = link + id
        except:
            pass
        return text
        # except:
        #     return text

    def parse_from_language(self, lang='en'):
        path = osp.join(self.lang_path, self.lang_dict[lang])
        with open(path, "rb") as f:
            self.lang = json.load(f)


if __name__ == '__main__':
    # .py to .exe
    # os.system("pyinstaller -F main.py")
    # print(get_path_content("test2"))
    # file_last_subtract_1("path_label.txt")
    pass