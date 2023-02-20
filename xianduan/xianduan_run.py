import glob
from math import sqrt

import cv2
import os
import numpy as np


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, "a")
    for i in range(len(data)):
        s = (
            str(data[i]).replace("[ ", "").replace("[", "").replace("]", "")
        )  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", "").replace(",", "") + "\n"  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

def xianduan_func(img_type:str):
    if img_type == 'FD':
        imgPath = "xianduan/xianduan/fd_circle_out/"
        files = glob.glob(imgPath + '/*.jpg')
        files.sort()
        print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
        for file in files:
            print(file)
            print(os.path.basename(file))
            img = cv2.imread(file)
            img0 = cv2.imread(file)
            imgname = os.path.splitext(os.path.basename(file))[0]
            print(imgname)
            origin_img = cv2.imread(file)
            try:
                circle_txt = np.loadtxt("xianduan/xianduan/circle_points/output/fd/CircleTxt/"+imgname+".txt", dtype=int)
                print(circle_txt)
            except:
                circle_txt = np.array([0, 0, 0])
            if circle_txt.ndim==1:
                circle_txt=circle_txt.reshape(1,3)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ## 创建一个LSD对象
            fld = cv2.ximgproc.createFastLineDetector()
            ### 执行检测结果
            lines = fld.detect(img)
            ### 绘制检测结果
            color = 100
            out_path = "xianduan/xianduan/xianduanjiance/fd_result/" + imgname + "/"
            if not os.path.isdir(out_path):  # 创建文件夹
                os.makedirs(out_path)
            print(lines)
            for dline in lines:
                x0 = int(round(dline[0][0]))
                y0 = int(round(dline[0][1]))
                x1 = int(round(dline[0][2]))
                y1 = int(round(dline[0][3]))
                # if (x0-x1)**2+(y0-y1)**2 < 400:
                #     continue
                cv2.line(img0, (x0, y0), (x1, y1), (0, 0, 255), 3)
                # print(x0, y0, x1, y1)
            cv2.imencode('.jpg', img0)[1].tofile(out_path + "初始检测后.jpg")
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # # 进行二值化处理
            # ret, binary = cv2.threshold(gray, 125, 200, cv2.THRESH_BINARY)  # 阈值函数
            # binary_med = cv2.medianBlur(binary, 1)  # 进行中式滤波
            # # cv2.imwrite("./xianduan/xianduanjiance/阈值分割后.jpg", binary)  # 保存进行阈值分割后的图像

            # cv2.imencode('.jpg', binary)[1].tofile(out_path + "yuzhi.jpg")
            # low_threshold = 80
            # high_threshold = 100
            # edges = cv2.Canny(binary_med, low_threshold, high_threshold)  # 中值滤波后进行边缘检测
            #
            # # cv2.imwrite("./xianduan/xianduanjiance/边缘检测后.jpg", edges)  # 边缘信息
            # cv2.imencode('.jpg', edges)[1].tofile(out_path + "边缘检测后.jpg")
            #
            # rho = 1  # distance resolution in pixels of the Hough grid
            # theta = np.pi / 360  # angular resolution in radians of the Hough grid
            # threshold = 25  # minimum number of votes (intersections in Hough grid cell)
            # min_line_length = 30  # minimum number of pixels making up a line
            # max_line_gap = 3  # maximum gap in pixels between connectable line segmentsc
            #
            # # make a blank the same size as the original image to draw on
            # # line_image = cv2.imread("steam.png")
            # line_image_1 = np.copy(img) * 0  # 复制相同的大小的图像 图像像素都为0
            # # run Hough on edge detected image
            # lines = cv2.HoughLinesP(
            #     edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap
            # )
            # print(lines)
            # for line in lines:
            #     for x1, y1, x2, y2 in line:
            #         cv2.line(line_image_1, (x1, y1), (x2, y2), (255, 255, 255), 1)
            #
            # # cv2.imshow("lines_edges", lines_edges)
            # # cv2.imwrite("./xianduan/xianduanjiance/霍夫变换后.jpg", line_image_1)
            # cv2.imencode('.jpg', line_image_1)[1].tofile(out_path + "霍夫变换后.jpg")
            cv2.imwrite(out_path + "yuzhi.jpg", origin_img)
            line_image = np.copy(origin_img) * 0
            print(len(lines))

            try:
                open("xianduan/information/data.txt", "w").close()
            except:
                print("None")

            text_save("xianduan/information/data.txt", lines)

            print(lines.dtype)

            for line in lines:
                x1, y1, x2, y2 = line[0]
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                loc = []
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 1)
                # print(type(x1))

            # cv2.imshow("lines_edges", lines_edges)
            cv2.imwrite(out_path + "all_lines.jpg", line_image)
            cv2.imencode('.jpg', line_image)[1].tofile(out_path + "所有线段.jpg")
            ###################################分离出竖直和水平的线段数据##########################

            data_s = np.loadtxt("xianduan/information/data.txt")

            data_s.astype(np.int64)

            data_s = data_s[np.lexsort(data_s[:, ::-1].T)]

            data_c = np.copy(data_s)

            shape_a = data_s.shape

            row_number = shape_a[0]

            line_number = shape_a[1]

            # print (data_s)

            open("xianduan/information/data_shuiping.txt", "w").close()
            open("xianduan/information/data_shuzhi.txt", "w").close()
            X_0 = 0
            X_2 = 0
            for data in data_s:
                x1, y1, x2, y2 = data
                x1 = np.int0(x1)
                y1 = np.int0(y1)
                x2 = np.int0(x2)
                y2 = np.int0(y2)
                # min_distance = 999
                # for data2 in circle_txt:
                #     circle_x, circle_y, circle_r = data2
                #     circle_x = int(circle_x)
                #     circle_y = int(circle_y)
                #     circle_r = int(circle_r)
                #     distance1 = sqrt((x2 - circle_x) ** 2 + (y2 - circle_y) ** 2)
                #     distance2 = sqrt((x1 - circle_x) ** 2 + (y1 - circle_y) ** 2)
                #     distance = min(distance1, distance2)
                #     if distance < min_distance:
                #         min_distance = distance
                # if min_distance <= 100 or sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) >= 30:
                if abs(x1 - x2) <= 3:
                    if y1 > y2:
                        temp_x = x1
                        temp_y = y1
                        x1 = x2
                        y1 = y2
                        x2 = temp_x
                        y2 = temp_y
                    distance_shuzhi = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                    if distance_shuzhi >= 30:
                        file = open("xianduan/information/data_shuzhi.txt", "a")
                        file.write(str(x1))
                        file.write(" ")
                        file.write(str(y1))
                        file.write(" ")
                        file.write(str(x2))
                        file.write(" ")
                        file.write(str(y2))
                        file.write("\n")
                        X_0 += 1
                        # continue


                elif abs(y1 - y2) <= 3:

                    if x1 > x2:
                        temp_x = x1
                        temp_y = y1
                        x1 = x2
                        y1 = y2
                        x2 = temp_x
                        y2 = temp_y
                    file = open("xianduan/information/data_shuiping.txt", "a")
                    file.write(str(x1))
                    file.write(" ")
                    file.write(str(y1))
                    file.write(" ")
                    file.write(str(x2))
                    file.write(" ")
                    file.write(str(y2))
                    file.write("\n")
                    X_0 += 1
                    # continue    
        
            # #####################对分离出的水平线段进行拟合降噪##########################
            os.system("python xianduan/new_noise_6.10.py %s %s" % (imgname, "fd"))
            # # os.system("python ./new_noise_6.10.py")
            os.system("python xianduan/shuzhi_noise.py %s %s" % (imgname, "fd"))
            # ######################将处理后的水平线段与竖直线段的数据汇总####################
            os.system("python xianduan/jiehe——6.10.py %s %s" % (imgname, "fd"))
            # #######################将数据进行排序####################
            os.system("python xianduan/jiehe_6.11.py")
            # #######################对比分析每一条线段的数据，如果两个线段是相连的，便拟合成一条直线##############
            os.system("python xianduan/data_shuiping.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/data_shuzhi.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/circle_nihe.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/circle_nihe2.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/circle_nihe3.py %s %s" % (imgname, "fd"))
            # os.system("python ./circle_nihe4.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/circle_nihe5.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/line_merge_main.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/data_zhenghe.py %s %s" % (imgname, "fd"))
            os.system("python xianduan/draw.py %s %s" % (imgname, "fd"))


    if img_type == 'SAMA':
        imgPath = "./xianduan/sama_circle_out/"
        files = glob.glob(imgPath + '/*.jpg')
        files.sort()
        print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
        for file in files:
            print(file)
            print(os.path.basename(file))
            img = cv2.imread(file)
            imgname = os.path.splitext(os.path.basename(file))[0]
            print(imgname)
            origin_img = cv2.imread(file)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 进行二值化处理
            ret, binary = cv2.threshold(gray, 125, 200, cv2.THRESH_BINARY)  # 阈值函数
            binary_med = cv2.medianBlur(binary, 1)  # 进行中式滤波
            # cv2.imwrite("./xianduan/xianduanjiance/阈值分割后.jpg", binary)  # 保存进行阈值分割后的图像
            out_path = "./xianduan/xianduanjiance/sama_result/" + imgname + "/"
            if not os.path.isdir(out_path):  # 创建文件夹
                os.makedirs(out_path)
            cv2.imencode('.jpg', binary)[1].tofile(out_path + "yuzhi.jpg")
            low_threshold = 80
            high_threshold = 100
            edges = cv2.Canny(binary_med, low_threshold, high_threshold)  # 中值滤波后进行边缘检测

            # cv2.imwrite("./xianduan/xianduanjiance/边缘检测后.jpg", edges)  # 边缘信息
            cv2.imencode('.jpg', edges)[1].tofile(out_path + "边缘检测后.jpg")

            rho = 1  # distance resolution in pixels of the Hough grid
            theta = np.pi / 360  # angular resolution in radians of the Hough grid
            threshold = 25  # minimum number of votes (intersections in Hough grid cell)
            min_line_length = 30  # minimum number of pixels making up a line
            max_line_gap = 3  # maximum gap in pixels between connectable line segmentsc

            # make a blank the same size as the original image to draw on
            # line_image = cv2.imread("steam.png")
            line_image_1 = np.copy(img) * 0  # 复制相同的大小的图像 图像像素都为0
            # run Hough on edge detected image
            lines = cv2.HoughLinesP(
                edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap
            )
            print(lines)
            for line in lines:
                for x1, y1, x2, y2 in line:
                    cv2.line(line_image_1, (x1, y1), (x2, y2), (255, 255, 255), 1)

            # cv2.imshow("lines_edges", lines_edges)
            cv2.imwrite("./xianduan/xianduanjiance/霍夫变换后.jpg", line_image_1)
            cv2.imencode('.jpg', line_image_1)[1].tofile(out_path + "霍夫变换后.jpg")
            line_image = np.copy(origin_img) * 0
            print(len(lines))

            try:
                open("data.txt", "w").close()
            except:
                print("None")

            text_save("data.txt", lines)

            print(lines.dtype)

            for line in lines:
                x1, y1, x2, y2 = line[0]
                loc = []
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 1)
                # print(type(x1))

            # cv2.imshow("lines_edges", lines_edges)
            cv2.imwrite(out_path + "all_lines.jpg", line_image)
            cv2.imencode('.jpg', line_image)[1].tofile(out_path + "所有线段.jpg")
            ###################################分离出竖直和水平的线段数据##########################

            data_s = np.loadtxt("data.txt")

            data_s.astype(np.int64)

            data_s = data_s[np.lexsort(data_s[:, ::-1].T)]

            data_c = np.copy(data_s)

            shape_a = data_s.shape

            row_number = shape_a[0]

            line_number = shape_a[1]

            # print (data_s)

            open("data_shuiping.txt", "w").close()
            open("data_shuzhi.txt", "w").close()
            X_0 = 0
            X_2 = 0
            for data in data_s:
                x1, y1, x2, y2 = data
                x1 = np.int0(x1)
                y1 = np.int0(y1)
                x2 = np.int0(x2)
                y2 = np.int0(y2)

                if abs(x1 - x2) < 3:
                    file = open("data_shuzhi.txt", "a")
                    file.write(str(x1))
                    file.write(" ")
                    file.write(str(y1))
                    file.write(" ")
                    file.write(str(x2))
                    file.write(" ")
                    file.write(str(y2))
                    file.write("\n")
                    X_0 += 1
                    continue

                else:
                    file = open("data_shuiping.txt", "a")
                    file.write(str(x1))
                    file.write(" ")
                    file.write(str(y1))
                    file.write(" ")
                    file.write(str(x2))
                    file.write(" ")
                    file.write(str(y2))
                    file.write("\n")
                    X_0 += 1
                    continue
            # #####################对分离出的水平线段进行拟合降噪##########################
            os.system("python ./new_noise_6.10.py %s %s" % (imgname, "sama"))
            # # os.system("python ./new_noise_6.10.py")
            os.system("python ./shuzhi_noise.py %s %s" % (imgname, "sama"))
            # ######################将处理后的水平线段与竖直线段的数据汇总####################
            os.system("python ./jiehe——6.10.py %s %s" % (imgname, "sama"))
            # #######################将数据进行排序####################
            os.system("python ./jiehe_6.11.py")
            # #######################对比分析每一条线段的数据，如果两个线段是相连的，便拟合成一条直线##############
            os.system("python ./data_shuiping.py %s %s" % (imgname, "sama"))
            os.system("python ./data_shuzhi.py %s %s" % (imgname, "sama"))
            os.system("python ./circle_nihe.py %s %s" % (imgname, "sama"))
            os.system("python ./circle_nihe2.py %s %s" % (imgname, "sama"))
            os.system("python ./circle_nihe3.py %s %s" % (imgname, "sama"))
            os.system("python ./circle_nihe4.py %s %s" % (imgname, "sama"))
            os.system("python ./circle_nihe5.py %s %s" % (imgname, "sama"))
            os.system("python ./line_merge_main.py %s %s" % (imgname, "sama"))
            os.system("python ./data_xianduan_nihe.py %s %s" % (imgname, "sama"))

# gray = cv2.cvtColor(line_image_1, cv2.COLOR_BGR2GRAY)
# # 进行二值化处理
# kernel = np.ones((4, 4), np.uint8)
# erosion = cv2.erode(gray, kernel)  # 腐蚀操作
# # cv2.imwrite("./xianduan/xianduanjiance/腐蚀操作后.jpg", erosion)
# cv2.imencode('.jpg', erosion)[1].tofile("./xianduan/xianduanjiance/腐蚀操作后.jpg")
#
# ret, binary = cv2.threshold(erosion, 120, 240, cv2.THRESH_BINARY)
#
# binary_2 = cv2.medianBlur(binary, 3)
# # cv2.imwrite("./xianduan/xianduanjiance/中值滤波后.jpg", binary_2)
# cv2.imencode('.jpg', binary_2)[1].tofile("./xianduan/xianduanjiance/中值滤波后.jpg")
# low_threshold = 80
#
# high_threshold = 100
# edges = cv2.Canny(binary_2, low_threshold, high_threshold)
#
# # cv2.imwrite("./xianduan/xianduanjiance/第二次边缘检测后.jpg", edges)
# cv2.imencode('.jpg', edges)[1].tofile("./xianduan/xianduanjiance/第二次边缘检测后.jpg")
# rho = 1  # distance resolution in pixels of the Hough grid
# theta = np.pi / 360  # angular resolution in radians of the Hough grid
# threshold = 25  # minimum number of votes (intersections in Hough grid cell)
# min_line_length = 35  # minimum number of pixels making up a line
# max_line_gap = 25  # maximum gap in pixels between connectable line segmentsc
#
# # make a blank the same size as the original image to draw on
# # line_image = cv2.imread("steam.png")
# line_image = np.copy(origin_img) * 0
# # run Hough on edge detected image
# lines = cv2.HoughLinesP(
#     edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap
# )

# c=1.5
# #####################对分离出的水平线段进行拟合降噪##########################
# os.system("python ./new_noise_6.10.py %f" % c)
# # os.system("python ./new_noise_6.10.py")
# os.system("python ./shuzhi_noise.py")
# ######################将处理后的水平线段与竖直线段的数据汇总####################
# # os.system("python ./jiehe——6.10.py")
# #######################将数据进行排序####################
# os.system("python ./jiehe_6.11.py")
# #######################对比分析每一条线段的数据，如果两个线段是相连的，便拟合成一条直线##############
# os.system("python ./data_shuiping.py")
# os.system("python ./data_shuzhi.py")
