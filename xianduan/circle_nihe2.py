#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from math import sqrt

import cv2
import numpy as np

_author_ = '张起凡'
imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
data_line = np.loadtxt("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/data_result.txt", dtype=int)
print(data_line)
circle_line = np.loadtxt("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle.txt", dtype=int)
try:
    circle_txt = np.loadtxt("xianduan/xianduan/circle_points/output/"+classfy+"/CircleTxt/"+imgname+".txt", dtype=int)
    print(circle_txt)
except:
    circle_txt = [0, 0, 0]
if circle_txt.ndim==1:
    circle_txt=circle_txt.reshape(1,3)
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
            for m in range(line_length):
                x111, y111, x222, y222 = data_line[m]
                x111 = int(x111)
                y111 = int(y111)
                x222 = int(x222)
                y222 = int(y222)
                circle_distance1=999
                circle_distance2=999
                for data in circle_txt:
                    circle_x,circle_y,circle_r=data
                    circle_x=int(circle_x)
                    circle_y=int(circle_y)
                    circle_r=int(circle_r)
                    distance1=sqrt((x11-circle_x)**2+(y11-circle_y)**2)
                    distance2 = sqrt((x22 - circle_x) ** 2 + (y22 - circle_y)**2)
                    distance3 = sqrt((x111 - circle_x) ** 2 + (y111 - circle_y)**2)
                    distance4 = sqrt((x222 - circle_x) ** 2 + (y222 - circle_y)**2)
                    min_distance1=min(distance1,distance2)
                    min_distance2=min(distance3,distance4)
                    if min_distance1<circle_distance1:
                        circle_distance1=min_distance1
                    if min_distance2<circle_distance2:
                        circle_distance2 = min_distance2


                if x2 == x222 and y2 == y222 and circle_distance1<=50 and circle_distance2<=50:

                    print(2)
                    # data_line[j] = [0, 0, 0, 0]
                    # data_line[m] = [0, 0, 0, 0]
                    flag[j] = 1
                    flag[m] = 1
                if x2 == x111 and y2 == y111:
                    print(2)
                    # data_line[j] = [0, 0, 0, 0]
                    # data_line[m] = [0, 0, 0, 0]
                    flag[j] = 1
                    flag[m] = 1
print(data_line)
for i in range(line_length):
    if flag[i] == 1:
        data_line[i] = [0, 0, 0, 0]
img = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
# print(img)
# img = np.copy(img) * 0
open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe2.txt", "w").close()
for data in data_line:

    x1, y1, x2, y2 = data
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1==0 and x2==0 and y1==0 and y2==0:
        continue
    file = open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe2.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write('\n')
    file.close()
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
for data in circle_line:
    x1, y1, x2, y2 = data
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
cv2.imwrite("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/CirclePoints_nihe_1.jpg", img)
