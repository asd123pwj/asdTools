from base_model import BaseModel
import os
import random
import json
import copy



class Divide_CocoLabel_file(BaseModel):
    def __init__(self, dataset_path="labeling/highway"):
        super().__init__()
        self.dataset_path = dataset_path
        self.label_path = os.path.join(dataset_path, "annotations/instances_default.json")
        self.image_path = os.path.join(dataset_path, "images")

    def load_from_file(self):
        with open(self.label_path, 'r') as f:
            self.coco_dict_train = json.load(f)
            self.coco_dict_test = copy.deepcopy(self.coco_dict_train)

    def sort_by_img_id(self):
        """
        return:
            imgs_id: list, for getting valid imgs_id which have annotations
        """
        imgs_id = set()
        # img_ann_dict = {}
        for i, ann in enumerate(self.coco_dict_train["annotations"]):
            img_id = ann["image_id"]
            # ann_id = ann["id"]
            imgs_id.add(img_id)
            # if img_id not in img_ann_dict.keys():
            #     img_ann_dict[img_id] = [ann_id]
            # else:
            #     img_ann_dict[img_id].append(ann_id)
        return list(imgs_id)

    def divide_id(self, imgs_id, prob=0.7):
        random.shuffle(imgs_id)
        train_num = int(len(imgs_id) * prob)
        imgs_id_train = imgs_id[:train_num]
        imgs_id_test = imgs_id[train_num:]
        # id_shuffle = [i for i in range(len(imgs_id))]
        # id_shuffle = random.shuffle(id_shuffle)

        # imgs_id_train = []
        # img_ann_dict_train = {}
        # imgs_id_test = []
        # img_ann_dict_test = {}
        # for i in id_shuffle:
            # if i < train_num:
                # imgs_id_train.append(imgs_id[i])
                # img_ann_dict_train[imgs_id[i]] = img_ann_dict[imgs_id[i]]
            # else: 
                # imgs_id_test.append(imgs_id[i])
                # img_ann_dict_test[imgs_id[i]] = img_ann_dict[imgs_id[i]]

        return imgs_id_train, imgs_id_test
        
    def list2d_to_list1d(self, list2d):
        # ref: https://blog.csdn.net/Yolandera/article/details/82847022
        list1d = [i for item in list2d for i in item]
        return list1d

    def delete_id(self, imgs_id, coco_dict):
        imgs_info = coco_dict["images"]
        anns_info = coco_dict["annotations"]
        img_id_to_new_img_id = {}
        img_id = 0
        ann_id = 0
        imgs_info_new = []
        anns_info_new = []
        for i, img in enumerate(imgs_info):
            if img["id"] in imgs_id:
                img_id += 1
                # img_id to new_img_id
                img_id_to_new_img_id[img["id"]] = img_id
                # modify to new info
                img["id"] = img_id
                # add to result
                imgs_info_new.append(img)
        for i, ann in enumerate(anns_info):
            if ann["image_id"] in imgs_id:
                ann_id += 1
                # modify to new info
                ann["image_id"] = img_id_to_new_img_id[ann["image_id"]]
                ann["id"] = ann_id
                anns_info_new.append(ann)
        return imgs_info_new, anns_info_new


    
    def run(self):
        dataset_path = input("Input dataset path:")
        prob = float(input("Input probabilty of train set (default: 0.9):") or 0.9)
        self.dataset_path = dataset_path
        self.label_path = os.path.join(dataset_path, "annotations/instances_default.json")
        self.image_path = os.path.join(dataset_path, "images")
        self.load_from_file()
        imgs_id = self.sort_by_img_id()
        train_ids, test_ids = self.divide_id(imgs_id, prob)
        train_imgs_info, train_anns_info = self.delete_id(train_ids, self.coco_dict_train)
        test_imgs_info, test_anns_info = self.delete_id(test_ids, self.coco_dict_test)
        self.coco_dict_train["images"] = train_imgs_info
        self.coco_dict_train["annotations"] = train_anns_info
        self.coco_dict_test["images"] = test_imgs_info
        self.coco_dict_test["annotations"] = test_anns_info
        self.log2file(self.coco_dict_train, "instances_train.json")
        self.log2file(self.coco_dict_test, "instances_test.json")
        self.log("done")




# class Divide_CocoLabel_file(BaseModel):
#     """
#     A tools for divide coco label file to get train set and test set.

#     class_all.txt:
#         0 (1).py 0
#         0 (2).py 1
#         0 (3).py 2
#         0 (4).py 2
#         0 (5).py 1
#     -->
#     train.txt:
#         0 (1).py 0
#         0 (2).py 1
#         0 (4).py 2
#     test.txt:
#         0 (3).py 2
#         0 (5).py 1
#     """
#     def __init__(self):
#         super(Divide_CocoLabel_file, self).__init__()

#     def run(self):
#         root = input("Input path:")
#         prob = float(input("Input probabilty of train set (default: 0.7):") or 0.7)
#         with open(root, 'r') as f:
#             path_label_list = f.readlines()
#         random.shuffle(path_label_list)
#         train_set_len = int(len(path_label_list) * 0.7)
#         path_label_list_train = path_label_list[:train_set_len]
#         path_label_list_test = path_label_list[train_set_len:]
#         path_label_list_train_sort = self.sort_list(path_label_list_train)
#         path_label_list_test_sort = self.sort_list(path_label_list_test)
#         self.log2file(path_label_list_train_sort, log_path="train.txt", show=True)
#         self.log2file(path_label_list_test_sort, log_path="test.txt", show=True)
#         self.log('done')
        


if __name__ == "__main__":
    Divide_CocoLabel_file().run()