#   coding=gbk
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import cv2
from paddleocr import PaddleOCR
from tuyuan.mods import getFileList
from multiprocessing import Pool, cpu_count
import time


def err_call_back(err):
    print(f'{str(err)}')


def info_FD_work(basename, images, i):
    FD_X1 = 2830
    FD_Y1 = 2732
    FD_X2 = 3526
    FD_Y2 = 2814
    FD_TYPE_X1 = 3040
    FD_TYPE_Y1 = 2933
    FD_TYPE_X2 = 3250
    FD_TYPE_Y2 = 3000

    FD_GONGDIAN_X1 = 3040
    FD_GONGDIAN_Y1 = 3030
    FD_GONGDIAN_X2 = 3250
    FD_GONGDIAN_Y2 = 3090

    FD_CAIYOU_X1 = 3040
    FD_CAIYOU_Y1 = 3118
    FD_CAIYOU_X2 = 3250
    FD_CAIYOU_Y2 = 3176

    FD_DQT_X1 = 3632
    FD_DQT_Y1 = 2938
    FD_DQT_X2 = 3827
    FD_DQT_Y2 = 2998

    FD_KY_X1 = 3632
    FD_KY_Y1 = 3031
    FD_KY_X2 = 3827
    FD_KY_Y2 = 3090

    FD_XT_X1 = 3632
    FD_XT_Y1 = 3122
    FD_XT_X2 = 3795
    FD_XT_Y2 = 3178

    FD_TUHAO_X1 = 4040
    FD_TUHAO_Y1 = 3032
    FD_TUHAO_X2 = 4450
    FD_TUHAO_Y2 = 3080

    FD_BANBEN_X1 = 3960
    FD_BANBEN_Y1 = 3120
    FD_BANBEN_X2 = 4056
    FD_BANBEN_Y2 = 3171

    FD_YEHAO_X1 = 4244
    FD_YEHAO_Y1 = 3119
    FD_YEHAO_X2 = 4410
    FD_YEHAO_Y2 = 3172
    if not os.path.isdir(f'output_info/output_FD'):
        os.makedirs(f'output_info/output_FD')
    file = open(f'output_info/output_FD/{basename}_info.txt', mode='w')
    file.write('image_name')
    file.write(' ')
    file.write('shebei_type')
    file.write(' ')
    file.write('power_sys')
    file.write(' ')
    file.write('gongdian')
    file.write(' ')
    file.write('jiekou')
    file.write(' ')
    file.write('rongyu')
    file.write(' ')
    file.write('system_num')
    file.write(' ')
    file.write('image_num')
    file.write(' ')
    file.write('version')
    file.write(' ')
    file.write('page_num')
    file.write('\n')

    img = cv2.imread(images[i])
    name_img = img[FD_Y1:FD_Y2, FD_X1:FD_X2]
    sbt_img = img[FD_TYPE_Y1:FD_TYPE_Y2, FD_TYPE_X1:FD_TYPE_X2]
    gd_img = img[FD_GONGDIAN_Y1:FD_GONGDIAN_Y2, FD_GONGDIAN_X1:FD_GONGDIAN_X2]
    cyj_img = img[FD_CAIYOU_Y1:FD_CAIYOU_Y2, FD_CAIYOU_X1:FD_CAIYOU_X2]
    dq_img = img[FD_DQT_Y1:FD_DQT_Y2, FD_DQT_X1:FD_DQT_X2]
    ky_img = img[FD_KY_Y1:FD_KY_Y2, FD_KY_X1:FD_KY_X2]
    xt_img = img[FD_XT_Y1:FD_XT_Y2, FD_XT_X1:FD_XT_X2]
    tuhao_img = img[FD_TUHAO_Y1:FD_TUHAO_Y2, FD_TUHAO_X1:FD_TUHAO_X2]
    banben_img = img[FD_BANBEN_Y1:FD_BANBEN_Y2, FD_BANBEN_X1:FD_BANBEN_X2]
    yehao_img = img[FD_YEHAO_Y1:FD_YEHAO_Y2, FD_YEHAO_X1:FD_YEHAO_X2]
    ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)
    result_1 = ocr.ocr(name_img, cls=False)
    print(result_1)
    result_2 = ocr.ocr(sbt_img, cls=False)
    print(result_2)
    result_3 = ocr.ocr(gd_img, cls=False)
    print(result_3)
    result_4 = ocr.ocr(cyj_img, cls=False)
    print(result_4)
    result_5 = ocr.ocr(dq_img, cls=False)
    print(result_5)
    result_6 = ocr.ocr(ky_img, cls=False)
    print(result_6)
    result_7 = ocr.ocr(xt_img, cls=False)
    print(result_7)
    result_8 = ocr.ocr(tuhao_img, cls=False)
    print(result_8)
    result_9 = ocr.ocr(banben_img, cls=False)
    print(result_9)
    result_10 = ocr.ocr(yehao_img, cls=False)
    print(result_10)

    if len(result_1) == 0:
        file.write('null')
        file.write(' ')
    else:
        print(result_1, len(result_1))
        file_name = result_1[0][1][0]
        name_pre = file_name[:3]
        name_af = file_name[3:]
        if 'o' in name_af:
            name_af = name_af.replace('o', '0')
        if 'O' in name_af:
            name_af = name_af.replace('O', '0')
        if ' ' in name_af:
            name_af = name_af.replace(' ', '')

        file_name_1 = name_pre + name_af
        file.write(str(file_name_1))
        file.write(' ')
    if len(result_2) == 0:
        file.write('null')
        file.write(' ')
    else:
        file.write(str(result_2[0][1][0]))
        file.write(' ')
    if len(result_3) == 0:
        file.write('null')
        file.write(' ')
    else:
        file.write(str(result_3[0][1][0]))
        file.write(' ')
    if len(result_4) == 0:
        file.write('null')
        file.write(' ')
    else:
        file.write(str(result_4[0][1][0]))
        file.write(' ')
    if len(result_5) == 0:
        file.write('null')
        file.write(' ')
    else:
        file_name_1 = result_5[0][1][0]
        if ' ' in file_name_1:
            file_name_1 = file_name_1.replace(' ', '')
        file.write(str(file_name_1))
        file.write(' ')
    if len(result_6) == 0:
        file.write('null')
        file.write(' ')
    else:
        file.write(str(result_6[0][1][0]))
        file.write(' ')
    if len(result_7) == 0:
        file.write('null')
        file.write(' ')
    else:
        file.write(str(result_7[0][1][0]))
        file.write(' ')
    if len(result_8) == 0:
        file.write('null')
        file.write(' ')
    else:
        file_name = result_8[0][1][0]
        if 'YVM0YKS' in file_name and file_name[-2:] == '33':
            file_name = file_name[:-2] + '35'
        file.write(str(file_name))
        file.write(' ')
    if len(result_9) == 0:
        file.write('null')
        file.write(' ')
    else:

        file.write(str(result_9[0][1][0]))
        file.write(' ')
    if len(result_10) == 0:
        file.write('null')
        file.write('\n')
    else:

        file.write(str(result_10[0][1][0]))
        file.write('\n')


def getFileName_ocr(method):


    number = int(cpu_count() / 2)
    pool = Pool(processes=number)
    start = time.time()
    path = f'input_{method}'
    images = getFileList(path, [], 'jpg')
    images.sort()
    print(images)
    len_0 = len(images)
    for i in range(len_0):
        if '\\' in images[i]:
            images[i] = images[i].replace('\\', '/')
        print(images[i])
        image_no = os.path.basename(images[i])
        basename = os.path.splitext(image_no)[0]

        if 'FD' in path:
            pool.apply_async(info_FD_work, (basename, images, i,), error_callback=err_call_back)
        else:
            print("????????????FD")
    pool.close()
    pool.join()
    end = time.time()
    print("??????????????????   ??????????", end - start, "seconds")


if __name__ == '__main__':
    getFileName_ocr('FD')
# SAMA_X1 = 2803
#     SAMA_Y1 = 2897
#     SAMA_X2 = 3728
#     SAMA_Y2 = 2991
#
#     SAMA_TUHAO_X1 = 2803
#     SAMA_TUHAO_Y1 = 3040
#     SAMA_TUHAO_X2 = 3728
#     SAMA_TUHAO_Y2 = 3080
#
#     SAMA_XT_X1 = 2843
#     SAMA_XT_Y1 = 3125
#     SAMA_XT_X2 = 3000
#     SAMA_XT_Y2 = 3174
#
#     SAMA_BANTBEN_X1 = 3179
#     SAMA_BANTBEN_Y1 = 3133
#     SAMA_BANTBEN_X2 = 3247
#     SAMA_BANTBEN_Y2 = 3170
#
#     SAMA_YEHAO_X1 = 3470
#     SAMA_YEHAO_Y1 = 3131
#     SAMA_YEHAO_X2 = 3639
#     SAMA_YEHAO_Y2 = 3171
# if 'SAMA' in path:
        #     if not os.path.isdir(f'output_info/output_SAMA'):
        #         os.makedirs(f'output_info/output_SAMA')
        #     file = open(f'output_info/output_SAMA/output_{i}_info.txt', 'w')
        #     file.write('image_name')
        #     file.write(' ')
        #     file.write('image_number')
        #     file.write(' ')
        #     file.write('system_number')
        #     file.write(' ')
        #     file.write('version')
        #     file.write(' ')
        #     file.write('page_number')
        #     file.write('\n')
        #     img =cv2.imread(path+'/'+images[i])
        #     name_img =img[SAMA_Y1:SAMA_Y2,SAMA_X1:SAMA_X2]
        #     tuhao_img = img[SAMA_TUHAO_Y1:SAMA_TUHAO_Y2,SAMA_TUHAO_X1:SAMA_TUHAO_X2]
        #     xt_img = img[SAMA_XT_Y1:SAMA_XT_Y2,SAMA_XT_X1:SAMA_XT_X2]
        #     bb_img = img[SAMA_BANTBEN_Y1:SAMA_BANTBEN_Y2,SAMA_BANTBEN_X1:SAMA_BANTBEN_X2]
        #     yh_img =img[SAMA_YEHAO_Y1:SAMA_YEHAO_Y2,SAMA_YEHAO_X1:SAMA_YEHAO_X2]
        #     ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)
        #
        #     result_1 = ocr.ocr(name_img, cls=False)
        #     result_2 = ocr.ocr(tuhao_img, cls=False)
        #     result_3 = ocr.ocr(xt_img, cls=False)
        #     result_4 = ocr.ocr(bb_img, cls=False)
        #     result_5 = ocr.ocr(yh_img, cls=False)
        #     file.write(str(result_1[0][1][0]))
        #     file.write(' ')
        #     file.write(str(result_2[0][1][0]))
        #     file.write(' ')
        #     file.write(str(result_3[0][1][0]))
        #     file.write(' ')
        #     file.write(str(result_4[0][1][0]))
        #     file.write(' ')
        #     file.write(str(result_5[0][1][0]))
        #     file.write('\n')
        #     return file