import sys

import  numpy as np
import cv2

imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
# image = cv2.imread(r'D:\Program Files (x86)\Pycharm2021\PyCharm 2021.2.3\PycharmProjects\work2\xianduan\xianduanjiance\lines_edges_2.jpg')
image = cv2.imread("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/yuzhi.jpg")
# image = np.copy(image) * 0
data_s = np.loadtxt("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/output_line.txt",dtype=int,usecols=(0,1,2,3))
for data in data_s:
    x1, y1, x2, y2 = data
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
cv2.imwrite("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/final_line.jpg", image)