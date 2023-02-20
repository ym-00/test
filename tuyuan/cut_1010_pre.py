import glob
import os
import cv2
import sys
from tuyuan.mods import getFileList

# if len(sys.argv) > 1:
#     img_type = sys.argv[1]
#     print('The Method is '+ img_type)
#
# if len(sys.argv) > 2:
#     paths = sys.argv[2]
#     print('The input path is ' + paths)


'''
用于逻辑图元涂白的前置切割操作，
'''


def cut_func_pre(img_type: str, paths: str):

    area_1_x_start, area_1_x_end = 0, 0
    area_2_x_start, area_2_x_end = 0, 0
    area_3_x_start, area_3_x_end = 0, 0
    area_4_x_start, area_4_x_end = 0, 0
    area_5_x_start, area_5_x_end = 0, 0
    area_1_y_start, area_1_y_end = 0, 0
    area_2_y_start, area_2_y_end = 0, 0
    area_3_y_start, area_3_y_end = 0, 0
    area_4_y_start, area_4_y_end = 0, 0
    area_5_y_start, area_5_y_end = 0, 0

    if img_type == 'FD':
        area_1_x_start, area_1_x_end = 237, 663
        area_2_x_start, area_2_x_end = 668, 1184
        area_3_x_start, area_3_x_end = 1189, 3656
        area_4_x_start, area_4_x_end = 3661, 4155
        area_5_x_start, area_5_x_end = 4159, 4596
        area_1_y_start, area_1_y_end = 67, 2715
        area_2_y_start, area_2_y_end = 67, 2715
        area_3_y_start, area_3_y_end = 67, 2715
        area_4_y_start, area_4_y_end = 67, 2715
        area_5_y_start, area_5_y_end = 67, 2715

    elif img_type == 'SAMA':
        area_1_x_start, area_1_x_end = 237, 4596
        area_2_x_start, area_2_x_end = 237, 4596
        area_3_x_start, area_3_x_end = 237, 4596
        area_4_x_start, area_4_x_end = 237, 4596
        area_5_x_start, area_5_x_end = 237, 4596
        area_1_y_start, area_1_y_end = 67, 425
        area_2_y_start, area_2_y_end = 430, 2171
        area_3_y_start, area_3_y_end = 2176, 2534
        area_4_y_start, area_4_y_end = 2539, 2874
        area_5_y_start, area_5_y_end = 2539, 2874

    imgPath = paths
    '''
     11-11日新增代码，用于遍历输入文件夹对其重新排序  ----1-》01.jpg
    '''
    files_1 = glob.glob(imgPath + '/*.jpg')
    print("\033[32m共检索到图片数量：{}\033[0m".format(len(files_1)))
    for i in files_1:
        name = os.path.basename(imgPath + i)
        name = str(name)
        name = name.replace('images_', '')
        name = name.replace('.jpg', '')
        src = os.path.join(os.path.abspath(''),i)
        if len(name) == 1:
            up_name = '0' + name
            dst = os.path.join(os.path.abspath(imgPath + '/'), 'images_' + up_name + '.jpg')
            os.rename(src,dst)

    count = 0  # 记录图纸的个数

    files = getFileList(imgPath,[],'jpg')
    files.sort()
    for file in files:
        print(file)
        print('正在裁切第 {} 张图片'.format(count + 1))
        outputPath = f"./output_{img_type}"
        # if not os.path.isdir(outputPath+"/output_%d" % count):  # 创建文件夹
        #     os.makedirs(outputPath+"/output_%d" % count)

        if count < 10:
            if not os.path.isdir(outputPath+"/output_0%d" % count):
                os.makedirs(outputPath + "/output_0%d" % count)
        else:
            if not os.path.isdir(outputPath + "/output_%d" % count):
                os.makedirs(outputPath+"/output_%d" % count)
        # [y:y, x:x],第一个坐标是纵坐标 第二个是横坐标 以左上角为(0, 0)开始
        img = cv2.imread(file)
        img_cut_1 = img[area_1_y_start:area_1_y_end, area_1_x_start: area_1_x_end]
        img_cut_2 = img[area_2_y_start:area_2_y_end, area_2_x_start: area_2_x_end]
        img_cut_3 = img[area_3_y_start:area_3_y_end, area_3_x_start: area_3_x_end]
        img_cut_4 = img[area_4_y_start:area_4_y_end, area_4_x_start: area_4_x_end]
        img_cut_5 = img[area_5_y_start:area_5_y_end, area_5_x_start: area_5_x_end]
        img_cut_6 = img[area_1_y_start:area_5_y_end, area_1_x_start: area_5_x_end]
        if not os.path.isdir('path/'):  # 创建文件夹
            os.makedirs('path/')
        if count <10:
            if not os.path.isdir(outputPath + "/output_0%d/area" % count):  # 创建文件夹
                os.makedirs(outputPath + "/output_0%d/area" % count)
            if not os.path.isdir(outputPath + "/output_0%d/" % count + "0%d" % count):  # 创建文件夹
                os.makedirs(outputPath + "/output_0%d/" % count + "0%d" % count)
        else:
            if not os.path.isdir(outputPath + "/output_%d/area" % count):  # 创建文件夹
                os.makedirs(outputPath + "/output_%d/area" % count)
            if not os.path.isdir(outputPath + "/output_%d/" % count + "%d" % count):  # 创建文件夹
                os.makedirs(outputPath + "/output_%d/" % count + "%d" %count)
        if count < 10:
            img_save_path = outputPath + '/output_0%d/area/' % count
        else:
            img_save_path = outputPath + '/output_%d/area/' % count

        #11-08修改-----
        # cv2.imwrite(img_save_path + "img_cut_1.jpg", img_cut_1)
        # cv2.imwrite(img_save_path + "img_cut_2.jpg", img_cut_2)
        # cv2.imwrite(img_save_path + "img_cut_3.jpg", img_cut_3)
        # cv2.imwrite(img_save_path + "img_cut_4.jpg", img_cut_4)
        # cv2.imwrite(img_save_path + "img_cut_5.jpg", img_cut_5)
        # cv2.imwrite(img_save_path + "start(237,67)___img_cut_6.jpg", img_cut_6)
        # cv2.imwrite("./output/output_%d/start(237,67)___img_cut_6.jpg", img_cut_6)
        # cv2.imwrite(outputPath+'/output_%d/img_clean.jpg' % count, img_cut_6)
        # cv2.imwrite(outputPath+'/output_%d/img_mark.jpg' % count, img_cut_6)
        if count < 10 :
            cv2.imwrite(outputPath + '/output_0%d/' % count + "0%d/img_org.jpg" % count, img)
            cv2.imwrite('./path/output_0%d.jpg' % count, img_cut_6)
        else:
            cv2.imwrite(outputPath + '/output_%d/' % count + "%d/img_org.jpg" % count, img)
            cv2.imwrite('./path/output_%d.jpg' % count, img_cut_6)



        count = count + 1

def main():
    cut_func_pre('FD', './input_FD')
if __name__ == '__main__':
    main()
