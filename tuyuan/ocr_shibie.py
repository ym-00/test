import numpy as np
import cv2
import os
from paddleocr import PaddleOCR ,draw_ocr
from os import walk
'''

    22-11-16日新增或修改单个矩形识别方法，将矩形坐标由左上角换为中心坐标，并手动实现多个cd或dc分层
    
    22-11-18新增方法path_triangle_create() 用于对三角文件进行处理
'''
cope_file = []
List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'C', 'I']
#圆形切片识别，识别信息将保存在对应文件夹下的label文件中
def rec_circles(path):
    Filelist =getFileList(path)
    Filelist.sort()
    print(Filelist)
    for i in Filelist:
        path1 = path + '/' + i
        for j in range(1,6):
            path_circles = path1 + '/circles/img_cut_' + str(j) + '_circles'
            if not os.path.isdir(path_circles):
                # print(path_circles + "不存在")
                print()
            else:
                create_descriptors(path_circles)
                print("已完成对" +path_circles + "文件夹的识别" )
#矩形文件识别
def rec_contours(path):
    Filelist =getFileList(path)
    Filelist.sort()
    print(Filelist)
    # print(Filelist)
    for i in Filelist:
        path1 = path + '/' + i
        for j in range(1,6):
            path_contours = path1 + '/contours/img_cut/img_cut_' + str(j)
            if not os.path.isdir(path_contours):
                # print(path_contours + "不存在")
                print()
            else:
                contours_2(path_contours)
                create_descriptors_contours(path_contours)
                print("已完成对" + path_contours + "文件夹的识别")
        path_triangle = path1 +'/triangle'
        if not os.path.isdir(path_triangle):
            # print(path_contours + "不存在")
            print(path_triangle +"不存在")
        else:
            path_triangle_create(path_triangle, path1)
def path_triangle_create(path, path1):
    files = []
    ocr_t = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
    files.sort()
    for f in files:
        if '.jpg' not in f:
            # print(f)
            continue
        else:
            img = cv2.imread(path + "/" +f)
            text = ocr_t.ocr(img, cls=False)
            result = text
            file_name = ''
            for i in range(0,len(result)):
                if '\\' in result[i][1][0]:
                    print()
                else:
                    file_name += result[i][1][0] + '_'
            file_name = file_name[:-1]
            if file_name == '':
                file_name = 'null'
            if 'YCAM009KA' in file_name:
                file_name = file_name + '_Y'
            if '/' in file_name:
                file_name =file_name.replace('/','')
            if not os.path.isdir(path1 + '/contours/img_cut/img_cut_6/label/'):
                os.makedirs(path1 + '/contours/img_cut/img_cut_6/label/')
            Note = open(path1 + '/contours/img_cut/img_cut_6/label/' + 'triangle_' + file_name + '_' + f[9:-4] + '.txt', mode='w')
            titile_ocr(Note)
            site = f[:-4].split('_')
            print(site)
            x1 = int(site[1])
            y1 = int(site[2])
            x2 = int(site[3])
            y2 = int(site[4])
            x = int((x1 + x2)/2)
            y = int((y1 + y2)/2)
            w = x2 - x1
            h = y2 - y1
            Note.write('triangle ' + file_name + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + ' ' + f[9:-4])

def create_descriptors(folder):
    # rec_model_dir='../out/rec/en_PP-OCRv3_rec_infer/',det_model_dir='../out/det/db_mv3_5_infer/',
    ocr_c = PaddleOCR(det_model_dir='../out/det/db_mv3_5_infer/', use_angle_cls=False, use_gpu=False, lang='en', show_log=False)
    files = []
    # Note = open(folder[0:12] + 'rec.txt', mode='a')
    for (dirpath, dirnames, filenames) in walk(folder):
        files.extend(filenames)
    files.sort()
    for f in files:
        if '.jpg' not in f:
            # print(f)
            continue
        else:
            img = cv2.imread(folder + "/" +f)
            img_1 = cv2.resize(img,(90,90))
            # cv2.imshow("111",img_1)
            # cv2.waitKey(0)
            img_2 = img_1[0:90,5:88]
            # cv2.imshow("111", img_2)
            # cv2.waitKey(0)
            text = ocr_c.ocr(img_2, cls=False)
            result = text
            file_name = ''

            for i in range(0,len(result)):
                if '\\' in result[i][1][0]:
                    print()
                else:
                    file_name += result[i][1][0]
                    # file_name = result[i][1][0] + '_' + f[:-4]

                    # Note = open(folder + '/label/' + file_name + '.txt', mode='w')
                    # Note.write(result[i][1][0] + ' ' + f[:-4])
            if file_name == '' or file_name == '1' or file_name == '7':
                a = Template_Match(img_2)
                file_name = str(a)
                # if a == '7':
                #     file_name = 'C'
                if file_name == '':
                    file_name = 'null'
            if '/' in file_name:
                file_name = file_name.replace('/', '')
            if ' ' in file_name:
                file_name = file_name.replace(' ', '')
            if file_name == '01':
                file_name = 'QI'
            if not os.path.isdir(folder + '/label'):
                os.makedirs(folder + '/label')
            Note = open(folder + '/label/' + 'circles_' + file_name + '_' + f[:-4] + '.txt', mode='w')
            titile_ocr(Note)
            site = f[:-4].split('_')
            print(site)

            Note.write('circles ' + file_name + ' ' + site[0] + ' ' + site[1] + ' ' + site[2] + ' ' + site[2] + ' ' + f[:-4])

def titile_ocr(Note):
    Note.write('type')
    Note.write(' ')
    Note.write('name')
    Note.write(' ')
    Note.write('x')
    Note.write(' ')
    Note.write('y')
    Note.write(' ')
    Note.write('w')
    Note.write(' ')
    Note.write('h')
    Note.write(' ')
    Note.write('main')
    Note.write('\n')

def create_descriptors_contours(folder):
    ocr_con = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)
    files = []
    # Note = open(folder[0:12] + 'rec.txt', mode='a')
    for (dirpath, dirnames, filenames) in walk(folder):
        files.extend(filenames)
    files.sort()
    print(files)
    for f in files:
        if '.jpg' not in f:
            # print(f)
            continue
        elif f in cope_file:
            continue
        else:
            img = cv2.imread(folder + "/" + f)
            text = ocr_con.ocr(img, cls=False)
            result = text
            file_name = ''

            for i in range(0, len(result)):
                if '\\' in result[i][1][0]:
                    print()
                else:
                    file_name += result[i][1][0]
                    # file_name = result[i][1][0] + '_' + f[:-4]

                    # Note = open(folder + '/label/' + file_name + '.txt', mode='w')
                    # Note.write(result[i][1][0] + ' ' + f[:-4])
            if not os.path.isdir(folder + '/label'):
                os.makedirs(folder + '/label')
            if file_name == '': # 如果识别字符为空则对其进行旋转进行识别
                img_ro = rotate_bound(img,90)
                text = ocr_con.ocr(img_ro, cls=False)
                result = text
                for i in range(0, len(result)):
                    if '\\' in result[i][1][0]:
                        print()
                    else:
                        file_name += result[i][1][0]
            if len(file_name) == 0:
                file_name = 'null'
            if ' ' in file_name:
                file_name = file_name.replace(' ', '_')
            if '/' in file_name:
                file_name = file_name.replace('/', '')# 因字符中存在'/'会导致创建txt文件失败，故先删去，以后有其他想法再进行更换。
            site = f[:-4].split('_')
            if int(site[1]) < 100:
                continue
            #以下内容为11-16日新增或修改，将矩形坐标由左上角换为中心坐标，并手动实现多个cd或dc分层
            k = 0
            x = int(site[0])
            y = int(site[1])
            w = int(site[2])
            h = int(site[3])
            x_c = int(x + w/2)
            y_c = int(y + h/2)

            if file_name == 'CDCD' or file_name =='DCDC':
                k = k+1
                file_name = file_name[:2]
            if file_name == 'DCDCDC' or file_name =='CDCDCD':
                k = k + 2
                file_name = file_name[:2]
            if file_name == 'SR':
                k = k + 3
            Note = open(folder + '/label/' + 'contours_' + file_name + '_' + f[:-4] + '.txt', mode='w')
            titile_ocr(Note)

            print(file_name + "是小矩形")
            if k == 0:
                Note.write('contour ' + file_name + ' ' + str(x_c) + ' ' + str(y_c) + ' ' + str(w) + ' ' + str(h) + ' ' + f[:-4])
            elif k == 1:
                y_c_1 = int(y_c - h/4)
                y_c_2 = int(y_c + h/4)
                h_1 = int(h/2)
                Note.write('contour ' + file_name + ' ' + str(x_c) + ' ' + str(y_c_1) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])
                Note.write('\n')
                Note.write('contour ' + file_name + ' ' + str(x_c) + ' ' + str(y_c_2) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])
            elif k == 2:
                y_c_1 = int(y + h/6)
                y_c_2 = int(y_c_1 * 3)
                y_c_3 = int(y_c_1 * 5)
                h_1 = int(h/3)
                Note.write('contour ' + file_name + ' ' + str(x_c) + ' ' + str(y_c_1) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])
                Note.write('\n')
                Note.write('contour ' + file_name + ' ' + str(x_c) + ' ' + str(y_c_2) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])
                Note.write('\n')
                Note.write('contour ' + file_name + ' ' + str(x_c) + ' ' + str(y_c_3) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])
            elif k == 3:
                y_c_1 = int(y_c - h/4)
                y_c_2 = int(y_c + h/4)
                h_1 = int(h/2)
                Note.write('contour ' + 'S' + ' ' + str(x_c) + ' ' + str(y_c_1) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])
                Note.write('\n')
                Note.write('contour ' + 'R' + ' ' + str(x_c) + ' ' + str(y_c_2) + ' ' + str(w) + ' ' + str(h_1) + ' ' + f[:-4])

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def getFileList(dir):
    """
    获取文件夹下的所以子目录
    输入 dir：文件夹根目录
    返回： 所有子目录
    root:当前目录路径，dirs：当前路径下所有子目录，files：当前路径下所有非目录子文件
    """
    Filelist = []
    for root, dirs, files in os.walk(dir):
        Filelist.append(dirs)

    return Filelist[0]

def main():
    print("ocr_10_12文本的识别功能的基本方法库")
    # rec_circles('output_FD/')
    rec_contours('output_FD/')
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
        print("去燥完成")
        return img

def contours_2(path):
    files = []
    ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
    
    files.sort()
    print(files)
    for f in files:
        print(f)
        if '.jpg' not in f:
            # print(f)
            continue
        else:
            list1 = f[:-4].split('_')
            x_o = int(list1[0])
            y_o = int(list1[1])
            h_o = int(list1[2])
            w_o = int(list1[3])
            # x_start = x_o - h_o/2
            # y_start = y_o - w_o/2
            x_start = x_o
            y_start = y_o
            img =cv2.imread(path + '/' + f)
            t = img.shape
            h = img.shape[0]
            w = img.shape[1]

            if img is None:
                continue
            origin_img = img
            img_mask = img.copy()
            # result = ocr.ocr(img_mask, cls=False)
            # # print(result)
            print(f)
            # for i in range(0,len(result)):
            #     # print(result[i][0][0][1])
            #     x_1 = int(result[i][0][0][1])
            #     x_2 = int(result[i][0][2][1])
            #     y_1 = int(result[i][0][0][0])
            #     y_2 = int(result[i][0][2][0])
            #     img_mask[x_1-2:x_2-1,y_1:y_2] = 255
            gray = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)


            # 进行二值化处理
            kernel_size = 5
            blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
            # cv2.imshow("edges_2221", img_mask)
            # cv2.waitKey(0)
            ret, binary = cv2.threshold(blur_gray, 23, 240, cv2.THRESH_BINARY)
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
                # return img
                continue
            for line in lines:
                for x1, y1, x2, y2 in line:
                    cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 9)

            edges_1 = cv2.Canny(line_image, low_threshold, high_threshold)



            # edges_2 = cv2.dilate(edges_1, (15, 15))  # 膨胀
            # edges_3 = cv2.erode(edges_2, (15, 15))  # 膨胀
            edges_4 = cv2.morphologyEx(edges_1, cv2.MORPH_CLOSE, (15, 15))
            #此处为2022-11-21日修改内容
            #edges_4 = edges_4[3:h - 3, 0:w]
            # cv2.imshow("edges_1", edges_4)
            # cv2.waitKey(0)
            contours, hier = cv2.findContours(edges_4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours is None:
                return img
            print("数量", len(contours))
            contour_num_valid = 0
            if len(contours) < 3:
                # create_descriptors_contours(path)
                continue
            else:
                list_all = []
                for c in contours:  # 遍历轮廓
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
                    if (h < 0 or w < 0):
                        continue
                    contour_num_valid += 1  # 统计出当前有效轮廓数量

                cout_i = 0
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
                        if (h < 10 or w < 10):
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
                        x_a2 = int(x_a2)
                        y_a2 = int(y_a2)
                        if y_min < 6:
                            y_min = 6
                        img_cut = origin_img[y_min - 5:y_max + 5, x_min:x_max + 10]  # 切片裁剪图像
                        out_path_1 = path + '/a/'
                        result1 = ocr.ocr(img_cut, cls=False)
                        file_name1 = ''
                        for i in range(0, len(result1)):
                            if '\\' in result1[i][1][0]:
                                print()
                            else:
                                file_name1 += result1[i][1][0]
                        if file_name1 == '':
                            img_ro = rotate_bound(img_cut,90)
                            result1_ro = ocr.ocr(img_ro, cls=False)
                            for i in range(0, len(result1_ro)):
                                if '\\' in result1_ro[i][1][0]:
                                    print()
                                else:
                                    file_name1 += result1_ro[i][1][0]
                        if file_name1 == '':
                            file_name1 = 'null'
                        list_cut = [str(cout_i), str(x_a2) + '_' + str(y_a2) + '_' + str(w) + '_' + str(h), file_name1]
                        # list_cut[0] = str(i)
                        # list_cut[1] = str(x_a2) + '/' + str(y_a2) + '/' + str(w) + '/' + str(h)
                        # list_cut[2] = file_name1
                        file_name1.replace(' ', '_')
                        list_all.append(list_cut)
                        cout_i = cout_i + 1
                        # if not os.path.isdir(out_path_1):  # 创建文件夹
                        #     os.makedirs(out_path_1)
                        # out_pathd = "{0}{1}_{2}_{3}_{4}.jpg".format(out_path_1, str(x_a2), str(y_a2), str(w),str(h))
                        # cv2.imwrite(out_pathd, img_cut)

                        contour_num_valid = 0
                # a = list_all.reverse()
                # print(a)
                for i in list_all:
                    if int(i[0]) == int(len(list_all) - 1):
                        if ' ' in i[2]:
                            i[2] = i[2].replace(' ', '_')
                        if '/' in i[2]:
                            i[2] = i[2].replace('/','')
                        if not os.path.isdir(path + '/label/'):
                            os.makedirs(path + '/label/')
                        Note = open(path + '/label/' + 'contour_' + i[2] + '_' + i[1] + '.txt', mode='w')
                        titile_ocr(Note)
                        # Note.write(file_name + ' ' + f[:-4])
                list_all.reverse()
                for j in list_all:
                    site = j[1]
                    list_site = site.split('_')
                    str_site = list_site[0] + ' ' + list_site[1] + ' ' + list_site[2] + ' ' +list_site[3] + ' ' + f[:-4]
                    if ' ' in j[2]:
                        name = j[2].replace(' ', '_')
                    else:
                        name = j[2]
                    Note.write('contour ' + name + ' ' + str_site + '\n')
                cope_file.append(f)


def Template_Match(image):
    # 单文件夹内的最佳得分
    best_score = []
    for i in range(11):
        # 单个图片的得分
        score = []
        ForderPath = 'Template/' + List[i]
        # 遍历单文件夹（每一个文件匹配）
        for filename in os.listdir(ForderPath):
            # 路径
            path = 'Template/' + List[i] + '/' + filename
            # 模板
            template = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)  # 彩（类似imread）
            gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)  # 灰
            ret, template = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  # 二值
            h, w = template.shape
            image = cv2.resize(image, (w, h))

            # 模板匹配，得到得分（匹配度越高，得分越大）
            template1 = cv2.cvtColor(template,cv2.COLOR_BGR2RGB)
            result = cv2.matchTemplate(image, template1, cv2.TM_CCOEFF)
            score.append(result[0][0])  # 得分（每张模板图）

        # 一个文件夹的最高得分（得分越高，匹配度越高）
        best_score.append(max(score))
        # 根据所有文件夹的最佳得分确定下标
        index = best_score.index(max(best_score))
    return List[index]


if __name__=='__main__':
    main()