#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import numpy as np

_author_ = '张起凡'
imgname = sys.argv[1]
print(imgname)
classfy=sys.argv[2]
print(classfy)
data_s = np.loadtxt("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/output_line.txt",dtype=int)
row=len(data_s)
open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/output_line.txt", "w").close()
for i in range(row):
    x1,y1,x2,y2,belong=data_s[i]
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)
    belong=int(belong)
    if abs(x1-x2)<=5:
        print("竖线")
        if y1>y2:
            data_s[i]=[x2,y2,x1,y1,belong]
    else:
        print("横线或者斜线")
        if x1>x2:
            data_s[i]=[x2,y2,x1,y1,belong]
for i in range(row):
    x1,y1,x2,y2,belong=data_s[i]
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)
    belong = int(belong)
    file = open("xianduan/xianduan/xianduanjiance/"+classfy+"_result/"+imgname+"/output_line.txt", 'a')
    file.write(str(x1))
    file.write(' ')
    file.write(str(y1))
    file.write(' ')
    file.write(str(x2))
    file.write(' ')
    file.write(str(y2))
    file.write(' ')
    file.write(str(belong))
    file.write('\n')
    file.close()