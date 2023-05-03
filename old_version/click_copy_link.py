import keyboard
import pyperclip
import time
from base_model import BaseModel


class Click_copy_link(BaseModel):
    """
    Middle-click to copy link
    What it happen when middle click:
        1. Click F6 to point to URL.
        2. Ctrl-C to copy.
        3. Ctrl-W to leave.
        4. Write to file.
    """
    def __init__(self):
        self.path = 'link.txt'
        self.sleep = 0.2
        self.time_old = 0

    def help(self):
        """ Help function
        Print the help message
        """
        self.log(self.__doc__)

    def copy_link(self):
        time.sleep(self.sleep * 2)
        keyboard.press_and_release('ctrl+tab')
        time.sleep(self.sleep)
        keyboard.press_and_release('f6')
        time.sleep(self.sleep)
        keyboard.press_and_release('ctrl+c')
        time.sleep(self.sleep)
        keyboard.press_and_release('ctrl+w')
        # time.sleep(self.sleep)
        return pyperclip.paste()

    def handle_mouse_event(self, mouse_event):
        if isinstance(mouse_event, mouse.ButtonEvent):
            time_new = mouse_event.time
            if mouse_event.button == 'middle' and mouse_event.event_type == 'up' and time_new != self.time_old:
                text = self.copy_link()
                text = self.clear_taobao_link(text)
                self.append2file(self.path, text+'\n')
                self.log(f"Append to '{self.path}': {text}")
                # time.sleep(self.sleep)
                self.time_old = time_new

    def run(self):
        """ Main function
        listen mouse event
        """
        self.help()
        self.path = input("Input storage path (default: link.txt)") or 'link.txt'
        self.sleep = float(input("Input time interval (default: 0.25s):") or 0.25)
        while True:
            mouse.hook(self.handle_mouse_event)
            mouse.wait()

    def run_chs(self):
        """ Main function
        listen mouse event
        """
        # self.help()
        self.log("回车选择默认，如果出现链接不能正常复制，请将时间间隔增加")
        self.path = input("输入商品链接存储文件 (默认: 淘宝商品链接.txt)") or '淘宝商品链接.txt'
        self.sleep = float(input("输入时间间隔 (默认: 0.25s):") or 0.25)
        self.log("开始复制，鼠标中键点击淘宝商品以复制链接...")
        while True:
            mouse.hook(self.handle_mouse_event)
            mouse.wait()


if __name__ == '__main__':
    Click_copy_link().run_chs()
