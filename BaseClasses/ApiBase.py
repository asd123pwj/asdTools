from BaseClasses.BaseModel import BaseModel


class ApiBase(BaseModel):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)