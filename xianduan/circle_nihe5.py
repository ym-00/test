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
data_line = np.loadtxt("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe3.txt", dtype=int)
print(data_line)
circle_line = np.loadtxt("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_xie_3.txt", dtype=int)
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
flag = [0] * circle_length
img = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
# img = np.copy(img) * 0
open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_line.txt", "w").close()
file = open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_line.txt", 'a')
file.write('x1')
file.write(' ')
file.write('y1')
file.write(' ')
file.write('x2')
file.write(' ')
file.write('y2')
file.write(' ')
file.write('belong')
file.write('\n')
file.close()
open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/input_line.txt", "w").close()


open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/common_line.txt", "w").close()
file = open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/common_line.txt", 'a')
file.write('x1')
file.write(' ')
file.write('y1')
file.write(' ')
file.write('x2')
file.write(' ')
file.write('y2')
file.write('\n')
file.close()

open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/all_line.txt", "w").close()
file = open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/all_line.txt", 'a')
file.write('x1')
file.write(' ')
file.write('y1')
file.write(' ')
file.write('x2')
file.write(' ')
file.write('y2')
file.write(' ')
file.write('belong')
file.write('\n')
file.close()
data_xie=[]
for i in range(circle_length):
    x1, y1, x2, y2 = circle_line[i]
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    for j in range(i + 1, circle_length):
        x11, y11, x22, y22 = circle_line[j]
        x11 = int(x11)
        y11 = int(y11)
        x22 = int(x22)
        y22 = int(y22)
        if x1 == x11 and y1 == y11:
            continue
        if abs(x2 - x11) <= 3 or abs(y2 - y11) <= 3:
            print("小圆点可能连接")
            # distance=sqrt((x11-x2)**2+(y11-y2)**2)
            if abs(y1-y11)<=20:
                print("距离满足条件")
                flag[i]=1
                flag[j]=1
                cv2.line(img, (x1, y1), (x22, y22), (0, 255, 0), 3)
                data_xie.append([x1,y1,x22,y22])
            # file = open("./xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/total_line.txt", 'a')
            # file.write(str(x1))
            # file.write(' ')
            # file.write(str(y1))
            # file.write(' ')
            # file.write(str(x22))
            # file.write(' ')
            # file.write(str(y22))
            # file.write('\n')
            # file.close()
for i in range(circle_length):
    if flag[i]==1:
        circle_line[i]=[0,0,0,0]
print(circle_line)
for i in range(circle_length):
    x1, y1, x2, y2 = circle_line[i]
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1==0 and y1==0 and x2==0 and y2==0:
        continue
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    data_xie.append([x1,y1,x2,y2])
    # file = open("./xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/total_line.txt", 'a')
    # file.write(str(x1))
    # file.write(' ')
    # file.write(str(y1))
    # file.write(' ')
    # file.write(str(x2))
    # file.write(' ')
    # file.write(str(y2))
    # file.write('\n')
    # file.close()
print("data_xie")
print(data_xie)
circle_count=0
for i in range(len(data_xie)):
    x1,y1,x2,y2=data_xie[i]
    if x1==0 and y1==0 and x2==0 and y2==0:
        continue
    file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write(' ')
    file.write(str(circle_count))
    file.write('\n')
    file.close()

    file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/all_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write(' ')
    file.write(str(circle_count))
    file.write('\n')
    file.close()
    file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/input_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write(' ')
    file.write(str(circle_count))
    file.write('\n')
    file.close()
    for j in range(i+1,len(data_xie)):
        x11, y11, x22, y22 = data_xie[j]
        if abs(x1-x11)<=3:
            print('小圆点为同一组')
            data_xie[j]=[0,0,0,0]
            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_line.txt", 'a')
            file.write(str(x11))
            file.write(' ')
            file.write(str(y11))
            file.write(' ')
            file.write(str(x22))
            file.write(' ')
            file.write(str(y22))
            file.write(' ')
            file.write(str(circle_count))
            file.write('\n')
            file.close()
            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/all_line.txt", 'a')
            file.write(str(x11))
            file.write(' ')
            file.write(str(y11))
            file.write(' ')
            file.write(str(x22))
            file.write(' ')
            file.write(str(y22))
            file.write(' ')
            file.write(str(circle_count))
            file.write('\n')
            file.close()
            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/input_line.txt", 'a')
            file.write(str(x11))
            file.write(' ')
            file.write(str(y11))
            file.write(' ')
            file.write(str(x22))
            file.write(' ')
            file.write(str(y22))
            file.write(' ')
            file.write(str(circle_count))
            file.write('\n')
            file.close()
    circle_count+=1

for data in data_line:
    x1, y1, x2, y2 = data
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
    file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/common_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write('\n')
    file.close()
    file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/all_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write(' ')
    file.write(str(-1))
    file.write('\n')
    file.close()
    file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/input_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write(' ')
    file.write(str(-1))
    file.write('\n')
    file.close()
cv2.imwrite("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/CirclePoints_nihe_4.jpg", img)
