import cv2
from paddleocr import PaddleOCR

#用于获取图片的名称
#可直接引用getFileName()函数，path传入图片路径
#result返回图片名称
def getFileName(path):
    SAMA_X1 = 2803
    SAMA_Y1 = 2897
    SAMA_X2 = 3728
    SAMA_Y2 = 2991

    FD_X1 = 2830
    FD_Y1 = 2732
    FD_X2 = 3526
    FD_Y2 = 2814

    if 'SAMA' in str(path):
        img =cv2.imread(path)
        name_img = img[SAMA_Y1:SAMA_Y2,SAMA_X1:SAMA_X2]
        ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch',show_log=False)
        result = ocr.ocr(name_img, cls=False)
        print(result)
        return result[0][1][0]
    elif 'FD' in str(path):
        img = cv2.imread(path)
        name_img = img[FD_Y1:FD_Y2, FD_X1:FD_X2]
        ocr = PaddleOCR(ruse_angle_cls=False, use_gpu=False, lang='ch',show_log=False)
        result = ocr.ocr(name_img, cls=False)
        return result[0][1][0]
    else:
        print("文件名不包含SAMA和FD")

if __name__=='__main__':
    path_fd = 'D:/project/module/inout_FD/images_17.jpg'
    path_sama = 'D:/project/module/input_SAMA/images_18.jpg'
    result = getFileName(path_sama)
    print(result)