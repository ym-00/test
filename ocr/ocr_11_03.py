import cv2
from paddleocr import PaddleOCR

def getFileName_ocr(path):
    SAMA_X1 = 2803
    SAMA_Y1 = 2897
    SAMA_X2 = 3728
    SAMA_Y2 = 2991

    SAMA_TUHAO_X1 = 2803
    SAMA_TUHAO_Y1 = 3040
    SAMA_TUHAO_X2 = 3728
    SAMA_TUHAO_Y2 = 3080

    SAMA_XT_X1 = 2843
    SAMA_XT_Y1 = 3125
    SAMA_XT_X2 = 3000
    SAMA_XT_Y2 = 3174

    SAMA_BANTBEN_X1 = 3179
    SAMA_BANTBEN_Y1 = 3133
    SAMA_BANTBEN_X2 = 3247
    SAMA_BANTBEN_Y2 = 3170

    SAMA_YEHAO_X1 = 3470
    SAMA_YEHAO_Y1 = 3131
    SAMA_YEHAO_X2 = 3639
    SAMA_YEHAO_Y2 = 3171

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

    if 'SAMA' in str(path):
        file_1 = []
        img =cv2.imread(path)
        name_img =img[SAMA_Y1:SAMA_Y2,SAMA_X1:SAMA_X2]
        tuhao_img = img[SAMA_TUHAO_Y1:SAMA_TUHAO_Y2,SAMA_TUHAO_X1:SAMA_TUHAO_X2]
        xt_img = img[SAMA_XT_Y1:SAMA_XT_Y2,SAMA_XT_X1:SAMA_XT_X2]
        bb_img = img[SAMA_BANTBEN_Y1:SAMA_BANTBEN_Y2,SAMA_BANTBEN_X1:SAMA_BANTBEN_X2]
        yh_img =img[SAMA_YEHAO_Y1:SAMA_YEHAO_Y2,SAMA_YEHAO_X1:SAMA_YEHAO_X2]
        ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)

        result_1 = ocr.ocr(name_img, cls=False)
        result_2 = ocr.ocr(tuhao_img, cls=False)
        result_3 = ocr.ocr(xt_img, cls=False)
        result_4 = ocr.ocr(bb_img, cls=False)
        result_5 = ocr.ocr(yh_img, cls=False)
        file_1.append(result_1[0][1][0])
        file_1.append(result_2[0][1][0])
        file_1.append(result_3[0][1][0])
        file_1.append(result_4[0][1][0])
        file_1.append(result_5[0][1][0])
        return file_1
    elif 'FD' in path:
        file = []
        img = cv2.imread(path)
        name_img = img[FD_Y1:FD_Y2, FD_X1:FD_X2]
        sbt_img = img[FD_TYPE_Y1:FD_TYPE_Y2,FD_TYPE_X1:FD_TYPE_X2]
        gd_img = img[FD_GONGDIAN_Y1:FD_GONGDIAN_Y2,FD_GONGDIAN_X1:FD_GONGDIAN_X2]
        cyj_img = img[FD_CAIYOU_Y1:FD_CAIYOU_Y2,FD_CAIYOU_X1:FD_CAIYOU_X2]
        dq_img = img[FD_DQT_Y1:FD_DQT_Y2,FD_DQT_X1:FD_DQT_X2]
        ky_img = img[FD_KY_Y1:FD_KY_Y2, FD_KY_X1:FD_KY_X2]
        xt_img = img[FD_XT_Y1:FD_XT_Y2, FD_XT_X1:FD_XT_X2]
        tuhao_img = img[FD_TUHAO_Y1:FD_TUHAO_Y2,FD_TUHAO_X1:FD_TUHAO_X2]
        banben_img = img[FD_BANBEN_Y1:FD_BANBEN_Y2,FD_BANBEN_X1:FD_BANBEN_X2]
        yehao_img = img[FD_YEHAO_Y1:FD_YEHAO_Y2, FD_YEHAO_X1:FD_YEHAO_X2]
        ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch', show_log=False)
        result_1 = ocr.ocr(name_img, cls=False)
        result_2 = ocr.ocr(sbt_img, cls=False)
        result_3 = ocr.ocr(gd_img, cls=False)
        result_4 = ocr.ocr(cyj_img, cls=False)
        result_5 = ocr.ocr(dq_img, cls=False)
        result_6 = ocr.ocr(ky_img, cls=False)
        result_7 = ocr.ocr(xt_img, cls=False)
        result_8 = ocr.ocr(tuhao_img, cls=False)
        result_9 = ocr.ocr(banben_img, cls=False)
        result_10 = ocr.ocr(yehao_img, cls=False)
        file.append(result_1[0][1][0])
        file.append(result_2[0][1][0])
        file.append(result_3[0][1][0])
        file.append(result_4[0][1][0])
        file.append(result_5[0][1][0])
        file.append(result_6[0][1][0])
        file.append(result_7[0][1][0])
        file.append(result_8[0][1][0])
        file.append(result_9[0][1][0])
        file.append(result_10[0][1][0])


        print(file)
        return result_1[0][1][0]
    else:
        print("文件名不包含SAMA和FD")

if __name__=='__main__':
    path_fd = 'input_FD/images_17.jpg'
    path_sama = 'input_SAMA/images_18.jpg'
    result = getFileName_ocr(path_fd)
    print(result)