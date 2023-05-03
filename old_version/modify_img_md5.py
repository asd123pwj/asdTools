from base_model import BaseModel


class ModifyImgMD5(BaseModel):
    def __init__(self):
        super().__init__()
        self.permission_lower = ('png', 'jpg', 'jpeg', 'mp4')
        self.permission_upper = ('PNG', 'JPG', 'JPEG', 'MP4')
        self.permission = (*self.permission_upper, *self.permission_lower)
        self.content_modify = "MODIFYMD5"

    def modify_MD5(self, img_path):
        if img_path[-3:] in self.permission:
            with open(img_path, 'a') as f:
                f.write(self.content_modify)
            return True
        else:
            return False

    def run(self):
        path = input("Input path:")
        path_content = self.get_path_content(path, mode="allfile")
        i = 1
        for img_path in path_content:
            if self.modify_MD5(img_path):
                self.log(f"{i}: Modify {img_path}")
                i += 1
        self.log("done")

    
if __name__ == "__main__":
    ModifyImgMD5().run()