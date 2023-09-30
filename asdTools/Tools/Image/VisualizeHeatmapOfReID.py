from torchvision.transforms.functional import to_pil_image
from asdTools.Classes.Image.ImageBase import ImageBase
from torchcam.utils import overlay_mask
from torchcam.methods import GradCAM

class VisualizeHeatmapOfReID(ImageBase):
    """ Sample: Sample/VisualizeHeatmapOfReID
    使用torch-cam可视化热力图，仅测试于ReID模型。
    Visualize heatmap by torch-cam, test only on ReID.
    
    torch-cam: `pip install torchcam` or `conda install -c frgfm torchcam`, GitHub: https://github.com/frgfm/torch-cam
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(multipleFiles=True, **kwargs)

    def __call__(self, 
            model, 
            imgs_dir:str, 
            transform,
            img_ext:list=["png", "jpg", "jpeg"],
            torchCamMethod=GradCAM,
            device="cuda") -> str:
        self.run(model, imgs_dir, transform, img_ext, torchCamMethod, device)
        
    def run(self, model, imgs_dir:str, transform, img_ext:list, torchCamMethod, device) -> str:
        self.begining()
        # get paths of imgs from img_dir
        imgs_path = self.get_paths_from_dir(imgs_dir)
        self.log(f"{len(imgs_path)} files found in {imgs_dir}")
        imgs_path = self.filter_ext(imgs_path, img_ext)
        self.log(f"{len(imgs_path)} images found after filter extension by {img_ext}")
        # init torchCam
        model.to(device).eval()
        cam_extractor = torchCamMethod(model)

        for i, img_path in enumerate(imgs_path):
            # model(x)
            img = self.read_img(img_path)
            x = transform(img).unsqueeze(0).to(device)
            out = model(x)
            # visualize feature
            activation_map = cam_extractor(class_idx=0, scores=out.unsqueeze(0))[0]
            result = overlay_mask(img, to_pil_image(activation_map, mode='F'), alpha=0.5)
            # save img
            save_path = self.remove_root_of_path(path=img_path, root=imgs_dir)
            save_middle_dir = self.get_dir_of_file(save_path)
            save_name = self.get_name_of_file(save_path, True)
            save_path = self.save_image(result, output_middle_dir=save_middle_dir, output_file=save_name)
            self.log(f"{i+1}/{len(imgs_path)}: the heatmap of {img_path} has been saved to {save_path}.")
        self.done()


if __name__ == "__main__":
    """ 
    ---------- usage example ---------- 
    -- you can simply insert VisualizeHeatmapOfReID() in the train.py or main.py
    -- and then set value of imgs_dir

    from asdTools.Tools.Image.VisualizeHeatmapOfReID import VisualizeHeatmapOfReID
    from models.img_resnet import ResNet50
    import data.img_transforms as T
    
    imgs_dir = "../../../../Datasets/PRCC"

    weight = "logs/0/baseline.pth.tar"
    checkpoint = torch.load(weight)
    model = ResNet50(config)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.cuda().eval()
    
    transform_test = T.Compose([
        T.Resize((256, 128)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    color_heatmap = VisualizeHeatmapOfReID()
    color_heatmap(model, imgs_dir, transform_test)
    """
