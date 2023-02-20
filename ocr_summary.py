import json
from os import walk, path
import pandas as pd
import os
import json
from ocr.ocr_name_10_11 import getFileName
import os
from PIL import Image
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


'''
更新记录：
    （1）对10.22py文件的修改本
        主要在第75-80行加入了一个新的方法，使单元器件和多元器件用空行隔开存储，改变属性名称为belong，该字段存的是元器件的位置信息用于溯源时使用
    （2）
        date：2020-10-18
        将每张图整理好的txt文件转为json文件并进行规范化，并在信息中添加文件名称，更新代码从133行开始
        
     2022-11-04 新增对img_clean图纸直接识别功能，并将文字信息保存到label/img_clean.txt文件
     对文件进行遍历，如果外部文字和图形的距离小于阈值T则将文字信息添加到元件的属性中,控制阈值t的代码在第281行。
    2022-11-17 更新： 添加了null_con_mthod方法，此方法用于生成null_con类型的数据，并将其保存在汇总文件中
'''

#总的运行函数 用于文本信息整合
def ocr_Summary(path):
    result = getFileList(path) #获取对应图片的文件夹根目录
    result.sort()
    print(result)

    k = 0
    for f in result:
        # if "22" not in f:
        #     continue
        if not os.path.isdir(path +'/'+ f + '/label'):
            os.makedirs(path +'/'+ f + '/label')
        # 11月四日更新内存 ------ 先对每张图片直接进行文字识别 并将信息保存到label中
        img_clean(path +'/'+ f)
        # 保存元器件name，x,y,w,h,mian的txt
        vpath = path + '/'+f + '/label/' + f + '.json'
        Note = open(path +'/'+ f + '/label/' + f + '_o.txt', mode='w')
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
        Note.write(' ')
        Note.write('out') #11月4日新增
        Note.write('\n')

        Location = open(path + '/'+f + '/label/' + f + '_l.txt', mode='w')
        # Location.write('type')
        # Location.write(' ')
        Location.write('name')
        Location.write(' ')
        Location.write('x0 y0')
        Location.write(' ')
        Location.write('x1 y1')
        Location.write(' ')
        Location.write('x2 y2')
        Location.write(' ')
        Location.write('x3 y3')
        Location.write(' ')
        Location.write('belong')
        Location.write('\n')
        file_path_1 = path +'/'+ f + '/'
        for j in range(1, 6):
            files = []
            path_contours = file_path_1 + '/circles/img_cut_' + str(j) + '_circles'
            if not os.path.isdir(path_contours):
                # print(path_contours + "不存在")
                print()
            else:
                for (dirpath, dirnames, filenames) in walk(path_contours):
                    files.extend(filenames)
                for j in files:
                    if '.txt' in j:
                        ocr_sum_mothd(path_contours + '/label/' + j, Note, Location, [], vpath ,file_path_1)
                    else:
                        continue
        List_c = []
        for k in range(1, 7):
            files = []

            path_contours_c = file_path_1 + '/contours/img_cut/img_cut_' + str(k)
            if not os.path.isdir(path_contours_c):
                # print(path_contours + "不存在")
                print()
            else:
                for (dirpath, dirnames, filenames) in walk(path_contours_c):
                    files.extend(filenames)
                files.sort()
                for j in files:
                    print(j)
                    if '.txt' in j:
                        ocr_sum_mothd(path_contours_c + '/label/' + j, Note, Location, List_c, vpath,file_path_1)
                        if 'PUMP' in j and os.path.getsize(file_path_1 + 'null_con.txt'):
                            null_con_mothd(path_contours_c + '/label/' + j, Note, Location)
                        if 'PNEUM' in j and os.path.getsize(file_path_1 + 'null_con.txt'):
                            null_con_mothd(path_contours_c + '/label/' + j, Note, Location)
                        if 'MOTOR' in j and os.path.getsize(file_path_1 + 'null_con.txt'):
                            null_con_mothd(path_contours_c + '/label/' + j, Note, Location)
                    else:
                        continue
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write(' ')
        Note.write('End')
        Note.write('\n')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write(' ')
        Location.write('End')
        Location.write('\n')
        if len(List_c) == 0:
            continue
        else:
            ocr_sum_muti(Note, Location, List_c, vpath)
        Note.close()
        Location.close()
        '''
        date：2020-10-18
        将每张图整理好的txt文件转为json文件并进行规范化，并添加文件名称
        '''
        root = path + '/'+f + '/label/' + f
        df_path = root + '_l.txt'
        df_json = pd.read_csv(df_path, sep='\s+', encoding='utf-8')
        ak = pd.DataFrame(df_json)
        vjosn = ak.to_json(path_or_buf=root + '_l.json', orient='records')
        with open(root + '_l.json', 'r') as write_r:
            load_dict = json.load(write_r)
        with open(root + '_l.json', 'w') as write_f:
            write_f.write(json.dumps([{'file_name': f, 'data': d} for d in load_dict], indent=4, ensure_ascii=False))

        df_path_o = root + '_o.txt'
        df_json_o = pd.read_csv(df_path_o, sep='\s+', encoding='utf-8')
        ak_o = pd.DataFrame(df_json_o)
        vjosn_o = ak_o.to_json(path_or_buf=root + '_o.json', orient='records')
        with open(root + '_o.json', 'r') as write_r_o:
            load_dict_o = json.load(write_r_o)
        with open(root + '_o.json', 'w') as write_f_o:
            write_f_o.write(json.dumps([{'file_name': f, 'data': d} for d in load_dict_o], indent=4, ensure_ascii=False))

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


def ocr_sum_muti(Note, Location, List, vpath):
    for i in List:
        df_1 = pd.read_csv(i, sep='\s+', encoding='utf-8')
        len_0 = df_1.shape[0]
        number_12 = 0
        number_22 = 0
        for number_12 in range(len_0):
            data1 = df_1.loc[number_12]
            type_0, name_0, x_0, y_0, w_0, h_0, main_0 = data1
            Note.write(str(type_0))
            Note.write(' ')
            Note.write(str(name_0))
            Note.write(' ')
            Note.write(str(x_0))
            Note.write(' ')
            Note.write(str(y_0))
            Note.write(' ')
            Note.write(str(w_0))
            Note.write(' ')
            Note.write(str(h_0))
            Note.write(' ')
            Note.write(str(main_0))
            Note.write(' ')
            Note.write('null')
            Note.write('\n')
        for number_22 in range(len_0):
            data1 = df_1.loc[number_22]
            if number_22 == 0:
                name_main = data1[1]
            type_0, name_0, x_0, y_0, w_0, h_0, main_0 = data1
            x1 = x_0 - w_0 / 2
            y1 = y_0

            x2 = x_0
            y2 = y_0 - h_0 / 2

            x3 = x_0 + w_0 / 2
            y3 = y_0

            x4 = x_0
            y4 = y_0 + h_0 / 2

            Location.write(str(name_0))
            Location.write(' ')
            Location.write(str(x1) + ' ' + str(y1))
            Location.write(' ')
            Location.write(str(x2) + ' ' + str(y2))
            Location.write(' ')
            Location.write(str(x3) + ' ' + str(y3))
            Location.write(' ')
            Location.write(str(x4) + ' ' + str(y4))
            Location.write(' ')
            Location.write(str(name_main))
            # Location.write(' ')
            # Location.write(str(main_0))
            Location.write('\n')
#此方法用于生成null_con类型的数据
def null_con_mothd(file, Note, Location):
    df_1 = pd.read_csv(file, sep='\s+', encoding='utf-8')
    len_0 = df_1.shape[0]
    number_12 = 0
    number_22 = 0
    new_name = ''
    list_null = []
    x_1 = '111'
    w_1 = 0
    h_1 = 0
    list_null_1 = []
    for number_12 in range(len_0):
        data1 = df_1.loc[number_12]
        print(data1)
        type_0, name_0, x_0, y_0, w_0, h_0, main_0 = data1
        print(name_0)
        list_null_1.append(name_0)
        if number_12 == 0:
            main_name = name_0
        if 'MODE' in str(name_0):  # 找到第一个连接null_con的矩形
            new_name = str(name_0)
            x_1 = str(x_0)
            list_null.append(y_0)
            w_1 = w_0
            h_1 = h_0
            main_1 = main_0
            print(str(name_0) + ' 123456789')
            continue
        if str(x_0) == x_1:
            new_name = new_name + '--' + str(name_0)
            list_null.append(y_0)
    print(list_null)
    if list_null[0] is None:
        print("11")
    else:
        y_1 = list_null[0]
        y_2 = list_null[-1]
        w_final = w_1 + 28
        h_final = y_2 - y_1 + h_1
        x_final = int(x_1) + 14
        y_final = int((y_2 + y_1) / 2)
        x0 = x_final - w_final / 2
        y0 = y_final - h_final / 2
        x1 = x_final + w_final / 2
        y1 = y_final - h_final / 2
        x2 = x_final + w_final / 2
        y2 = y_final + h_final / 2
        x3 = x_final - w_final / 2
        y3 = y_final + h_final / 2
        # 在label_o中加入null_con的信息
        new_name='new_con_'+str(new_name)
        Note.write('null_con')
        Note.write(' ')
        Note.write(str(new_name))
        Note.write(' ')
        Note.write(str(x_final))
        Note.write(' ')
        Note.write(str(y_final))
        Note.write(' ')
        Note.write(str(w_final))
        Note.write(' ')
        Note.write(str(h_final))
        Note.write(' ')
        Note.write(str(main_1))
        Note.write(' ')
        Note.write('null')
        Note.write('\n')
        # 在label_l中加入null_con的信息
        Location.write(str(new_name))
        Location.write(' ')
        Location.write(str(x0) + ' ' + str(y0))
        Location.write(' ')
        Location.write(str(x1) + ' ' + str(y1))
        Location.write(' ')
        Location.write(str(x2) + ' ' + str(y2))
        Location.write(' ')
        Location.write(str(x3) + ' ' + str(y3))
        Location.write(' ')
        Location.write(main_name)
        # Location.write(' ')
        # Location.write(str(main_0))
        Location.write('\n')
def ocr_sum_mothd(file, Note, Location, List, vpath, path):
    df_0 = pd.read_csv(file, sep='\s+', encoding='utf-8')
    # ak = pd.DataFrame(df_0)
    # vjosn = ak.to_json(path_or_buf=vpath,orient='records')
    column_0 = df_0.shape[1]
    len_0 = df_0.shape[0]
    # try:
    #     open(file, "w").close()
    # except:
    #     print('None')
    print(df_0)
    number_12 = 0
    number_22 = 0
    print(len_0)

    if len_0 > 1:
        List.append(file)
        print(Note)
        # List1 =str(Note)
        # list2 = List1.split(' ')
        # file_name = list2[1]
        # file_name_1 = file_name[6:-1]

    else:
        print()
        name_new = 'null'
        for number_12 in range(len_0):
            print(number_12)
            print('zheli')
            data1 = df_0.loc[number_12]
            # if number_12 == 0:
            #     name_o = data1[1]
            type_0, name_0, x_0, y_0, w_0, h_0, main_0 = data1
            # x_0_c = int(x_0) + int(w_0)/2
            # y_0_c = int(y_0) + int(h_0)/2
            if os.path.exists(path + '/label/img_clean.txt'):
                print('--------------------------------------------------------------------------')

                text_clean = pd.read_csv(path + '/label/img_clean.txt', sep='\s+', encoding='utf-8')
                len_clean = text_clean.shape[0]
                dis_o = 1100
                j = 0
                for i in range(len_clean):
                    data_clean = text_clean.loc[i]
                    name_1, x_1, y_1 = data_clean
                    if name_0 == 'End':
                        continue
                    import math
                    a1 = float(x_0) - float(x_1)
                    a2 = float(y_0) - float(y_1)
                    dis = math.sqrt(a1 ** 2 + a2 ** 2)

                    if dis < 110:
                        if dis_o < dis:
                            continue
                        if y_1 > y_0:
                            continue
                        # if j == 0:
                        name_new = name_1
                        # else:
                        #     name_new = name_new + '_' + name_1
                        dis_o = dis
                        print(name_new)
                        j = j + 1
            name_new=str(name_new)
            
            if 'SH' in name_new and '_' not in name_new and 'RRPF' not in name_new:
                name_new = name_new[:-1] + '_' + name_new[-1:]
            if 'SH' in name_new and '.' not in name_new and 'RRPF' not in name_new and 'VFLF' not in name_new and 'SAMA' not in name_new and 'IRMF' not in name_new:
                name_new = name_new[:2] + '.' + name_new[2:]
            #以下为11-26日新增内容*******************
            name_new = str(name_new)
            if '[' in name_new:
                name_new = name_new.replace('[', 'I')
            if '*' in name_new:
                name_new = name_new.replace('*', 'I')
            if '_ICAM' in name_new:
                name_new = name_new.replace('_ICAM', '_YCAM')
            if '_CAM' in name_new:
                name_new = name_new.replace('_CAM', '_YCAM')
            if '_AM' in name_new:
                name_new = name_new.replace('_AM', '_YCAM')
            # if 'YCAM' in name_new and 'IIC' not in name_new:
            #     name_new = 'IIC_' + name_new

            if '0DD' in name_new:
                name_new = name_new.replace('0DD', 'ODD')
            if 'DDI_' in name_new:
                name_new = name_new.replace('DDI_', 'DD_')
            if 'IIC_IC_' in name_new:
                name_new = name_new.replace('IIC_IC_', 'IIC_')
            if 'TO_' in name_new:
                name_new = name_new.replace('TO_', 'TQ')
            if '_1_' in name_new:
                name_new = name_new.replace('_1_', '_')
            if '_I_' in name_new:
                name_new = name_new.replace('_I_', '_')
            if 'Q_Y' in name_new:
                name_new = name_new.replace('Q_Y', 'QY')
            #*********************************************************
            
            Note.write(str(type_0))
            Note.write(' ')
            Note.write(str(name_0))
            Note.write(' ')
            Note.write(str(x_0))
            Note.write(' ')
            Note.write(str(y_0))
            Note.write(' ')
            Note.write(str(w_0))
            Note.write(' ')
            Note.write(str(h_0))
            Note.write(' ')
            Note.write(str(main_0))
            Note.write(' ')
            Note.write(str(name_new))
            Note.write('\n')
        # 以下代码是新增-10-24
        for number_22 in range(len_0):
            data1 = df_0.loc[number_22]
            if number_12 == 0:
                name_o = data1[1]
            type_0, name_0, x_0, y_0, w_0, h_0, main_0 = data1
            x1 = x_0 - w_0 / 2
            y1 = y_0

            x2 = x_0
            y2 = y_0 - h_0 / 2

            x3 = x_0 + w_0 / 2
            y3 = y_0

            x4 = x_0
            y4 = y_0 + h_0 / 2

            # Location.write(str(type_0))
            # Location.write(' ')
            if str(type_0) == 'circles':
                name_0 = 'circles_'+str(name_0)
            Location.write(str(name_0))
            Location.write(' ')
            Location.write(str(x1) + ' ' + str(y1))
            Location.write(' ')
            Location.write(str(x2) + ' ' + str(y2))
            Location.write(' ')
            Location.write(str(x3) + ' ' + str(y3))
            Location.write(' ')
            Location.write(str(x4) + ' ' + str(y4))
            Location.write(' ')
            Location.write(str(name_o))
            # Location.write(' ')
            # Location.write(str(main_0))
            Location.write('\n')


def main():
    ocr_Summary('output_FD')

from paddleocr import PaddleOCR ,draw_ocr
import cv2

#此方法11-26日更新，可直接替换
def img_clean(path):
    if os.path.exists(path + '/img_clean.jpg'):
        img = cv2.imread(path + '/img_clean.jpg')
        # cv2.imwrite(path + '/show.jpg', img)
        # a = img.shape
        # h = int(a[0])
        # w = int(a[1])
        # img = cv.resize(img,dsize=(int(w/2),int(h/2)))
        name1 = ''
        ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False,  det_db_box_thresh=0.3, drop_score=0.1)
        ocr_en = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='en', show_log=False,det_limit_side_len = 2300,det_db_score_mode="slow", det_db_box_thresh=0, drop_score=0)
        result = ocr_en.ocr(img, cls=False)
        mark = 0
        for i in range(len(result)):
            name1 = name1 + result[i][1][0]

        # result1 = ocr.ocr(path + '/area/img_cut_4.jpg', cls=False)
        # if '34' in path:
        #     result = ocr_en.ocr(img, cls=False)
        # else:
        #     result = ocr.ocr(img, cls=False)
        print(1)
        print(path)
        Note = open(path + '/label/img_clean.txt', mode='w')
        Note.write('name')
        Note.write(' ')
        Note.write('x')
        Note.write(' ')
        Note.write('y')
        Note.write('\n')
        for i in range(len(result)):
            name = result[i][1][0]

            if name == '':
                name = 'null'
            list1 = result[i][0]
            list1_1 = list1[0]
            list1_2 = list1[2]
            x1 = int(list1_1[0])
            y1 = int(list1_1[1])
            x2 = int(list1_2[0])
            y2 = int(list1_2[1])
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            # if 3421 < x < 3921:
            #     continue
            if '?' in name:
                img_cut = img[x1:x2, y1:y2]
                result_cult = ocr_en.ocr(img_cut, cls=False)
                name = result[0][1][0]
            if x == '' or y == '':
                x = 'null'
                y = 'null'
            # if '110' in name:
            #     name = 'IIC'
            if ' ' in name:
                name = name.replace(' ', '')
            if '(' in name:
                name = name.replace('(', 'Y')
            if '0)' in name:
                name = name.replace('0)', 'ODD')
            Note.write(name)
            Note.write(' ')
            Note.write(str(x))
            Note.write(' ')
            Note.write(str(y))
            Note.write('\n')
            print(result[i][1][0])
            print(type(result[i][0]))

if __name__ == '__main__':
    main()