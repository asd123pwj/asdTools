from asdTools.Classes.Base.CommandBase import CommandBase
from asdTools.Classes.Base.UnitBase import UnitBase
from asdTools.Classes.Base.TimeBase import TimeBase
from asdTools.Classes.Base.VarBase import VarBase
from asdTools.Classes.Base.IOBase import IOBase


class BaseModel(CommandBase, UnitBase, TimeBase, VarBase, IOBase):
    def __init__(self, name:str="", log_dir:str="", log_file:str="", log_level="all", **kwargs) -> None:
       
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
        self.log_dir = f"./Logs/time_current/{self.name}" if log_dir == "" else log_dir
        self.log_file = f"{self.name}_{time_current}.log" if log_file == "" else log_file
        self.log_level = log_level
        self.log_level_table = {"message": 0, "all": 0, "warning": 1, "error": 2, "none":3}

    def generate_output_path(self, output_dir:str="", output_file:str=""):
        if output_dir == "":
            output_dir = self.log_dir
        if output_file == "":
            output_file = f"{self.name}_{self.get_time(True)}.log"
        output_path = self.join(output_dir, output_file)
        return output_path

    def log(self, content, logTime:bool=True, level="message") -> str:
        """
        Logs the content to the console and to a file.

        Args:
            content (str): Content to log.
            logTime (bool): If True, prepends the log message with a timestamp. Defaults to True.

        Returns:
            str: Timestamp of the log message.
        """
        time_current = self.get_time()
        if self.log_level_table[level] >= self.log_level_table[self.log_level]:
            if level == "warning":
                content = "Warning: " + content
            if level == "error":
                content = "Error: " + content
            if logTime:
                content = f"{time_current}: {content}"
            content_end = '' if content[-1] == '\n' else '\n'
            print(content, end=content_end)
            log_path = self.generate_output_path(output_file=self.log_file)
            self.save_file(f"{content}{content_end}", log_path, mode='a')
        return time_current

    def input(self, message="Input: ", needLog=False) -> str:
        """
        Displays a message and returns the user input as a string.

        Args:
            message (str): Message to display. Defaults to "Input: ".

        Returns:
            str: User input as a string.
        """
        content = input(message)
        if needLog:
            self.log(f"{message}{content}")
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