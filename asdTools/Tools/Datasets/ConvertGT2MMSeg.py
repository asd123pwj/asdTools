from asdTools.Classes.Image.ImageBase import ImageBase


class ConvertGT2MMSeg(ImageBase):
    """
    将GT图片转为MMSegmentation所需的图片格式。支持处理RGB图与灰度图。
    Convert GT images to the image format required by MMSegmentation. It can handle RGB images and grayscale images.
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __call__(self, imgs_dir:str="", output_dir:str="", mapping_path:str="") -> list:
        return self.run(imgs_dir, output_dir, mapping_path)

    def run(self, imgs_dir:str="", output_dir:str="", mapping_path:str="") -> list:
        if imgs_dir == "":
            imgs_dir = self.input("Input folder path:", needLog=True)
        imgs_path = self.get_paths_from_dir(imgs_dir)
        self.log(f"{len(imgs_path)} files in {imgs_dir}.")
        imgs_path = self.filter_ext(imgs_path, ["png", "jpg", "jpeg"])
        self.log(f"{len(imgs_path)} images in {imgs_dir}.")

        self.log("Start to analyze images color...")
        color_count_dict = self.count_imgs_color(imgs_path)
        self.log(f"These images has {len(color_count_dict)} pixel value:")
        self.log(color_count_dict)
        time_now = self.get_time(True)
        color_count_path = self.generate_output_path(output_dir, f"color_count_{time_now}.json")
        color_count_str = self.convert_json_to_str(color_count_dict)
        self.save_file(color_count_str, color_count_path)

        if mapping_path == "":
            self.log('If you need to specify the conversion results for each color, ')
            self.log('please create a JSON file in the format of {"before": "after"}, ')
            self.log('For example {"0": "0", "255": "1"} for grayscale images, ')
            self.log('and {"(0, 0, 0)": "0" , "(255, 255, 255)": "1"} for RGB images.')
            self.log("If you don't need to specify the color mapping, please leave it blank.")
            mapping_path = self.input("Input json path: ", needLog=True)
        if mapping_path == "":
            color_mapping = {}
            for i, k in enumerate(color_count_dict.keys()):
                color_mapping[k] = i
        else:
            color_mapping = self.read_json(mapping_path)
            color_mapping = self.convert_val_adaptive(color_mapping)

        imgs_res_path = {}
        for img_path in imgs_path:
            img_array = self.read_img(img_path, "array")
            img_res = self.generate_image("L", (img_array.shape[0], img_array.shape[1]))
            for i in range(img_array.shape[0]):
                for j in range(img_array.shape[1]):
                    try:
                        val_ori = tuple(img_array[i][j])
                    except:
                        val_ori = int(img_array[i][j])
                    val_new = color_mapping[val_ori]
                    img_res.putpixel((j, i), val_new)
            img_res_name = self.get_name_of_file(img_path, True)
            img_res_path = self.save_image(img_res, output_dir, img_res_name)
            imgs_res_path[img_path] = img_res_path
            self.log(f"The MMSeg format of {img_path} is saved in {img_res_path}")

        return imgs_res_path
        

if __name__ == "__main__":
    # imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\train\gt2"
    # imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\train\vl"
    mapping_path = r"F:\0_DATA\1_DATA\Datasets\VITL\seed1\train\color_mapping.json"
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\train\gt"
    ConvertGT2MMSeg(log_dir="./Logs/seed0/train/gt")(imgs_dir, mapping_path=mapping_path)
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\test\gt"
    ConvertGT2MMSeg(log_dir="./Logs/seed0/test/gt")(imgs_dir, mapping_path=mapping_path)
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed0\val\gt"
    ConvertGT2MMSeg(log_dir="./Logs/seed0/val/gt")(imgs_dir, mapping_path=mapping_path)
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed1\train\gt"
    ConvertGT2MMSeg(log_dir="./Logs/seed1/train/gt")(imgs_dir, mapping_path=mapping_path)
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed1\test\gt"
    ConvertGT2MMSeg(log_dir="./Logs/seed1/test/gt")(imgs_dir, mapping_path=mapping_path)
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\VITL\seed1\val\gt"
    ConvertGT2MMSeg(log_dir="./Logs/seed1/val/gt")(imgs_dir, mapping_path=mapping_path)
    