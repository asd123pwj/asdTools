from asdTools.Classes.Base.RewriteBase import RewriteBase
import numpy as np
import operator
import random
import json
import math
import copy
import ast


class VarBase(RewriteBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def convert_val_adaptive(self, strr:str) -> dict:  
        # Thanks to ChatGPT      
        if isinstance(strr, dict):
            return {self.convert_val_adaptive(k): self.convert_val_adaptive(v) for k, v in strr.items()}
        if isinstance(strr, list):
            return [self.convert_val_adaptive(e) for e in strr]
        if isinstance(strr, str):
            return self.parse_value(strr)
        return strr

    def convert_json_to_str(self, jsonn:dict) -> str:
        json_res = {}
        for k, v in jsonn.items():
            json_res[str(k)] = str(v)
        return json_res

    def convert_arr_item_to_str(self, arr:np.ndarray):
        listt = arr.tolist()
        listt = self.convert_list_item_to_str(listt)
        return listt

    def convert_list_item_to_str(self, listt:list):
        list_res = []
        for item in listt:
            if isinstance(item, list):
                list_res.append(self.convert_list_item_to_str(item))
            else:
                list_res.append(str(item))
        return list_res

    def count_in_dict(self, dictt:dict, key:str, value=1) -> bool:
        if key in dictt:
            dictt[key] += value
            return True
        else:
            dictt[key] = value
            return False

    def check_equal(self, val1, val2) -> bool:
        if isinstance(val1, list):
            if not isinstance(val1, list):
                return False
            val1_sort = sorted(val1)
            val2_sort = sorted(val2)
            isEqual = val1_sort == val2_sort
            return isEqual

    def get_dict_value(self, dictt:dict, key:str, default_value):
        if key in dictt:
            value = dictt[key]
        else:
            value = default_value
        return value

    def get_list_value(self, listt:list, index:int, default_value):
        try:
            value = listt[index]
        except:
            value = default_value
        return value

    def json_write_pass_empty(self, jsonn:dict, key:str, value) -> bool:        
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
                jsonn[key] = value
                return True
        elif isinstance(value, list):
            if value:
                jsonn[key] = value
                return True
        return False

    def merge_dict(self, dict1:dict, dict2:dict) -> dict:
        # Only test in int type.
        dic_res = copy.deepcopy(dict1)
        for k2, v2 in dict2.items():
            v1 = self.get_dict_value(dic_res, k2, 0)
            value = self.merge_value(v1, v2)
            dic_res[k2] = value
        return dic_res

    def merge_2list_to_dcit(self, key_list, val_list, empty_value="EMPTY VALUE"):
        res = {}
        for i, key in enumerate(key_list):
            value = self.get_list_value(val_list, i, empty_value)
            res[key] = value
        return res

    def merge_value(self, val1, val2):
        if isinstance(val1, int):
            return val1 + val2
        elif isinstance(val1, float):
            return val1 + val2
        elif isinstance(val1, str):
            return val1 + val2
        elif isinstance(val1, list):
            return val1.extend(val2)

    def parse_value(self, value):
        # Thanks to ChatGPT
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        try:
            return ast.literal_eval(value)
        except (ValueError, TypeError):
            pass
        try:
            return ast.literal_eval(value)
        except (ValueError, TypeError):
            pass
        return value

    def split_list(self, listt:list, ratios:tuple, isRandom:bool=True):
        listt_copy = listt.copy()
        res = []
        if isRandom:
            random.shuffle(listt_copy)
        if isinstance(ratios, float):
            ratios = (ratios)
        start = 0
        ratio_total = 0
        for ratio in ratios:
            ratio_total += ratio
            if ratio_total >= 0.99999:
                res.append(listt_copy[start:])
                break
            else:
                split_len = math.ceil(len(listt) * ratio)
                res.append(listt_copy[start:start+split_len])
                start += split_len
        return res
