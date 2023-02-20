from os import walk
import os
import pandas as pd
import cv2
import glob
import subprocess
'''
日期：2022-11-07
作用：调用yolo识别图片中逻辑的图元，将信息存储到对应文件下的logic.txt，并将对应的位置在图中涂白，保存图片为img_clean.jpg

调用方式：
    form 11_07.py import txt_func, cut_func
    txt_func('output_FD'):存放图元信息的跟文件夹
    cut_func('output_FD')：同上

'''
def getFileList(dir):
    """
    获取文件夹下的所以子目录
    输入 dir：文件夹根目录
    返回： 所有子目录
    root:当前目录路径，dirs：当前路径下所有子目录，files：当前路径下所有非目录子文件
    """
    Filelist = []
    for root, dirs, files in walk(dir):
        Filelist.append(dirs)

    return Filelist[0]
def txt_func(paths: str):
    result = getFileList(paths)
    result.sort()
    print(result)
    # for f in result:
    #     imgPath = paths + '/path/' + f + '.jpg'
    #     txtPath = paths + '/' + f
    #     print(imgPath)
    #     os.system('python yolov5/detect.py --source ' + imgPath + ' --weights yolov5/pretrained/best.pt --savedir ' + txtPath)
    subprocess.check_call('python yolov5/detect.py --source path/ --weights yolov5/pretrained/yolo221203.pt', shell=True)
    #print(imgPath)
def cut_logic(paths: str):
    result = getFileList(paths)
    result.sort()
    print(result)
    i = 0
    # if not os.path.exists('./input_FD_1/'):
    #     os.mkdir('input_FD_1/')
    for j in result:
        imgPath_1 = 'path/' + j + '.jpg'
        txtPath_1 = paths + '/' + j + '/all.txt'
        i = i + 1
        if os.path.getsize(txtPath_1) :
            df_0 = pd.read_csv(txtPath_1, sep='\s+', encoding='utf-8', header=None)
            len_0 = df_0.shape[0]
            number_12 = 0
            count = 0
            img_tmp_clean = cv2.imread(imgPath_1)
            for number_12 in range(len_0):
                data1 = df_0.loc[number_12]

                type_0, score, x1, y1, x2, y2 = data1
                filename = str(type_0) + '_' + str(x1) + '_' + str(y1) + '_' + str(x2) + '_' + str(y2)
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                path_file=paths + '/' +j +'/logic/'
                path_file_t = paths + '/' + j + '/triangle/'
                if not os.path.isdir(path_file):
                    os.makedirs(path_file)
                if not os.path.isdir(path_file_t):
                    os.makedirs(path_file_t)
                img_cut = img_tmp_clean[y1:y2, x1:x2]
                cv2.imwrite(path_file + filename + '.jpg', img_cut)
                # ----------2022-11-18新增------------------------------
                if str(type_0) == 'triangle':
                    if not os.path.isdir(path_file_t):
                        os.makedirs(path_file_t)
                    print('---------------------------------------------')
                    print(paths + '/' + j + '/triangle/' + filename + '.jpg')
                    cv2.imwrite(paths + '/' + j + '/triangle/' + filename + '.jpg', img_cut)
                # ----------2022-11-18新增------------------------------
                if str(type_0) == 'null_con':
                    cv2.rectangle(img_tmp_clean, (x1+10, y1), (x2, y2), (255, 255, 255), -1)
                elif str(type_0)=='SW':
                    cv2.rectangle(img_tmp_clean, (x1, y1), (x2-20, y2), (255, 255, 255), -1)
                else:
                    cv2.rectangle(img_tmp_clean, (x1, y1), (x2, y2), (255, 255, 255), -1)
            cv2.imwrite(imgPath_1, img_tmp_clean)
        else:
            img_tmp_clean = cv2.imread(imgPath_1)
            cv2.imwrite(imgPath_1, img_tmp_clean)

def main():
    txt_func('output_FD')
    cut_logic('output_FD')
    # os.system('python yolov5/detect.py --source yolov5/data/images/images_5.jpg --weights yolov5/pretrained/best.pt --savedir output/output_4/')
if __name__ == '__main__':
    main()