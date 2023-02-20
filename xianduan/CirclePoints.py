import math
import os

import cv2
import numpy as np
from tuyuan.mods import getFileList,salt


def cir(img,classfy,imgname,img_number,filed):
    out_path_0 = "xianduan/circle_points/output/"+classfy+"/"
    if not os.path.isdir(out_path_0):
        os.makedirs(out_path_0)

    out_path = out_path_0 + str(imgname) + '_circles/'
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    result_path=out_path_0 + str(imgname) + '_result/'
    if not os.path.isdir(result_path):
        os.makedirs(result_path)

    circle_out_path="xianduan/"+classfy+"_circle_out/"
    if not os.path.isdir(circle_out_path):
        os.makedirs(circle_out_path)
    # if not os.path.isdir("xianduan/circle_points/output/fd"):  # 创建文件夹
    #     os.makedirs("xianduan/circle_points/output/"+classfy+"/")
    conv_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, binary = cv2.threshold(gray, 31, 255, cv2.THRESH_BINARY)
    binary = cv2.erode(binary, conv_kernel)  # 膨胀

    low_threshold = 80
    high_threshold = 100
    edges = cv2.Canny(binary, low_threshold, high_threshold)
    cv2.imwrite(out_path_0 + str(imgname) + '_edges.jpg', edges)

    # cv2.imshow("img_cut", edges)
    # cv2.waitKey(0)

    black = np.copy(img) * 0

    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=15, minRadius=10, maxRadius=20)
    # print(circles)
    if circles is None:
        cv2.imwrite(circle_out_path + str(imgname) + '.jpg', img)
        return img
    circles = circles[0]
    print(circles)

    temporary_path="xianduan/circle_points/output/"+classfy+"/circles/"
    if not os.path.isdir(temporary_path):  # 创建文件夹
        os.makedirs(temporary_path)
    # 先将一张原图存储到circles目录下，以便后续在其上标记红圈
    cv2.imwrite(temporary_path+str(imgname)+'.jpg', img)


    print('-------------我是条分割线-----------------')
    s = 0
    if not os.path.isdir("./xianduan/circle_points/output/" + classfy + "/CircleTxt/"):  # 创建文件夹
        os.makedirs("./xianduan/circle_points/output/" + classfy + "/CircleTxt/")
    open("./xianduan/circle_points/output/" + classfy + "/CircleTxt/" + imgname + ".txt", "w").close()
    for circle in circles:
        # 圆的基本信息

        # 坐标行列(就是圆心)
        x = round(circle[0])
        print(x)
        y = round(circle[1])
        print(y)
        # 半径
        r = math.ceil(circle[2])
        print(r)
        file = open("./xianduan/circle_points/output/" + classfy + "/CircleTxt/" + imgname + ".txt", 'a')
        file.write(str(x))
        file.write(' ')
        file.write(str(y))
        file.write(' ')
        file.write(str(r))
        file.write('\n')
        file.close()
        # 在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
        # img_1 = cv2.circle(black, (x, y), r, (0, 0, 255), 2, 8, 0)

        # cv2.imshow("img1", img_1)
        # cv2.waitKey(0)
        x = round(circle[0])
        print(x)
        y = round(circle[1])
        print(y)
        # 半径
        r = math.ceil(circle[2])
        print(r)
        img_cut = img[int(y - r) : int(y + r) , int(x - r) : int(x + r)]

        # cv2.imshow("img_cut", img_cut)
        # cv2.waitKey(0)

        # img = cv2.circle(img, (x, y), r, (255, 255, 255), -1)
        # img = cv2.circle(img, (x, y), r, (255, 255, 255), 15, 10, 0)

        # cv2.imshow("img", img)
        # cv2.waitKey(0)

        # img_tmp1 = cv2.circle(img_tmp, (x, y), r, (0, 0, 255), 2, 8, 2)  # 在其上标记本次检测到的圆圈
        # img_02 = cv2.circle(img, (x, y), r + 15, (255, 255, 255), -1)


        # 将标记好的图片重新保存到文件

        if not os.path.isdir(out_path):  # 创建文件夹
            os.makedirs(out_path)
        if img_number == 1:
            deviant = 0
            x = x + deviant
            out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + "_" + str(r) + '_' + str(r) + ".jpg"  # 图像保存路径
        if img_number == 2:
            deviant = 450
            x = x + deviant
            out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + "_" + str(r) + '_' + str(r) + ".jpg"  # 图像保存路径
        if img_number == 3:
            deviant = 992
            x = x + deviant
            out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + "_" + str(r) + '_' + str(r) + ".jpg"  # 图像保存路径
        if img_number == 4:
            deviant = 3572
            x = x + deviant
            out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + "_" + str(r) + '_' + str(r) + ".jpg"  # 图像保存路径
        if img_number == 5:
            deviant = 4537
            x = x + deviant
            out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + "_" + str(r) + '_' + str(r) + ".jpg"  # 图像保存路径
        if img_number == 6:
            deviant = 0
            x = x + deviant
            out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + "_" + str(r) + '_' + str(r) + ".jpg"  # 图像保存路径
        cv2.imwrite(out_pathd, img_cut)
        s += 1
    img_tmp = cv2.imread(temporary_path+str(imgname)+'.jpg')  # 读取img_circle.jpg
    for circle in circles:
        # 圆的基本信息

        # 坐标行列(就是圆心)
        x = round(circle[0])
        print(x)
        y = round(circle[1])
        print(y)
        # 半径
        r = math.ceil(circle[2])
        print(r)
        img_tmp1 = cv2.circle(img_tmp, (x, y), r, (0, 0, 255), 2, 8, 0)  # 在其上标记本次检测到的圆圈
    if not os.path.isdir(result_path):  # 创建文件夹
        os.makedirs(result_path)
    cv2.imwrite(result_path+"img_circle_effect.jpg", img_tmp1)
    img_tmp = cv2.imread(temporary_path+str(imgname)+'.jpg')  # 读取img_circle.jpg
    for circle in circles:
        x = round(circle[0])
        print(x)
        y = round(circle[1])
        print(y)
        # 半径
        r = math.ceil(circle[2])
        print(r)
        result = cv2.circle(img_tmp, (x, y), r, (255, 255, 255), -1)  # 在其上标记本次检测到的圆圈
    cv2.imwrite(result_path+"img_circle_result.jpg", result)
    cv2.imwrite(circle_out_path + str(imgname) + '.jpg', result)
    return img

# org_img_folder = 'D:/project/module/line/FD_nodottedline'
#
# # 检索文件
# imglist = getFileList(org_img_folder, [], 'jpg')
# print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
# img_number = 1
# for imgpath in imglist:
#     out_path = "../xianduan/circle_points/output/"
#     filed = "out"
#     if not os.path.isdir(out_path):  # 创建文件夹
#         os.makedirs(out_path)
#     imgname = os.path.splitext(os.path.basename(imgpath))[0]
#     img = cv2.imread(imgpath)
#     origin_img = cv2.imread(imgpath)
#     circle = cir(img,"fd")


def circle_point(method):
    if method == 'FD':
        org_img_folder="../line/FD_nodottedline/"

        # 检索文件
        imglist = getFileList(org_img_folder, [], 'jpg')
        print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
        img_number = 1
        for imgpath in imglist:
            out_path = "xianduan/circle_points/output/"
            filed = "out"
            if not os.path.isdir(out_path):  # 创建文件夹
                os.makedirs(out_path)
            imgname = os.path.splitext(os.path.basename(imgpath))[0]
            img = cv2.imread(imgpath)
            origin_img = cv2.imread(imgpath)
            circle = cir(img, "fd" ,imgname,img_number,filed)

    if method == 'SAMA':
        org_img_folder='../line/SAMA_nodottedline/'

        # 检索文件
        imglist = getFileList(org_img_folder, [], 'jpg')
        print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
        img_number = 1
        for imgpath in imglist:
            out_path = "xianduan/circle_points/output/"
            filed = "out"
            if not os.path.isdir(out_path):  # 创建文件夹
                os.makedirs(out_path)
            imgname = os.path.splitext(os.path.basename(imgpath))[0]
            img = cv2.imread(imgpath)
            origin_img = cv2.imread(imgpath)
            circle = cir(img, "sama" ,imgname,img_number,filed)


if __name__ == "__main__":
    circle_point('FD')
    # circle_point('SAMA')

