import keyboard
import pyperclip
import os

"""
Shortcut in Windows: 
    Rename: F2
    Copy: Ctrl+C
    Paste: Ctrl+V
    Enter: Enter
How to RENAME a new file from a old file?
    1. Click on the old file you want to copy.
    2. Press F2 for copy.
    3. Press Ctrl+C to copy.
    4. Click on the new file you want to paste.
    5. Press F2 for paste.
    6. Press Ctrl+V to paste.
"""

class Quick_rename_file():
    """ 
    Quick rename one file for windows.
    Click file1 and file2 to rename file2 as follow:
    点击文件1与文件2以重命名文件2：
    Step:
        1. Run the script                       运行脚本
        2. Click on the old file.               点击旧文件
        3. Press <q> to copy the file name.     按<q>复制文件名
        4. Click on the new file.               点击新文件
        5. Press <e> to paste the file name.    按<e>粘贴文件名
        6. Press <esc> to exit.                 按<esc>退出
    """

    def copy_fun(self):
        """ Copy function
        Copy the text with F2, Ctrl+C and Enter
        """
        keyboard.press_and_release('f2')
        keyboard.press_and_release('ctrl+c')
        keyboard.press_and_release('enter')
        # show the copied text
        self.log(f'Copy: {pyperclip.paste()}')
        
    def paste_fun(self):
        """ Paste function
        Paste the copied text with F2, Ctrl+V and Enter
        """
        keyboard.press_and_release('f2')
        keyboard.press_and_release('ctrl+v')
        keyboard.press_and_release('enter')
        # show the copied text
        self.log(f'Paste: {pyperclip.paste()}')

    def handle_keyboard_event(self, keyboard_event):
        """ Handle keyboard event
        To trigger the copy and paste function
        """
        if keyboard_event.name == 'q' and keyboard_event.event_type == 'up':
            self.copy_fun()
        elif keyboard_event.name == 'e' and keyboard_event.event_type == 'up':
            self.paste_fun()
        elif keyboard_event.name == 'esc' and keyboard_event.event_type == 'up':
            os._exit(0)

    def help(self):
        """ Help function
        Print the help message
        """
        self.log(self.__doc__)

    def run(self):
        """ Main function
        listen keyboard event
        """
        self.help()
        keyboard.hook(self.handle_keyboard_event)
        keyboard.wait()

