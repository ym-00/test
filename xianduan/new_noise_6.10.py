import shutil
import sys

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
imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
shutil.copyfile("xianduan/information/data_shuiping.txt","xianduan/information/data_shuipingnihe.txt")
for m in range(15):
    img = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
    # cv2.namedWindow('demo', 0)
    # cv2.imshow('demo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    image = np.copy(img)

    data_s = np.loadtxt('xianduan/information/data_shuipingnihe.txt')

    data_s.astype(np.int64)
    print(data_s.ndim)
    try:
        data_s = data_s[np.lexsort(data_s[:, ::-1].T)]
    except Exception:
        print("坐标空白")
    print(data_s)

    data_c = np.copy(data_s)

    shape_a = data_s.shape

    row_number = shape_a[0]
    for i in range(row_number):
        x1, y1, x2, y2 = data_s[i]
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1>x2:
            data_s[i]=[x2,y2,x1,y1]
    # line_number = shape_a[1]

    # print (data_s)

    open("xianduan/information/data_shuipingnihe.txt", "w").close()
    for i in range(row_number):
        x1, y1, x2, y2 = data_s[i]
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        if x1 and x2 == 0:
            continue
        for j in range(i+1,row_number):
            x11, y11, x22, y22 = data_s[j]
            x11 = np.int0(x11)
            y11 = np.int0(y11)
            x22 = np.int0(x22)
            y22 = np.int0(y22)
            dif_x1 = abs(x1 - x11)
            dif_y1 = abs(y1 - y11)

            dif_x2 = abs(x2 - x22)
            dif_y2 = abs(y2 - y22)

            lenth_1 = abs(x1 - x2)
            lenth_2 = abs(x11 - x22)
            if dif_y1 < 10 and dif_y2 < 10:
                if lenth_1 >= lenth_2:
                    if x1 < x11 and x2 > x22:
                        data_s[j] = [0, 0, 0, 0]
                else:
                    if x1 > x11 and x2 < x22:
                        data_s[i] = [0, 0, 0, 0]
    # X_0 = 0
    # X_2 = 0
    # for data in data_s:
    #
    #     catch = 0
    #
    #     x1, y1, x2, y2 = data
    #     x1 = np.int0(x1)
    #     y1 = np.int0(y1)
    #     x2 = np.int0(x2)
    #     y2 = np.int0(y2)
    #
    #
    #     if x1 and x2 == 0:
    #         X_0 += 1
    #         continue
    #     X_1 = 0
    #     for data_1 in data_c:
    #
    #         if X_0 > X_1 or X_0 == X_1:
    #             X_1 += 1
    #             continue
    #
    #         x1_1, y1_1, x2_1, y2_1 = data_1
    #         x1_1 = np.int0(x1_1)
    #         y1_1 = np.int0(y1_1)
    #         x2_1 = np.int0(x2_1)
    #         y2_1 = np.int0(y2_1)
    #         #
    #         # if abs(x1_1 - x2_1) < 3:
    #         #     X_1 += 1
    #         #     continue
    #
    #         dif_x1 = abs(x1 - x1_1)
    #         dif_y1 = abs(y1 - y1_1)
    #
    #         dif_x2 = abs(x2 - x2_1)
    #         dif_y2 = abs(y2 - y2_1)
    #
    #         lenth_1 = abs(x1 - x2)
    #         lenth_2 = abs(x1_1 - x2_1)
    #
    #
    #         if dif_y1 < 10 and dif_y2 < 10:
    #             if lenth_1 >= lenth_2:
    #                 if x1 <= x1_1 and x2 >= x2_1:
    #                     data_s[X_1] = [0, 0, 0, 0]
    #             else:
    #                 if x1 >= x1_1 and x2 <= x2_1:
    #                     data_s[X_0] = [0, 0, 0, 0]
    #         #     if max(lenth_1, lenth_2) > max(dif_x1, dif_x2) or abs(max(lenth_1, lenth_2) - max(dif_x1, dif_x2)) < 40:
    #         #         print(x1, y1, x2, y2)
    #         #         print(X_1)
    #         #         data_s[X_1] = [0, 0, 0, 0]
    #         #         # X_2 += 1
    #         #         break
    #         X_1 += 1
    #         # if X_2 > 1:
    #         #     break
    #     X_0 += 1

    print(data_s)


    data_s = np.unique(data_s, axis=0) # 去除重复行
    for data in data_s:
        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        # if x1==0 and x2==0 and y1==0 and y2==0:
        #     continue
        file = open('xianduan/information/data_shuipingnihe.txt', 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write('\n')
        file.close()
    data_s = np.loadtxt('xianduan/information/data_shuipingnihe.txt')
    data_s.astype(np.int64)
    print(data_s)
    print(data_s.shape)


    # data_s=data_s.reshape(1,4)
    for data in data_s:

        x1, y1, x2, y2 = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)


        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
    # cv2.imwrite("./xianduan/xianduanjiance/lines_edges_1_noise.jpg", image)
    cv2.imencode('.jpg', image)[1].tofile("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/水平降噪后.jpg")

        # print("xxxx",dif_x1,dif_x2)
