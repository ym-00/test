import sys
import warnings
from math import sqrt

import numpy as np
import cv2

print("————————————————————————————以下是结合部分——————————————————————————————————")
imgname = sys.argv[1]
print(imgname)
classfy = sys.argv[2]
print(classfy)
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    data_s = np.loadtxt('xianduan/information/data_shuipingnihe.txt', dtype=int)
    data_s_1 = np.loadtxt('xianduan/information/data_shuzhinihe.txt', dtype=int)
    try:
        data_circle=np.loadtxt("xianduan/xianduan/circle_points/output/"+classfy+"/CircleTxt/"+imgname+".txt",dtype=int)
    except:
        data_circle=np.array([0,0,0])
        print("没有小圆点")

print(data_s_1)
print(data_circle)
if data_s.ndim==1:
    data_s=data_s.reshape(1,4)
if data_s_1.ndim==1:
    data_s_1=data_s_1.reshape(1,4)
if data_circle.ndim==1:
    data_circle=data_circle.reshape(1,3)
open("xianduan/information/data_jiehe_shuiping.txt", "w").close()
open("xianduan/information/data_jiehe_shuzhi.txt", "w").close()
data_s = data_s.astype(np.int64)
data_s_1 = data_s_1.astype(np.int64)
data_s = data_s[np.lexsort(data_s[:, ::-1].T)]
# data_s_1 = data_s_1[np.lexsort(data_s_1[:, ::-1].T)]
# data_s_1=data_s_1[np.lexsort(data_s_1[:,::-1].T)]
data_c = np.copy(data_s)

shape_a = data_s.shape

row_number = shape_a[0]

# line_number = shape_a[1]

img = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
image = np.copy(img)
image_1 = np.copy(img)
shuiping_length = len(data_s)
shuzhi_length = len(data_s_1)
# data_c = np.copy(data_s)
# data_v = np.copy(data_s_1)
X_0 = 0
for i in range(shuiping_length):
    x1, y1, x2, y2 = data_s[i]
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    Circle_flg=False
    for data in data_circle:
        circle_x,circle_y,circle_r=data
        circle_x = np.int0(circle_x)
        circle_y=np.int0(circle_y)
        circle_r=np.int0(circle_r)
        print("圆点坐标没问题")
        circle_distance1=sqrt((x1-circle_x)**2+(y1-circle_y)**2)
        circle_distance2=sqrt((x2-circle_x)**2+(y2-circle_y)**2)
        if circle_distance1<=30 or circle_distance2<=30:
            Circle_flg=True
    if Circle_flg==True:
        continue
    if Circle_flg==False:
        for j in range(i + 1, shuiping_length):
            x11, y11, x22, y22 = data_s[j]
            x11 = np.int0(x11)
            y11 = np.int0(y11)
            x22 = np.int0(x22)
            y22 = np.int0(y22)
            if abs(y1 - y11) <= 1 and abs(y2 - y22) <= 1:
                print("竖直坐标相同")
                if x2 < x11 and x11 - x2 <= 10:
                    data_s[i] = [x1, y1, x22, y22]
                    data_s[j] = [0, 0, 0, 0]
                    x2 = x22
                    y2 = y22
                if x1 > x22 and x1 - x22 <= 10:
                    data_s[i] = [x11, y11, x2, y2]
                    data_s[j] = [0, 0, 0, 0]
                    x1 = x11
                    y1 = y11


for i in range(shuzhi_length):
    print("竖直")
    print(data_s_1[i])
    x1, y1, x2, y2 = data_s_1[i]
    if y1 > y2:
        data_s_1[i] = [x2, y2, x1, y1]
print(data_s_1)
for i in range(shuzhi_length):
    x1, y1, x2, y2 = data_s_1[i]
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    Circle_flg = False
    for data in data_circle:
        circle_x, circle_y, circle_r = data
        circle_x = np.int0(circle_x)
        circle_y = np.int0(circle_y)
        circle_r = np.int0(circle_r)
        print("圆点坐标没问题")
        circle_distance1 = sqrt((x1 - circle_x) ** 2 + (y1 - circle_y) ** 2)
        circle_distance2 = sqrt((x2 - circle_x) ** 2 + (y2 - circle_y) ** 2)
        if circle_distance1 <= 30 or circle_distance2 <= 30:
            Circle_flg = True
    if Circle_flg == True:
        continue
    if Circle_flg == False:
        for j in range(i + 1, shuzhi_length):
            x11, y11, x22, y22 = data_s_1[j]
            x11 = np.int0(x11)
            y11 = np.int0(y11)
            x22 = np.int0(x22)
            y22 = np.int0(y22)
            if abs(x1 - x11) <= 1 and abs(x2 - x22) <= 1:
                print("水平坐标相同")
                if y2 < y11 and y11 - y2 <= 40:
                    data_s_1[i] = [x1, y1, x22, y22]
                    data_s_1[j] = [0, 0, 0, 0]
                    x2 = x22
                    y2 = y22
                if y1 > y22 and y1 - y22 <= 40:
                    data_s_1[i] = [x11, y11, x2, y2]
                    data_s_1[j] = [0, 0, 0, 0]
                    x1 = x11
                    y1 = y11

# for data in data_s:
#     x1, y1, x2, y2 = data
#     x1 = np.int0(x1)
#     y1 = np.int0(y1)
#     x2 = np.int0(x2)
#     y2 = np.int0(y2)
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
#         if y1 == y2 == y1_1 == y2_1:
#             if x1_1 - x2 > 0 and x1_1 - x2 <= 5:
#                 data_s[X_0] = [x1, y1, x2_1, y2_1]
#                 data_s[X_1] = [0, 0, 0, 0]
#             if x1 - x2_1 > 0 and x1 - x2_1 <= 5:
#                 data_s[X_0] = [x1_1, y1, x2, y2]
#                 data_s[X_1] = [0, 0, 0, 0]
#         X_1 += 1
#     X_0 += 1
# for i in range(len(data_s_1)):
#     x1, y1, x2, y2 = data_s_1[i]
#     x1 = np.int0(x1)
#     y1 = np.int0(y1)
#     x2 = np.int0(x2)
#     y2 = np.int0(y2)
#     if x1 == x2 and y1 > y2:
#         data_s_1[i] = [x2, y2, x1, y1]
# print(data_s_1)
# data_v = np.copy(data_s_1)
# X_0 = 0
# for data in data_s_1:
#     x1, y1, x2, y2 = data
#     x1 = np.int0(x1)
#     y1 = np.int0(y1)
#     x2 = np.int0(x2)
#     y2 = np.int0(y2)
#     X_1 = 0
#     for data_1 in data_v:
#         if X_0 > X_1 or X_0 == X_1:
#             X_1 += 1
#             continue
#         x1_1, y1_1, x2_1, y2_1 = data_1
#         x1_1 = np.int0(x1_1)
#         y1_1 = np.int0(y1_1)
#         x2_1 = np.int0(x2_1)
#         y2_1 = np.int0(y2_1)
#         if x1 == x2 == x1_1 == x2_1:
#             if y1_1 - y2 > 0 and y1_1 - y2 <= 20:
#                 data_s_1[X_0] = [x1, y1, x2, y2_1]
#                 y2 = y2_1
#                 data_s_1[X_1] = [0, 0, 0, 0]
#             if y1 - y2_1 > 0 and y1 - y2_1 <= 20:
#                 data_s_1[X_0] = [x1, y1_1, x2, y2]
#                 y1 = y1_1
#                 data_s_1[X_1] = [0, 0, 0, 0]
#         X_1 += 1
#     X_0 += 1
for data in data_s:
    x1, y1, x2, y2 = data
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        continue
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
    file = open('xianduan/information/data_jiehe_shuiping.txt', 'a')
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
    cv2.line(image_1, (x1, y1), (x2, y2), (0, 0, 255), 3)

    file = open('xianduan/information/data_jiehe_shuzhi.txt', 'a')
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
cv2.imencode('.jpg', image)[1].tofile("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/水平结合后.jpg")
# cv2.imwrite("./xianduan/xianduanjiance/lines_edges_1_jiehe2.jpg", image)
cv2.imencode('.jpg', image_1)[1].tofile("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/竖直结合后.jpg")
print("————————————————————————————线段结合部分结束——————————————————————————————————")
