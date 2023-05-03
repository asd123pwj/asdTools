from BaseClasses.IOBase import IOBase
import time


class Logger(IOBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def log(self, content, logTime:bool=True) -> None:
        if logTime:
            time_current = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            content = f"{time_current}: {content}"
        self.save_file(f"{content}\n", self.log_dir, self.log_file, mode='a')
        print(content, end='')

