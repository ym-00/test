# -*- coding: utf-8 -*-
import fitz
import shutil
import time
import os
import glob
import cv2
import sys
from multiprocessing import Pool, cpu_count
from paddleocr import PaddleOCR, draw_ocr


# fitz就是pip install PyMuPDF

def work_00(pg, pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath)
    page = pdfDoc[pg - 1]
    rotate = int(0)
    # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
    # 此处若是不做设置，默认图片大小为：792X612, dpi=96
    zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
    zoom_y = 4
    mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    rect = page.rect
    clip = fitz.Rect(rect.tl + 15, rect.br - 13)
    pix = page.get_pixmap(matrix=mat, alpha=False, clip=clip)
    if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
        os.makedirs(imagePath)  # 若图片文件夹不存在就创建
    pix.writePNG(imagePath + '/' + 'images_%s.jpg' % pg)  # 将图片写入指定的文件夹内


def work2(count, file):
    ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, show_log=False)
    k = 0
    print('正在处理第 {} 张图片'.format(count + 1))
    img = cv2.imread(file)
    print(img.shape)
    if img.shape[0] == 3254 or img.shape[0]==3256  and img.shape[1] ==4649 or img.shape[1]==4652:
        print('#########')
        img_cut_org = img[225:283, 1473:1783]
        # cv2.imshow("edge", img_cut_org)
        # cv2.imshow("111", img)
        # cv2.waitKey(0)
        result_1 = ocr.ocr(img_cut_org, cls=False)
        title_name = result_1[0][1][0]
        print(title_name)
        if 'NC' in title_name:
            k = 1
        if 'F-SC3' in title_name:
            k = 1
        if k == 1:
            print(k)
            outputPath = f"./input_FD"
            if not os.path.exists(outputPath):  # 判断存放图片的文件夹是否存在
                os.makedirs(outputPath)

            file1 = file.replace('./input\\', '')
            file2 = file1.replace('images_', '')
            file3 = file2.replace('.jpg', '')
            print(file3)

            shutil.copy(file, outputPath + f'/images_{file3}.jpg')
        else:
            print('筛选不到')
    else:
        print("不是要识别的图纸")


def err_call_back(err):
    print(f'{str(err)}')


def pyMuPDF_fitz(pdfPath, page_number):
    number = int(cpu_count() / 2)
    try:
        page_number = int(page_number)
    except:
        print("FREE")

    pool = Pool(processes=2)  # 子进程数
    # pdfPath = r"input.pdf"
    imagePath = "input"
    startTime_pdf2img = time.time()  # 开始时间
    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    if page_number == None:
        for pg in range(1, pdfDoc.page_count + 1):
            pool.apply_async(work_00, (pg, pdfPath, imagePath,), error_callback=err_call_back)
    else:
        for pg in range(1, pdfDoc.page_count + 1):
            if pg == page_number:
                pool.apply_async(work_00, (pg, pdfPath, imagePath,), error_callback=err_call_back)
        # func(pg,page)
    pool.close()
    pool.join()
    endTime_pdf2img = time.time()  # 结束时间
    print('pdf转图片已完成! pdf2img时间=', (endTime_pdf2img - startTime_pdf2img), 'seconds')


def shaixuan(paths: str):
    number = int(cpu_count() / 2)
    pool = Pool(processes=2)
    start = time.time()
    imgPath = paths  # ./input
    files = glob.glob(imgPath + '/*.jpg')
    print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
    count = 0  # 记录图纸的个数
    for file in files:
        # print(file)
        pool.apply_async(work2, (count, file,), error_callback=err_call_back)
        count = count + 1
    pool.close()
    pool.join()
    end = time.time()
    print("筛选已完成！   筛选时间为", end - start, "seconds")

# def pyMuPDF_fitz(pdfPath):
#     imagePath = "./input"
#     startTime_pdf2img = time.time()  # 开始时间
#     print("imagePath=" + imagePath)
#     pdfDoc = fitz.open(pdfPath)
#     for pg in range(pdfDoc.page_count):
#         page = pdfDoc[pg]
#         rotate = int(0)
#         # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
#         # 此处若是不做设置，默认图片大小为：792X612, dpi=96
#         zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
#         zoom_y = 4
#         mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
#         rect = page.rect
#         clip = fitz.Rect(rect.tl + 15, rect.br - 13)
#         pix = page.get_pixmap(matrix=mat, alpha=False, clip=clip)

#         if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
#             os.makedirs(imagePath)  # 若图片文件夹不存在就创建
#         if pg < 7:
#             continue

#         pix.save(imagePath + '/' + 'images_%s.jpg' % pg)  # 将图片写入指定的文件夹内


#     endTime_pdf2img = time.time()  # 结束时间
#     print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img),'seconds')


# def shaixuan(paths: str):
#     imgPath = paths  # ./input
#     files = glob.glob(imgPath + '/*.jpg')
#     print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
#     # for i in files:
#     #     name = os.path.basename(imgPath + i)
#     #     name = str(name)
#     #     name = name.replace('images_', '')
#     #     name = name.replace('.jpg', '')
#     #     src = os.path.join(os.path.abspath(''), i)
#     #     if len(name) == 1:
#     #         up_name = '0' + name
#     #         dst = os.path.join(os.path.abspath(imgPath + '/'), 'images_' + up_name + '.jpg')
#     #         os.rename(src, dst)

#     count = 0  # 记录图纸的个数
#     ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, show_log=False)

#     for file in files:
#         print(file)
#         k = 0
#         print('正在处理第 {} 张图片'.format(count + 1))
#         img = cv2.imread(file)
#         img_cut_org = img[225:283, 1473:1783]
#         # cv2.imshow("edge", img_cut_org)
#         # cv2.imshow("111", img)
#         # cv2.waitKey(0)
#         result_1 = ocr.ocr(img_cut_org, cls=False)
#         print(result_1)
#         title_name = result_1[0][1][0]
#         if 'NC' in title_name:
#             k = k + 1
#         if 'F-SC3' in title_name:
#             k = k + 1
#         if k == 0:
#             print(k)
#             continue

#         outputPath = f"./input_FD"
#         if not os.path.exists(outputPath):  # 判断存放图片的文件夹是否存在
#             os.makedirs(outputPath)

#         file1 = file.replace('./input/', '')
#         file2 = file1.replace('images_', '')
#         file3 = file2.replace('.jpg', '')
#         print(file3)

#         shutil.copy(file, outputPath+f'/images_{file3}.jpg')

#         count = count + 1


# if __name__ == "__main__":
#

