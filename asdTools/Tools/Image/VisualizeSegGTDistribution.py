from asdTools.Classes.Image.ImageBase import ImageBase
import matplotlib.pyplot as plt
import numpy as np


class VisualizeSegGTDistribution(ImageBase):
    # v0.0.14b: fix bugs, support scale_mode (lazy for comments).
    """
    可视化GT分布，GT的类别需要从0开始递增。示例见Sample/VisualizeSegGTDistribution
    Visualize GT distribution, the class ID should be increase progressively from 0. See sample in Sample/VisualizeSegGTDistribution
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(multipleFiles=True, **kwargs)

    def __call__(self, 
                 imgs_dir:str="", 
                 img_height:int=512, 
                 img_width:int=512, 
                 device:str="cuda", 
                 ignore_index:int=-1,
                 scale_mode:str="") -> list:
        return self.run(imgs_dir, img_height, img_width, device, ignore_index, scale_mode)

    def run(self, imgs_dir:str, img_height:int, img_width:int, device:str, ignore_index:int, scale_mode:str) -> list:
        if imgs_dir == "":
            imgs_dir = self.input("Input folder path:", needLog=True)
        imgs_path = self.get_paths_from_dir(imgs_dir)
        self.log(f"{len(imgs_path)} files in {imgs_dir}.")
        imgs_path = self.filter_ext(imgs_path, ["png", "jpg", "jpeg"])
        self.log(f"{len(imgs_path)} images in {imgs_dir}.")
        color_count_dict = self.count_imgs_color(imgs_path)
        num_classes = len(color_count_dict.keys())
        self.log(f"Number of classes: {num_classes}.")
        self.log(f"Device: {device}.")
        self.log(f"Resize images to {img_height}x{img_width} (HxW).")
        self.log(f"Scale mode: {scale_mode if scale_mode!='' else 'None'}.")
        self.log(f"Ignore index: {ignore_index if ignore_index!=-1 else 'None'}.")

        GT_info = {
            "max count in single pixel": 0,
            "min count in single pixel": 0,
            "number of GT imgs": 0,
            "sum of pixel": 0,
            "sum of pixel (%)": 0.0, 
            "average GT pixel of a img": 0,
            "average GT pixel of a img (%)": 0.0,
        }
        GT_infos = {f"class-{cls:03d}": GT_info.copy() for cls in range(num_classes)}

        if device == "cpu":
            GT_count = np.zeros((img_height, img_width, num_classes))
            for i, img_path in enumerate(imgs_path):
                img = self.read_img(img_path, "Array", h=img_height, w=img_width)
                one_hot = np.eye(num_classes)[img]
                GT_count += one_hot

                unique_classes_in_image = np.unique(img)
                for cls in unique_classes_in_image:
                    GT_infos[f"class-{cls:03d}"]["number of GT imgs"] += 1

                self.log(f"{i+1}/{len(imgs_path)}: Get GT distribution for {img_path}")
            GT_count = GT_count.transpose(2, 0, 1)
        else:
            import torch
            GT_count = torch.zeros((num_classes, img_height, img_width), device='cuda')
            for i, img_path in enumerate(imgs_path):
                img = self.read_img(img_path, "Array", h=img_height, w=img_width)
                img_tensor = torch.tensor(img, device='cuda', dtype=torch.int64)
                one_hot = torch.zeros((num_classes, img_height, img_width), device='cuda', dtype=torch.int64)
                one_hot.scatter_(0, img_tensor.unsqueeze(0), 1)
                GT_count += one_hot

                unique_classes_in_image = img_tensor.unique()
                for cls in unique_classes_in_image:
                    GT_infos[f"class-{cls.item():03d}"]["number of GT imgs"] += 1

                self.log(f"{i+1}/{len(imgs_path)}: Get GT distribution for {img_path}")
            GT_count = GT_count.cpu().numpy()

        GT_maxs = GT_count.max(axis=(1, 2), keepdims=True)
        GT_mins = GT_count.min(axis=(1, 2), keepdims=True)
        GT_diff = GT_maxs - GT_mins
        GT_diff[GT_diff == 0] = 1
        GT_distribution = (GT_count - GT_mins) / GT_diff
        # GT_distribution = GT_distribution * 1.5 - 0.25
        
        average_GT_max = 0
        average_GT_average = 0
        num_GT_imgs_max = 0
        num_GT_imgs_average = 0
        sum_GTPixels = int(GT_count[:, :, :].sum())
        if ignore_index != -1:
            sum_GTPixels = sum_GTPixels - GT_count[ignore_index, :, :].sum()

        for cls in range(num_classes):
            if cls == ignore_index:
                continue
            GT_infos[f"class-{cls:03d}"]["max count in single pixel"] = int(GT_maxs[cls, 0, 0])
            GT_infos[f"class-{cls:03d}"]["min count in single pixel"] = int(GT_mins[cls, 0, 0])
            GT_infos[f"class-{cls:03d}"]["sum of pixel"] = int(GT_count[cls, :, :].sum())
            GT_infos[f"class-{cls:03d}"]["sum of pixel (%)"] = np.round(float(GT_infos[f"class-{cls:03d}"]["sum of pixel"]) / sum_GTPixels * 100, 4)
            GT_infos[f"class-{cls:03d}"]["average GT pixel of a img"] = int(GT_count[cls, :, :].sum() / GT_infos[f"class-{cls:03d}"]["number of GT imgs"])
            GT_infos[f"class-{cls:03d}"]["average GT pixel of a img (%)"] = np.round(float(GT_infos[f"class-{cls:03d}"]["average GT pixel of a img"]) / (img_height * img_width) * 100, 4)
            
            average_GT_max = max(average_GT_max, GT_infos[f"class-{cls:03d}"]["average GT pixel of a img"])
            average_GT_average += GT_infos[f"class-{cls:03d}"]["average GT pixel of a img"]
            num_GT_imgs_max = max(num_GT_imgs_max, GT_infos[f"class-{cls:03d}"]["number of GT imgs"])
            num_GT_imgs_average += GT_infos[f"class-{cls:03d}"]["number of GT imgs"]
        average_GT_average /= (num_classes - 1) if ignore_index != -1 else num_classes
        num_GT_imgs_average /= (num_classes - 1) if ignore_index != -1 else num_classes

        for cls in range(num_classes):
            if cls == ignore_index:
                continue

            # Sorry, I'm lazy to comment scale_mode
            if scale_mode == "max of 'average GT pixel of a img'":
                scale = GT_infos[f"class-{cls:03d}"]["average GT pixel of a img"] / average_GT_max
            elif scale_mode == "average of 'average GT pixel of a img'":
                scale = min(GT_infos[f"class-{cls:03d}"]["average GT pixel of a img"] / average_GT_average, 1)
            elif scale_mode == "max of 'number of GT imgs'":
                scale = GT_infos[f"class-{cls:03d}"]["number of GT imgs"] / num_GT_imgs_max
            elif scale_mode == "average of 'number of GT imgs'":
                scale = min(GT_infos[f"class-{cls:03d}"]["number of GT imgs"] / num_GT_imgs_average, 1)
            else:
                scale = 1
            scale = max(scale, 0.25)
            GT_show = GT_distribution[cls] * scale

            GT_show = plt.get_cmap('rainbow')(GT_show)[..., :3] 
            GT_show = (GT_show * 255).astype(np.uint8)
            save_path_GTDistribution = self.save_image(GT_show, output_file=f"class-{cls:03d}.png")
            self.log(f"{cls+1}/{num_classes}: Save GT distribution of class-{cls} to {save_path_GTDistribution}")
        
            GT_show = torch.tensor(GT_show[:, :, :])
            ax = plt.subplot(10, 15, cls,) 
            plt.imshow(GT_show)
            plt.axis('off')
        plt.show(block=True)
        try: 
            del GT_infos[f"class-{ignore_index:03d}"]
        except:
            pass

        self.log(f"max of 'average GT pixel of a img': {average_GT_max}")
        self.log(f"average of 'average GT pixel of a img': {average_GT_average}")  
        self.log(f"max of 'number of GT imgs': {num_GT_imgs_max}")
        self.log(f"average of 'number of GT imgs': {num_GT_imgs_average}")

        save_path_GTInfo = self.generate_output_path(output_file="GT_infos.json")
        GT_infos = self.convert_numpyType_to_builtinType(GT_infos)
        self.save_file(GT_infos, log_path=save_path_GTInfo)
        self.log(f"GT infos saved to {save_path_GTInfo}")
        self.done()
        

if __name__ == "__main__":
    # Slow, use cpu.
    # imgs_dir = r"Sample\VisualizeSegGTDistribution\Sample1-before+after\before"
    # VisualizeSegGTDistribution()(imgs_dir, img_height=512, img_width=512, device="cpu")

    # Fast, use gpu (cuda) by torch.
    # imgs_dir = r"Sample\VisualizeSegGTDistribution\Sample1-before+after\before"
    # VisualizeSegGTDistribution()(imgs_dir, img_height=512, img_width=512)
    
    scale_mode = "max of 'average GT pixel of a img'"
    scale_mode = "average of 'average GT pixel of a img'"
    scale_mode = "max of 'number of GT imgs'"
    scale_mode = "average of 'number of GT imgs'"
    scale_mode = ""
    imgs_dir = r"F:\0_DATA\1_DATA\Datasets\ADE20K\ADEChallengeData2016\annotations\training"
    # imgs_dir = r"F:\0_DATA\1_DATA\Datasets\ADE20K\ADEChallengeData2016\annotations\validation"
    # imgs_dir = r"F:\0_DATA\1_DATA\Datasets\TTPLA\annotations\train"
    VisualizeSegGTDistribution()(imgs_dir, ignore_index=0, scale_mode=scale_mode)