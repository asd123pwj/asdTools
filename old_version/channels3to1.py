from base_model import BaseModel
import cv2
import numpy as np


class Channels3to1(BaseModel):
    def __init__(self):
        super().__init__()
        pass


    def run(self):
        path = input("Input path: ")
        files_path = self.get_path_content(path, 'allfile')
        
        self.log(f"Path: {path}")
        for i, file_path in enumerate(files_path):
            self.log(f"{i+1}: {file_path}")
        for i, file_path in enumerate(files_path):
            img = cv2.imread(file_path)
            H, W, C = img.shape
            img = img[:, :, 0].tolist()
            for h in range(H):
                for w in range(W):
                    if img[h][w] != 0:
                        img[h][w] = [1]
                    else:
                        img[h][w] = [0]
            img = np.array(img)
            save_path = self.log_dir + "/"+ self.path2name(file_path, keep_ext=True)
            cv2.imwrite(save_path, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
            self.log(f"{i+1}: {file_path} converted (H, W, 3) -> (H, W, 1) to {save_path}")
        

if __name__ == "__main__":
    Channels3to1().run()