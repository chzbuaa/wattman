import os, sys


def search(curpath, s):
    L = os.listdir(curpath)  #列出当前目录下所有文件
    global i
    for subpath in L:  #遍历当前目录所有文件
        if os.path.isdir(os.path.join(curpath, subpath)):  #若文件仍为目录，递归查找子目录
            newpath = os.path.join(curpath, subpath)
            search(newpath, s)
        elif os.path.isfile(os.path.join(curpath, subpath)) and s in subpath:  #若为文件，判断是否包含搜索字串
            print(os.path.join(curpath, subpath))
            i = i+1
i=0
workingpath = sys.argv[1]
s = sys.argv[2]
search(workingpath, s)
print("搜索出来的文件数量为：",i)