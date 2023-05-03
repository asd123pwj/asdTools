from base_model import BaseModel
from pycocotools.coco import COCO
import numpy as np


class Coco2Mask(BaseModel):
    def __init__(self):
        super().__init__()
        # self.log_file = f"AutoDelete_{time.time()}.log"
        pass

    def get_mask(self, coco, img_id):
        img = np.zeros((coco.imgs[img_id]["height"], coco.imgs[img_id]["width"]))
        anns_id = coco.getAnnIds(imgIds = img_id)
        anns = coco.loadAnns(anns_id)
        for ann in anns:
            img = np.maximum(img, coco.annToMask(ann) * (ann["category_id"] + 1))
        return img

    def run(self):
        path = input("Input path: ")
        # path = r"F:\0_DATA\1_DATA\Datasets\TTPLA\trainval.json"
        coco = COCO(path)
        
        self.log(f"json path: {path}")
        img_ids = coco.getImgIds()
        for i, img_id in enumerate(img_ids):
            img = self.get_mask(coco, img_id)
            save_name = self.path2name(coco.imgs[img_id]["file_name"]) + '.png'
            save_path = self.save_array_as_img(img, save_name, mode='imageio')
            self.log(f"{i+1}: {save_path} has generated")



if __name__ == "__main__":
    Coco2Mask().run()