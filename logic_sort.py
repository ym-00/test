import os
import shutil

import cv2
import numpy as np
from tuyuan.mods import getFileList
def zhenghe():
    count_0 = 0
    for root, dirs, files in os.walk("output_FD"):
        dirs.sort()
        for f in dirs:
            path = os.path.join(root, f)
            print(path)
            if os.path.exists(path+'/logic.txt'):
                lines = np.loadtxt(path+'/logic.txt', dtype=str,ndmin=2)
                file = open(path+'/label'+"/"+f+'_l.txt', 'a')
                print(file)
                file.write('\n')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                file.write(' ')
                file.write('End2')
                for line in lines:
                    name, p, x1, y1, x2, y2 = line
                    name = name + '_' + str(count_0)
                    file.write('\n')
                    file.write(str(name))
                    file.write(' ')
                    file.write(str(x1))
                    file.write(' ')
                    file.write(str(y1))
                    file.write(' ')
                    file.write(str(x1))
                    file.write(' ')
                    file.write(str(y2))
                    file.write(' ')
                    file.write(str(x2))
                    file.write(' ')
                    file.write(str(y1))
                    file.write(' ')
                    file.write(str(x2))
                    file.write(' ')
                    file.write(str(y2))
                    file.write(' ')
                    file.write(str(name))
                    count_0 = count_0 + 1
                file.close()
        break


def main():
    zhenghe()
    # os.system('python yolov5/detect.py --source yolov5/data/images/images_5.jpg --weights yolov5/pretrained/best.pt --savedir output/output_4/')
if __name__ == '__main__':
    main()