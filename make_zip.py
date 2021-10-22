# -*-coding:utf-8-*-
import os
import zipfile
#这个函数的作用是将文件夹压缩成zip，参数localPath是待压缩文件夹的路径，pname是压缩后的zip的路径
def make_zip(localPath, pname):
    #这段是创建一个空白的zip文件，下面是把原本文件夹中的内容写入到zip文件中
    zipf = zipfile.ZipFile(pname, 'w', zipfile.ZIP_DEFLATED)
    #pre_len是文件夹所在路径的长度，包括文件夹本身，os.path.dirname去掉文件名返回路径
    pre_len = len(os.path.dirname(localPath))
#    print(pre_len)
#    print(os.path.dirname(localPath))
    #获取每个文件，并把文件路径拼起来，也就是文件夹中所有文件的路径，并将这些文件写入压缩包中
    for parent, dirnames, filenames in os.walk(localPath):
        for filename in filenames:
#            print(parent,filename)
            pathfile = os.path.join(parent, filename)
            print(pathfile)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            print(pathfile[pre_len:])
            print(arcname)
            zipf.write(pathfile, arcname)
    zipf.close()

if __name__ == "__main__":
    path = "D:\\360bizhi\\"
    make_zip(path, "D:\\360bizhi.zip")