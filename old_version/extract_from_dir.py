from base_model import BaseModel
import cv2
import shutil


class ExtractFromDir(BaseModel):
    # A dataset split to train, test, val, all of these path are belong to 'split path'
    # And there are another dir which have all files in dataset, but no split, I call it "source path"
    # Here, we input train set "split path", and "source path",
    # then we extract files in "source" which have the same name with files in "split".
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        # split_path = input("Input split path: ")
        split_path = r"F:\0_DATA\1_DATA\Datasets\pcseg7000\images\val"
        split_files_path = self.get_path_content(split_path, 'allfile', 'name')

        # source_path = input("Input source path: ")
        source_path = r"F:\0_DATA\1_DATA\Datasets\pcseg7000\annotations"
        source_files_path = self.get_path_content(source_path, 'allfile')
        
        self.log(f"split_path: {split_path}, source_path: {source_path}")
        # for i, file_path in enumerate(files_path):
        #     self.log(f"{i+1}: {file_path}")
        k = 0
        for i, file_path in enumerate(source_files_path):
            if self.path2name(file_path, keep_ext=False) in split_files_path:
                save_path = self.log_dir + "/"+ self.path2name(file_path, keep_ext=True)
                shutil.copyfile(file_path, save_path)
                k += 1
                self.log(f"{k}: {file_path} extracted to {save_path}.")



if __name__ == "__main__":
    ExtractFromDir().run()