# -*- coding: utf-8 -*-
from multiprocessing import Pool
import fitz
import time
import os


def work(pg, pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath)
    page = pdfDoc[pg]
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

def err_call_back(err):
    print(f'{str(err)}')

def pyMuPDF_fitz():
    pool=Pool(processes=4)  #子进程数
    pdfPath = r"input.pdf"
    imagePath = "input"
    startTime_pdf2img = time.time()  # 开始时间
    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        if pg > 6:
            pool.apply_async(work,(pg,pdfPath,imagePath,),error_callback=err_call_back)
            # func(pg,page)
    pool.close()
    pool.join()
    endTime_pdf2img = time.time()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img) ,'seconds')




if __name__ == "__main__":
    pyMuPDF_fitz()

