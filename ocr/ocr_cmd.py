import argparse
from ocr_10_12 import *

'''
    此文件为ocr的cmd模块
    使用方法在命令输入：python ocr_cmd.py --path output/
    请--path 后面输入存放图片的主文件夹，将自动识别文件下面所以子文件中的矩形和圆形切片。
'''


# # 初始化参数构造器
# parser = argparse.ArgumentParser()
#
# # 在参数构造器中添加两个命令行参数
# parser.add_argument('--path', type=str, default='output/')
# parser.add_argument('--message', type=str, default='111')
#
# # 获取所有的命令行参数
# args = parser.parse_args()
#调用圆形识别方法，生成的txt文件将保存在图片所在目录中的label下。
path='output/'
rec_circles(path)
#调用矩形识别方法
rec_contours(path)
print("文本识别模块已全部完成！")
