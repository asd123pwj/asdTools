from base_model import BaseModel
import os


class AutoDelete(BaseModel):
    def __init__(self):
        super().__init__()
        # self.log_file = f"AutoDelete_{time.time()}.log"
        pass

    def run(self):
        path = input("Input path: ")
        size = input("Input file size threshold you want to delete (default 50M): ") or ('50M')
        files_path = self.get_path_content(path, 'allfile')
        files_delete = []
        for file_path in files_path:
            condition = {
                'size_min': size,
                'ext_allow': ['pth', 'pt', 't'],
                'name_forbid': ['epoch_99.t']
            }
            if self.is_file_meet(file_path, condition):
                files_delete.append(file_path)
        self.log(f"Path: {path}")
        self.log(f"Size: {size}")
        for i, file_path in enumerate(files_delete):
            self.log(f"{i+1}: {file_path}")
        is_delete = input("Check files above, if you want to delete them, input 'DELETE' to continue: ")
        if is_delete == 'DELETE':
            for i, file_path in enumerate(files_delete):
                os.remove(file_path)
                self.log(f"{i+1}: {file_path} has removed")
        else:
            self.log("Cancel delete.")
        



if __name__ == "__main__":
    AutoDelete().run()