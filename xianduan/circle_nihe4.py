#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import cv2
import numpy as np

_author_ = '张起凡'
imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
data_line = np.loadtxt("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe2.txt", dtype=int)
print(data_line)
circle_line = np.loadtxt("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_xie_3.txt", dtype=int)
if circle_line.ndim==1:
    circle_line=circle_line.reshape(1,4)
circle_line = circle_line[np.lexsort(circle_line[:, ::-1].T)]
print(circle_line)
line_length = len(data_line)
flag = [0] * line_length
print(flag)
circle_length = len(circle_line)
print(line_length)
print(line_length)

for i in range(circle_length):
    x1, y1, x2, y2 = circle_line[i]
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    # print(x1)
    for j in range(line_length):
        x11, y11, x22, y22 = data_line[j]
        x11 = int(x11)
        y11 = int(y11)
        x22 = int(x22)
        y22 = int(y22)
        # print(x11)
        if x1 == x11 and y1 == y11:
            print(1)
            data_line[j]=[0,0,0,0]
        if x2==x22 and y2==y22:
            print(3)
            data_line[j] = [0, 0, 0, 0]



img = cv2.imread("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe.jpg")
# print(img)
img = np.copy(img) * 0
print(flag)
print(data_line)

open("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe3.txt", "w").close()
for data in data_line:

    x1, y1, x2, y2 = data
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1==0 and x2==0 and y1==0 and y2==0:
        continue
    file = open("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe3.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write('\n')
    file.close()
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
for data in circle_line:
    x1, y1, x2, y2 = data
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
cv2.imwrite("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/CirclePoints_nihe_three.jpg", img)