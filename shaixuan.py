# -*- coding: utf-8 -*-
import cv2
from paddleocr import PaddleOCR, draw_ocr
import glob
import shutil

def shaixuan(paths: str):
    imgPath = paths  # ./input
    files = glob.glob(imgPath + '/*.jpg')
    print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
    # for i in files_1:
    #     name = os.path.basename(imgPath + i)
    #     name = str(name)
    #     name = name.replace('images_', '')
    #     name = name.replace('.jpg', '')
    #     src = os.path.join(os.path.abspath(''), i)
    #     if len(name) == 1:
    #         up_name = '0' + name
    #         dst = os.path.join(os.path.abspath(imgPath + '/'), 'images_' + up_name + '.jpg')
    #         os.rename(src, dst)

    count = 0  # 记录图纸的个数
    ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, show_log=False)

    for file in files:
        print(file)
        k = 0
        print('正在处理第 {} 张图片'.format(count + 1))
        img = cv2.imread(file)
        img_cut_org = img[225:283, 1473:1783]
        # cv2.imshow("edge", img_cut_org)
        # cv2.imshow("111", img)
        # cv2.waitKey(0)
        result_1 = ocr.ocr(img_cut_org, cls=False)
        print(result_1)
        title_name = result_1[0][1][0]
        if 'NC' in title_name:
            k = k + 1
        if 'F-SC3' in title_name:
            k = k + 1
        if k == 0:
            print(k)
            continue

        outputPath = f"./input_FD"
        if not os.path.exists(outputPath):  # 判断存放图片的文件夹是否存在
            os.makedirs(outputPath)

        file1 = file.replace('./input/', '')
        file2 = file1.replace('images_', '')
        file3 = file2.replace('.jpg', '')
        print(file3)

        shutil.copy(file, outputPath+f'/images_{file3}.jpg')

        count = count + 1
