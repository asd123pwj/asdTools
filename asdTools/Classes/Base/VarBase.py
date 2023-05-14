import json


class VarBase():
    def __init__(self, **kwargs):
        pass

    @staticmethod
    def json_write_pass_empty(json:dict, key:str, value) -> bool:        
        """
        Write key-value pair to a dictionary if value is not empty.

        Args:
        - json (dict): The dictionary to write to.
        - key (str): The key of the key-value pair to write.
        - value (str or list): The value of the key-value pair to write.

        Returns:
        - bool: True if the value is not empty and has been successfully written to the dictionary, False otherwise.
        """
        # wait for improvement
        if isinstance(value, str):
            if value != "":
                json[key] = value
                return True
        elif isinstance(value, list):
            if value:
                json[key] = value
                return True
        return False

    @staticmethod
    def convert_str2json(str) -> dict:
        """
        Convert a JSON string to a dictionary.

        Args:
        - str (str): The JSON string to convert.

        Returns:
        - dict: The dictionary converted from the JSON string.
        """
        return json.loads(str)
