import glob
import os
import cv2
import numpy as np

def contours_2(img, img_number,img_type, x_start, y_start, count, file):
    filePath = f"./output_{img_type}"
    # if count < 10:
    #     out_path = filePath + f"/output_0%d/contours/" % count
    # else:
    #     out_path = filePath + f"/output_%d/contours/" % count
    out_path = filePath + f"/" + file + "/contours/"
    filed = "out"
    origin_img = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 进行二值化处理
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
    ret, binary = cv2.threshold(blur_gray, 138, 240, cv2.THRESH_BINARY)
    # cv2.imwrite("./output/output_%d/A1.jpg" % count, binary)
    low_threshold = 80
    high_threshold = 100
    edges = cv2.Canny(binary, low_threshold, high_threshold)

    # define the Hough Transform parameters
    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 360  # angular resolution in radians of the Hough grid
    threshold = 30  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 25  # minimum number of pixels making up a line
    max_line_gap = 13  # maximum gap in pixels between connectable line segmentsc

    # make a blank the same size as the original image to draw on
    # line_image = cv2.imread("steam.png")
    line_image = np.copy(img) * 0
    # run Hough on edge detected image
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    if lines is None:
        return img

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 9)

    edges_1 = cv2.Canny(line_image, low_threshold, high_threshold)
    contours, hier = cv2.findContours(edges_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours is None:
        return img
    # print("数量", len(contours))
    contour_num_valid = 0
    for c in contours:  # 遍历轮廓
        print('1----------------------------------')
        rect = cv2.minAreaRect(c)  # 生成最小外接矩形
        box_ = cv2.boxPoints(rect)
        h = abs(box_[3, 1] - box_[1, 1])
        h_2 = h / 2
        h_2 = np.int0(h_2)
        w = abs(box_[3, 0] - box_[1, 0])
        w_2 = w / 2
        w_2 = np.int0(w_2)
        # 只保留需要的轮廓
        if (h > 2000 or w > 2000):
            continue
        if (h < 40 or w < 40):
            continue
        contour_num_valid += 1  # 统计出当前有效轮廓数量
        if contour_num_valid > 2:
            for c in contours:  # 遍历轮廓
                rect = cv2.minAreaRect(c)  # 生成最小外接矩形
                # print("个数", len(rect))
                box_ = cv2.boxPoints(rect)
                h = abs(box_[3, 1] - box_[1, 1])
                w = abs(box_[3, 0] - box_[1, 0])
                # 只保留需要的轮廓
                if (h > 4000 or w > 4000):
                    continue
                if (h < 40 or w < 40):
                    continue
                box = cv2.boxPoints(rect)  # 计算最小面积矩形的坐标
                box = np.int0(box)  # 将坐标规范化为整数
                a1, a2, a3 = rect
                a1 = np.int0(a1)
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
                if y_min < 0:
                    continue
                # print(x_max, y_max, x_min, y_min)
                h = np.int0(h)
                w = np.int0(w)
                # print("宽，高", w, h)
                # print("坐标", a1)
                x_a2 = a1[0]
                y_a2 = a1[1]
                x_a2 = x_a2 + x_start
                y_a2 = y_a2 + y_start
                img_cut = origin_img[y_min:y_max, x_min:x_max + 10]  # 切片裁剪图像
                out_path_1 = out_path + str(img_number) + '/'
                if not os.path.isdir(out_path_1):  # 创建文件夹
                    os.makedirs(out_path_1)
                out_pathd = "{0}{1}{2}_{3}_{4}_{5}.jpg".format(out_path_1, filed[:-4], str(x_a2), str(y_a2), str(w), str(h))
                cv2.imwrite(out_pathd, img_cut)
                contour_num_valid = 0


def cir(img, count, imgpath, img_number, img_type,imgname, current_info, filed, img_tmp_mark, img_tmp_clean,
                         x_deviant_from_1_to_2, y_deviant_from_1_to_2, x_deviant_from_1_to_3, y_deviant_from_1_to_3,
                         x_deviant_from_1_to_4, y_deviant_from_1_to_4,
                         x_deviant_from_1_to_5, y_deviant_from_1_to_5, file):
    filePath = f"./output_{img_type}"
    out_path_0 = filePath + f"/" + file + "/circles/"
    out_path = out_path_0 +  str(imgname) + '_circles/'
    if not os.path.isdir(filePath + "/" + file + "/circles/"):  # 创建文件夹
        os.makedirs(filePath + f"/" + file + "/circles/")

    conv_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    cir_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cir_gray = cv2.GaussianBlur(cir_gray, (5, 5), 0)
    ret, binary = cv2.threshold(cir_gray, 31, 255, cv2.THRESH_BINARY)
    binary = cv2.erode(binary, conv_kernel)  # 膨胀
    low_threshold = 80
    high_threshold = 100
    edges = cv2.Canny(binary, low_threshold, high_threshold)
    cv2.imwrite(out_path_0 + str(imgname) + '_edges.jpg', edges)
    black = np.copy(img) * 0
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=45, minRadius=17, maxRadius=60)
    img_cut_name = os.path.splitext(os.path.basename(imgpath))[0]  # 获取图片名 img_cut_1

    if img_number == 6:
        print(current_info + "当前正在处理未切割的第6区域，控制台信息已省略")

    # 如果未发现圆形，则返回
    if circles is None:
        print(current_info + "\033[31m未找到圆形 ({}.jpg)\033[0m".format(img_cut_name))
        return img

    # 如果发现圆形，则继续
    circle_num = 1

    for circle in circles[0]:
        x = int(circle[0])  # 圆心坐标（x，行）
        y = int(circle[1])  # 圆心坐标（y，列）
        r = int(circle[2])  # 圆半径长度

        if img_number != 6:
            print(current_info + "circle_{} [r: {}  x: {}  y: {}]".format(circle_num, r, x, y))

        img_circle_cut = img[y - r:y + r, x - r:x + r]  # 对圆所在位置进行裁剪，图片赋值给 img_circle_cut

        if not os.path.isdir(out_path):  # 创建文件夹
            os.makedirs(out_path)
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
            pass

        out_pathd = out_path + filed[:-4] + str(x) + "_" + str(y) + '_' + str(r) + ".jpg"  # 图像保存路径
        cv2.imwrite(out_pathd, img_circle_cut)
        cv2.circle(img_tmp_mark, (x, y), r, (0, 0, 255), 5)  # 在其上【标记】本次检测到的圆圈
        cv2.circle(img_tmp_clean, (x, y), r + 8, (255, 255, 255), -1)  # 在其上【擦除】本次检测到的圆圈

        circle_num = circle_num + 1
    print(current_info + "\033[32m共找到圆形: {}\033[0m".format(circle_num-1))
    return img


def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


def salt(img, n):
    # 椒盐去燥
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
        return img

def cv_imwrite(filename,src):
    cv2.imencode('.jpg',src)[1].tofile(filename)