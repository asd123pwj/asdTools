from base_model import BaseModel
import os
import shutil

class RenameFileByDir(BaseModel):
    def __init__(self):
        super().__init__()
        # self.log_file = f"AutoDelete_{time.time()}.log"
        pass

    def run(self):
        dir_path = input("Input dir path:")
        self.log(f"Dir path: {dir_path}")
        # path = input("Input path: ")
        # size = input("Input file size threshold you want to delete (default 50M): ") or ('50M')
        files_path = self.get_path_content(dir_path, 'allfile')
        files_json = files_path
        # files_json = []
        # for file_path in files_path:
        #     condition = {
        #         # 'size_min': size,
        #         'ext_allow': ['png', 'jpg', 'json'],
        #         # 'name_allow': ['label.png']
        #     }
        #     if self.is_file_meet(file_path, condition):
        #         files_json.append(file_path)
        # self.log(f"Size: {size}")
        for i, file_path in enumerate(files_json):
            self.log(f"{i+1}: {file_path}")
        # is_delete = input("Check files above, if you want to delete them, input 'DELETE' to continue: ")
        # if is_delete == 'DELETE':
        j = 0
        for i, file_path in enumerate(files_json):
            # os.remove(file_path)
            
            save_path = self.log_dir + "/" + self.path_to_last_dir(file_path) + "_" + self.path2name(file_path, keep_ext=True)
            shutil.move(file_path, save_path)
            self.log(f"{j+1}: {file_path} has moved to {save_path}")
            j += 1
        

if __name__ == "__main__":
    RenameFileByDir().run()