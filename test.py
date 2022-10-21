import os
import re
images_path = '/home/lxm/Desktop/ReDet/data/HRSC2016/Train/images'   # 图片存放目录
txt_save_path = '/home/lxm/Desktop/ReDet/data/HRSC2016/train.txt'  # 生成的图片列表清单txt文件名
fw = open(txt_save_path, "w")
for filename in os.listdir(images_path):
    print(filename.split(".")[0])
    fw.write(filename.split(".")[0] + '\n')

images_path = '/home/lxm/Desktop/ReDet/data/HRSC2016/Test/images'   # 图片存放目录
txt_save_path = '/home/lxm/Desktop/ReDet/data/HRSC2016/test.txt'  # 生成的图片列表清单txt文件名
fw = open(txt_save_path, "w")
for filename in os.listdir(images_path):
    print(filename.split(".")[0])
    fw.write(filename.split(".")[0] + '\n')
