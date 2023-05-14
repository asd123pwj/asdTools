from asdTools.Classes.Base.BaseModel import BaseModel
import requests


class ApiBase(BaseModel):
    # wait for improvemnt
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def post(url:str, data, headers:dict):
        response = requests.post(url, json=data, headers=headers)
        return response
