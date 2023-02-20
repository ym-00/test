#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
import sys

_author_ = '张起凡'
import numpy as np
import cv2
import warnings
shutil.copyfile("xianduan/information/data_shuzhi.txt", "xianduan/information/data_shuzhinihe.txt")
imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
for i in range(15):
    img = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
    # cv2.namedWindow('demo', 0)
    # cv2.imshow('demo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    image = np.copy(img)
    # cv2.namedWindow('demo', 0)
    # cv2.imshow('demo', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        data_vertical = np.loadtxt('xianduan/information/data_shuzhinihe.txt')

    print(data_vertical)
    if data_vertical.ndim==1:
        data_vertical=data_vertical.reshape(1,4)
    data_vertical=data_vertical.astype(np.int64)  # 数据类型转换
    # print(data_vertical)
    try:
        data_vertical = data_vertical[np.lexsort(data_vertical[:, ::-1].T)]
    except Exception:
        print("坐标为空")

    # print(data_vertical.T)
    # print(data_vertical)
    data_c = np.copy(data_vertical)
    shape_a = data_vertical.shape
    print(shape_a)
    row_number = shape_a[0]
    print(row_number)
    # line_number = shape_a[1]
    X_0 = 0
    X_2 = 0
    for data in data_vertical:
        catch = 0
        x1, y1, x2, y2 = data
        # print(x1)
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1 and x2 == 0:
            X_0 += 1
            continue
        X_1 = 0
        for data_1 in data_c:
            if X_0 > X_1 or X_0 == X_1:
                X_1 += 1
                continue
            x1_1, y1_1, x2_1, y2_1 = data_1
            x1_1 = np.int0(x1_1)
            y1_1 = np.int0(y1_1)
            x2_1 = np.int0(x2_1)
            y2_1 = np.int0(y2_1)
            dif_x1 = abs(x1 - x1_1)
            dif_y1 = abs(y1 - y1_1)

            dif_x2 = abs(x2 - x2_1)
            dif_y2 = abs(y2 - y2_1)
            lenth_1 = abs(y1 - y2)
            lenth_2 = abs(y1_1 - y2_1)
            if dif_x1 < 10 and dif_x2 < 10:
                # if max(lenth_1, lenth_2) > max(dif_y1, dif_y2) or abs(max(lenth_1, lenth_2) - max(dif_y1, dif_y2)) < 30:
                #     print(x1, x2, y1, y2)
                #     print(X_1)
                #     data_vertical[X_1] = [0, 0, 0, 0]
                if lenth_1 >= lenth_2:
                    if y1 < y1_1 and y2 > y2_1:
                        print(x1, x2, y1, y2)
                        data_vertical[X_1] = [0, 0, 0, 0]

                else:
                    if y1 > y1_1 and y2 < y2_1:
                        data_vertical[X_0] = [0, 0, 0, 0]
            X_1 += 1
        X_0 += 1
    # data_c = np.copy(data_vertical)
    # X_0 = 0
    # X_2 = 0
    # for data in data_vertical:
    #     catch = 0
    #     x1, y1, x2, y2 = data
    #     # print(x1)
    #     x1 = np.int0(x1)
    #     y1 = np.int0(y1)
    #     x2 = np.int0(x2)
    #     y2 = np.int0(y2)
    #     if x1 and x2 == 0:
    #         X_0 += 1
    #         continue
    #     X_1 = 0
    #     for data_1 in data_c:
    #         if X_0 > X_1 or X_0 == X_1:
    #             X_1 += 1
    #             continue
    #         x1_1, y1_1, x2_1, y2_1 = data_1
    #         x1_1 = np.int0(x1_1)
    #         y1_1 = np.int0(y1_1)
    #         x2_1 = np.int0(x2_1)
    #         y2_1 = np.int0(y2_1)
    #         dif_x1 = abs(x1 - x1_1)
    #         dif_y1 = abs(y1 - y1_1)
    #
    #         dif_x2 = abs(x2 - x2_1)
    #         dif_y2 = abs(y2 - y2_1)
    #         lenth_1 = abs(y1 - y2)
    #         lenth_2 = abs(y1_1 - y2_1)
    #         if dif_x1 < 10 and dif_x2 < 10:
    #             if max(lenth_1, lenth_2) > max(dif_y1, dif_y2) or abs(max(lenth_1, lenth_2) - max(dif_y1, dif_y2)) < 30:
    #                 print(x1, x2, y1, y2)
    #                 print(X_1)
    #                 data_vertical[X_1] = [0, 0, 0, 0]
    #             # if lenth_1 >= lenth_2:
    #             #     if y1 < y1_1 and y2 > y2_1:
    #             #         print(x1, x2, y1, y2)
    #             #         data_vertical[X_1] = [0, 0, 0, 0]
    #             # else:
    #             #     if y1 > y1_1 and y2 < y2_1:
    #             #         data_vertical[X_0] = [0, 0, 0, 0]
    #         X_1 += 1
    #     X_0 += 1
    print(data_vertical)
    for data in data_vertical:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
    cv2.imencode('.jpg', image)[1].tofile("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/竖直降噪后.jpg")
    data_vertical = np.unique(data_vertical, axis=0)  # 去除重复行
    file = open("xianduan/information/data_shuzhinihe.txt", "w").close()
    for data in data_vertical:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            continue
        file = open('xianduan/information/data_shuzhinihe.txt', 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()
