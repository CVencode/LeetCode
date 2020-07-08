# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-06-29
Introduction:删除文件夹及其内容
"""
import os
import shutil

"""删除某个文件"""


def deleteFile(path):
    if os.path.exists(path):
        # 删除文件，可使用以下两种方法。
        os.remove(path) # path指的是文件的绝对路径,如：os.remove(r"E:\code\practice\data\1.py")
        # os.unlink(path)
    else:
        print('no such file:%s' % path)


"""删除某路径下的文件内容"""


def deleteAllFile(path):
    delList = []
    # path = "D:/BaiduNetdiskDownload/Flickr1024/Test"
    for f in os.listdir(path):
        filePath = os.path.join(path, f)
        if os.path.isfile(filePath):
            os.remove(filePath)
            print(filePath + " was removed!")
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath, True)
        print("Directory: " + filePath + " was removed!")


path = 'E:/a1Yajing/计算机学院毕业生照片'  # 文件路径
deleteAllFile(path)