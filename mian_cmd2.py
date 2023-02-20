# -*- coding: utf-8 -*-
import os
import sys
from tuyuan.cut_1010_pre import cut_func_pre
from tuyuan.cut_1010 import cut_func
from tuyuan.bianli_1010 import bianli_func
from importlib import reload
from tuyuan.ocr_shibie import *
from xianduan.line_clear import lineclear_func
from xianduan.CirclePoints import *
from xianduan.xianduan_run import *
from ocr_summary import *
from pipei_1119_final_0 import *
from tuyuan.mods import getFileList
from bbbjson import outjson
from tuyuan.ocr_tuinformation import getFileName_ocr
from tuyuan.det_logic_11_07 import txt_func, cut_logic
from logic_sort import zhenghe
from yolov5.detect import run
from delete import *
from pdf2image_11016 import *
from shaixuan import *


# coding=gbk
# -*- coding: utf-8 -*-
def main():
    if len(sys.argv) > 1:  # 如果命令行参数大于1
        method = sys.argv[1]  # method取第一个参数的值（除去脚本自身）
        method = method.upper()  # 统一

    if len(sys.argv) > 2:  # 如果命令行参数大于4
        pdf_path = sys.argv[2]  # pdf路径就是命令行的第四个参数（除去脚本自身）

    if method == 'FD' or method == 'SAMA':
        ocr_path = f'output_{method}'
        if method == 'FD':
            del_file(method)
            pyMuPDF_fitz()
            # shaixuan("./input")
            # # # # # #剪切图片
            # cut_func_pre(method,paths)
            # txt_func(f'output_{method}')
            # cut_logic(f'output_{method}')
            # cut_func(method, './path')
            # # # # # #检测元器件
            # bianli_func(method)
            # #ocr识别图片右下角信息
            # getFileName_ocr(method)
            # # ocr识别圆形
            # rec_circles(ocr_path)
            # # #ocr识别矩形

            # rec_contours(ocr_path)
            # # #整合一张图所有的元器件

            # ocr_Summary(ocr_path)
            # # #清除虚线
            # # lineclear_func(method)
            # # # # #擦除小圆点
            # # circle_point(method)
            # # # #线段检测
            # #xianduan_func(method)
            # # # # 整合逻辑门和元件
            # zhenghe()
            # 元件和线段匹配
            # pipei(method)
            # pipei2(method)
            #
            # pipei3(method)
            # pipei4(method)
            # # 输出json格式
            # outjson(paths, ocr_path,name)
        else:
            method == method
        if method == 'SAMA':
            del_file(method)
            cut_func(method, paths)
            # txt_func(f'output_{method}_2')
            # cut_func_2(f'output_{method}_2')
            # bianli_func(method)
            # getFileName_ocr(method)
            # rec_circles(ocr_path)
            # rec_contours(ocr_path)
            # ocr_Summary(ocr_path)
            # lineclear_func(method)
            # circle_point(method)
            # xianduan_func(method)
            # pipei(method)


        else:
            method == method

    else:
        print('Command not found')
        exit(-1)


# def cut_1010(img_type: str, path: str):
#     func(img_type, path)
#     # 有返回值的返回 没返回值的直接调用


if __name__ == "__main__":
    main()
