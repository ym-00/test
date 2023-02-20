# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
import sys
import warnings
import numpy as np
import cv2

def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[ ', '').replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


def new_noise_0610(imgname:str,classfy:str):
    shutil.copyfile("xianduan/data_shuiping.txt","xianduan/data_shuipingnihe.txt")
    for m in range(15):
        img = cv2.imread('xianduan/common_picture.jpg')
        # cv2.namedWindow('demo', 0)
        # cv2.imshow('demo', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        image = np.copy(img) * 0

        data_s = np.loadtxt('xianduan/data_shuipingnihe.txt')

        data_s.astype(np.int64)
        try:
            data_s = data_s[np.lexsort(data_s[:, ::-1].T)]
        except Exception:
            print("坐标空白")

        print(data_s)

        data_c = np.copy(data_s)

        shape_a = data_s.shape

        row_number = shape_a[0]

        line_number = shape_a[1]

        # print (data_s)

        open("xianduan/data_shuipingnihe.txt", "w").close()

        X_0 = 0
        X_2 = 0
        for data in data_s:

            catch = 0
            x1, y1, x2, y2 = data
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
                #
                # if abs(x1_1 - x2_1) < 3:
                #     X_1 += 1
                #     continue

                dif_x1 = abs(x1 - x1_1)
                dif_y1 = abs(y1 - y1_1)

                dif_x2 = abs(x2 - x2_1)
                dif_y2 = abs(y2 - y2_1)

                lenth_1 = abs(x1 - x2)
                lenth_2 = abs(x1_1 - x2_1)


                if dif_y1 < 10 and dif_y2 < 10:
                    if lenth_1 >= lenth_2:
                        if x1 <= x1_1 and x2 >= x2_1:
                            data_s[X_1] = [0, 0, 0, 0]
                    else:
                        if x1 >= x1_1 and x2 <= x2_1:
                            data_s[X_0] = [0, 0, 0, 0]
                #     if max(lenth_1, lenth_2) > max(dif_x1, dif_x2) or abs(max(lenth_1, lenth_2) - max(dif_x1, dif_x2)) < 40:
                #         print(x1, y1, x2, y2)
                #         print(X_1)
                #         data_s[X_1] = [0, 0, 0, 0]
                #         # X_2 += 1
                #         break
                X_1 += 1
                # if X_2 > 1:
                #     break
            X_0 += 1

        print(data_s)



        data_s = np.unique(data_s, axis=0) # 去除重复行
        for data in data_s:
            x1, y1, x2, y2 = data
            x1 = np.int0(x1)
            y1 = np.int0(y1)
            x2 = np.int0(x2)
            y2 = np.int0(y2)
            if x1==0 and x2==0 and y1==0 and y2==0:
                continue
            file = open('xianduan/data_shuipingnihe.txt', 'a')
            file.write(str(x1))
            file.write(' ')
            file.write(str(y1))
            file.write(' ')
            file.write(str(x2))
            file.write(' ')
            file.write(str(y2))
            file.write('\n')
            file.close()
        data_s = np.loadtxt('xianduan/data_shuipingnihe.txt')
        data_s.astype(np.int64)
        print(data_s)
        for data in data_s:
            x1, y1, x2, y2 = data
            x1 = np.int0(x1)
            y1 = np.int0(y1)
            x2 = np.int0(x2)
            y2 = np.int0(y2)
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        # cv2.imwrite("./xianduan/xianduanjiance/lines_edges_1_noise.jpg", image)
        cv2.imencode('.jpg', image)[1].tofile("xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/水平降噪后.jpg")

            # print("xxxx",dif_x1,dif_x2)

def shuzhi_noise(imgname:str,classfy:str):

    shutil.copyfile("xianduan/data_shuzhi.txt", "xianduan/data_shuzhinihe.txt")

    for i in range(15):
        img = cv2.imread('xianduan/common_picture.jpg')
        # cv2.namedWindow('demo', 0)
        # cv2.imshow('demo', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        image = np.copy(img) * 0
        # cv2.namedWindow('demo', 0)
        # cv2.imshow('demo', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            data_vertical = np.loadtxt('xianduan/data_shuzhinihe.txt')

        print(data_vertical)
        data_vertical = data_vertical.astype(np.int64)  # 数据类型转换
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
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imencode('.jpg', image)[1].tofile(
            "xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/竖直降噪后.jpg")
        data_vertical = np.unique(data_vertical, axis=0)  # 去除重复行
        file = open("xianduan/data_shuzhinihe.txt", "w").close()
        for data in data_vertical:
            x1, y1, x2, y2 = data
            x1 = np.int0(x1)
            y1 = np.int0(y1)
            x2 = np.int0(x2)
            y2 = np.int0(y2)
            if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
                continue
            file = open('xianduan/data_shuzhinihe.txt', 'a')
            file.write(str(x1))
            file.write(' ')
            file.write(str(y1))
            file.write(' ')
            file.write(str(x2))
            file.write(' ')
            file.write(str(y2))
            file.write('\n')
            file.close()

def jiehe_0610(imgname:str,classfy:str):

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        data_s = np.loadtxt('xianduan/data_shuipingnihe.txt')
        data_s_1 = np.loadtxt('xianduan/data_shuzhinihe.txt')

    print(data_s_1)
    open("xianduan/data_jiehe_shuiping.txt", "w").close()
    open("xianduan/data_jiehe_shuzhi.txt", "w").close()
    data_s = data_s.astype(np.int64)

    # data_s = data_s[np.lexsort(data_s[:, ::-1].T)]
    # data_s_1 = data_s_1[np.lexsort(data_s[:, ::-1].T)]

    data_c = np.copy(data_s)

    shape_a = data_s.shape

    row_number = shape_a[0]

    # line_number = shape_a[1]

    img = cv2.imread('xianduan/common_picture.jpg')
    image = np.copy(img) * 0
    image_1 = np.copy(img) * 0
    data_c = np.copy(data_s)
    data_v = np.copy(data_s_1)
    X_0 = 0

    for data in data_s:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
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
            if y1 == y2 == y1_1 == y2_1:
                if x1_1 - x2 > 0 and x1_1 - x2 <= 5:
                    data_s[X_0] = [x1, y1, x2_1, y2_1]
                    data_s[X_1] = [0, 0, 0, 0]
                if x1 - x2_1 > 0 and x1 - x2_1 <= 5:
                    data_s[X_0] = [x1_1, y1, x2, y2]
                    data_s[X_1] = [0, 0, 0, 0]
            X_1 += 1
        X_0 += 1
    for i in range(len(data_s_1)):
        x1, y1, x2, y2 = data_s_1[i]
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1 == x2 and y1 > y2:
            data_s_1[i] = [x2, y2, x1, y1]
    print(data_s_1)
    data_v = np.copy(data_s_1)
    X_0 = 0
    for data in data_s_1:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        X_1 = 0
        for data_1 in data_v:
            if X_0 > X_1 or X_0 == X_1:
                X_1 += 1
                continue
            x1_1, y1_1, x2_1, y2_1 = data_1
            x1_1 = np.int0(x1_1)
            y1_1 = np.int0(y1_1)
            x2_1 = np.int0(x2_1)
            y2_1 = np.int0(y2_1)
            if x1 == x2 == x1_1 == x2_1:
                if y1_1 - y2 > 0 and y1_1 - y2 <= 20:
                    data_s_1[X_0] = [x1, y1, x2, y2_1]
                    y2 = y2_1
                    data_s_1[X_1] = [0, 0, 0, 0]
                if y1 - y2_1 > 0 and y1 - y2_1 <= 20:
                    data_s_1[X_0] = [x1, y1_1, x2, y2]
                    y1 = y1_1
                    data_s_1[X_1] = [0, 0, 0, 0]
            X_1 += 1
        X_0 += 1
    for data in data_s:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            continue
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        file = open('xianduan/data_jiehe_shuiping.txt', 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()

    for data in data_s_1:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            continue
        cv2.line(image_1, (x1, y1), (x2, y2), (0, 0, 255), 1)

        file = open('xianduan/data_jiehe_shuzhi.txt', 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()

    # cv2.imwrite("./xianduan/xianduanjiance/lines_edges_1_jiehe1.jpg", image_1)
    cv2.imencode('.jpg', image)[1].tofile(
        "xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/水平结合后.jpg")
    # cv2.imwrite("./xianduan/xianduanjiance/lines_edges_1_jiehe2.jpg", image)
    cv2.imencode('.jpg', image_1)[1].tofile(
        "xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/竖直结合后.jpg")

def jiehe_0611():
    data_t = np.loadtxt('xianduan/data_jiehe.txt')

    try:
        open("xianduan/data_jiehe.txt", "w").close()
    except:
        print('None')
    data_t = data_t[np.lexsort(data_t[:, ::-1].T)]

    print(data_t)

    for data in data_t:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if abs(x1 - x2) < 5:
            x1 = min(x1, x2)
            x2 = min(x1, x2)
        if abs(y1 - y2) < 5:
            y1 = min(y1, y2)
            y2 = min(y1, y2)
        if x1 > x2:
            file = open('xianduan/data_jiehe.txt', 'a')
            file.write(str(x2))
            file.write(' ')
            file.write(str(y2))
            file.write(' ')
            file.write(str(x1))
            file.write(' ')
            file.write(str(y1))
            file.write('\n')
        else:
            if y1 < y2:
                file = open('xianduan/data_jiehe.txt', 'a')
                file.write(str(x2))
                file.write(' ')
                file.write(str(y2))
                file.write(' ')
                file.write(str(x1))
                file.write(' ')
                file.write(str(y1))
                file.write('\n')

            else:
                file = open('xianduan/data_jiehe.txt', 'a')
                file.write(str(x1))
                file.write(' ')
                file.write(str(y1))
                file.write(' ')
                file.write(str(x2))
                file.write(' ')
                file.write(str(y2))
                file.write('\n')

def data_shuiping(imgname:str,classfy:str):
    img = cv2.imread('xianduan/common_picture.jpg')
    img = np.copy(img) * 0
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        data_s = np.loadtxt('xianduan/data_jiehe_shuiping.txt')
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
    open("xianduan/data_nihe.txt", "w").close()
    X_0 = 0
    i = 0
    for i in range(row_number):
        x1, y1, x2, y2 = data_s[i]
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        # print(data_s[i])
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            i += 1
            continue
        j = i + 1
        for j in range(row_number):
            x1_1, y1_1, x2_1, y2_1 = data_s[j]
            x1_1 = np.int0(x1_1)
            y1_1 = np.int0(y1_1)
            x2_1 = np.int0(x2_1)
            y2_1 = np.int0(y2_1)
            if x1_1 == 0 and x2_1 == 0 and y1_1 == 0 and y2_1 == 0:
                j += 1
                continue
            dif_x1 = abs(x1 - x1_1)
            dif_y1 = abs(y1 - y1_1)

            dif_x2 = abs(x2 - x2_1)
            dif_y2 = abs(y2 - y2_1)
            lenth_1 = abs(y1 - y2)
            lenth_2 = abs(y1_1 - y2_1)
            if 0 < dif_y1 < 10 and 0 < dif_y2 < 10:
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
                    elif x1 >= x1_1 and x1 >= x2_1 and x1 - x2_1 <= 10:
                        data_s[i] = [x1_1, y1, x2, y2]
                        x1 = x1_1
                        data_s[j] = [0, 0, 0, 0]
                    elif x2 <= x1_1 and x2 <= x2_1 and x1_1 - x2 <= 10:
                        data_s[i] = [x1, y1, x2_1, y2]
                        x2 = x2_1
                        data_s[j] = [0, 0, 0, 0]
                    elif x1 <= x1_1 and x2 >= x2_1:
                        data_s[j] = [0, 0, 0, 0]
                else:
                    if x1 <= x1_1 and x2 >= x1_1:
                        data_s[j] = [x1, y1_1, x2_1, y2_1]
                        data_s[i] = [0, 0, 0, 0]
                    elif x2 >= x2_1 and x1 <= x2_1:
                        data_s[j] = [x1_1, y1_1, x2, y2_1]
                        data_s[i] = [0, 0, 0, 0]
                    elif x1 >= x1_1 and x2 <= x2_1:
                        data_s[i] = [0, 0, 0, 0]
                    elif x1 >= x2_1 and x1 >= x2_1 and x1 - x2_1 <= 10:
                        data_s[j] = [x1_1, y1_1, x2, y2_1]
                        data_s[i] = [0, 0, 0, 0]
                    elif x2 <= x1_1 and x2 <= x2_1 and x1_1 - x2 <= 10:
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
        file = open('xianduan/data_nihe.txt', 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()
    data_s = np.loadtxt('xianduan/data_nihe.txt')
    data_s = data_s.astype(np.int64)
    for data in data_s:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv2.imencode('.jpg', img)[1].tofile("xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/水平拟合后.jpg")

def data_shuzhi(imgname:str,classfy:str):

    img = cv2.imread('xianduan/common_picture.jpg')
    img = np.copy(img) * 0
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        data_s = np.loadtxt('xianduan/data_jiehe_shuzhi.txt')

    # print(data_s)
    try:
        data_s = data_s[np.lexsort(data_s[:, ::-1].T)]  # 按第一列排序
    except Exception:
        print("坐标为空")

    # print(data_s)
    data_s = data_s.astype(np.int64)  # 变换数据格式

    data_c = np.copy(data_s)
    shape_a = data_s.shape

    row_number = shape_a[0]
    # row_number=int(row_number)
    print(row_number)
    # line_number = shape_a[1]
    i = 0
    for i in range(row_number):
        x1, y1, x2, y2 = data_s[i]
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if y1 > y2:
            data_s[i] = [x2, y2, x1, y1]
        i += 1
    # open("data_nihe.txt", "w").close()
    i = 0
    for i in range(row_number):
        x1, y1, x2, y2 = data_s[i]
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        # print(data_s[i])
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            i += 1
            continue
        j = i + 1
        for j in range(row_number):
            x1_1, y1_1, x2_1, y2_1 = data_s[j]
            x1_1 = np.int0(x1_1)
            y1_1 = np.int0(y1_1)
            x2_1 = np.int0(x2_1)
            y2_1 = np.int0(y2_1)
            if x1_1 == 0 and x2_1 == 0 and y1_1 == 0 and y2_1 == 0:
                j += 1
                continue
            dif_x1 = abs(x1 - x1_1)
            dif_y1 = abs(y1 - y1_1)

            dif_x2 = abs(x2 - x2_1)
            dif_y2 = abs(y2 - y2_1)
            lenth_1 = abs(y1 - y2)
            lenth_2 = abs(y1_1 - y2_1)
            if 0 < dif_x1 < 10 and 0 < dif_x2 < 10:
                if lenth_1 >= lenth_2:
                    print(1)
                    if y1 >= y1_1 and y1 <= y2_1:
                        data_s[i] = [x1, y1_1, x2, y2]
                        y1 = y1_1
                        data_s[j] = [0, 0, 0, 0]
                    elif y2 <= y2_1 and y2 >= y1_1:
                        data_s[i] = [x1, y1, x2, y2_1]
                        y2 = y2_1
                        data_s[j] = [0, 0, 0, 0]
                    elif y1 >= y1_1 and y1 >= y2_1 and y1 - y2_1 <= 10:
                        data_s[i] = [x1, y1_1, x2, y2]
                        y1 = y1_1
                        data_s[j] = [0, 0, 0, 0]
                    elif y2 <= y1_1 and y1_1 - y2 <= 10:
                        data_s[i] = [x1, y1, x2, y2_1]
                        y2 = y2_1
                        data_s[j] = [0, 0, 0, 0]
                    elif y1 <= y1_1 and y2 >= y2_1:
                        data_s[j] = [0, 0, 0, 0]
                else:
                    if y1 <= y1_1 and y2 >= y1_1:
                        data_s[j] = [x1_1, y1, x2_1, y2_1]
                        data_s[i] = [0, 0, 0, 0]
                    elif y2 >= y2_1 and y1 <= y1_1:
                        data_s[j] = [x1_1, y1_1, x2_1, y2]
                        data_s[i] = [0, 0, 0, 0]
                    elif y1 >= y1_1 and y2 <= y2_1:
                        data_s[i] = [0, 0, 0, 0]
                    elif y2 <= y1_1 and y1_1 - y2 <= 10:
                        data_s[j] = [x1_1, y1, x2_1, y2_1]
                        data_s[i] = [0, 0, 0, 0]
                    elif y1 >= y2_1 and y1 - y2_1 <= 10:
                        data_s[j] = [x1_1, y1_1, x2_1, y2]
                        data_s[i] = [0, 0, 0, 0]

    data_s = np.unique(data_s, axis=0)  # 去除重复行

    print(data_s)
    for data in data_s:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            continue
        file = open('xianduan/data_nihe.txt', 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()
    data_s = np.loadtxt('xianduan/data_nihe.txt')
    data_s = data_s.astype(np.int64)
    for data in data_s:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv2.imencode('.jpg', img)[1].tofile("xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/完全拟合后.jpg")



