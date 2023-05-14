import json
import os


class IOBase():
    def __init__(self, **kwargs) -> None:
        pass

    @staticmethod
    def get_paths_from_dir(path:str, 
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
    def get_dir_of_file(path:str, lastDir:bool=False) -> str:
        """
        Returns the directory of the given file path.

        Args:
        - path (str): The file path.
        - lastDir (bool): If True, returns only the last directory in the path.

        Returns:
        - str: The directory of the given file path.

        """
        dir_name = os.path.dirname(path)
        if lastDir:
            dir_name = os.path.basename(dir_name)
        return dir_name

    @staticmethod
    def get_name_of_file(path:str, keepExt:bool=False) -> str:
        """
        Returns the name of the given file path.

        Args:
        - path (str): The file path.
        - keepExt (bool): If True, returns the file name along with its extension.

        Returns:
        - str: The name of the given file path.

        """
        _, file_name = os.path.split(path)
        if keepExt:
            return file_name
        file, _ = os.path.splitext(file_name)
        return file

    @staticmethod
    def add_suffix(path:str, suffix:str="_suffix") -> str:
        """
        Add suffix to the directory or file name in the given path and return the new path.

        Args:
        - path (str): Path to the directory or file.
        - suffix (str, optional): Suffix to add to the file or directory name. Default is "_suffix".

        Returns:
        - str: Path with added suffix.

        Raises:
        - None

        Example:
        >>> add_suffix('/path/to/directory', '_new')
        '/path/to/directory_new'
        >>> add_suffix('/path/to/file.txt', '_new')
        '/path/to/file_new.txt'
        """
        if os.path.isdir(path):
            dir_root, dir_name = os.path.split(path)
            dir_name += suffix
            path = os.path.join(dir_root, dir_name)
        elif os.path.isfile(path):
            file_root, file_name = os.path.split(path)
            file_name_root, file_name_ext = os.path.splitext(file_name)
            file_name = file_name_root + suffix + file_name_ext
            path = os.path.join(file_root, file_name)
        else:
            path += suffix
        return path

    @staticmethod
    def join(*arg:str) -> str:
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
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        return False

    @staticmethod
    def exists(path):
        isExists = os.path.exists(path)
        return isExists

    def save_file(self, 
                  content, 
                  log_path:str="./Logs/log.txt",
                  mode:str='w') -> str:
        log_dir = self.get_dir_of_file(log_path)
        self.mkdir(log_dir)
        with open(log_path, mode, encoding='utf8') as f:
            if isinstance(content, list):
                f.write("".join(content))
            elif isinstance(content, str):
                f.write(content)
            elif isinstance(content, dict):
                json.dump(content, f, indent=2, sort_keys=True, ensure_ascii=False)
            else:
                f.write(str(content))
        return log_path

    def read_json(self, path:str):
        with open(path, "r", encoding="utf8") as f:
            content = json.load(f)
        return content

    @staticmethod
    def check_file(path:str) -> bool:
        """
        Checks if the given path points to a file.

        Args:
        - path (str): The path to check.

        Returns:
        - bool: True if the path points to a file, False otherwise.

        """
        if os.path.isfile(path):
            return True
        return False
        
    @staticmethod
    def check_dir(path:str) -> bool:
        """
        Checks if the given path points to a directory.

        Args:
        - path (str): The path to check.

        Returns:
        - bool: True if the path points to a directory, False otherwise.

        """
        if os.path.isdir(path):
            return True
        return False

    @staticmethod
    def check_path(path:str) -> str:
        """
        Checks if the given path points to a valid location.

        Args:
        - path (str): The path to check.

        Returns:
        - str: False if the path points to a file or directory, True otherwise.

        """
        if os.path.isfile(path):
            return False
        elif os.path.isdir(path):
            return False
        else:
            return True

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

    @staticmethod
    def check_name(path:str, name_list:list, keepExt:bool=True, allow:bool=True) -> bool:
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
        _, file_name = os.path.split(path)
        if not keepExt:
            file_name, _ = os.path.splitext(file_name)
        if file_name in name_list:
            return True if allow else False
        else:
            return False if allow else True

    def filter_ext(self, paths, ext_list:list=[], allow:bool=True) -> list:
        """
        Filters a list of file paths based on the extensions.

        Args:
        - paths (list): A list of file paths to filter.
        - ext_list (list): A list of extensions to allow or disallow. If empty, all extensions will be allowed.
        - allow (bool): If True, the files with the extensions in the ext_list will be allowed. If False, they will be disallowed.

        Returns:
        - list: A list of file paths filtered based on the given extensions.

        """
        res = []
        for path in paths:
            if self.check_ext(path, ext_list, allow):
                res.append(path)
        return res