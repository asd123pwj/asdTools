from base_model import BaseModel
import os


class AutoBackup(BaseModel):
    def __init__(self):
        super().__init__()
        self.max_size = 10 * 1024 * 1024   # unit: Byte
        pass

    def is_large(self, path):
        file_size = os.path.getsize(path)
        if file_size > self.max_size:
            return True
        else:
            return False

    def run(self):
        path = input("Input path")
        size = int(input("Input max file size (unit: Byte, default 10M)")) or (10 * 1024 * 1024)
        self.max_size = size


if __name__ == "__main__":
    AutoBackup().run()