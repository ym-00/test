#!/usr/bin/env python3
# -*- coding: utf-8 -*-
_author_ = '张起凡'
import glob
import os
import cv2


#imgPath = "./output_SAMA/output_clean"
#这份代码的路径都是绝对路径。。。

def lineclear_func(img_type:str):

    if img_type == 'FD':
        if not os.path.exists('line/FD_nodottedline/'):
            os.mkdir('line/FD_nodottedline/')
        files = glob.glob('line_clean\*.jpg')
        print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
        for file in files:
            print(file)
            print(os.path.basename(file))
            pic = cv2.imread(file)
            cv2.line(pic, (428, 0), (428, 2648), (255, 255, 255), 3)
            cv2.line(pic, (949, 0), (949, 2648), (255, 255, 255), 3)
            cv2.line(pic, (3422, 0), (3422, 2648), (255, 255, 255), 3)
            cv2.line(pic, (3920, 0), (3920, 2648), (255, 255, 255), 3)
            cv2.line(pic, (0, 132), (4358, 132), (255, 255, 255), 3)
            cv2.rectangle(pic, (0, 0), (4358, 221), (255, 255, 255), -1);
            cv2.imwrite('line/FD_nodottedline/' + os.path.basename(file), pic)

    if img_type == 'SAMA':

        files = glob.glob(r'D:\project\module\output_SAMA\output_clean\*.jpg')
        print("\033[32m共检索到图片数量：{}\033[0m".format(len(files)))
        for file in files:
            print(file)
            print(os.path.basename(file))
            pic = cv2.imread(file)
            # cv2.line(pic, (428, 0), (428, 2648), (255, 255, 255), 3)
            # cv2.line(pic, (949, 0), (949, 2648), (255, 255, 255), 3)
            # cv2.line(pic, (3422, 0), (3422, 2648), (255, 255, 255), 3)
            # cv2.line(pic, (3920, 0), (3920, 2648), (255, 255, 255), 3)
            cv2.line(pic, (0, 359), (4361, 359), (255, 255, 255), 3)
            cv2.line(pic, (0, 2106), (4361, 2106), (255, 255, 255), 3)
            cv2.line(pic, (0, 2468), (4361, 2468), (255, 255, 255), 3)
            cv2.rectangle(pic, (0, 0), (670, 2646), (255, 255, 255), -1);
            cv2.imwrite('D:/project/module/line/SAMA_nodottedline/' + os.path.basename(file), pic)
