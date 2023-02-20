import glob
import pandas as pd
import json
import numpy as np
import os
import math
from tuyuan.mods import getFileList

def outjson(paths: str, outimage: str,namess:str):
    dataend = []
    flag = "FD"
    flag1 = "fd"
    if (outimage.endswith("FD") or outimage.endswith("fd")):  #  ��   
        flag = "FD"
    elif (outimage.endswith("SAMA") or outimage.endswith("sama")):
        flag = "SAMA"
    if (outimage.endswith("FD") or outimage.endswith("fd")):  #  ��   
        flag1 = "fd"
    elif (outimage.endswith("SAMA") or outimage.endswith("sama")):
        flag1 = "sama"
    files = glob.glob(paths + '/*.jpg')
    files.sort()
    print(files)
    count = 0  #   ??? ?   
    qqq = ""
    for file in files:
        if count < 10:
            # if file[-2:-1] is 0:
             #   ?        ��    ��
            pa = paths + file
            cutdispose = []
            b = os.path.abspath(pa)
            print(b)
            name = os.path.basename(b)
            name = str(name)
            name = name[-6:-4]
            print(name)
            for i in range(5):
                datah = {}
                rectangle2 = []
                circle2 = []  #?      
                logicgate = []  #  ?       
                j = i + 1
                c = os.path.abspath(outimage)
                datah["chlidpath"] = c + "/output_0%d/area/img_cut_%d.jpg" % (count, j)
                datah["chlidname"] = "img_cut_%d.jpg" % j
                path = outimage + '/output_0%d/contours/img_cut/img_cut_%d/label' % (count, j)
                if os.path.isdir(path):
                    files = []
                    for file in os.listdir(path):
                        if file.endswith(".txt"):
                            file_path = os.path.join(path, file)
                            files.append(file_path)
                    files.sort()
                    for file in files:
                        df1 = pd.read_csv(file, sep='\s+', encoding='UTF-8')
                        len_0 = df1.shape[0]
                        # for i in range(len_0):
                        #     data = df1.loc[i]
                        #     type, name, x, y, w, h, main, out = data
                        #     print(type, name, x, y, w, h, main, out)
                        path = outimage + '/output_0%d/contours/img_cut/img_cut_%d/' % (count, j)
                        dirs = os.listdir(path)
                        dirs.sort()
                        for dir in dirs:
                            pa = path + dir
                            if dir.startswith(df1.iat[0, 6]):
                                a = os.path.abspath(pa)
                        path = outimage + '/output_0%d/label/output_0%d_o.txt' % (count, count)
                        if not os.path.exists(path):
                            path = os.path.abspath(outimage + '/output_0%d/label/output_0%d_o.txt' % (count, j))
                        df2 = pd.read_csv(path, sep='\s+', encoding='UTF-8')
                        for k in range(df2.shape[0]):
                            if str(df2.iat[k, 1]).startswith(str(df1.iat[0, 1])) and str(df2.iat[k,2]).startswith(str(df1.iat[0,2])) and str(df2.iat[k,3]).startswith(str(df1.iat[0,3])):
                                rectangle = {}
                                childrectangle = []
                                rectangle["type"] = str(df1.iat[0, 0])
                                rectangle["rectanglepath"] = a
                                rectangle["rectanglename"] = str(df1.iat[0, 1])
                                rectangle["location"] = str(str(int(df2.iat[k, 2]))+"_"+str(int(df2.iat[k, 3])))
                                rectangle["otherrectanglename"] = str(df2.iat[k, 7])  #    ?    bug ?? 
                                if len_0 > 1:
                                    for i in range(len_0):
                                        if i == 0:
                                            continue
                                        path = outimage + '/output_0%d/label/output_0%d_o.txt' % (count, count)
                                        df2 = pd.read_csv(path, sep='\s+', encoding='UTF-8')
                                        for q in range(df2.shape[0]):
                                            if str(df2.iat[q, 1]).startswith(str(df1.iat[i, 1])) and str(df2.iat[q, 2]).startswith(str(df1.iat[i, 2])) and str(df2.iat[q, 3]).startswith(str(df1.iat[i, 3])):
                                                rectangle1 = {}
                                                rectangle1["type"] = str(df1.iat[i, 0])
                                                rectangle1["rectanglename"] = str(df1.iat[i, 1])
                                                rectangle1["location"] = str(df2.iat[q, 2]+"_"+df2.iat[q, 3]+"_"+df2.iat[q, 4]+"_"+df2.iat[q, 5])
                                                rectangle1["otherrectangle"] = str(df2.iat[q, 7])
                                                childrectangle.append(rectangle1)
                                                break
                                rectangle["childrectangle"] = childrectangle
                                rectangle2.append(rectangle)
                    datah["rectangle"] = rectangle2
                path1 = outimage + '/output_0%d/circles/img_cut_%d_circles/label' % (count, j)
                if os.path.isdir(path1):
                    files = []
                    path1list=os.listdir(path1)
                    path1list.sort()
                    for file in path1list:
                        if file.endswith(".txt"):
                            file_path = os.path.join(path1, file)
                            files.append(file_path)
                    files.sort()
                    for file in files:
                        df1 = pd.read_csv(file, sep='\s+', encoding='UTF-8')
                        path = outimage + r'/output_0%d/circles/img_cut_%d_circles/' % (count, j)
                        dirs = os.listdir(path)
                        dirs.sort()
                        for dir in dirs:
                            pa = path + dir
                            if dir.startswith(df1.iat[0, 6]):
                                a = os.path.abspath(pa)
                        path = outimage + r'/output_0%d/label/output_0%d_o.txt' % (count, count)
                        df2 = pd.read_csv(path, sep='\s+', encoding='UTF-8')
                        for i in range(df2.shape[0]):
                            if str(df2.iat[i, 1]).startswith(str(df1.iat[0, 1])) and str(df2.iat[i,2]) == str(df1.iat[0,2]):
                                circle = {}
                                circle["circlepath"] = a
                                circle["circlename"] = str(df1.iat[0, 1])
                                circle["location"] = str(df1.iat[0, 6])
                                circle["othercircle"] = str(df2.iat[i, 7])
                                circle["type"] = str(df1.iat[0, 0])
                                circle2.append(circle)
                                break 
                    datah["circle"] = circle2
                line_edge_image = {}
                binaryimage = {}
                path = outimage + '/output_0%d/' % count
                dirs = os.listdir(path)
                dirs.sort()
                for dir in dirs:
                    pa = path + dir
                    if dir.startswith("binary_img_cut_%d" %j):
                        a = os.path.abspath(pa)
                        binaryimage["binaryimagepath"] = a
                        binaryimage["binaryimagename "] = str(dir)
                        datah["binaryimage"] = [binaryimage]
                for dir in dirs:
                    pa = path + dir
                    if dir.startswith("line_edges_img_cut_%d" %j):
                        a = os.path.realpath(pa)
                        line_edge_image["line_edge_path"] = a
                        line_edge_image["line_edge_name"] = str(dir)
                        datah["line_edge_image"] = [line_edge_image]
                cutdispose.append(datah)

            # datah = {}
            # datah["chlidpath"] = "D:/project/module/output_SAMA/output_0/area/img_cut_1.jpg"
            # datah["chlidname"] = "img_cut_1.jpg"
            # datah["rectangle"] = rectangle2
            # datah["circle"] = [circle]
            # datah["binaryimage"] = [binaryimage]
            # datah["line_edge_image"] = [line_edge_image]

            datag = {}  # wholedispose
            datag["nodottedline"] = os.path.abspath("line/" + flag + "_nodottedline/output_0%d.jpg") % count
            datag["removecircle"] = os.path.abspath("xianduan/" + flag1 + "_circle_out/output_0%d.jpg") % count
            datag["mark"] = os.path.abspath(outimage + "/output_0%d/img_mark.jpg") % count
            datag["clean"] = os.path.abspath(outimage + "/output_0%d/img_clean.jpg") % count
            df2 = pd.read_csv('xianduan/xianduan/xianduanjiance/' + flag1 + '_result/output_0%d/output_line.txt' % count,
                              sep='\s+', encoding='UTF-8',header=None,names=['x1','y1','x2','y2','z'])
            len_1 = df2.shape[0]
            line = []
            for i in range(len_1):
                dataf = {}  # line1
                dataf["x1"] = str(df2.iat[i,0])
                dataf["y1"] = str(df2.iat[i,1])
                dataf["x2"] = str(df2.iat[i,2])
                dataf["y2"] = str(df2.iat[i,3])
                line.append(dataf)

            datad = {}  # line
            datad["linepath"] = os.path.abspath(
                "xianduan/xianduan/xianduanjiance/" + flag1 + "_result/output_0%d/output_line.txt") % count
            datad["line1"] = line
            datal = []
            df10 = pd.read_csv('./output_' + flag + '/output_0%d/label/output_0%d_l.txt' % (count, count), sep='\s+', encoding='UTF-8')  # �����߶���Ϣ���ļ���
            len_0 = df10.shape[0]
            flag2 = 0  # ������ʶֻ����End2����Ķ�������ΪEnd2����Ķ��������߼���
            type = ""  # �߼��ŵ�����
            for i in range(len_0):
                if str(df10.iat[i, 0]) == "End2":
                    flag2 = 1
                if flag2 == 0 or str(df10.iat[i, 0]) == "End2":
                    continue
                if str(df10.iat[i, 0]).startswith("and"):
                    type = "and"
                elif str(df10.iat[i, 0]).startswith("or"):
                    type = "or"
                elif str(df10.iat[i, 0]).startswith("not"):
                    type = "not"
                a = 0  # �������������
                bbbb = 0  # �������������
                df1 = pd.read_csv('./output_FD'+ f'/output_0{count}/label/dianxian.txt', sep='\s+', encoding='UTF-8')
                len_1 = df1.shape[0]
                for k in range(len_1):
                    if df10.iat[i, 0] == df1.iat[k, 0]:
                        a = a + 1
                    elif df10.iat[i, 0] == df1.iat[k, 8]:
                        bbbb = bbbb + 1
                datalogic = {}
                path = outimage + '/output_0%d/logic/' % count
                dirs = os.listdir(path)
                dirs.sort()
                abspath = ""
                for dir in dirs:
                    pa = path + dir
                    ps= str(str(type)+"_"+df10.iat[i, 1]+"_"+df10.iat[i, 2])
                    if dir.startswith(ps):
                        abspath = os.path.abspath(pa)
                datalogic["logic_image_path"] = abspath
                datalogic["type"] = str(type)
                datalogic["name"] = str(df10.iat[i, 0])
                datalogic["logic_location"] = str(int(df10.iat[i, 1]))+"_"+ str(int(df10.iat[i, 2]))
                datalogic["outnumber"] = str(a)
                datalogic["intnumber"] = str(bbbb)
                datal.append(datalogic)
            df1 = pd.read_csv(f'./output_{flag}/output_0{count}/label/dianxian.txt', sep='\s+', encoding='UTF-8')
            len_0 = df1.shape[0]
            connected = []
            for i in range(len_0):
                flag10 = ""     #������ֵ����
                datac = {}  # connected
                datac["pinA_name"] = str(df1.iat[i, 0])
                if str(df1.iat[i, 0]).startswith("circle"):
                    flag10 = "circles"
                elif str(df1.iat[i, 0]).startswith("and"):
                    flag10 = "and"
                elif str(df1.iat[i, 0]).startswith("or"):
                    flag10 = "or"
                elif str(df1.iat[i, 0]).startswith("not"):
                    flag10 = "not"
                else:
                    flag10 = "contour"
                datac["pinA_type"] = str(flag10)
                # df2 = pd.read_csv('./output_' + flag + '/output_0%d/label/output_0%d_l.txt' % (count, count), sep='\s+', encoding='UTF-8')  # �����߶���Ϣ���ļ���
                # len_2 = df2.shape[0]
                # locations = ""  #������¼����
                # for k in range(len_2):
                #     if str(df1.iat[i][1]) == str(df2.iat[k][3]) and str(df1.iat[i][2]) == str(df2.iat[k][2]):
                #         locations = str(df2.iat[i][1])+"_"+str(df2.iat[i][1])            
                if math.isnan(df1.iat[i, 1]) and math.isnan(df1.iat[i, 2]) : 
                    datac["pinA_location"] = str(df1.iat[i, 1])+"_" +str(df1.iat[i, 2])
                else:
                    datac["pinA_location"] = str(int(df1.iat[i, 1]))+"_" +str(int(df1.iat[i, 2]))
                datac["pinA_belong"] = str(df1.iat[i, 3])
                datac["lineA_x"] = str(df1.iat[i, 4])
                datac["lineA_y"] = str(df1.iat[i, 5])
                datac["lineB_x"] = str(df1.iat[i, 6])
                datac["lineB_y"] = str(df1.iat[i, 7])
                datac["pinB_name"] = str(df1.iat[i, 8])
                flag10 = ""  # ������ֵ����
                if str(df1.iat[i, 8]).startswith("circle"):
                    flag10 = "circles"
                elif str(df1.iat[i, 8]).startswith("and"):
                    flag10 = "and"
                elif str(df1.iat[i, 8]).startswith("or"):
                    flag10 = "or"
                elif str(df1.iat[i, 8]).startswith("not"):
                    flag10 = "not"
                else:
                    flag10 = "contour"
                datac["pinB_location"] = str(int(df1.iat[i, 9]))+"_" +str(int(df1.iat[i, 10]))
                datac["pinB_type"] = str(flag10)
                datac["pinB_belong"] = str(df1.iat[i, 11])
                connected.append(datac)
            qqq='0'
            datab = {}  # pipei
            datab["pipeipath"] = os.path.abspath("/output_"+flag+"/output_0%d/label/dianxian.txt") % count
            datab["connected"] = connected
            # for file in os.listdir("output_info"):
            #     name1 = os.path.basename(file)
            #     name1 = str(name)
            #     name1 = name.replace('images_', '')
            #     name1 = name.replace('_info.txt', '')
                
                # if name1 is name:
                #     qqq =name1
            count = count + 1
           
            df = pd.read_csv(f'output_info/output_{flag}/images_{name}_info.txt', sep='\s+', encoding='UTF-8',index_col=False,header=None,names=['0','1','2','3','4','5','6','7','8','9','10']) 
            df=df.drop(0)
            dataa = {}
            dataa["path"] = b
            print(df)
            print(str(df.iat[0,10]))
            if str(df.iat[0,10]) is not "nan":
                dataa["imagename"] = str(df.iat[0, 0])
                dataa["devicetype"] = str(df.iat[0, 1])
                dataa["powersystem"] = str(df.iat[0, 2])
                dataa["enginesystem"] = str(df.iat[0, 3])
                dataa["interfacetype"] = str(str(df.iat[0,4])+""+str(df.iat[0, 5]))
                dataa["chenyutype"] = str(df.iat[0, 6])
                dataa["systemnumber"] = str(df.iat[0,7])
                dataa["imagenumber"] = str(df.iat[0,8])
                dataa["versions"] = str(df.iat[0, 9])
                dataa["pagenumber"] = str(df.iat[0,10])
            if str(df.iat[0,10]) =="nan":
                dataa["imagename"] = str(df.iat[0, 0])
                dataa["devicetype"] = str(df.iat[0, 1])
                dataa["powersystem"] = str(df.iat[0,2 ])
                dataa["enginesystem"] = str(df.iat[0,3 ])
                dataa["interfacetype"] = str(df.iat[0,4])
                dataa["chenyutype"] = str(df.iat[0, 5])
                dataa["systemnumber"] = str(df.iat[0,6 ])
                dataa["imagenumber"] = str(df.iat[0,7])
                dataa["versions"] = str(df.iat[0, 8])
                dataa["pagenumber"] = str(df.iat[0,9 ])
            dataa["cutdispose"] = cutdispose
            dataa["wholedispose"] = datag
            dataa["line"] = datad
            dataa["logicgate"] = datal
            dataa["pipei"] = datab
            dataend.append(dataa)
            # date = {u'versions': [{u'status': u'CURRENT', u'id': u'v2.3', u'links': [{u'href': u'http://controller:9292/v2/', u'rel': u'self'}]}, {u'status': u'SUPPORTED', u'id': u'v2.2', u'links': [{u'href': u'http://controller:9292/v2/', u'rel': u'self'}]}, {u'status': u'SUPPORTED', u'id': u'v2.1', u'links': [{u'href': u'http://controller:9292/v2/', u'rel': u'self'}]}, {u'status': u'SUPPORTED', u'id': u'v2.0', u'links': [{u'href': u'http://controller:9292/v2/', u'rel': u'self'}]}, {u'status': u'SUPPORTED', u'id': u'v1.1', u'links': [{u'href': u'http://controller:9292/v1/', u'rel': u'self'}]}, {u'status': u'SUPPORTED', u'id': u'v1.0', u'links': [{u'href': u'http://controller:9292/v1/', u'rel': u'self'}]}]}
            #print(json.dumps(dataa, ensure_ascii=False, indent=4))
        else:
            # if file[-2:-1] is 0:
            # ???????????��????��
            pa = paths + file
            cutdispose = []
            b = os.path.abspath(pa)
            print(b)
            name = os.path.basename(b)
            name = str(name)
            name = name[-6:-4]
            print(name)
            for i in range(5):
                datah = {}
                rectangle2 = []
                circle2 = []
                j = i + 1
                c = os.path.abspath(outimage)
                datah["chlidpath"] = c + "/output_%d/area/img_cut_%d.jpg" % (count, j)
                datah["chlidname"] = "img_cut_%d.jpg" % j
                path = outimage + '/output_%d/contours/img_cut/img_cut_%d/label' % (count, j)
                if os.path.isdir(path):
                    files = []
                    for file in os.listdir(path):
                        if file.endswith(".txt"):
                            file_path = os.path.join(path, file)
                            files.append(file_path)
                    files.sort()
                    for file in files:
                        df1 = pd.read_csv(file, sep='\s+', encoding='UTF-8')
                        len_0 = df1.shape[0]
                        # for i in range(len_0):
                        #     data = df1.loc[i]
                        #     type, name, x, y, w, h, main, out = data
                        #     print(type, name, x, y, w, h, main, out)
                        path = outimage + '/output_%d/contours/img_cut/img_cut_%d/' % (count, j)
                        dirs = os.listdir(path)
                        for dir in dirs:
                            pa = path + dir
                            if dir.startswith(df1.iat[0, 6]):
                                a = os.path.abspath(pa)
                        path = outimage + '/output_%d/label/output_%d_o.txt' % (count, count)
                        if not os.path.exists(path):
                            path = os.path.abspath(outimage + '/output_%d/label/output_%d_o.txt' % (count, j))
                        df2 = pd.read_csv(path, sep='\s+', encoding='UTF-8')
                        for k in range(df2.shape[0]):
                            if str(df2.iat[k, 1]).startswith(str(df1.iat[0, 1])) and str(df2.iat[k, 2]).startswith(
                                    str(df1.iat[0, 2])) and str(df2.iat[k, 3]).startswith(str(df1.iat[0, 3])):
                                rectangle = {}
                                childrectangle = []
                                rectangle["type"] = str(df1.iat[0, 0])
                                rectangle["rectanglepath"] = a
                                rectangle["rectanglename"] = str(df1.iat[0, 1])
                                rectangle["location"] = str(str(int(df2.iat[k, 2]))+"_"+str(int(df2.iat[k, 3])))
                                rectangle["otherrectanglename"] = str(df2.iat[k, 7])  # ????????bug????
                                if len_0 > 1:
                                    for i in range(len_0):
                                        if i == 0:
                                            continue
                                        path = outimage + '/output_%d/label/output_%d_o.txt' % (count, count)
                                        df2 = pd.read_csv(path, sep='\s+', encoding='UTF-8')
                                        for q in range(df2.shape[0]):
                                            if str(df2.iat[q, 1]).startswith(str(df1.iat[i, 1])) and str(
                                                    df2.iat[q, 2]).startswith(str(df1.iat[i, 2])) and str(
                                                df2.iat[q, 3]).startswith(str(df1.iat[i, 3])):
                                                rectangle1 = {}
                                                rectangle1["type"] = str(df1.iat[i, 0])
                                                rectangle1["rectanglename"] = str(df1.iat[i, 1])
                                                rectangle1["location"] = str(df2.iat[q, 2]+"_"+df2.iat[q, 3]+"_"+df2.iat[q, 4]+"_"+df2.iat[q, 5])
                                                rectangle1["otherrectangle"] = str(df2.iat[q, 7])
                                                childrectangle.append(rectangle1)
                                                break
                                rectangle["childrectangle"] = childrectangle
                                rectangle2.append(rectangle)
                            datah["rectangle"] = rectangle2
                path1 = outimage + '/output_%d/circles/img_cut_%d_circles/label' % (count, j)
                if os.path.isdir(path1):
                    files = []
                    for file in os.listdir(path1):
                        if file.endswith(".txt"):
                            file_path = os.path.join(path1, file)
                            files.append(file_path)
                    for file in files:
                        df1 = pd.read_csv(file, sep='\s+', encoding='UTF-8')
                        path = outimage + r'/output_%d/circles/img_cut_%d_circles/' % (count, j)
                        dirs = os.listdir(path)
                        for dir in dirs:
                            pa = path + dir
                            if dir.startswith(df1.iat[0, 6]):
                                a = os.path.abspath(pa)
                        path = outimage + r'/output_%d/label/output_%d_o.txt' % (count, count)
                        df2 = pd.read_csv(path, sep='\s+', encoding='UTF-8')
                        for i in range(df2.shape[0]):
                            if str(df2.iat[i, 1]).startswith(str(df1.iat[0, 1])) and str(df2.iat[i, 2]) == str(
                                    df1.iat[0, 2]):
                                circle = {}
                                circle["circlepath"] = a
                                circle["circlename"] = str(df1.iat[0, 1])
                                circle["location"] = str(df1.iat[0, 6])
                                circle["othercircle"] = str(df2.iat[i, 7])
                                circle["type"] = str(df1.iat[0, 0])
                                circle2.append(circle)
                                break
                    datah["circle"] = circle2
                line_edge_image = {}
                binaryimage = {}
                path = outimage + '/output_%d/' % count
                dirs = os.listdir(path)
                for dir in dirs:
                    pa = path + dir
                    if dir.startswith("binary_img_cut_%d" % j):
                        a = os.path.abspath(pa)
                        binaryimage["binaryimagepath"] = a
                        binaryimage["binaryimagename "] = str(dir)
                        datah["binaryimage"] = [binaryimage]
                for dir in dirs:
                    pa = path + dir
                    if dir.startswith("line_edges_img_cut_%d" % j):
                        a = os.path.realpath(pa)
                        line_edge_image["line_edge_path"] = a
                        line_edge_image["line_edge_name"] = str(dir)
                        datah["line_edge_image"] = [line_edge_image]
                cutdispose.append(datah)

            # datah = {}
            # datah["chlidpath"] = "D:/project/module/output_SAMA/output_0/area/img_cut_1.jpg"
            # datah["chlidname"] = "img_cut_1.jpg"
            # datah["rectangle"] = rectangle2
            # datah["circle"] = [circle]
            # datah["binaryimage"] = [binaryimage]
            # datah["line_edge_image"] = [line_edge_image]

            datag = {}  # wholedispose
            datag["nodottedline"] = os.path.abspath("line/" + flag + "_nodottedline/output_%d.jpg") % count
            datag["removecircle"] = os.path.abspath("xianduan/" + flag1 + "_circle_out/output_%d.jpg") % count
            datag["mark"] = os.path.abspath(outimage + "/output_%d/img_mark.jpg") % count
            datag["clean"] = os.path.abspath(outimage + "/output_%d/img_clean.jpg") % count
            df2 = pd.read_csv('xianduan/xianduan/xianduanjiance/' + flag1 + '_result/output_%d/output_line.txt' % count,
                              sep='\s+', encoding='UTF-8', header=None, names=['x1', 'y1', 'x2', 'y2','z'])
            len_1 = df2.shape[0]
            line = []
            for i in range(len_1):
                dataf = {}  # line1
                dataf["x1"] = str(df2.iat[i, 0])
                dataf["y1"] = str(df2.iat[i, 1])
                dataf["x2"] = str(df2.iat[i, 2])
                dataf["y2"] = str(df2.iat[i, 3])
                line.append(dataf)

            datad = {}  # line
            datad["linepath"] = os.path.abspath(
                "xianduan/xianduan/xianduanjiance/" + flag + "_result/output_0%d/output_line.txt") % count
            datad["line1"] = line
            datal = []
            df10 = pd.read_csv('./output_' + flag + '/output_%d/label/output_%d_l.txt' % (count, count), sep='\s+',
                               encoding='UTF-8')  # �����߶���Ϣ���ļ���
            len_0 = df10.shape[0]
            flag2 = 0  # ������ʶֻ����End2����Ķ�������ΪEnd2����Ķ��������߼���
            type = ""  # �߼��ŵ�����
            for i in range(len_0):
                if str(df10.iat[i, 0]) == "End2":
                    flag2 = 1
                if flag2 == 0 or str(df10.iat[i, 0]) == "End2":
                    continue
                if str(df10.iat[i, 0]).startswith("and"):
                    type = "and"
                elif str(df10.iat[i, 0]).startswith("or"):
                    type = "or"
                elif str(df10.iat[i, 0]).startswith("not"):
                    type = "not"
                a = 0  # �������������
                bbbb = 0  # �������������
                df1 = pd.read_csv('./output_FD' + f'/output_{count}/label/dianxian.txt', sep='\s+', encoding='UTF-8')
                len_1 = df1.shape[0]
                for k in range(len_1):
                    if df10.iat[i, 0] == df1.iat[k, 0]:
                        a = a + 1
                    elif df10.iat[i, 0] == df1.iat[k, 8]:
                        bbbb = bbbb + 1
                datalogic = {}
                path = outimage + '/output_%d/logic/' % count
                dirs = os.listdir(path)
                abspath = ""
                for dir in dirs:
                    pa = path + dir
                    ps = str(str(type) + "_" + df10.iat[i, 1] + "_" + df10.iat[i, 2])
                    if dir.startswith(ps):
                        abspath = os.path.abspath(pa)
                datalogic["logic_image_path"] = abspath
                datalogic["type"] = str(type)
                datalogic["name"] = str(df10.iat[i, 0])
                datalogic["logic_location"] = str(int(df10.iat[i, 1])) + "_" + str(int(df10.iat[i, 2]))
                datalogic["outnumber"] = str(a)
                datalogic["intnumber"] = str(bbbb)
                datal.append(datalogic)
            df1 = pd.read_csv(f'./output_{flag}/output_{count}/label/dianxian.txt', sep='\s+', encoding='UTF-8')
            len_0 = df1.shape[0]
            connected = []
            for i in range(len_0):
                flag10 = ""  # ������ֵ����
                datac = {}  # connected
                datac["pinA_name"] = str(df1.iat[i, 0])
                if str(df1.iat[i, 0]).startswith("circle"):
                    flag10 = "circles"
                elif str(df1.iat[i, 0]).startswith("and"):
                    flag10 = "and"
                elif str(df1.iat[i, 0]).startswith("or"):
                    flag10 = "or"
                elif str(df1.iat[i, 0]).startswith("not"):
                    flag10 = "not"
                else:
                    flag10 = "contour"
                datac["pinA_type"] = str(flag10)
                # df2 = pd.read_csv('./output_' + flag + '/output_0%d/label/output_0%d_l.txt' % (count, count), sep='\s+', encoding='UTF-8')  # �����߶���Ϣ���ļ���
                # len_2 = df2.shape[0]
                # locations = ""  #������¼����
                # for k in range(len_2):
                #     if str(df1.iat[i][1]) == str(df2.iat[k][3]) and str(df1.iat[i][2]) == str(df2.iat[k][2]):
                #         locations = str(df2.iat[i][1])+"_"+str(df2.iat[i][1])
                if math.isnan(df1.iat[i, 1]) and math.isnan(df1.iat[i, 2]) : 
                    datac["pinA_location"] = str(df1.iat[i, 1])+"_" +str(df1.iat[i, 2])
                else:
                    datac["pinA_location"] = str(int(df1.iat[i, 1]))+"_" +str(int(df1.iat[i, 2]))
                datac["pinA_belong"] = str(df1.iat[i, 3])
                datac["lineA_x"] = str(df1.iat[i, 4])
                datac["lineA_y"] = str(df1.iat[i, 5])
                datac["lineB_x"] = str(df1.iat[i, 6])
                datac["lineB_y"] = str(df1.iat[i, 7])
                datac["pinB_name"] = str(df1.iat[i, 8])
                flag10 = ""  # ������ֵ����
                if str(df1.iat[i, 8]).startswith("circle"):
                    flag10 = "circles"
                elif str(df1.iat[i, 8]).startswith("and"):
                    flag10 = "and"
                elif str(df1.iat[i, 8]).startswith("or"):
                    flag10 = "or"
                elif str(df1.iat[i, 8]).startswith("not"):
                    flag10 = "not"
                else:
                    flag10 = "contour"
                datac["pinB_location"] = str(int(df1.iat[i, 9])) + "_" + str(int(df1.iat[i, 10]))
                datac["pinB_type"] = str(flag10)
                datac["pinB_belong"] = str(df1.iat[i, 11])
                connected.append(datac)
            datab = {}  # pipei
            datab["pipeipath"] = os.path.abspath("/output_" + flag + "/output_%d/label/dianxian.txt") % count
            datab["connected"] = connected
            # for file in os.listdir("output_info"):
            #     name1 = os.path.basename(file)
            #     name1 = str(name)
            #     name1 = name.replace('images_', '')
            #     name1 = name.replace('_info.txt', '')
            #     if name1 is name:
            #         qqq = name1
            count = count + 1
            # print(qqq)
            
            df = pd.read_csv(f'output_info/output_{flag}/images_{name}_info.txt', sep='\s+', encoding='UTF-8',index_col=False,header=None,names=['0','1','2','3','4','5','6','7','8','9','10']) 
            df=df.drop(0)
            dataa = {}
            dataa["path"] = b
            print(df)
            print(str(df.iat[0,10]))
            if str(df.iat[0,10]) is not "nan":
                dataa["imagename"] = str(df.iat[0, 0])
                dataa["devicetype"] = str(df.iat[0, 1])
                dataa["powersystem"] = str(df.iat[0, 2])
                dataa["enginesystem"] = str(df.iat[0, 3])
                dataa["interfacetype"] = str(str(df.iat[0,4])+""+str(df.iat[0, 5]))
                dataa["chenyutype"] = str(df.iat[0, 6])
                dataa["systemnumber"] = str(df.iat[0,7])
                dataa["imagenumber"] = str(df.iat[0,8])
                dataa["versions"] = str(df.iat[0, 9])
                dataa["pagenumber"] = str(df.iat[0,10])
            if str(df.iat[0,10]) =="nan":
                dataa["imagename"] = str(df.iat[0, 0])
                dataa["devicetype"] = str(df.iat[0, 1])
                dataa["powersystem"] = str(df.iat[0,2 ])
                dataa["enginesystem"] = str(df.iat[0,3 ])
                dataa["interfacetype"] = str(df.iat[0,4])
                dataa["chenyutype"] = str(df.iat[0, 5])
                dataa["systemnumber"] = str(df.iat[0,6 ])
                dataa["imagenumber"] = str(df.iat[0,7])
                dataa["versions"] = str(df.iat[0, 8])
                dataa["pagenumber"] = str(df.iat[0,9 ])
            dataa["cutdispose"] = cutdispose
            dataa["wholedispose"] = datag
            dataa["line"] = datad
            dataa["logicgate"] = datal
            dataa["pipei"] = datab
            dataend.append(dataa)
    with open(f"json/{namess}.json", 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(dataend, ensure_ascii=False, indent=4))
    os.rename(f"json/{namess}.json", f"json/{namess}_final.json")
    

def main():
    outjson("input_FD", "output_FD")
if __name__ == '__main__':
    main()