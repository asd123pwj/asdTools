from base_model import BaseModel
from PIL import Image
import scipy.io as scio
import numpy as np


class Mat2Png(BaseModel):
    def __init__(self):
        super().__init__()
        pass

    def mat2png(self, file_path):
        data_mat = scio.loadmat(file_path)
        data_mat = data_mat['groundTruth'][0][0][0][0][0]
        # print(data_mat)
        # data_mat = data_mat * 255
        data_img = Image.fromarray(data_mat.astype(np.uint8))
        return data_img

    def run(self, path=""):
        if path == "":
            path = input("Input path: ")
        files_path = self.get_path_content(path, 'allfile')
        self.log(f"Path: {path}")
        for i, file_path in enumerate(files_path):
            self.log(f"{i+1}: {file_path}")
            
        for i, file_path in enumerate(files_path):
            data_img = self.mat2png(file_path)
            save_path = self.log_dir + "/" + self.path2name(file_path) + ".png"
            data_img.save(save_path)
            self.log(f"{i+1}: {file_path} has generated as {save_path}")       


if __name__ == "__main__":
    Mat2Png().run()