#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from math import sqrt

_author_ = '张起凡'
import cv2
import os
import numpy as np
imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
try:
    circle_txt = np.loadtxt("xianduan/xianduan/circle_points/output/"+classfy+"/CircleTxt/"+imgname+".txt")
except Exception:
    circle_txt=np.array([0,0,0])
    print("未检测到小圆点")
# print(circle_txt)
if circle_txt.ndim==1:
    circle_txt=circle_txt.reshape(1,3)
print(circle_txt[0])
line_txt=np.loadtxt('xianduan/information/data_nihe.txt')

line_txt=line_txt.astype(np.int64)
line_txt=line_txt[np.lexsort(line_txt[:,::-1].T)]
row=len(line_txt)
print(line_txt)
print(row)
img=cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
# print(img)
open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle.txt", "w").close()
for data in circle_txt:
    lst = [0] * row
    x=data[0]
    y=data[1]
    r=data[2]
    if x==0 and y==0 and r==0:
        continue
    r_left=x-r
    r_right=x+r
    r_up=y-r
    r_down=y+r
    print(r_left,r_right,r_up,r_down)
    i=0
    min_left=999
    min_up=999
    min_right=999
    min_down=999
    for data_1 in line_txt:
        line_x1=int(data_1[0])
        line_y1 = int(data_1[1])
        line_x2 = int(data_1[2])
        line_y2 = int(data_1[3])
        distance_left1=sqrt((r_left-line_x1)**2+(y-line_y1)**2)
        # print(distance_left1)
        distance_left2 = sqrt((r_left - line_x2) ** 2 + (y - line_y2) ** 2)
        if distance_left1<20 or distance_left2<20:
            if min(distance_left1,distance_left2)<min_left:
                min_left = min(distance_left1, distance_left2)
                lst[i] = 1



        distance_right1 = sqrt((r_right - line_x1) ** 2 + (y - line_y1) ** 2)
        distance_right2 = sqrt((r_right - line_x2) ** 2 + (y - line_y2) ** 2)
        if distance_right1 < 20 or distance_right2 < 20:
            if min(distance_right1,distance_right2)<min_right:
                min_right=min(distance_right1,distance_right2)
                lst[i] = 3
        distance_up1 = sqrt((x - line_x1) ** 2 + (r_up - line_y1) ** 2)
        distance_up2 = sqrt((x - line_x2) ** 2 + (r_up - line_y2) ** 2)
        if distance_up1 < 20 or distance_up2 < 20:
            if min(distance_up1, distance_up2) < min_up:
                min_up = min(distance_up1, distance_up2)
                lst[i] = 2

        distance_down1 = sqrt((x - line_x1) ** 2 + (r_down - line_y1) ** 2)
        distance_down2 = sqrt((x - line_x2) ** 2 + (r_down - line_y2) ** 2)
        if distance_down1 < 20 or distance_down2 < 20:
            if min(distance_down1,distance_down2)<min_down:
                min_down=min(distance_down1,distance_down2)
                lst[i] = 4
        i+=1
    i=0
    print(lst)
    data_test=[]
    for i in range(row):
        if lst[i]!=0:
            data_test.append(line_txt[i])
            i+=1
    data_test=np.array(data_test)
    try:
        data_test = data_test[np.lexsort(data_test[:, ::-1].T)]
    except Exception:
        print("坐标为空")
    circle_row=len(data_test)
    print(circle_row)
    i=0
    main_line = 0


    for i in range(circle_row):

        test=data_test[i]
        # print(test)
        x1=test[0]
        y1=test[1]
        x2=test[2]
        y2=test[3]
        if abs(y1-y2)<=20:
            print('横线')
            main_line=1
            j=i+1
            if x2<x:
                for j in range(circle_row):
                    test2 = data_test[j]
                    # print(test2)
                    x11 = test2[0]
                    y11 = test2[1]
                    x22 = test2[2]
                    y22 = test2[3]
                    if abs(x11 - x22) <= 20:
                        print("竖线")
                        if y11 < y2 and y22 < y2:
                            if y11 < y22:
                                x_temp = x11
                                y_temp = y11
                                cv2.line(img, (x1, y1), (x_temp, y_temp), (0, 255, 0), 3)
                                file = open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle.txt", 'a')
                                file.write(str(x1))
                                file.write(' ')
                                file.write(str(y1))
                                file.write(' ')
                                file.write(str(x_temp))
                                file.write(' ')
                                file.write(str(y_temp))
                                file.write('\n')
                                file.close()
                            if y11 > y22:
                                x_temp = x22
                                y_temp = y22
                                cv2.line(img, (x1, y1), (x_temp, y_temp), (0, 255, 0), 3)
                                file = open(
                                    "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt", 'a')
                                file.write(str(x1))
                                file.write(' ')
                                file.write(str(y1))
                                file.write(' ')
                                file.write(str(x_temp))
                                file.write(' ')
                                file.write(str(y_temp))
                                file.write('\n')
                                file.close()
                        if y11 > y2 and y22 > y2:
                            if y11 < y22:
                                x_temp = x22
                                y_temp = y22
                                cv2.line(img, (x1, y1), (x_temp, y_temp), (0, 255, 0), 3)
                                file = open(
                                    "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt", 'a')
                                file.write(str(x1))
                                file.write(' ')
                                file.write(str(y1))
                                file.write(' ')
                                file.write(str(x_temp))
                                file.write(' ')
                                file.write(str(y_temp))
                                file.write('\n')
                                file.close()
                            if y11 > y22:
                                x_temp = x11
                                y_temp = y11
                                cv2.line(img, (x1, y1), (x_temp, y_temp), (0, 255, 0), 3)
                                file = open(
                                    "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt", 'a')
                                file.write(str(x1))
                                file.write(' ')
                                file.write(str(y1))
                                file.write(' ')
                                file.write(str(x_temp))
                                file.write(' ')
                                file.write(str(y_temp))
                                file.write('\n')
                                file.close()
                    else:
                        print('横线')
                        if x11>x:
                            x_temp=x22
                            y_temp=y22
                            cv2.line(img, (x1, y1), (x_temp, y_temp), (0, 255, 0), 3)
                            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt",
                                        'a')
                            file.write(str(x1))
                            file.write(' ')
                            file.write(str(y1))
                            file.write(' ')
                            file.write(str(x_temp))
                            file.write(' ')
                            file.write(str(y_temp))
                            file.write('\n')
                            file.close()
                    # j += 1
        elif abs(x1-x2)<20 and main_line==0:
            print('竖线')
            if y1<y and y2<y:
                j = i + 1
                for j in range(circle_row):
                    test2 = data_test[j]
                    x11 = test2[0]
                    y11 = test2[1]
                    x22 = test2[2]
                    y22 = test2[3]
                    if abs(y11 - y22) < 20:
                        print("横线")
                        if x22 < x and x11 < x:
                            x_temp = x11
                            y_temp = y11
                            if y1 < y2:
                                x_c = x1
                                y_c = y1
                            else:
                                x_c = x2
                                y_c = y2
                            cv2.line(img, (x_c, y_c), (x_temp, y_temp), (0, 255, 0), 3)
                            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt",
                                        'a')
                            file.write(str(x_c))
                            file.write(' ')
                            file.write(str(y_c))
                            file.write(' ')
                            file.write(str(x_temp))
                            file.write(' ')
                            file.write(str(y_temp))
                            file.write('\n')
                            file.close()
                        if x22 > x and x11 > x:
                            x_temp = x22
                            y_temp = y22
                            if y1 < y2:
                                x_c = x1
                                y_c = y1
                            else:
                                x_c = x2
                                y_c = y2
                            cv2.line(img, (x_c, y_c), (x_temp, y_temp), (0, 255, 0), 3)
                            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt",
                                        'a')
                            file.write(str(x_c))
                            file.write(' ')
                            file.write(str(y_c))
                            file.write(' ')
                            file.write(str(x_temp))
                            file.write(' ')
                            file.write(str(y_temp))
                            file.write('\n')
                            file.close()

                    else:
                        if y11>y and y22>y:
                            if y1 < y2:
                                x_c = x1
                                y_c = y1
                            else:
                                x_c = x2
                                y_c = y2
                            if y11 < y22:
                                x_temp = x22
                                y_temp = y22
                            else:
                                x_temp = x11
                                y_temp = y11
                            cv2.line(img, (x_c, y_c), (x_temp, y_temp), (0, 255, 0), 3)
                            file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt",
                                        'a')
                            file.write(str(x_c))
                            file.write(' ')
                            file.write(str(y_c))
                            file.write(' ')
                            file.write(str(x_temp))
                            file.write(' ')
                            file.write(str(y_temp))
                            file.write('\n')
                            file.close()
                    # j += 1
            if y1 > y and y2 > y:
                j = i + 1
                for j in range(circle_row):
                    test2 = data_test[j]
                    x11 = test2[0]
                    y11 = test2[1]
                    x22 = test2[2]
                    y22 = test2[3]
                    if abs(y11 - y22) < 20:
                        print("横线")
                        if x22 < x and x11 < x:
                            x_temp=x11
                            y_temp=y11
                            if y1<y2:
                                x_c=x2
                                y_c=y2
                            else:
                                x_c = x1
                                y_c = y1
                            # cv2.line(img, (x_c, y_c), (x_temp, y_temp), (0, 255, 0), 1)
                        if x22 > x and x11 > x:
                            x_temp = x22
                            y_temp = y22
                            if y1<y2:
                                x_c=x2
                                y_c=y2
                            else:
                                x_c = x1
                                y_c = y1
                            # cv2.line(img, (x_c, y_c), (x_temp, y_temp), (0, 255, 0), 1)
                    else:
                        if y11<y and y22<y:
                            if y1 < y2:
                                x_c = x1
                                y_c = y1
                            else:
                                x_c = x2
                                y_c = y2
                            if y11 < y22:
                                x_temp = x22

                                y_temp = y22
                            else:
                                x_temp = x11
                                y_temp = y11
                            # cv2.line(img, (x_c, y_c), (x_temp, y_temp), (0, 255, 0), 1)

                    # j+=1



        # i+=1


    print(data_test)
img=cv2.imwrite("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/circle_nihe.jpg",img)