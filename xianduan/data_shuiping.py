#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import warnings

_author_ = '张起凡'
import numpy as np
import cv2
import os

imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[ ', '').replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


img = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
img = np.copy(img)
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    data_s = np.loadtxt('xianduan/information/data_jiehe_shuiping.txt')
if data_s.ndim==1:
    data_s=data_s.reshape(1,4)
print(data_s)
try:
    data_s = data_s[np.lexsort(data_s[:, ::-1].T)]  # 按第一列排序
except Exception:
    print("坐标为空")

print(data_s)
data_s = data_s.astype(np.int64)  # 变换数据格式
data_c = np.copy(data_s)
shape_a = data_s.shape

row_number = shape_a[0]

# line_number = shape_a[1]
open("xianduan/information/data_nihe.txt", "w").close()
X_0 = 0
i = 0
for i in range(row_number):
    x1, y1, x2, y2 = data_s[i]
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    if x1>x2:
        data_s[i]=[x2,y2,x1,y1]
for i in range(row_number):
    x1, y1, x2, y2 = data_s[i]
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    # print(data_s[i])
    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        continue
    for j in range(i+1,row_number):
        x1_1, y1_1, x2_1, y2_1 = data_s[j]
        x1_1 = np.int0(x1_1)
        y1_1 = np.int0(y1_1)
        x2_1 = np.int0(x2_1)
        y2_1 = np.int0(y2_1)
        if x1_1 == 0 and x2_1 == 0 and y1_1 == 0 and y2_1 == 0:
            continue
        dif_x1 = abs(x1 - x1_1)
        dif_y1 = abs(y1 - y1_1)

        dif_x2 = abs(x2 - x2_1)
        dif_y2 = abs(y2 - y2_1)
        lenth_1 = abs(x1 - x2)
        lenth_2 = abs(x1_1 - x2_1)
        if 0 <= dif_y1 <= 10 and 0 <= dif_y2 <= 10:
            if lenth_1 >= lenth_2:
                print(1)
                if x1 >= x1_1 and x1 <= x2_1:
                    data_s[i] = [x1_1, y1, x2, y2]
                    x1 = x1_1
                    data_s[j] = [0, 0, 0, 0]
                elif x2 <= x2_1 and x2 >= x1_1:
                    data_s[i] = [x1, y1, x2_1, y2]
                    x2 = x2_1
                    data_s[j] = [0, 0, 0, 0]
                elif x1 >=x1_1 and x1 >= x2_1 and x1 - x2_1 <= 20:
                    data_s[i] = [x1_1, y1, x2, y2]
                    x1 = x1_1
                    data_s[j] = [0, 0, 0, 0]
                elif x2 <= x1_1 and x2<=x2_1 and x1_1 - x2 <= 20:
                    data_s[i] = [x1, y1, x2_1, y2]
                    x2 = x2_1
                    data_s[j] = [0, 0, 0, 0]
                elif x1 <= x1_1 and x2 >= x2_1:
                    data_s[j] = [0, 0, 0, 0]
            else:
                if x1<=x1_1 and x2 >= x1_1:
                    data_s[j] = [x1, y1_1, x2_1, y2_1]
                    data_s[i] = [0, 0, 0, 0]
                elif x2>=x2_1 and x1<=x2_1:
                    data_s[j] = [x1_1, y1_1, x2, y2_1]
                    data_s[i] = [0, 0, 0, 0]
                elif x1>=x1_1 and x2 <= x2_1:
                    data_s[i] = [0, 0, 0, 0]
                elif x1 >=x2_1 and x1>=x2_1 and x1 - x2_1 <= 10:
                    data_s[j] = [x1_1, y1_1, x2, y2_1]
                    data_s[i] = [0, 0, 0, 0]
                elif x2 <= x1_1  and x2<=x2_1 and x1_1-x2 <= 10:
                    data_s[j] = [x1, y1_1, x2_1, y2_1]
                    data_s[i] = [0, 0, 0, 0]

data_s = np.unique(data_s, axis=0)  # 去除重复行
print(data_s)
for data in data_s:
    x1, y1, x2, y2 = data
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        continue
    file = open('xianduan/information/data_nihe.txt', 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write('\n')
    file.close()
data_s = np.loadtxt('xianduan/information/data_nihe.txt')
data_s = data_s.astype(np.int64)
if data_s.ndim==1:
    data_s=data_s.reshape(1,4)
for data in data_s:
    x1, y1, x2, y2 = data
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
cv2.imencode('.jpg', img)[1].tofile("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/水平拟合后.jpg")
