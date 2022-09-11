import os
import pickle
import cv2

path = "work_dirs/ReDet_re50_refpn_3x_hrsc2016/results_pkl"

file_list = {}
for file in os.listdir(path):
    f = open(os.path.join(path, file), 'rb')
    f = pickle.load(f)
    file_list[file.split('-')[-1].split('.')[0]] = f

print(file_list)

# 展示一幅图
img = file_list['train']['image_data'][0]
cv2.imshow("img",img)

