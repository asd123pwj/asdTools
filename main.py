from quick_rename_dir import Quick_rename_dir
from quick_rename_file import Quick_rename_file
    
def main():
    print("1. One file rename   单文件重命名")
    print("2. Directory rename  文件夹内文件重命名")
    mode = input("Choose mode   选择模式: ")
    if mode == "1":
        Quick_rename_file().run()
    elif mode == "2":
        Quick_rename_dir().run()


if __name__ == "__main__":
    main()
