from file2txt import File2txt
from quick_rename_dir import Quick_rename_dir               # v1.0
from quick_rename_file import Quick_rename_file             # v1.0
from quick_prefix_dir import Quick_prefix_dir               # v1.1
from generate_empty_backup import Generate_empty_backup     # v1.2
from quick_divide import Quick_divide                       # v1.2
from file2txt import File2txt                               # v1.2
from divide_ClsLabel_file import Divide_ClsLabel_file             # v1.3


def main():
    print("0. Exit  退出")
    print("1. Rename one file \t单文件重命名")
    print("2. Rename directory \t文件夹内文件重命名")
    print("3. Add a prefix to directory \t为文件夹添加前缀")
    print("4. Generate empty backup \t创建空备份文件")
    print("5. Devide files into group \t按组分割文件")
    print("6. Convert path into txt \t将路径内文件记录为txt")
    print("7. Divide label file to trainset and testset \t分割标签文件为训练集与测试集")
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
        elif mode == "4":
            Generate_empty_backup().run()
        elif mode == "5":
            Quick_divide().run()
        elif mode == "6":
            File2txt().run()
        elif mode == "7":
            Divide_ClsLabel_file().run()
        else:
            input("Error mode.")


if __name__ == "__main__":
    main()