#   coding=utf-8
import cv2
img = cv2.imread(r"D:\project\modulepro\module\1.jpg")
templ = cv2.imread(r"D:\project\modulepro\module\4.jpg")
height, width, c = templ.shape
#相关系数
results = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
print(results)
for y in range(len(results)):
    for x in range(len(results[y])):
        if results[y][x] > 0.75:#准确率大于0.75
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)
            cv2.rectangle(img, (x, y), (x + width, y + height), (255, 255, 255), -1)
cv2.imshow("img", img)
cv2.imshow("templ", templ)
cv2.waitKey()
cv2.destroyAllWindows()