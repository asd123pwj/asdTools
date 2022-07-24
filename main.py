from quick_rename_dir import Quick_rename_dir
from quick_rename_file import Quick_rename_file
from quick_prefix_dir import Quick_prefix_dir
    
def main():
    print("0. Exit  退出")
    print("1. Rename one file   单文件重命名")
    print("2. Rename directory  文件夹内文件重命名")
    print("3. Add a prefix to directory  为文件夹添加前缀")
    while True:
        mode = input("Choose mode   选择模式: ")
        if mode == "0":
            break
        elif mode == "1":
            Quick_rename_file().run()
        elif mode == "2":
            Quick_rename_dir().run()
        elif mode == "3":
            Quick_prefix_dir().run()
        else:
            input("Error mode.")


if __name__ == "__main__":
    main()
