import keyboard
import pyperclip
import os
import time


class Quick_rename_dir():
    """
    Quick rename files in directory for windows.
    Copy the path of dir1 and dir2 to rename files in dir2 as follow:
    复制路径1与路径2以重命名路径2内文件：
    Step / 步骤:
        1. Run the script                                   运行脚本
        2. Copy the source directory path.                  复制源目录路径
        3. Press <q> to record source directory path.       按<q>记录源目录路径
        4. Copy the destination directory path.             复制目标目录路径
        5. Press <e> to record destination directory path.  按<e>记录目标目录路径
        6. Press <w> to rename destination directory path.  按<w>重命名目标目录路径
        7. Press <esc> to exit.                             按<esc>退出
    """
    def __init__(self):
        self.dir_dest = ''
        self.dir_source = ''

    def modify_file_name(self, dir_source, dir_dest):
        """ Modify file name
        dir_source: the source directory, name of these files in this directory will be copied.
        dir_dest: the destination directory, files in this directory will be renamed.
        Example:
            dir_source: C:\test\a.jpg
            dir_dest: C:\test\b.png
            The destination file name will be changed to a.jpg
        """
        # get the file name in source directory, and remove directory file
        file_source_list = os.listdir(dir_source)
        file_source_list = [file for file in file_source_list if not os.path.isdir(os.path.join(dir_source, file))]
        # get the file name in destination directory, and remove directory file
        file_dest_list = os.listdir(dir_dest)
        file_dest_list = [file for file in file_dest_list if not os.path.isdir(os.path.join(dir_dest, file))]
        # create tmp file name
        timestamp = str(int(time.time()))
        file_tmp_list = [str(i)+'_'+timestamp for i in range(len(file_dest_list))]

        # rename the destination file to tmp name
        for i in range(len(file_tmp_list)):
            file_source = file_tmp_list[i]
            file_dest = file_dest_list[i]
            os.rename(dir_dest + '\\' + file_dest, dir_dest + '\\' + file_source)

        time.sleep(0.5)

        # rename the destination file
        for i in range(len(file_source_list)):
            file_source = file_source_list[i]
            file_dest = file_tmp_list[i]
            os.rename(dir_dest + '\\' + file_dest, dir_dest + '\\' + file_source)
        return True

    def handle_keyboard_event(self, keyboard_event):
        """ Handle keyboard event
        To trigger the copy and paste function
        """
        if keyboard_event.name == 'q' and keyboard_event.event_type == 'up':
            self.dir_source = pyperclip.paste()
            print("Source dir: ", self.dir_source)
        elif keyboard_event.name == 'e' and keyboard_event.event_type == 'up':
            self.dir_dest = pyperclip.paste()
            print("Destination dir: ", self.dir_dest)
        elif keyboard_event.name == 'w' and keyboard_event.event_type == 'up':
            try:
                self.modify_file_name(self.dir_source, self.dir_dest)
                print("Success")
            except:
                print("Failed")
        elif keyboard_event.name == 'esc' and keyboard_event.event_type == 'up':
            os._exit(0)

    def help(self):
        print(self.__doc__)

    def run(self):
        self.help()
        keyboard.hook(self.handle_keyboard_event)
        keyboard.wait()
