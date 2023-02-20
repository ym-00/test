#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
import sys
from math import sqrt

import cv2
import numpy as np

imgname = sys.argv[1]
print(imgname)
classfy = sys.argv[2]
print(classfy)
_author_ = '张起凡'
print('------------------------------以下是拟合3部分----------------------------------')
shutil.copyfile("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_nihe2.txt",
                "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_nihe3.txt")
shutil.copyfile("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle.txt",
                "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt")
img = cv2.imread("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/CirclePoints_nihe_1.jpg")
cv2.imwrite("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/CirclePoints_nihe_2_0.jpg", img)
for m in range(1, 5):
    print("循环开始", m)

    data_line = np.loadtxt("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_nihe3.txt",
                           dtype=int)
    print(data_line)
    circle_line = np.loadtxt("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt",
                             dtype=int)
    if circle_line.ndim == 1:
        circle_line = circle_line.reshape(1, 4)
    circle_line = circle_line[np.lexsort(circle_line[:, ::-1].T)]
    print(circle_line)
    open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt", "w").close()
    img = cv2.imread(
        "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/CirclePoints_nihe_2_%d.jpg" % (m - 1))
    line_length = len(data_line)
    circle_line_length = len(circle_line)


    for i in range(circle_line_length):
        x1, y1, x2, y2 = circle_line[i]
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        min_distance = 999
        min_distance_x = 0
        min_distance_y = 0

        for j in range(line_length):
            x11, y11, x22, y22 = data_line[j]
            x11 = int(x11)
            y11 = int(y11)
            x22 = int(x22)
            y22 = int(y22)
            distance = sqrt((x1 - x22) ** 2 + (y1 - y22) ** 2)
            distance2 = sqrt((x1 - x22) ** 2 + (y2 - y22) ** 2)
            if distance <= 30 and distance <= min_distance:
                min_distance = distance
                min_distance_x = x11
                min_distance_y = y11
                circle_line[i] = [0, 0, 0, 0]
        if min_distance_x == 0 and min_distance_y == 0:
            continue
        cv2.line(img, (min_distance_x, min_distance_y), (x2, y2), (0, 255, 0), 3)
        file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt", 'a')
        file.write(str(min_distance_x))
        file.write(' ')
        file.write(str(min_distance_y))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()
    cv2.imwrite(
        "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/CirclePoints_nihe_2_%d.jpg" % m, img)
    for i in range(circle_line_length):
        x1, y1, x2, y2 = circle_line[i]
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        min_distance = 999
        min_distance_x = 0
        min_distance_y = 0
        for j in range(line_length):
            x11, y11, x22, y22 = data_line[j]
            x11 = int(x11)
            y11 = int(y11)
            x22 = int(x22)
            y22 = int(y22)
            distance = sqrt((x2 - x11) ** 2 + (y2 - y11) ** 2)
            distance2 = sqrt((x2 - x22) ** 2 + (y2 - y22) ** 2)
            distance3 = sqrt((x2 - x22) ** 2 + (y2 - y22) ** 2)
            if distance <= 10 and distance < min_distance:
                min_distance = distance
                min_distance_x = x22
                min_distance_y = y22
                circle_line[i] = [0, 0, 0, 0]
            if distance2 <= 10 and distance2 < min_distance:
                min_distance = distance2
                min_distance_x = x11
                min_distance_y = y11
                circle_line[i] = [0, 0, 0, 0]
            if distance3 <= 40 and distance3 < min_distance and x11 < x2 and x22 > x2:
                min_distance = distance3
                min_distance_x = x22
                min_distance_y = y22
                circle_line[i] = [0, 0, 0, 0]

        if min_distance_x == 0 and min_distance_y == 0:
            continue
        cv2.line(img, (x1, y1), (min_distance_x, min_distance_y), (0, 255, 0), 3)
        file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt", 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(min_distance_x))
        file.write(' ')
        file.write(str(min_distance_y))
        file.write('\n')
        file.close()
    cv2.imwrite(
        "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/CirclePoints_nihe_2_%d.jpg" % m, img)
    print(circle_line)
    for data in circle_line:
        x1, y1, x2, y2 = data
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            continue
        file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt", 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()
    # 以下
    data_line = np.loadtxt("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_nihe3.txt",
                           dtype=int)
    print(data_line)
    circle_line = np.loadtxt("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_xie_3.txt",
                             dtype=int)
    if circle_line.ndim == 1:
        circle_line = circle_line.reshape(1, 4)

    print(circle_line)
    line_length = len(data_line)
    flag = [0] * line_length
    print(flag)
    circle_length = len(circle_line)
    print(line_length)
    print(line_length)
    # for i in range(circle_length):
    #     x1, y1, x2, y2 = circle_line[i]
    #     x1 = int(x1)
    #     y1 = int(y1)
    #     x2 = int(x2)
    #     y2 = int(y2)
    #     if x1>x2:
    #         circle_line[i]=[x2,y2,x1,y1]
    circle_line = circle_line[np.lexsort(circle_line[:, ::-1].T)]

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
                data_line[j] = [0, 0, 0, 0]
            if x2 == x22 and y2 == y22:
                print(3)
                data_line[j] = [0, 0, 0, 0]
            if x1 == x22 and y1 == y22:
                print(3)
                data_line[j] = [0, 0, 0, 0]
            if x2 == x11 and y2 == y11:
                print(3)
                data_line[j] = [0, 0, 0, 0]
            if y1 == y11 and abs(x22 - x2) <= 20:
                print(3)
                data_line[j] = [0, 0, 0, 0]
            # if abs(y2-y22)<=5  and abs(x2-x22)<=20:
            #     print(3)
            #     data_line[j] = [0, 0, 0, 0]
            # if abs(y1-y11)<=2 and abs(x22-x1)<=30 and abs(x11-x1)<=30:
            #     print(3)
            #     data_line[j] = [0, 0, 0, 0]

    img = cv2.imread("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/yuzhi.jpg")
    # print(img)
    # img = np.copy(img) * 0
    print(flag)
    print(data_line)

    open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_nihe3.txt", "w").close()
    for data in data_line:

        x1, y1, x2, y2 = data
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            continue
        file = open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/circle_nihe3.txt", 'a')
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
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    cv2.imwrite(
        "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/CirclePoints_nihe_3_%d.jpg" % m, img)
