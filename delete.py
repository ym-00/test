# -*- coding: utf-8 -*-
import glob
import pandas as pd
import json
import numpy as np
import os

from pipei_1119_final_0 import getfilelist
from tuyuan.mods import getFileList
import sys
import shutil
def del_file(method):
    # for root, dirs, files in os.walk(f'output_{methon}/output_mark', topdown=False):
    #     for name in files:
    #         os.remove(os.path.join(root, name))
    #     for name in dirs:
    #         os.rmdir(os.path.join(root, name))
    # for root, dirs, files in os.walk(f'output_{methon}/output_clean', topdown=False):
    #     for name in files:
    #         os.remove(os.path.join(root, name))
    #     for name in dirs:
    #         os.rmdir(os.path.join(root, name))
    # name = ""
    # # Filelist = getfilelist(f'output_{methon}')
    # # for file in Filelist:
    # #     name = os.path.basename(file)
    # #     name = str(name)
    # #     name = name.replace('output_', '')
    # #     Filelists = getfilelist(f'output_{methon}/{file}')
    # #     for files in Filelists:
    # #         print(files)
    # #         if str(files).endswith(name):
    # #             print(files)
    # #             shutil.rmtree(os.path.join(f'output_{methon}/'+file, name))
    # #             break
    for root, dirs, files in os.walk("line", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("yolov5/runs/detect", topdown=False):
        print(files)
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
        print('Yolo file has been deleted. ')
    for root, dirs, files in os.walk("path", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("input_FD", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("input", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    for root, dirs, files in os.walk("output_info", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("xianduan/information", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk(f'xianduan/xianduan/xianduanjiance/fd_result', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("xianduan/xianduan/fd_circle_out", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("xianduan/xianduan/circle_points", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk('line_clean', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk(f'output_{method}/output_clean', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk(f'output_{method}/output_mark', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk(f'output_{method}', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
def main():
    del_file("FD")
if __name__ == '__main__':
    main()