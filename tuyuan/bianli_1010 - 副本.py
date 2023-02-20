import os
import cv2
import numpy as np
from paddleocr import PaddleOCR ,draw_ocr
from tuyuan.mods import contours_2,getFileList,cir,salt


def bianli_func(img_type:str):
    area_1_x_start, area_1_x_end = 0, 0
    area_2_x_start, area_2_x_end = 0, 0
    area_3_x_start, area_3_x_end = 0, 0
    area_4_x_start, area_4_x_end = 0, 0
    area_5_x_start, area_5_x_end = 0, 0
    area_1_y_start, area_1_y_end = 0, 0
    area_2_y_start, area_2_y_end = 0, 0
    area_3_y_start, area_3_y_end = 0, 0
    area_4_y_start, area_4_y_end = 0, 0
    area_5_y_start, area_5_y_end = 0, 0

    if img_type == 'FD':
        area_1_x_start, area_1_x_end = 237, 663
        area_2_x_start, area_2_x_end = 668, 1184
        area_3_x_start, area_3_x_end = 1189, 3656
        area_4_x_start, area_4_x_end = 3661, 4155
        area_5_x_start, area_5_x_end = 4159, 4596
        area_1_y_start, area_1_y_end = 67, 2715
        area_2_y_start, area_2_y_end = 67, 2715
        area_3_y_start, area_3_y_end = 67, 2715
        area_4_y_start, area_4_y_end = 67, 2715
        area_5_y_start, area_5_y_end = 67, 2715
    elif img_type == 'SAMA':
        area_1_x_start, area_1_x_end = 237, 4596
        area_2_x_start, area_2_x_end = 237, 4596
        area_3_x_start, area_3_x_end = 237, 4596
        area_4_x_start, area_4_x_end = 237, 4596
        area_5_x_start, area_5_x_end = 237, 4596
        area_1_y_start, area_1_y_end = 67, 425
        area_2_y_start, area_2_y_end = 430, 2171
        area_3_y_start, area_3_y_end = 2176, 2534
        area_4_y_start, area_4_y_end = 2539, 2874
        area_5_y_start, area_5_y_end = 2539, 2874

    x_deviant_from_1_to_2 = area_2_x_start - area_1_x_start
    x_deviant_from_1_to_3 = area_3_x_start - area_1_x_start
    x_deviant_from_1_to_4 = area_4_x_start - area_1_x_start
    x_deviant_from_1_to_5 = area_5_x_start - area_1_x_start

    y_deviant_from_1_to_2 = area_2_y_start - area_1_y_start
    y_deviant_from_1_to_3 = area_3_y_start - area_1_y_start
    y_deviant_from_1_to_4 = area_4_y_start - area_1_y_start
    y_deviant_from_1_to_5 = area_5_y_start - area_1_y_start

    # 从 output_%d 开始
    count = 0
    filePath = f"./output_{img_type}"
    files = os.listdir(filePath)  # files:['output_0', 'output_1']
    files.sort()
    ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)

    # 从 output_<count> 开始
    for file in files:

        print('\033[34m开始处理图片: {} (从0开始)\033[0m'.format(count))
        if count < 10:
            org_img_folder = f'./output_{img_type}/output_0%d/area/' % count  # 当前图片所在路径（area文件夹内）
            org_img_folder_cb = f'./output_{img_type}/output_0%d/cir_con/' % count
            img_tmp_mark = cv2.imread(f"./output_{img_type}/output_0%d/img_mark.jpg" % count)  # 读取 img_mark.jpg，用于标记
            img_tmp_clean = cv2.imread(f"./output_{img_type}/output_0%d/img_clean.jpg" % count)  # 读取 img_clean.jpg，用于擦除
        else:
            org_img_folder = f'./output_{img_type}/output_%d/area/' % count  # 当前图片所在路径（area文件夹内）
            org_img_folder_cb = f'./output_{img_type}/output_%d/cir_con/' % count
            img_tmp_mark = cv2.imread(f"./output_{img_type}/output_%d/img_mark.jpg" % count)  # 读取 img_mark.jpg，用于标记
            img_tmp_clean = cv2.imread(f"./output_{img_type}/output_%d/img_clean.jpg" % count)  # 读取 img_clean.jpg，用于擦除


        # 检索文件，从./output/output_%d/area/检索，分别提取
        # ['./output/output_0/area/img_cut_1.jpg', ...]
        imglist = getFileList(org_img_folder, [], 'jpg')
        imglist.sort()
        imglist_cb = getFileList(org_img_folder_cb, [], 'jpg')
        imglist_cb.sort()
        # print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')

        if len(imglist) == 1:  # 这里应该不会到达
            count = count + 1
            continue

        img_number = 1  # 设置编号 img_number = 1

        # 依次处理 img_cut_1.jpg, img_cut_2.jpg, ...
        for imgpath in imglist:
            current_info = '图片: {}  区域: {}  '.format(count, img_number)
            if count < 10:
                out_path = f"./output_{img_type}/output_0%d/contours/" % count
            else:
                out_path = f"./output_{img_type}/output_%d/contours/" % count
            filed = "out"
            # 创建文件夹
            if not os.path.isdir(out_path):
                os.makedirs(out_path)
            imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取图片名 img_cut_1
            img = cv2.imread(imgpath)  # 读取 img_cut_1
            origin_img = cv2.imread(imgpath)  # 读取原始区域图片

            # 对该原始区域图片执行圆形检测
            circle = cir(img, count, imgpath, img_number, img_type,imgname, current_info, filed, img_tmp_mark, img_tmp_clean,
                         x_deviant_from_1_to_2, y_deviant_from_1_to_2, x_deviant_from_1_to_3, y_deviant_from_1_to_3,
                         x_deviant_from_1_to_4, y_deviant_from_1_to_4,
                         x_deviant_from_1_to_5, y_deviant_from_1_to_5)

            # 对该原始区域的矩形检测做准备
            gray = cv2.cvtColor(circle, cv2.COLOR_BGR2GRAY)  # 转换为灰度图片
            kernel_size = 5  # 二值化处理
            blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
            ret, binary = cv2.threshold(blur_gray, 22, 100, cv2.THRESH_BINARY)
            if count < 10:
                out_path_binary = f"./output_{img_type}/output_0%d/binary_" % count + str(imgname) + '.jpg'
            else:
                out_path_binary = f"./output_{img_type}/output_%d/binary_" % count + str(imgname) + '.jpg'

            cv2.imwrite(out_path_binary, binary)  # 保存二值化处理结果
            low_threshold = 20
            high_threshold = 100
            edges = cv2.Canny(binary, low_threshold, high_threshold)
            # define the Hough Transform parameters
            rho = 1  # distance resolution in pixels of the Hough grid
            theta = np.pi / 360  # angular resolution in radians of the Hough grid
            threshold = 25  # minimum number of votes (intersections in Hough grid cell)
            min_line_length = 35  # minimum number of pixels making up a line
            max_line_gap = 18  # maximum gap in pixels between connectable line segmentsc
            # make a blank the same size as the original image to draw on
            # line_image = cv2.imread("steam.png")
            line_image = np.copy(img) * 0
            # run Hough on edge detected image
            lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

            if lines is None:
                out_path_ALL_effect = out_path + 'effect/'
                if not os.path.isdir(out_path_ALL_effect):  # 创建文件夹
                    os.makedirs(out_path_ALL_effect)
                out_path_ALL_effect_1 = out_path_ALL_effect + filed[:-4] + str(
                    img_number) + "____img____effect____.jpg"  # 图像保存路径
                cv2.imwrite(out_path_ALL_effect_1, circle)
                img_number += 1
                # current_info = '图片: {}  区域: {}  '.format(count, img_number)
                continue

            # 此行所在循环：for imgpath in imglist（依次处理 img_cut_1.jpg, img_cut_2.jpg, ...）
            for line in lines:
                for x1, y1, x2, y2 in line:
                    a = abs(int(x1) - int(x2))
                    b = abs(int(y1) - int(y2))
                    if 1850 < int(x1) < 1900 and b > 300:
                        y2 = int(y2)+20
                    if 370 < int(x1) and int(x2) < 513 and 740 < int(y1) and int(y2) < 752:
                        x2 = int(x1) + 1
                    if 2077 < int(x1) and 2156 < int(x2) < 2191 and 1656 < int(y1) < 1675 and 1656 < int(y2) < 1675:
                        x2 = int(x2) + 100
                        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 5)
                    if 2077 < int(x1) and 2156 < int(x2) < 2191 and 1726 < int(y1) < 1740 and 1726 < int(y2) < 1740:
                        x2 = int(x2) + 170
                        x1 = int(x1) - 10
                        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 5)
                    else:
                        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 5)

            # draw the line on the original image
            lines_edges = cv2.addWeighted(line_image, 1, line_image, 1, 0)
            # cv2.imshow("lines_edges", lines_edges)
            if count < 10:
                out_path_binary = f"./output_{img_type}/output_0%d/line_edges_" % count + str(imgname) + '.jpg'
            else:
                out_path_binary = f"./output_{img_type}/output_%d/line_edges_" % count + str(imgname) + '.jpg'

            cv2.imwrite(out_path_binary, lines_edges)
            edges_1 = cv2.Canny(line_image, low_threshold, high_threshold)
            # 轮廓检测，contours 是 img_cut_1.jpg, img_cut_2.jpg, ... 的轮廓
            contours, hier = cv2.findContours(edges_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            rectangle_num = 0
            # 当前所在循环：for imgpath in imglist（依次处理 img_cut_1.jpg, img_cut_2.jpg, ... ）
            for c in contours:  # 遍历轮廓
                rect = cv2.minAreaRect(c)  # 生成最小外接矩形
                # print("个数", len(rect))
                box_ = cv2.boxPoints(rect)
                h = abs(box_[3, 1] - box_[1, 1])
                h_2 = h / 2
                w = abs(box_[3, 0] - box_[1, 0])
                w_2 = w / 2

                # 过大或过小的轮廓则跳过
                if (h > 10000 or w > 10000):
                    continue
                if (h < 40 or w < 40):
                    continue

                box = cv2.boxPoints(rect)  # 计算最小面积矩形的坐标
                box = np.int0(box)  # 将坐标规范化为整数

                cv2.drawContours(circle, [box], 0, (255, 255, 255), -1)
                x1, y1 = box[0]
                x2, y2 = box[1]
                x3, y3 = box[2]
                x4, y4 = box[3]
                x_min = np.min([x1, x2, x3, x4])
                y_min = np.min([y1, y2, y3, y4])
                x_max = np.max([x1, x2, x3, x4])
                y_max = np.max([y1, y2, y3, y4])
                x_min = np.int0(x_min)
                y_min = np.int0(y_min)
                x_max = np.int0(x_max)
                y_max = np.int0(y_max)
                a1, a2, a3 = rect
                a1 = np.int0(a1)
                c1 = (x_max + x_min) / 2
                c2 = (y_max + y_min) / 2
                img_cut = origin_img[y_min:y_max, x_min:x_max]  # 切片裁剪图像
                out_path_1 = out_path + "img_cut" + '/'

                if not os.path.isdir(out_path_1):  # 创建文件夹
                    os.makedirs(out_path_1)
                out_path_1 = out_path_1 + str(imgname) + '/'
                if not os.path.isdir(out_path_1):  # 创建文件夹
                    os.makedirs(out_path_1)

                h = np.int0(h)  # 矩形高度(纵向高度)
                w = np.int0(w)  # 矩形宽度(横向宽度)
                x_a1 = a1[0]
                y_a1 = a1[1]
                x_start = x_a1 - w_2  # 矩形左上角x坐标
                y_start = y_a1 - h_2  # 矩形左上角y坐标
                x_start = np.int0(x_start)
                y_start = np.int0(y_start)

                # 统一规定为矩形【左上角】的坐标
                x = x_start  # x = 矩形左上角x坐标
                y = y_start  # y = 矩形左上角y坐标

                if img_number == 1:
                    pass
                if img_number == 2:
                    x = x + x_deviant_from_1_to_2
                    y = y + y_deviant_from_1_to_2
                if img_number == 3:
                    x = x + x_deviant_from_1_to_3
                    y = y + y_deviant_from_1_to_3
                if img_number == 4:
                    x = x + x_deviant_from_1_to_4
                    y = y + y_deviant_from_1_to_4
                if img_number == 5:
                    x = x + x_deviant_from_1_to_5
                    y = y + y_deviant_from_1_to_5

                if img_number == 6:
                    if count < 10:
                        out_path_ALL_effect__2 = f'./output_{img_type}/output_0%d/contours/the_whole_parts_effect/' % count
                    else:
                        out_path_ALL_effect__2 = f'./output_{img_type}/output_%d/contours/the_whole_parts_effect/' % count
                    if not os.path.isdir(out_path_ALL_effect__2):  # 创建文件夹
                        os.makedirs(out_path_ALL_effect__2)
                    out_pathd = '{0}{1}centre({2}_{3}){4}_{5}.jpg'.format(out_path_1, filed[:-4], str(x), str(y),
                                                                          str(w), str(h))
                    try:
                        cv2.imwrite(out_pathd, img_cut)
                        contours_2(img_cut, img_number, x_start, y_start, count)
                    except:
                        print("None")

                if img_number != 6:
                    out_pathd = out_path_1 + filed[:-4] + str(x) + "_" + str(y) + "_" + str(w) + "_" + str(h) + ".jpg"
                    try:
                        cv2.imwrite(out_pathd, img_cut)
                        cv2.rectangle(img_tmp_mark, (x, y), (x + w, y + h), (255, 0, 0), 10)  # 在其上【标记】本次检测到的矩形
                        cv2.rectangle(img_tmp_clean, (x, y), (x + w + 7, y + h + 7), (255, 255, 255),
                                      -1)  # 在其上【擦除】本次检测到的矩形
                        rectangle_num = rectangle_num + 1
                        print(current_info + 'rectangle_{} [x: {}  y:{}  w:{}  h:{}]'.format(rectangle_num, x, y, w, h))
                        contours_2(img_cut, img_number, x_start, y_start, count)
                    except:
                        print(current_info + '\033[31mrectangle_{} (+1) Error\033[0m'.format(rectangle_num) + "")

            out_path_ALL_effect = out_path + 'effect/'
            if not os.path.isdir(out_path_ALL_effect):  # 创建文件夹
                os.makedirs(out_path_ALL_effect)
            if img_number < 6:
                out_path_ALL_effect_1 = out_path_ALL_effect + filed[:-4] + str(img_number) + "____img____effect____.jpg"
                cv2.imwrite(out_path_ALL_effect_1, circle)
            if img_number == 6:
                if count < 10:
                    out_path_ALL_effect__1 = f'./output_{img_type}/output_0%d/contours/the_whole_area_effect/' % count
                else:
                    out_path_ALL_effect__1 = f'./output_{img_type}/output_%d/contours/the_whole_area_effect/' % count
                if not os.path.isdir(out_path_ALL_effect__1):  # 创建文件夹
                    os.makedirs(out_path_ALL_effect__1)
                out_path_ALL_effect_1 = out_path_ALL_effect__1 + filed[:-4] + str(
                    img_number) + "____img____effect____.jpg"
                cv2.imwrite(out_path_ALL_effect_1, circle)

            # 前面已经将各个区域的处理结果到一张图片上
            # img_tmp_mark 是标记后的
            # img_tmp_clean 是擦除后的
            if count < 10:
                cv2.imwrite(f"./output_{img_type}/output_0%d/img_mark.jpg" % count, img_tmp_mark)  # 将【标记】完成后的图片重写保存至子目录
                cv2.imwrite(f"./output_{img_type}/output_0%d/img_clean.jpg" % count, img_tmp_clean)  # 将【擦除】完成后的图片重写保存至子目录
            else:
                cv2.imwrite(f"./output_{img_type}/output_%d/img_mark.jpg" % count, img_tmp_mark)  # 将【标记】完成后的图片重写保存至子目录
                cv2.imwrite(f"./output_{img_type}/output_%d/img_clean.jpg" % count, img_tmp_clean)  # 将【擦除】完成后的图片重写保存至子目录


            # 再保存一份到根目录
            img_tmp_mark_path = filePath + '/output_mark/'
            img_tmp_clean_path = filePath + '/output_clean/'
            if not os.path.isdir(img_tmp_mark_path):
                os.makedirs(img_tmp_mark_path)
            if not os.path.isdir(img_tmp_clean_path):
                os.makedirs(img_tmp_clean_path)
            
            cv2.imwrite(img_tmp_mark_path + "img_mark_%d.jpg" % count, img_tmp_mark)  # 将【标记】完成后的图片重写保存至根目录
            cv2.imwrite(img_tmp_clean_path + "img_clean_%d.jpg" % count, img_tmp_clean)  # 将【擦除】完成后的图片重写保存至根目录
            

            img_number += 1

            # 控制台输出
            # current_info = '图片: {}  区域: {}  '.format(count, img_number)
            if img_number < 6:
                if rectangle_num == 0:
                    print(current_info + "\033[31m未找到矩形, \033[0m" + "\033[32m共找到轮廓: {}\033[0m".format(len(contours)))
                else:
                    print(current_info + "\033[32m共找到矩形：{}, 共找到轮廓: {}\033[0m".format(rectangle_num, len(contours)))
        
        #对擦去矩形和圆形的图纸进行文本检测，将检测的文本擦掉并保存到line_clean文件夹中
        # img_line_clean = np.copy(img_tmp_clean)
        if not os.path.isdir( 'line_clean/'):
                os.makedirs('line_clean/')
        text = ocr.ocr(img_tmp_clean, cls=False)
        for i in text:
            print(text[0])
            size1 = i[0][0]
            size2 = i[0][2]
            x1 = int(size1[0])
            y1 = int(size1[1])
            x2 = int(size2[0])
            y2 = int(size2[1])
            cv2.rectangle(img_tmp_clean, (x1, y1), (x2, y2), (255, 255, 255), -1)
        cv2.imwrite('line_clean/' + file + '.jpg', img_tmp_clean)
        
        # print('---end--- count:{0}'.format(count))
        count = count + 1



def main():
    bianli_func('FD')
    # cut_func('output_FD')
    # os.system('python yolov5/detect.py --source yolov5/data/images/images_5.jpg --weights yolov5/pretrained/best.pt --savedir output/output_4/')
if __name__ == '__main__':
    main()