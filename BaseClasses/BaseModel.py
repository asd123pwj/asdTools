import time


class BaseModel():
    def __init__(self, log_dir:str="", log_file:str="", **kwargs) -> None:
        time_current = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        self.log_dir = f"./logs/{self.__class__.__name__}" if log_dir == "" else log_dir
        self.log_file = f"{self.__class__.__name__}_{time_current}.log" if log_file == "" else log_file



