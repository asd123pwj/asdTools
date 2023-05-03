import os
from BaseClasses.BaseModel import BaseModel


class IOBase(BaseModel):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def get_path_from_dir(path:str, 
                          type:str="file", 
                          needAbsPath:bool=False, 
                          keepExt:bool=True, 
                          includeSubfolder:bool=True)->list:
        """Return a list of file or directory paths in the specified directory and its subfolders.

        Args:
            path (str): The path to the directory to search.
            type (str, optional): The type of paths to include, either "file", "dir", or "filedir" (both). Defaults to "file".
            needAbsPath (bool, optional): If True, return absolute paths. Defaults to False.
            keepExt (bool, optional): If True, keep the file extension in the path. Defaults to True.
            includeSubfolder (bool, optional): If True, search in subfolders recursively. Defaults to True.

        Returns:
            list: A list of paths of the specified type found in the directory and its subfolders.

        """
        if os.path.isfile(path):
            return [path]
        paths = []
        for root, dirs, files in os.walk(path):
            if "file" in type:
                for file in files:
                    file_path = os.path.join(root, file)
                    if needAbsPath:
                        file_path = os.path.abspath(file_path)
                    if not keepExt:
                        file_path, _ = os.path.splitext(file_path)
                    paths.append(file_path)
            if "dir" in type:
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    paths.append(dir_path)
            if not includeSubfolder:
                break
        return paths

    @staticmethod
    def join_path(*arg:str) -> str:
        """
        Join one or more path components, regardless of operating system, and return the combined path.

        Args:
            *arg (str): one or more path components to join.

        Returns:
            str: the combined path.

        Example:
            >>> FileUtil.join_path('path', 'to', 'file.txt')
            'path/to/file.txt'
        """
        return os.path.join(*arg)
    
    @staticmethod
    def mkdir(path:str) -> bool:
        """
        Create a new directory if it does not exist.

        Args:
            path (str): the path of the directory to create.

        Returns:
            bool: True if the directory was created, False otherwise.

        Example:
            >>> FileUtil.mkdir('path/to/dir')
            True
        """
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        return False


    def save_file(self, 
                  content, 
                  log_dir:str="./logs",
                  log_file:str="log.txt", 
                  mode:str='w') -> str:
        """Save content to a file and return the path to the file.

        Args:
            content: The content to be saved to the file. Can be a string, list of strings, dictionary, or any object that can be converted to a string.
            log_dir (str, optional): The directory where the log file should be saved. Defaults to "./logs".
            log_file (str, optional): The name of the log file. Defaults to "log.txt".
            mode (str, optional): The mode in which to open the file. Defaults to 'w'.

        Returns:
            str: The path to the log file.

        """

        self.mkdir(log_dir)
        log_path = self.join_path(log_dir, log_file)
        with open(log_path, mode, encoding='utf8') as f:
            if isinstance(content, list):
                f.write("".join(content))
            elif isinstance(content, str):
                f.write(content)
            elif isinstance(content, dict):
                import json
                json.dump(content, f, indent=2, sort_keys=True, ensure_ascii=False)
            else:
                f.write(str(content))
        return log_path

    @staticmethod
    def convert_path2dir(path:str, lastDir:bool=False) -> str:
        """
        Get the directory name from a given path.

        Args:
        - path (str): The path to be processed.
        - lastDir (bool): A boolean flag indicating whether to return the last directory in the path. Default is False.

        Returns:
        - str: The directory name.

        """
        dirname = os.path.dirname(path)
        if lastDir:
            dirname = os.path.basename(dirname)
        return dirname

    @staticmethod
    def convert_path2name(path:str, keepExt:bool=False) -> str:
        """
        Get the file name from a given path.

        Args:
        - path (str): The path to be processed.
        - keepExt (bool): A boolean flag indicating whether to keep the file extension. Default is False.

        Returns:
        - str: The file name.

        """
        _, filename = os.path.split(path)
        if keepExt:
            return filename
        file, _ = os.path.splitext(filename)
        return file

    @staticmethod
    def check_file_dir(path:str) -> str:
        """
        Check whether a given path is a file or a directory.

        Args:
        - path (str): The path to be checked.

        Returns:
        - str: "file" if the path is a file, "dir" if the path is a directory, "neither" otherwise.

        """
        if os.path.isfile(path):
            return "file"
        elif os.path.isdir(path):
            return "dir"
        else:
            return "neither"

    @staticmethod
    def check_ext(path:str, ext_list:list, allow:bool=True) -> bool:
        """
        Check whether a given path has a valid extension.

        Args:
        - path (str): The path to be checked.
        - ext_list (list): A list of valid extensions.
        - allow (bool): A boolean flag indicating whether the extension should be allowed or not. Default is True.

        Returns:
        - bool: True if the path has a valid extension and allow is True, or if the path does not have a valid extension and allow is False. False otherwise.

        """
        _, file_name = os.path.split(path)
        _, ext = os.path.splitext(file_name)
        ext = ext[1:]
        if ext in ext_list:
            return True if allow else False
        else:
            return False if allow else True

    def check_name(self, path:str, name_list:list, keepExt:bool=True, allow:bool=True)->bool:
        """
        Check whether a given path has a valid file name.

        Args:
        - path (str): The path to be checked.
        - name_list (list): A list of valid file names.
        - keepExt (bool): A boolean flag indicating whether to keep the file extension. Default is True.
        - allow (bool): A boolean flag indicating whether the file name should be allowed or not. Default is True.

        Returns:
        - bool: True if the path has a valid file name and allow is True, or if the path does not have a valid file name and allow is False. False otherwise.

        """
        name = self.convert_path2name(path, keepExt)
        if name in name_list:
            return True if allow else False
        else:
            return False if allow else True



if __name__ == "__main__":
    pass