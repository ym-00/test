import numpy as np

data_t = np.loadtxt('xianduan/information/data_jiehe.txt')


try :
    open("xianduan/information/data_jiehe.txt", "w").close()
except:
    print('None')
data_t = data_t[np.lexsort(data_t[:, ::-1].T)]

print(data_t)

for data in data_t:
    x1, y1, x2, y2 = data
    x1 = np.int0(x1)
    y1 = np.int0(y1)
    x2 = np.int0(x2)
    y2 = np.int0(y2)
    if abs( x1-x2 ) < 5 :
        x1 = min(x1,x2)
        x2 = min(x1, x2)
    if abs( y1-y2 ) < 5 :
        y1 = min(y1,y2)
        y2 = min(y1, y2)
    if x1 > x2:
        file = open('xianduan/information/data_jiehe.txt', 'a')
        file.write(str(x2))
        file.write(' ')
        file.write(str(y2))
        file.write(' ')
        file.write(str(x1))
        file.write(' ')
        file.write(str(y1))
        file.write('\n')
    else:
        if y1 < y2:
            file = open('xianduan/information/data_jiehe.txt', 'a')
            file.write(str(x2))
            file.write(' ')
            file.write(str(y2))
            file.write(' ')
            file.write(str(x1))
            file.write(' ')
            file.write(str(y1))
            file.write('\n')

        else:
            file = open('xianduan/information/data_jiehe.txt', 'a')
            file.write(str(x1))
            file.write(' ')
            file.write(str(y1))
            file.write(' ')
            file.write(str(x2))
            file.write(' ')
            file.write(str(y2))
            file.write('\n')