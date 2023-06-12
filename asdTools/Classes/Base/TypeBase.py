from asdTools.Classes.Base.RewriteBase import RewriteBase


class TypeBase(RewriteBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def convert_gradioFiles_to_pathList(self, files):
        res = []
        for file in files:
            res.append(file.name)
        return res