from ClassesBase.IOBase import IOBase
import time


class BaseModel(IOBase):
    def __init__(self, name:str="", log_dir:str="", log_file:str="", **kwargs) -> None:
        super().__init__(**kwargs)
        time_current = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        if name == "":
            name = self.__class__.__name__
        self.log_dir = f"./logs/{name}" if log_dir == "" else log_dir
        self.log_file = f"{name}_{time_current}.log" if log_file == "" else log_file

    def log(self, content, logTime:bool=True) -> None:
        if logTime:
            time_current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            content = f"{time_current}: {content}"
        self.save_file(f"{content}\n", self.log_dir, self.log_file, mode='a')
        print(content, end='')

