from asdTools.Classes.Base.CommandBase import CommandBase
from asdTools.Classes.Base.UnitBase import UnitBase
from asdTools.Classes.Base.TimeBase import TimeBase
from asdTools.Classes.Base.VarBase import VarBase
from asdTools.Classes.Base.IOBase import IOBase


class BaseModel(CommandBase, UnitBase, TimeBase, VarBase, IOBase):
    def __init__(self, name:str="", log_dir:str="", log_file:str="", **kwargs) -> None:
        """
        Initializes the BaseModel instance.

        Args:
            name (str): Name of the instance. If not specified, defaults to the class name.
            log_dir (str): Directory to save logs. Defaults to "./logs/{name}".
            log_file (str): Name of the log file. Defaults to "{name}_{time}.log".
            **kwargs: Additional keyword arguments to pass to the parent class.
        """        
        super(CommandBase, self).__init__(**kwargs)
        super(UnitBase, self).__init__(**kwargs)
        super(TimeBase, self).__init__(**kwargs)
        super(VarBase, self).__init__(**kwargs)
        super(IOBase, self).__init__(**kwargs)
        time_current = self.get_time(True)
        if name == "":
            self.name = self.__class__.__name__
        else:
            self.name = name
        self.log_dir = f"./Logs/{self.name}" if log_dir == "" else log_dir
        self.log_file = f"{self.name}_{time_current}.log" if log_file == "" else log_file

    def log(self, content, logTime:bool=True) -> str:
        """
        Logs the content to the console and to a file.

        Args:
            content (str): Content to log.
            logTime (bool): If True, prepends the log message with a timestamp. Defaults to True.

        Returns:
            str: Timestamp of the log message.
        """
        time_current = self.get_time()
        if logTime:
            content = f"{time_current}: {content}"
        content_end = '' if content[-1] == '\n' else '\n'
        print(content, end=content_end)
        log_path = self.convert_path_to_log_dir(self.log_file)
        self.save_file(f"{content}{content_end}", log_path, mode='a')
        return time_current

    def convert_path_to_log_dir(self, path):
        path = self.join(self.log_dir, path)
        return path

    def input(self, message="Input: ") -> str:
        """
        Displays a message and returns the user input as a string.

        Args:
            message (str): Message to display. Defaults to "Input: ".

        Returns:
            str: User input as a string.
        """
        content = input(message)
        return content

    def raise_error(self, message:str, statue_code:int=-1) -> None:
        """
        Logs an error message and exits the program with a status code.

        Args:
            message (str): Error message to log.
            statue_code (int): Status code to exit with. Defaults to -1.
        """
        self.log(message)
        self.exit(statue_code)