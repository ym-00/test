#   coding=UTF-8
import numpy as np
import os
from os import walk
import pandas as pd
import math


def getfilelist(dir):
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

def pipei(imgtype:str):
    path = f'output_{imgtype}/'
    line_path = 'xianduan/xianduan/xianduanjiance/fd_result/'
    filelist = getfilelist(path)
    filelist.sort()
    # print(filelist)
    linelist = getfilelist(line_path)
    # linelist.sort(key=lambda x: int(x.split('_')[1]))
    linelist.sort()
    # print(linelist)
    len1 = len(filelist) - 2
    print("---------以下是匹配算法pipei111111111111111111111111---------")
    for i in range(0, len1):
        ocr_path = path + filelist[i] + '/label/' + filelist[i] + '_l.txt'
        data_component = pd.read_csv(ocr_path, sep='\s+', encoding='UTF-8', error_bad_lines=False)
        # print(data_component)
        paths = line_path + linelist[i] + '/output_line.txt'
        if os.path.exists(paths):
            lines = pd.read_csv(paths, header=None, sep='\s+', encoding='UTF-8', error_bad_lines=False)
            len_0 = lines.shape[0]
            file = open(path + filelist[i] + '/label/'+'dianxian.txt', 'w' ,encoding='UTF-8')
            file.write('pinA_name')
            file.write(' ')
            file.write('pinA_x')
            file.write(' ')
            file.write('pinA_y')
            file.write(' ')
            file.write('pinA_belong')
            file.write(' ')
            file.write('lineA_x')
            file.write(' ')
            file.write('lineA_y')
            file.write(' ')
            file.write('lineB_x')
            file.write(' ')
            file.write('lineB_y')
            file.write(' ')
            file.write('pinB_name')
            file.write(' ')
            file.write('pinB_x')
            file.write(' ')
            file.write('pinB_y')
            file.write(' ')
            file.write('pinB_belong')
            file.write('\n')
            CD_left = []
            CD_right = []
            left_name = []
            right_name= []
            left = []  # 保存左端点的x轴
            left1 = []  # 保存左端点的y轴
            right = []  # 保存左端点的x轴
            right1 = []  # 保存左端点的y轴
            for k in range(len_0):
                # print(lines.loc[i])
                line_x1, line_y1, line_x2, line_y2 ,belong_line= lines.loc[k]
                line_x1 = int(line_x1)
                line_y1 = int(line_y1)
                line_x2 = int(line_x2)
                line_y2 = int(line_y2)
                if abs(line_x1-line_x2)<=5 and abs(line_x1-line_x2)<=35:   #
                    continue
                row_numbers = len(data_component)
                row_numbers = row_numbers
                flag = 0
                count=0
                count1=0
                df_left = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong'])
                df_right = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong'])
                belong2=""
                flag333 = 0
                x66 = 0
                y66 = 0
                flag444=0
                for row_number in range(row_numbers):
                    name = data_component.loc[row_number, "name"]
                    if name == "D/C" or name == "C/D":
                        name = name.replace("/","")
                    if name == "End":
                        flag = 1
                        continue
                    if name == "End2":
                        flag = 2
                        continue

                    # x_1 = float(data_component.loc[row_number, 'x0'])
                    # x_1_1 = math.ceil(x_1)

                    x1 = float(data_component.loc[row_number, 'x0'])
                    x1 = math.ceil(x1)
                    y1 = float(data_component.loc[row_number, 'y0'])
                    y1 = math.ceil(y1)
                    x2 = float(data_component.loc[row_number, 'x1'])
                    x2 = math.ceil(x2)
                    y2 = float(data_component.loc[row_number, 'y1'])
                    y2 = math.ceil(y2)
                    x3 = float(data_component.loc[row_number, 'x2'])
                    x3 = math.ceil(x3)
                    y3 = float(data_component.loc[row_number, 'y2'])
                    y3=math.ceil(y3)
                    x4 = float(data_component.loc[row_number, 'x3'])
                    x4=math.ceil(x4)
                    y4 = float(data_component.loc[row_number, 'y3'])
                    y4=math.ceil(y4)
                    belong = data_component.loc[row_number, "belong"]
                    if str(name).startswith("new_con"):
                        x55 = x2
                        y55 = (y2 + y3) / 2
                        x5 = x1
                        y5 = (y1 + y4) / 2
                        d_1 = math.sqrt(((line_x1 - x5) ** 2 + (line_y1 - y5) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x1 - x55) ** 2 + (line_y1 - y55) ** 2))
                        d_3 = int(d_3)
                        d_min_left = min(d_1, d_3)
                        d_1 = math.sqrt(((line_x2 - x5) ** 2 + (line_y2 - y5) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x2 - x55) ** 2 + (line_y2 - y55) ** 2))
                        d_3 = int(d_3)
                        d_min_right = min(d_1, d_3)
                        count1 = count1 + 1
                        count = count + 1
                        df2_left = pd.DataFrame([[name, d_min_left, x1, y1, belong]],
                                                columns=['name', 'distance', 'x', 'y', 'belong'])
                        df2_right = pd.DataFrame([[name, d_min_right, x1, y1, belong]],
                                                 columns=['name', 'distance', 'x', 'y', 'belong'])
                        df_left = pd.concat([df_left, df2_left], ignore_index=True)
                        df_right = pd.concat([df_right, df2_right], ignore_index=True)
                        continue
                    if flag == 0:
                        d_1 = math.sqrt(((line_x1 - x1) ** 2 + (line_y1 - y1) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x1 - x3) ** 2 + (line_y1 - y3) ** 2))
                        d_3 = int(d_3)
                        d_min_left = min(d_1, d_3)
                        d_1 = math.sqrt(((line_x2 - x1) ** 2 + (line_y2 - y1) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x2 - x3) ** 2 + (line_y2 - y3) ** 2))
                        d_3 = int(d_3)
                        d_min_right = min(d_1, d_3)
                        count1 = count1 + 1
                        count = count + 1
                        df2_left = pd.DataFrame([[name, d_min_left, x2, y1, belong]],
                                                columns=['name', 'distance', 'x', 'y', 'belong'])
                        df2_right = pd.DataFrame([[name, d_min_right, x2, y1, belong]],
                                                 columns=['name', 'distance', 'x', 'y', 'belong'])
                        df_left = pd.concat([df_left, df2_left], ignore_index=True)
                        df_right = pd.concat([df_right, df2_right], ignore_index=True)
                    if flag == 1:
                        if name is not "CD" and name is not "DC" and name is not "D/C":
                            flag444=1
                        else:
                            flag444=0
                        if name == belong and flag444==0:
                                continue
                        if str(name).startswith("AUTO/MAN"):
                            belong2 = belong
                            x66=x1
                            y66=y1
                            continue
                        if abs(x66-x1)<5 and belong == belong2:
                            continue
                        d_1 = math.sqrt(((line_x1 - x1) ** 2 + (line_y1 - y1) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x1 - x3) ** 2 + (line_y1 - y3) ** 2))
                        d_3 = int(d_3)
                        d_min_left = min(d_1, d_3)

                        d_1 = math.sqrt(((line_x2 - x1) ** 2 + (line_y2 - y1) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x2 - x3) ** 2 + (line_y2 - y3) ** 2))
                        d_3 = int(d_3)
                        d_min_right = min(d_1, d_3)
                        count1 = count1 + 1
                        count = count + 1
                        df2_left = pd.DataFrame([[name, d_min_left, x2, y1, belong]],
                                                columns=['name', 'distance', 'x', 'y', 'belong'])
                        df2_right = pd.DataFrame([[name, d_min_right, x2, y1, belong]],
                                                 columns=['name', 'distance', 'x', 'y', 'belong'])
                        df_left = pd.concat([df_left, df2_left], ignore_index=True)
                        df_right = pd.concat([df_right, df2_right], ignore_index=True)
                    if flag == 2:
                        x55 = x2
                        y55 = (y2 + y3) / 2
                        x5 = x1
                        y5 = (y1 + y4) / 2
                        d_1 = math.sqrt(((line_x1 - x5) ** 2 + (line_y1 - y5) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x1 - x55) ** 2 + (line_y1 - y55) ** 2))
                        d_3 = int(d_3)
                        d_min_left = min(d_1, d_3)
                        d_1 = math.sqrt(((line_x2 - x5) ** 2 + (line_y2 - y5) ** 2))
                        d_1 = int(d_1)
                        d_3 = math.sqrt(((line_x2 - x55) ** 2 + (line_y2 - y55) ** 2))
                        d_3 = int(d_3)
                        d_min_right = min(d_1, d_3)
                        count1 = count1 + 1
                        count = count + 1
                        df2_left = pd.DataFrame([[name, d_min_left, x1, y1, belong]],
                                                columns=['name', 'distance', 'x', 'y', 'belong'])
                        df2_right = pd.DataFrame([[name, d_min_right, x1, y1, belong]],
                                                 columns=['name', 'distance', 'x', 'y', 'belong'])
                        df_left = pd.concat([df_left, df2_left], ignore_index=True)
                        df_right = pd.concat([df_right, df2_right], ignore_index=True)
                        # if line_y2 > (y1 - 5) and line_y2 < (y2 + 5):
                        #      distance_logic_right = abs(line_x2 - x1)
                        #      count1 = count1 + 1
                        #      df2_right = pd.DataFrame(
                        #         [[name, distance_logic_right, x1, y1, belong]],  #保存左上顶点
                        #         columns=['name', 'distance', 'x', 'y', 'belong'])
                        #      df_right = pd.concat([df_right, df2_right], ignore_index=True)
                        #
                        # elif line_y1 > (y1 - 5) and line_y1 < (y2 + 5):
                        #      count = count + 1
                        #      distance_logic_left = abs(line_x1 - x3)
                        #      df2_left = pd.DataFrame(
                        #         [[name, distance_logic_left, x1, y1, belong]],
                        #         columns=['name', 'distance', 'x', 'y', 'belong'])
                        #      df_left = pd.concat([df_left, df2_left], ignore_index=True)
                # print("LEFT", df_left)
                # print("RIGHT", df_right)
                # 对左右两个端点匹配的数值进行排序
                df_left = df_left.sort_values("distance")
                df_right = df_right.sort_values("distance")
                # 重置索引
                df_left = df_left.reset_index(drop=True)
                df_right = df_right.reset_index(drop=True)
                # print("LEFT111111111111111111111", '\n', df_left)
                # print("RIGHT11111111111111111111", '\n', df_right)
                # if lines.loc[i][0] == 2645 and lines.loc[i][1] == 1881 and lines.loc[i][2] == 2808 and lines.loc[i][3] == 1492:
                #     break 3157 1402 3308 1836
                # 接下来检测左右两个端点的最小distance，若最小distance大于某个阈值则该线段没有连接任何元件，输出null
                # 符合条件的则按照【左端点连接的元件部分的信息】【线段信息】【右端点连接的线段信息进行输出】
                if count == 0 or count1 == 0:
                    break

                lname, ld, lx, ly, lb = df_left.loc[0]
                rname, rd, rx, ry, rb = df_right.loc[0]
                for k in range(len(CD_left)):
                    if rx == CD_left[k] and ry == CD_right[k]:
                        rname, rd, rx, ry, rb = df_right.loc[1]
                l = [lname, lx, ly, lb]  # 左端点连接元件的信息
                r = [rname, rx, ry, rb]  # 右端点连接元件的信息
                flag888 = 0
                flag999 = 0
                #加个判断，如果该线在元器件左边的左边，那么说明是线是返回的，故需要左右调整
                if lines.loc[k][0] <= lx or lines.loc[k][2] <= lx:
                    if lines.loc[k][0] < lines.loc[k][2]:  #如果线段起点坐标的x轴小于终点坐标的x轴则反过来
                        l = [rname, rx, ry, rb]
                        r = [lname, lx, ly, lb]
                if str(r[0]).startswith("new_con"):
                    l = [rname, rx, ry, rb]
                    r = [lname, lx, ly, lb]
                if df_left.loc[0, 'distance'] < 50 and df_right.loc[0,'distance'] < 150:   #一般来说线段的起点是没有问题的
                    if lx == rx and ly == ry:
                        continue
                    if l[0] == "DC":  #如果存在DC在左边的直接跳过
                        continue
                    if str(r[0]).startswith("DC"):
                        CD_left.append(r[1])
                        CD_right.append(r[2])
                    for i in range(len(left)):
                        if left[i] == l[1] and left1[i] == l[2] and right[i] == r[1] and right1[i] == r[2]:
                            flag888 = 1
                        # if (left_name=="YCAM009VA全开" and left[i] == 1258 and left1[i] == 1765) or  (left_name=="YCAM009VA全开" and left[i] == 1258 and left[i] == 1258)   :  # 判断左端有无矩形相连好几次
                        #     #left[i] == l[1] and left1[i] == l[2] and
                        #     # if str(l[0]).startswith("or") or str(l[0]).startswith("not") or str(l[0]).startswith(
                        #     #         "and") or str(l[0]).startswith("new_con"):
                        #     #     print("1")
                        #     # else:
                        #     flag888 = 1
                    if str(l[0]) == "nan" and str(l[3]) is not "nan":
                        continue
                    if str(r[0]) == "nan" and str(r[3]) is not "nan":
                        continue
                    if str(l[0]).startswith("circles") and str(r[0]).startswith("circles"):
                            continue
                    if flag888 == 1:
                        continue

                    left_name.append(l[0])
                    left.append(l[1])
                    left1.append(l[2])
                    right_name.append(r[0])
                    right.append(r[1])
                    right1.append(r[2])
                    if str(r[0]) in ("MANDMD","PERMITSTOP","RMTCONTROL","PERMITOPEN","PERMITCLS","AUTODMD"):
                        l = ["null", "null", "null", "null"]
                    file.write(str(l[0]))
                    file.write(' ')
                    file.write(str(l[1]))
                    file.write(' ')
                    file.write(str(l[2]))
                    file.write(' ')
                    file.write(str(l[3]))
                    file.write(' ')
                    file.write(str(lines.loc[k][0]))
                    file.write(' ')
                    file.write(str(lines.loc[k][1]))
                    file.write(' ')
                    file.write(str(lines.loc[k][2]))
                    file.write(' ')
                    file.write(str(lines.loc[k][3]))
                    file.write(' ')
                    file.write(str(r[0]))
                    file.write(' ')
                    file.write(str(r[1]))
                    file.write(' ')
                    file.write(str(r[2]))
                    file.write(' ')
                    file.write(str(r[3]))
                    file.write(' ')
                    file.write('\n')
                    continue
                if df_left.loc[0, 'distance'] > 50 and df_right.loc[0, 'distance'] < 100:
                    if str(rb).startswith('PUMP') or str(rb).startswith('PNEUM') or str(rb).startswith('MOTOR'):
                        l = ["null", "null", "null", "null"]
                        file.write(str(l[0]))
                        file.write(' ')
                        file.write(str(l[1]))
                        file.write(' ')
                        file.write(str(l[2]))
                        file.write(' ')
                        file.write(str(l[3]))
                        file.write(' ')
                        file.write(str(lines.loc[k][0]))
                        file.write(' ')
                        file.write(str(lines.loc[k][1]))
                        file.write(' ')
                        file.write(str(lines.loc[k][2]))
                        file.write(' ')
                        file.write(str(lines.loc[k][3]))
                        file.write(' ')
                        file.write(str(r[0]))
                        file.write(' ')
                        file.write(str(r[1]))
                        file.write(' ')
                        file.write(str(r[2]))
                        file.write(' ')
                        file.write(str(r[3]))
                        file.write(' ')
                        file.write('\n')
                        continue
                if df_left.loc[0, 'distance'] < 100 and df_right.loc[0, 'distance'] < 80:
                    if lx == rx and ly == ry:
                        continue
                    print(CD_left)
                    if l[0] == "DC":  #如果存在DC在左边的直接跳过
                        continue
                    if str(r[0]).startswith("DC"):
                        CD_left.append(r[1])
                        CD_right.append(r[2])
                    for i in range(len(left)):
                        if left[i] == l[1] and left1[i] == l[2] and right[i] == r[1] and right1[i] == r[2]:
                            flag888 = 1
                        # if left[i] == l[1] and left1[i] == l[2]:   #判断左端有无矩形相连好几次
                        #     if str(l[0]).startswith("or") or str(l[0]).startswith("not") or str(l[0]).startswith("and") or str(l[0]).startswith("new_con"):
                        #         print("1")
                        #     else:
                        #         flag888=1
                    if str(l[0])=="nan" and str(l[3]) is not "nan" and str(l[3]) is not "YCAM001RSIIC":
                        continue
                    if str(r[0])=="nan" and str(r[3]) is not "nan":
                        continue
                    if str(l[0]).startswith("circles") and str(r[0]).startswith("circles"):
                        continue
                    if flag888 == 1:
                        continue
                    if str(l[0])=="001VA全关":
                        if lines.loc[k][0]==lines.loc[k][2]:
                            continue
                    left_name.append(l[0])
                    left.append(l[1])
                    left1.append(l[2])
                    right_name.append(r[0])
                    right.append(r[1])
                    right1.append(r[2])
                    if str(r[0]) in ("MANDMD","PERMITSTOP","RMTCONTROL","PERMITOPEN","PERMITCLS","AUTODMD"):
                        l = ["null", "null", "null", "null"]
                    file.write(str(l[0]))
                    file.write(' ')
                    file.write(str(l[1]))
                    file.write(' ')
                    file.write(str(l[2]))
                    file.write(' ')
                    file.write(str(l[3]))
                    file.write(' ')
                    file.write(str(lines.loc[k][0]))
                    file.write(' ')
                    file.write(str(lines.loc[k][1]))
                    file.write(' ')
                    file.write(str(lines.loc[k][2]))
                    file.write(' ')
                    file.write(str(lines.loc[k][3]))
                    file.write(' ')
                    file.write(str(r[0]))
                    file.write(' ')
                    file.write(str(r[1]))
                    file.write(' ')
                    file.write(str(r[2]))
                    file.write(' ')
                    file.write(str(r[3]))
                    file.write(' ')
                    file.write('\n')
                    continue
                #
                # else:z
                # if lx == rx and ly == ry:
                #     continue
                # file.write(str(l[0]))
                # file.write(' ')
                # file.write(str(l[1]))
                # file.write(' ')
                # file.write(str(l[2]))
                # file.write(' ')
                # file.write(str(l[3]))
                # file.write(' ')
                # file.write(str(lines.loc[i][0]))
                # file.write(' ')
                # file.write(str(lines.loc[i][1]))
                # file.write(' ')
                # file.write(str(lines.loc[i][2]))
                # file.write(' ')
                # file.write(str(lines.loc[i][3]))
                # file.write(' ')
                # file.write(str(r[0]))
                # file.write(' ')
                # file.write(str(r[1]))
                # file.write(' ')
                # file.write(str(r[2]))
                # file.write(' ')
                # file.write(str(r[3]))
                # file.write(' ')
                # file.write('\n')
def pipei2(imgtype:str):
    path = f'output_{imgtype}/'
    filelist = getfilelist(path)
    filelist.sort()
    len1 = len(filelist) - 2
    print("---------以下是匹配算法pipei222222222222222222222222222222222---------")
    for i in range(0, len1):
        ocr_path = path + filelist[i] + '/label/' + filelist[i] + '_l.txt'
        data_component = pd.read_csv(ocr_path, sep='\s+', encoding='UTF-8', error_bad_lines=False)
        data_component1 = pd.read_csv(ocr_path, sep='\s+', encoding='UTF-8', error_bad_lines=False)
        # print(data_component)
        # print(data_component1)
        row_numbers = len(data_component)
        row_numbers = row_numbers
        flag1111=0
        for row_number in range(row_numbers):
            file = open(path + filelist[i] + '/label/'+'dianxian.txt', 'a',encoding='UTF-8')
            name1 = data_component.loc[row_number, "name"]
            if name1 == "End" or name1 =="End2":
                continue
            # if name1 == "End":
            #     break  # 如果遇到了End符号表示结束循环
            x11 = float(data_component.loc[row_number, 'x0'])
            x11 = math.ceil(x11)
            y11 = float(data_component.loc[row_number, 'y0'])
            y11 = math.ceil(y11)
            x22 = float(data_component.loc[row_number, 'x1'])
            x22 = math.ceil(x22)
            y22 = float(data_component.loc[row_number, 'y1'])
            y22 = math.ceil(y22)
            x33 = float(data_component.loc[row_number, 'x2'])
            x33 = math.ceil(x33)
            y33 = float(data_component.loc[row_number, 'y2'])
            y33 = math.ceil(y33)
            x44 = float(data_component.loc[row_number, 'x3'])
            x44 = math.ceil(x44)
            y44 = float(data_component.loc[row_number, 'y3'])
            y44 = math.ceil(y44)
            belong1 = data_component.loc[row_number, "belong"]
            row_numbers1= len(data_component1)
            row_numbers1 = row_numbers1
            df_left = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
            df_right = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
            count = 0
            if name1 in ("CD", "DC", "D/C"):
                for row_number in range(row_numbers1):
                    name = data_component.loc[row_number, "name"]
                    belong = data_component1.loc[row_number, "belong"]
                    if name == "End" or name == "End2":
                        continue
                    # if name == "End":
                    #     flag1111 = 1
                    #     continue
                    # if name == "End2":
                    #     continue
                    # if flag1111 == 1 and name == belong:
                    #     continue
                    x1 = float(data_component1.loc[row_number, 'x0'])
                    x1 = math.ceil(x1)
                    y1 = float(data_component1.loc[row_number, 'y0'])
                    y1 = math.ceil(y1)
                    x2 = float(data_component1.loc[row_number, 'x1'])
                    x2 = math.ceil(x2)
                    y2 = float(data_component1.loc[row_number, 'y1'])
                    y2 = math.ceil(y2)
                    x3 = float(data_component1.loc[row_number, 'x2'])
                    x3 = math.ceil(x3)
                    y3 = float(data_component1.loc[row_number, 'y2'])
                    y3 = math.ceil(y3)
                    x4 = float(data_component1.loc[row_number, 'x3'])
                    x4 = math.ceil(x4)
                    y4 = float(data_component1.loc[row_number, 'y3'])
                    y4 = math.ceil(y4)

                    # 记录有几行进入了df_right
                    if name1 == name:
                        continue
                    if name1 == "CD":  # CD中心点是（x22,y11）
                        if abs(y1 - y33) <= 50 and x3 < x11:
                            # if x4 <= x22 and y4 >= y11 and x2 <= x22 and y2 <= y11:  # 为了判断左边元器件的上下两点在CD中心点
                            count = count + 1
                            distance_logic_right = 0
                            df2_right = pd.DataFrame(
                                [[name1, distance_logic_right, x22, y11, belong1, x11,
                                  y11]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
                            print(df2_right)
                            df_right = pd.concat([df_right, df2_right], ignore_index=True)
                            distance_logic_left = abs(x11 - x3)
                            df2_left = pd.DataFrame(
                                [[name, distance_logic_left, x2, y1, belong, x3, y3]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
                            print(df2_left)
                            df_left = pd.concat([df_left, df2_left], ignore_index=True)
                    if name1 in ("DC","D/C"):  # CD中心点是（x22,y11）
                        if abs(y3 - y11) <= 30 and x1 > x33:
                            # if x4 <= x22 and y4 >= y11 and x2 <= x22 and y2 <= y11:  # 为了判断左边元器件的上下两点在CD中心点
                            count = count + 1
                            distance_logic_left = 0
                            df2_left = pd.DataFrame(
                                [[name1, distance_logic_left, x22, y11, belong1, x33,
                                  y33]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
                            print(df2_left)
                            df_left = pd.concat([df_left, df2_left], ignore_index=True)
                            distance_logic_right = abs(x33 - x1)
                            df2_right = pd.DataFrame(
                                [[name, distance_logic_right, x2, y1, belong, x1, y1]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
                            print(df2_right)
                            df_right = pd.concat([df_right, df2_right], ignore_index=True)
                if count is 0:
                    continue
                else:
                    print("LEFT", df_left)
                    print("RIGHT", df_right)
                    # 对左右两个端点匹配的数值进行排序
                    df_left = df_left.sort_values("distance")
                    df_right = df_right.sort_values("distance")
                    # 重置索引
                    df_left = df_left.reset_index(drop=True)
                    df_right = df_right.reset_index(drop=True)
                    print("LEFT111111111111111111111", '\n', df_left)
                    print("RIGHT11111111111111111111", '\n', df_right)

                    # 接下来检测左右两个端点的最小distance，若最小distance大于某个阈值则该线段没有连接任何元件，输出null
                    # 符合条件的则按照【左端点连接的元件部分的信息】【线段信息】【右端点连接的线段信息进行输出】

                    lname, ld, lx, ly, lb, left_x, left_y = df_left.loc[0]
                    rname, rd, rx, ry, rb, right_x, right_y = df_right.loc[0]
                    l = [lname, lx, ly, lb, left_x, left_y]  # 左端点连接元件的信息
                    r = [rname, rx, ry, rb, right_x, right_y]  # 右端点连接元件的信息
                    file.write(str(l[0]))
                    file.write(' ')
                    file.write(str(l[1]))
                    file.write(' ')
                    file.write(str(l[2]))
                    file.write(' ')
                    file.write(str(l[3]))
                    file.write(' ')
                    file.write(str(l[4]))
                    file.write(' ')
                    file.write(str(l[5]))
                    file.write(' ')
                    file.write(str(r[4]))
                    file.write(' ')
                    file.write(str(r[5]))
                    file.write(' ')
                    file.write(str(r[0]))
                    file.write(' ')
                    file.write(str(r[1]))
                    file.write(' ')
                    file.write(str(r[2]))
                    file.write(' ')
                    file.write(str(r[3]))
                    file.write(' ')
                    file.write('\n')
def pipei3(imgtype:str):

    path_0 = f'output_{imgtype}/'
    filelist = getfilelist(path_0)
    filelist.sort()
    len1 = len(filelist) - 2
    print("---------以下是匹配算法pipei3333333333333333333333333333333---------")
    for i in range(0, len1):
        path = path_0 + filelist[i] + '/label/'+'dianxian.txt'
        ocr_path = path_0 + filelist[i] + '/label/' + filelist[i] + '_l.txt'
        data_component = pd.read_csv(ocr_path, sep='\s+', encoding='utf-8', error_bad_lines=False)
        data_component1 = pd.read_csv(ocr_path, sep='\s+', encoding='utf-8', error_bad_lines=False)
        data_component2 = pd.read_csv(path, sep='\s+', encoding='utf-8',error_bad_lines=False)
        row_numbers = len(data_component2)
        row_numbers = row_numbers
        circles = []  # 存放圆形名字
        circles1 = []  # 存放相应圆形的中点x值
        circles2 = []  # 存放相应圆形的中点y值
        for row_number in range(row_numbers):   # 先找那个dianxian已经匹配好的东西里面有没有圆形，如果有的话保存到circles数组中
            name1 = data_component2.loc[row_number, "pinA_name"]
            pinA_x1 = data_component2.loc[row_number, "pinA_x"]
            pinA_y1 = data_component2.loc[row_number, "pinA_y"]
            name2 = data_component2.loc[row_number, "pinB_name"]
            pinB_x1 = data_component2.loc[row_number, "pinB_x"]
            pinB_y1 = data_component2.loc[row_number, "pinB_y"]
            if name1 == "End":
                break
            if str(name1).startswith('circle'):
                circles.append(str(name1))
                circles1.append(pinA_x1)
                circles2.append(pinA_y1)
            if str(name2).startswith('circle'):
                circles.append(str(name2))
                circles1.append(pinB_x1)
                circles2.append(pinB_y1)
        print(circles)
        row_numbers = len(data_component)
        row_numbers = row_numbers
        for row_number in range(row_numbers):
            file = open(path, 'a',encoding='UTF-8')
            name1 = data_component.loc[row_number, "name"]
            if name1 == "End":
                break
            flag = 0
            x11 = float(data_component.loc[row_number, 'x0'])
            x11 = math.ceil(x11)
            y11 = float(data_component.loc[row_number, 'y0'])
            y11 = math.ceil(y11)
            x22 = float(data_component.loc[row_number, 'x1'])
            x22 = math.ceil(x22)
            y22 = float(data_component.loc[row_number, 'y1'])
            y22 = math.ceil(y22)
            x33 = float(data_component.loc[row_number, 'x2'])
            x33 = math.ceil(x33)
            y33 = float(data_component.loc[row_number, 'y2'])
            y33 = math.ceil(y33)
            x44 = float(data_component.loc[row_number, 'x3'])
            x44 = math.ceil(x44)
            y44 = float(data_component.loc[row_number, 'y3'])
            y44 = math.ceil(y44)
            belong1 = data_component.loc[row_number, "belong"]
            for i in range(len(circles)):            #判断该圆形的名字在不在匹配过的文件中出现
                if name1 == str(circles[i]) and abs(int(circles1[i])-x11) <= 40 and abs(int(circles2[i])-y11 )<= 40:
                    flag = 1
                    break
            if flag == 1:
                continue
            if x11 <= 900 or x33 >= 3600:      #判断该圆形是不是在第三象限如不在则直接跳过
                continue
            row_numbers = len(data_component1)
            row_numbers = row_numbers
            df_left = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
            df_right = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
            df_self = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
            count = 0
            count1 = 0
            count2 = 0 #用来记录当前信息保存到左
            if str(name1).startswith('circle'):         #经过以上的判断以上还有圆形的话做比较
                for row_number in range(row_numbers):
                    name = data_component.loc[row_number, "name"]
                    if name == "End" or name == "End2" or name== "":
                        continue
                    x1 = float(data_component1.loc[row_number, 'x0'])
                    x1 = math.ceil(x1)
                    y1 = float(data_component1.loc[row_number, 'y0'])
                    y1 = math.ceil(y1)
                    x2 = float(data_component1.loc[row_number, 'x1'])
                    x2 = math.ceil(x2)
                    y2 = float(data_component1.loc[row_number, 'y1'])
                    y2 = math.ceil(y2)
                    x3 = float(data_component1.loc[row_number, 'x2'])
                    x3 = math.ceil(x3)
                    y3 = float(data_component1.loc[row_number, 'y2'])
                    y3 = math.ceil(y3)
                    x4 = float(data_component1.loc[row_number, 'x3'])
                    x4 = math.ceil(x4)
                    y4 = float(data_component1.loc[row_number, 'y3'])
                    y4 = math.ceil(y4)
                    belong = data_component1.loc[row_number, "belong"]
                    df_self = pd.DataFrame(
                                [[name1, 0, x22, y11, belong1, x33, y33]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'self_x', 'self_y'])
                    if name1 == name and x11 == x1 and y11 == y1:  # 排除自身因素
                        continue
                    #########11.19 bai更改
                    if abs(y3 - y11) <= 50:
                        if x11 > x3:
                            count = count + 1
                            distance_logic_left = abs(x11 - x3)
                            df2_left = pd.DataFrame(
                                [[name, distance_logic_left, x2, y1, belong, x3, y3]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
                            df_left = pd.concat([df_left, df2_left], ignore_index=True)
                        else:
                            # if x4 <= x22 and y4 >= y11 and x2 <= x22 and y2 <= y11:  # 为了判断左边元器件的上下两点在CD中心点
                            count1 = count1 + 1
                            distance_logic_right = abs(x33 - x1)
                            df2_right = pd.DataFrame(
                                    [[name, distance_logic_right, x2, y1, belong, x1, y1]],
                                    columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
                            print(df2_right)
                            df_right = pd.concat([df_right, df2_right], ignore_index=True)
                if count is 0 and count1 is not 0:
                    df_right = df_right.sort_values("distance")
                    df_right = df_right.reset_index(drop=True)
                    rname, rd, rx, ry, rb, right_x, right_y = df_right.loc[0]
                    lname, ld, lx, ly, lb, left_x, left_y = df_self.loc[0]
                    l = [lname, lx, ly, lb, left_x, left_y]  # 左端点连接元件的信息
                    r = [rname, rx, ry, rb, right_x, right_y]  # 右端点连接元件的信息
                    file.write(str(l[0]))
                    file.write(' ')
                    file.write(str(l[1]))
                    file.write(' ')
                    file.write(str(l[2]))
                    file.write(' ')
                    file.write(str(l[3]))
                    file.write(' ')
                    file.write(str(l[4]))
                    file.write(' ')
                    file.write(str(l[5]))
                    file.write(' ')
                    file.write(str(r[4]))
                    file.write(' ')
                    file.write(str(r[5]))
                    file.write(' ')
                    file.write(str(r[0]))
                    file.write(' ')
                    file.write(str(r[1]))
                    file.write(' ')
                    file.write(str(r[2]))
                    file.write(' ')
                    file.write(str(r[3]))
                    file.write(' ')
                    file.write('\n')
                    continue
                if count1 is 0 and count is not 0:
                    df_left = df_left.sort_values("distance")
                    df_left = df_left.reset_index(drop=True)
                    lname, ld, lx, ly, lb, left_x, left_y = df_left.loc[0]
                    rname, rd, rx, ry, rb, right_x, right_y = df_self.loc[0]
                    l = [lname, lx, ly, lb, left_x, left_y]  # 左端点连接元件的信息
                    r = [rname, rx, ry, rb, right_x, right_y]  # 右端点连接元件的信息
                    file.write(str(l[0]))
                    file.write(' ')
                    file.write(str(l[1]))
                    file.write(' ')
                    file.write(str(l[2]))
                    file.write(' ')
                    file.write(str(l[3]))
                    file.write(' ')
                    file.write(str(l[4]))
                    file.write(' ')
                    file.write(str(l[5]))
                    file.write(' ')
                    file.write(str(r[4]))
                    file.write(' ')
                    file.write(str(r[5]))
                    file.write(' ')
                    file.write(str(r[0]))
                    file.write(' ')
                    file.write(str(r[1]))
                    file.write(' ')
                    file.write(str(r[2]))
                    file.write(' ')
                    file.write(str(r[3]))
                    file.write(' ')
                    file.write('\n')
                    continue
                if count1 is 0 and count is 0:
                    continue
                if count1 is not 0 and count is not 0:
                    print("LEFT", df_left)
                    print("RIGHT", df_right)
                    # 对左右两个端点匹配的数值进行排序
                    df_left = df_left.sort_values("distance")
                    df_right = df_right.sort_values("distance")
                    # 重置索引
                    df_left = df_left.reset_index(drop=True)
                    df_right = df_right.reset_index(drop=True)
                    print("LEFT111111111111111111111", '\n', df_left)
                    print("RIGHT11111111111111111111", '\n', df_right)

                    # 接下来检测左右两个端点的最小distance，若最小distance大于某个阈值则该线段没有连接任何元件，输出null
                    # 符合条件的则按照【左端点连接的元件部分的信息】【线段信息】【右端点连接的线段信息进行输出】

                    lname, ld, lx, ly, lb, left_x, left_y = df_left.loc[0]
                    rname, rd, rx, ry, rb, right_x, right_y = df_right.loc[0]
                    if ld <= rd:
                        rname, rd, rx, ry, rb, right_x, right_y =df_self.loc[0]
                        l = [lname, lx, ly, lb, left_x, left_y]  # 左端点连接元件的信息
                        r = [rname, rx, ry, rb, right_x, right_y]  # 右端点连接元件的信息
                        file.write(str(l[0]))
                        file.write(' ')
                        file.write(str(l[1]))
                        file.write(' ')
                        file.write(str(l[2]))
                        file.write(' ')
                        file.write(str(l[3]))
                        file.write(' ')
                        file.write(str(l[4]))
                        file.write(' ')
                        file.write(str(l[5]))
                        file.write(' ')
                        file.write(str(r[4]))
                        file.write(' ')
                        file.write(str(r[5]))
                        file.write(' ')
                        file.write(str(r[0]))
                        file.write(' ')
                        file.write(str(r[1]))
                        file.write(' ')
                        file.write(str(r[2]))
                        file.write(' ')
                        file.write(str(r[3]))
                        file.write(' ')
                        file.write('\n')
                    elif ld > rd:
                        lname, ld, lx, ly, lb, left_x, left_y = df_self.loc[0]
                        l = [lname, lx, ly, lb, left_x, left_y]  # 左端点连接元件的信息
                        r = [rname, rx, ry, rb, right_x, right_y]  # 右端点连接元件的信息
                        file.write(str(l[0]))
                        file.write(' ')
                        file.write(str(l[1]))
                        file.write(' ')
                        file.write(str(l[2]))
                        file.write(' ')
                        file.write(str(l[3]))
                        file.write(' ')
                        file.write(str(l[4]))
                        file.write(' ')
                        file.write(str(l[5]))
                        file.write(' ')
                        file.write(str(r[4]))
                        file.write(' ')
                        file.write(str(r[5]))
                        file.write(' ')
                        file.write(str(r[0]))
                        file.write(' ')
                        file.write(str(r[1]))
                        file.write(' ')
                        file.write(str(r[2]))
                        file.write(' ')
                        file.write(str(r[3]))
                        file.write(' ')
                        file.write('\n')
def pipei4(imgtype:str):
    path_0 = f'output_{imgtype}/'
    filelist = getfilelist(path_0)
    filelist.sort()
    len1 = len(filelist) - 2
    print("---------以下是匹配算法pipei444444444444444444444444---------")
    for i in range(0,len1):
        logic = []
        path = path_0 + filelist[i] + '/label/'+'dianxian.txt'
        ocr_path = path_0 + filelist[i] + '/label/' + filelist[i] + '_l.txt'
        data_component = pd.read_csv(ocr_path, sep='\s+', encoding='utf-8', error_bad_lines=False)
        data_component1 = pd.read_csv(ocr_path, sep='\s+', encoding='utf-8', error_bad_lines=False)
        data_component2 = pd.read_csv(path, sep='\s+', encoding='utf-8',error_bad_lines=False)
        row_numbers = len(data_component2)
        row_numbers = row_numbers
        myflag = 0
        for row_number in range(row_numbers):   # 先判断有没有逻辑门有没有输出   有没有在左边出现
            name1 = data_component2.loc[row_number, "pinA_name"]
            # name2 = data_component2.loc[row_number, "pinB_name"]
            if str(name1).startswith('and') or str(name1).startswith('or') or str(name1).startswith('not'): #判断前缀是不是逻辑门因为有特殊矩形存在
                logic.append(str(name1))
                # if str(name2).startswith('and') or str(name2).startswith('or') or str(name2).startswith('not'):
                #     logic.append(str(name2))
        print(logic)
        row_numbers = len(data_component)
        row_numbers = row_numbers
        flag1 = 0
        for row_number in range(row_numbers):
            file = open(path, 'a',encoding='UTF-8')
            name1 = data_component.loc[row_number, "name"]
            if name1 == "End2":
                 flag1 = 1
            if flag1 is not 1:    #如果flag1不等于1的话那就是还没有逻辑门部门故跳过
                continue
            flag = 0
            for i in range(len(logic)):            #判断该逻辑门有没有输出 有输出的话那就直接跳过
                if name1 == str(logic[i]):
                    flag = 1
                    break
            if flag == 1:
                continue
            try:
                 x11 = float(data_component.loc[row_number, 'x0'])
            except:
                continue
            x11 = math.ceil(x11)
            y11 = float(data_component.loc[row_number, 'y0'])
            y11 = math.ceil(y11)
            x22 = float(data_component.loc[row_number, 'x1'])
            x22 = math.ceil(x22)
            y22 = float(data_component.loc[row_number, 'y1'])
            y22 = math.ceil(y22)
            x33 = float(data_component.loc[row_number, 'x2'])
            x33 = math.ceil(x33)
            y33 = float(data_component.loc[row_number, 'y2'])
            y33 = math.ceil(y33)
            x44 = float(data_component.loc[row_number, 'x3'])
            x44 = math.ceil(x44)
            y44 = float(data_component.loc[row_number, 'y3'])
            y44 = math.ceil(y44)
            x55 = x22
            y55 = (y22+y33)/2

            belong1 = data_component.loc[row_number, "belong"]
            row_numbers = len(data_component1)
            row_numbers = row_numbers
            df_left = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
            df_right = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
            # df_self = pd.DataFrame(columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
            count = 0
            count1 = 1
            # count2 = 0 #用来记录当前信息保存到左
            if str(name1).startswith('and') or str(name1).startswith('or') or str(name1).startswith('not'):         #经过以上的判断以上还有逻辑门的话做比较
                for row_number in range(row_numbers):
                    name = data_component.loc[row_number, "name"]
                    if name == "End" or name == "End2":
                        continue
                    x1 = float(data_component1.loc[row_number, 'x0'])
                    x1 = math.ceil(x1)
                    y1 = float(data_component1.loc[row_number, 'y0'])
                    y1 = math.ceil(y1)
                    x2 = float(data_component1.loc[row_number, 'x1'])
                    x2 = math.ceil(x2)
                    y2 = float(data_component1.loc[row_number, 'y1'])
                    y2 = math.ceil(y2)
                    x3 = float(data_component1.loc[row_number, 'x2'])
                    x3 = math.ceil(x3)
                    y3 = float(data_component1.loc[row_number, 'y2'])
                    y3 = math.ceil(y3)
                    x4 = float(data_component1.loc[row_number, 'x3'])
                    x4 = math.ceil(x4)
                    y4 = float(data_component1.loc[row_number, 'y3'])
                    y4 = math.ceil(y4)
                    x5 = x1
                    y5 = (y1 + y4) / 2
                    belong = data_component1.loc[row_number, "belong"]
                    # de_self = pd.DataFrame(
                    #             [[name1, 0, int((x11 + x33) / 2), int((y11 + y22) / 2), belong1, x33, y33]],
                    #             columns=['name', 'distance', 'x', 'y', 'belong', 'self_x', 'self_y'])
                    if name1 == name and x11 == x1 and y11 == y1:     #找到自己了则跳过
                        continue
                    if str(name).startswith('and') or str(name).startswith('or') or str(name).startswith('not'):
                        if abs(y5 - y55) <= 70 and x5 >= x55:  # 只存在逻辑门在左，丢失的线段在右
                            count = count + 1
                            distance_logic_left = 0  # 因为左边只能是自己所以不用排序直接赋值
                            df2_left = pd.DataFrame(
                                [[name1, distance_logic_left, x22, y11, belong1, x33,
                                  y33]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
                            print(df2_left)
                            df_left = pd.concat([df_left, df2_left], ignore_index=True)
                            distance_logic_right = abs(x5 - x55)
                            df2_right = pd.DataFrame(
                                [[name, distance_logic_right, x2, y1, belong, x1, y1]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
                            print(df2_right)
                            df_right = pd.concat([df_right, df2_right], ignore_index=True)
                    else:
                        if abs(y1 - y55) <= 70 and x1 >= x55:   #只存在逻辑门在左，丢失的线段在右
                            count = count + 1
                            distance_logic_left = 0   #因为左边只能是自己所以不用排序直接赋值
                            df2_left = pd.DataFrame(
                                [[name1, distance_logic_left, x22,y11 , belong1, x33,
                                  y33]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'left_x', 'left_y'])
                            print(df2_left)
                            df_left = pd.concat([df_left, df2_left], ignore_index=True)
                            distance_logic_right = abs(x1-x55)
                            df2_right = pd.DataFrame(
                                [[name, distance_logic_right, x2, y1, belong, x1, y1]],
                                columns=['name', 'distance', 'x', 'y', 'belong', 'right_x', 'right_y'])
                            print(df2_right)
                            df_right = pd.concat([df_right, df2_right], ignore_index=True)
                if count is 0:
                    continue
                else:
                    print("LEFT", df_left)
                    print("RIGHT", df_right)
                    # 对左右两个端点匹配的数值进行排序
                    df_left = df_left.sort_values("distance")
                    df_right = df_right.sort_values("distance")
                    # 重置索引
                    df_left = df_left.reset_index(drop=True)
                    df_right = df_right.reset_index(drop=True)
                    print("LEFT111111111111111111111", '\n', df_left)
                    print("RIGHT11111111111111111111", '\n', df_right)

                    # 接下来检测左右两个端点的最小distance，若最小distance大于某个阈值则该线段没有连接任何元件，输出null
                    # 符合条件的则按照【左端点连接的元件部分的信息】【线段信息】【右端点连接的线段信息进行输出】

                    lname, ld, lx, ly, lb, left_x, left_y = df_left.loc[0]
                    rname, rd, rx, ry, rb, right_x, right_y = df_right.loc[0]
                    # if abs(left_x-right_x) >=1000:
                    #     continue
                    l = [lname, lx, ly, lb, left_x, left_y]  # 左端点连接元件的信息
                    r = [rname, rx, ry, rb, right_x, right_y]  # 右端点连接元件的信息
                    file.write(str(l[0]))
                    file.write(' ')
                    file.write(str(l[1]))
                    file.write(' ')
                    file.write(str(l[2]))
                    file.write(' ')
                    file.write(str(l[3]))
                    file.write(' ')
                    file.write(str(l[4]))
                    file.write(' ')
                    file.write(str(l[5]))
                    file.write(' ')
                    file.write(str(r[4]))
                    file.write(' ')
                    file.write(str(r[5]))
                    file.write(' ')
                    file.write(str(r[0]))
                    file.write(' ')
                    file.write(str(r[1]))
                    file.write(' ')
                    file.write(str(r[2]))
                    file.write(' ')
                    file.write(str(r[3]))
                    file.write(' ')
                    file.write('\n')
def main():
    pipei("FD")
    # pipei2("FD")
    # pipei3("FD")
    # pipei4("FD")
if __name__=='__main__':
    main()


