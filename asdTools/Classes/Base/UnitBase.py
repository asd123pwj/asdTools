from asdTools.Classes.Base.RewriteBase import RewriteBase


class UnitBase(RewriteBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @staticmethod
    def convert_storage_units(size:float, input_unit:str="B", output_unit:str="GB"):
        unit_level = {"b":0, "B":1, "KB":2, "MB":3, "GB":4, "TB":5}
        for i in range(unit_level[input_unit]):
            if i == 0:
                size *= 8
            else:
                size *= 1024
        for i in range(unit_level[output_unit]):
            if i == 0:
                size /= 8
            else:
                size /= 1024
        return size

if __name__ == "__main__":
    unit_converter = UnitBase()
    size = 8 * 1024 * 1024 * 1024
    output = unit_converter.convert_storage_units(size, "B", "GB")
    pass