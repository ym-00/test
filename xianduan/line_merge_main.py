import os
import sys

import cv2
import numpy as np


def f1(data_s, index_line, index_line1, index_line2):
    img = cv2.imread('xianduan/common_picture.jpg')
    img = np.copy(img) * 0
    output_str = 'xianduan/xianduan/xianduanjiance/test/out_test_' + str(index_line) + '_lines_' + str(index_line1) + '_' + str(index_line2) + '.jpg'
    #draw_line_merge(img, data_s, output_str)


def draw_line_merge(img, data_s, output_str='output_0.jpg'):
    for data in data_s:
        x1, y1, x2, y2, belong = data
        if (belong >= 0):
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        else:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    #cv2.imwrite(output_str, img)


def check_and_merge(data_s, index_line1, index_line2, line1_point, line2_point):
    '''
    检查并合并： line1 点1  与  line2 点2
    line1点1=(line1_x1,line2_y1)
    line2点2=(line2_x1,line2_y1)
    return: 是否发生了合并，True 则表示发生了合并
    '''
    # 以 check_if_close(line1_x1, line1_y1, line2_x1, line2_y1) 为例
    # 进入的条件是检查发现，line1 点1 与 line2 点1 接近

    # 检查有几个线段是小圆点线段
    n = count_if_in_group(data_s, index_line1, index_line2)

    line1_x1, line1_y1, line1_x2, line1_y2, line1_group = data_s[index_line1]
    line2_x1, line2_y1, line2_x2, line2_y2, line2_group = data_s[index_line2]

    # n==0 和原来一样
    if (n == 0):
        line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2 = 0, 0, 0, 0
        if (line1_point == 1):
            line_merge_x1 = line1_x2
            line_merge_y1 = line1_y2
        elif (line1_point == 2):
            line_merge_x1 = line1_x1
            line_merge_y1 = line1_y1

        if (line2_point == 1):
            line_merge_x2 = line2_x2
            line_merge_y2 = line2_y2
        elif (line2_point == 2):
            line_merge_x2 = line2_x1
            line_merge_y2 = line2_y1
        data_s[index_line1] = line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2, line1_group
        data_s = np.delete(data_s, index_line2, axis=0)

        f1(data_s, data_s.shape[0], index_line1, index_line2)
        return data_s, True

    # n==2 不做任何操作
    elif (n == 2):
        return data_s, False

    elif (n == 11 or n == 22):
        # 如果line1 是重合线段
        if (n == 11):
            # line1 点 1
            if (line1_point == 1):
                if (check_if_point_of_group(data_s, line1_x1, line1_y1, index_line1)):
                    list_return = count_lines_in_group(data_s, line1_x1, line1_y1, index_line1)
                    data_s = merge_group_and_line(data_s, list_return, line2_x1, line2_y1, index_line2)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True
                else:
                    line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2 = 0, 0, 0, 0
                    if (line1_point == 1):
                        line_merge_x1 = line1_x2
                        line_merge_y1 = line1_y2
                    elif (line1_point == 2):
                        line_merge_x1 = line1_x1
                        line_merge_y1 = line1_y1

                    if (line2_point == 1):
                        line_merge_x2 = line2_x2
                        line_merge_y2 = line2_y2
                    elif (line2_point == 2):
                        line_merge_x2 = line2_x1
                        line_merge_y2 = line2_y1
                    data_s[index_line1] = line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2, line1_group
                    data_s = np.delete(data_s, index_line2, axis=0)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True

            # line1 点 2
            elif (line1_point == 2):
                if (check_if_point_of_group(data_s, line1_x2, line1_y2, index_line1)):
                    list_return = count_lines_in_group(data_s, line1_x2, line1_y2, index_line1)
                    data_s = merge_group_and_line(data_s, list_return, line2_x2, line2_y2, index_line2)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True

                else:
                    line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2 = 0, 0, 0, 0
                    if (line1_point == 1):
                        line_merge_x1 = line1_x2
                        line_merge_y1 = line1_y2
                    elif (line1_point == 2):
                        line_merge_x1 = line1_x1
                        line_merge_y1 = line1_y1
                    if (line2_point == 1):
                        line_merge_x2 = line2_x2
                        line_merge_y2 = line2_y2
                    elif (line2_point == 2):
                        line_merge_x2 = line2_x1
                        line_merge_y2 = line2_y1
                    data_s[index_line1] = line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2, line1_group
                    data_s = np.delete(data_s, index_line2, axis=0)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True

        # 如果line2 是重合线段
        elif (n == 22):
            # line2 点 1
            if (line2_point == 1):
                if (check_if_point_of_group(data_s, line2_x1, line2_y1, index_line2)):
                    list_return = count_lines_in_group(data_s, line2_x1, line2_y1, index_line2)
                    data_s = merge_group_and_line(data_s, list_return, line1_x1, line1_y1, index_line1)

                    f1(data_s, data_s.shape[0], index_line2, index_line2)
                    return data_s, True

                else:
                    line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2 = 0, 0, 0, 0
                    if (line1_point == 1):
                        line_merge_x1 = line1_x2
                        line_merge_y1 = line1_y2
                    elif (line1_point == 2):
                        line_merge_x1 = line1_x1
                        line_merge_y1 = line1_y1

                    if (line2_point == 1):
                        line_merge_x2 = line2_x2
                        line_merge_y2 = line2_y2
                    elif (line2_point == 2):
                        line_merge_x2 = line2_x1
                        line_merge_y2 = line2_y1
                    data_s[index_line1] = line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2, line1_group
                    data_s = np.delete(data_s, index_line2, axis=0)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True

            # line2 点 2
            elif (line2_point == 2):
                if (check_if_point_of_group(data_s, line2_x2, line2_y2, index_line2)):
                    list_return = count_lines_in_group(data_s, line2_x2, line2_y2, index_line2)
                    data_s = merge_group_and_line(data_s, list_return, line1_x2, line1_y2, index_line1)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True

                else:
                    line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2 = 0, 0, 0, 0
                    if (line1_point == 1):
                        line_merge_x1 = line1_x2
                        line_merge_y1 = line1_y2
                    elif (line1_point == 2):
                        line_merge_x1 = line1_x1
                        line_merge_y1 = line1_y1
                    if (line2_point == 1):
                        line_merge_x2 = line2_x2
                        line_merge_y2 = line2_y2
                    elif (line2_point == 2):
                        line_merge_x2 = line2_x1
                        line_merge_y2 = line2_y1
                    data_s[index_line1] = line_merge_x1, line_merge_y1, line_merge_x2, line_merge_y2, line1_group
                    data_s = np.delete(data_s, index_line2, axis=0)

                    f1(data_s, data_s.shape[0], index_line1, index_line2)
                    return data_s, True

        print('check_and_merge 发生错误')

    else:
        print('check_and_merge 发生错误')


def count_if_in_group(data_s, line1_index, line2_index):
    '''
    判断这 2 个线段，有几个是 小圆点线段（group >= 0）
    return:
    0 表示均为普通线段
    2 表示均为小圆点线段
    11 表示 line1 为小圆点线段
    22 表示 line2 为小圆点线段
    '''
    a = data_s[line1_index][4]
    b = data_s[line2_index][4]

    if ((a >= 0) and (b >= 0)):
        return 2
    elif (a >= 0):
        return 11
    elif (b >= 0):
        return 22
    else:
        return 0


def check_if_point_of_group(data_s, x, y, index_line, distance_if_close=5):
    '''
    检查这个点是不是所在组（group）的重叠点
    i:index_line 被检查线段的编号
    distance_if_close 被判定为相近的标准(<=)，默认为 5
    '''
    index_line_sum = data_s.shape[0]  # 剩余线段数(行)数
    g = data_s[index_line][4]  # 被检查线段的组号

    for i in range(0, index_line_sum):
        if (i == index_line):
            continue
        # 取出第 i 根线的数据
        x1, y1, x2, y2, group = data_s[i]
        # 首先判断是否同组
        if (g == group):
            # 检查此同组的第 i 根线段的 点1
            if (cauculate_distance(x, y, x1, y1) <= distance_if_close):
                return True
            # 检查此同组的第 i 根线段的 点2
            elif (cauculate_distance(x, y, x2, y2) <= distance_if_close):
                return True
        else:
            continue

    # 如果遍历结束也未能找到
    return False


def count_lines_in_group(data_s, x, y, index_line, distance_if_close=5):
    '''
    概述：输入重叠点，找到其它重叠点
    检查一共有多少个 与 小圆点线段 同组的 小圆点线段（group相等）

    index_line: 被检查的小圆点线段

    return: list_lines_index 返回一个列表，包括同组线段编号的集合（包括被查线段本身，按index升序排列）

    第一列 是 同组线段的编号（行号）
    第二列 是 1 或 2（点1 还是 点2 为重合点）
    '''
    index_line_sum = data_s.shape[0]  # 剩余线段数(行)数
    list_index_group_line = [[[] for i in range(2)] for i in range(index_line_sum)]  # 第1列 存储线段序号，第2列 存储点序号（1或2）
    g = data_s[index_line][4]  # 被检查线段的组号

    line_sum = 0  # 一共找到的同组线段数量

    for i in range(0, index_line_sum):
        # 取出第 i 根线的数据
        x1, y1, x2, y2, group = data_s[i]
        # 首先判断是否同组
        if (g == group):
            # 检查此同组的第 i 根线段的 点1
            if (cauculate_distance(x, y, x1, y1) <= distance_if_close):
                list_index_group_line[line_sum][0] = i
                list_index_group_line[line_sum][1] = 1
                line_sum = line_sum + 1
            # 检查此同组的第 i 根线段的 点2
            elif (cauculate_distance(x, y, x2, y2) <= distance_if_close):
                list_index_group_line[line_sum][0] = i
                list_index_group_line[line_sum][1] = 2
                line_sum = line_sum + 1
            else:
                print('count_lines_in_group 发生错误')

    # 重构 list 二维数组，删掉冗余行（空行）
    list_return = [[[] for i in range(2)] for i in range(line_sum)]
    for i in range(0, line_sum):
        list_return[i][0] = list_index_group_line[i][0]
        list_return[i][1] = list_index_group_line[i][1]

    return list_return


def merge_group_and_line(data, list_line_index, x, y, line_index):
    '''
    list_line_index: 坐标的列表 n行2列
    将 一组线段（的重合点） 与 单根普通线段 合并，
    x,y: 单根普通线段的 x,y
    line_index: 单根普通线段 的 行标
    '''
    n = len(list_line_index)  # 这组中有n行（根）线段

    # 提取 单根普通线段 的数据
    x1, y1, x2, y2, g = data[line_index]
    new_x, new_y = 0, 0

    # 如果是 单根普通线段 的 点1 与 重合点 重合，则重合点要延长到 单根普通线段 的 点2
    if ((x1 == x) and (y1 == y)):
        new_x = x2
        new_y = y2
    # 如果是 单根普通线段 的 点2 与 重合点 重合，则重合点要延长到 单根普通线段 的 点1
    elif ((x2 == x) and (y2 == y)):
        new_x = x1
        new_y = y1
    else:
        print('merge_group_and_line 方法出现错误，错误的 data, list, x, y, line_index ')
        print(data, list, x, y, line_index)

    for i in range(0, n):
        this_line_index = list_line_index[i][0]  # 行号（第几根）
        line_point_index = list_line_index[i][1]  # 坐标号（点1 还是 点2 为重合点）
        list_x1, list_y1, list_x2, list_y2, list_group = data[this_line_index]

        # 如果是 小圆点线段 的 点1 为重合点，则修改  小圆点线段 的 点1，将其延长
        if (line_point_index == 1):
            data[this_line_index] = new_x, new_y, list_x2, list_y2, list_group
        # 如果是 小圆点线段 的 点2 为重合点，则修改  小圆点线段 的 点1，将其延长
        elif (line_point_index == 2):
            data[this_line_index] = list_x1, list_y1, new_x, new_y, list_group
        else:
            print('merge_group_and_line 发生错误')

    # 删掉 单根普通线段 所在行
    data = np.delete(data, line_index, axis=0)
    return data


def cauculate_distance(x1, y1, x2, y2):
    distance = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
    return distance


def check_if_close(line1_x, line1_y, line2_x, line2_y, merge_pixels=20):
    '''
    通过两点距离，检查是否接近
    line1_x: 第一条线的 x 坐标
    merge_pixels: 接近的判定条件
    '''
    if (cauculate_distance(line1_x, line1_y, line2_x, line2_y) < merge_pixels):
        return True
    else:
        return False


def line_merge(data_s, if_show=False):
    flag_if_continue = True  # 是否重新检查
    while (flag_if_continue):
        index_line = data_s.shape[0] - 1  # 剩余线段数行数-1

        for index_line1 in range(0, index_line + 1):  # index_line1

            # group 表示是否为小圆点线段
            # group = -1 表示为普通线段
            line1_x1, line1_y1, line1_x2, line1_y2, line1_group = data_s[index_line1]

            flag_merge = False  # 是否发生了合并
            for index_line2 in range(0, index_line + 1):  # index_line2
                line2_x1, line2_y1, line2_x2, line2_y2, line2_group = data_s[index_line2]

                if (index_line1 == index_line2):
                    if (index_line1 == index_line - 1):
                        flag_merge = True
                        flag_if_continue = False
                        break
                    else:
                        continue
                else:
                    # 检查 线1-点1 与 线2-点1, 如果接近 则
                    if (check_if_close(line1_x1, line1_y1, line2_x1, line2_y1)):
                        data_s, flag_merge = check_and_merge(data_s, index_line1, index_line2, 1, 1)
                        if (flag_merge):
                            break
                    # 检查 线1-点1 与 线2-点2, 如果接近 则
                    elif (check_if_close(line1_x1, line1_y1, line2_x2, line2_y2)):
                        data_s, flag_merge = check_and_merge(data_s, index_line1, index_line2, 1, 2)
                        if (flag_merge):
                            break
                    # 检查 线1-点2 与 线2-点1, 如果接近 则
                    elif (check_if_close(line1_x2, line1_y2, line2_x1, line2_y1)):
                        data_s, flag_merge = check_and_merge(data_s, index_line1, index_line2, 2, 1)
                        if (flag_merge):
                            break
                    # 检查 线1-点2 与 线2-点2, 如果接近 则
                    elif (check_if_close(line1_x2, line1_y2, line2_x2, line2_y2)):
                        data_s, flag_merge = check_and_merge(data_s, index_line1, index_line2, 2, 2)
                        if (flag_merge):
                            break

            if (flag_merge):
                break

    return data_s


def line_merge_main(txt_input, txt_output, img_background, if_show=False):
    '''
    txt_input: 输入的 txt 文件路径，由四列构成 x1,y1,x2,y2
    img_background: 用于绘图时匹配的背景
    if_show: 是否展示合并过程
    '''

    img = cv2.imread('xianduan/common_picture.jpg')
    img = np.copy(img) * 0

    data_s = np.loadtxt(txt_input)
    data_s = data_s.astype(np.int64)  # 变换数据格式

    #draw_line_merge(img, data_s, output_str='xianduan/xianduan/xianduanjiance/test/out_origin.jpg')
    f1(data_s, data_s.shape[0], 0, 0)
    data_s = line_merge(data_s, True)

    # 将结果写回存入到txt
    data_s = np.unique(data_s, axis=0)
    for data in data_s:
        x1, y1, x2, y2, g = data
        x1 = np.int0(x1)
        y1 = np.int0(y1)
        x2 = np.int0(x2)
        y2 = np.int0(y2)
        file = open(txt_output, 'a')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write(' ')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write(' ')
        file.write(str(g))
        file.write('\n')

    img = cv2.imread('xianduan/common_picture.jpg')
    img = np.copy(img) * 0
    #draw_line_merge(img, data_s)


if __name__ == '__main__':
    global data_s
    imgname = sys.argv[1]
    print(imgname)
    classfy = sys.argv[2]
    print(classfy)
    if os.path.exists("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/input_line.txt"):
        open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/output_line.txt", "w").close()
        line_merge_main("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/input_line.txt",
                    "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/output_line.txt", True)
    
    else:
        open("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/output_line.txt", "w").close()
        line_merge_main("xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/data_result_belong.txt",
                        "xianduan/xianduan/xianduanjiance/" + classfy + "_result/" + imgname + "/output_line.txt", True)