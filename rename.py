import os

path = 'C:\\Users\\18713\Desktop\\vocimage'  # 文件路径
count = 1
filelist = os.listdir(path)  # 该文件夹下所有文件


def rename():
    global count
    for files in filelist:  # 遍历文件
        Olddir = os.path.join(path, files)  # 原来的文件路径
        filename = os.path.splitext(files)[0]  # 文件名
        filetype = os.path.splitext(files)[1]  # 文件扩展名
        print(filename)
        print(filetype)
        Newdir = os.path.join(path, "图" + str(count) + ".jpg")  # 新的文件路径
        os.rename(Olddir, Newdir)  # 重命名
        count += 1


rename()