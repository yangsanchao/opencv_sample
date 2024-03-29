import cv2
import numpy as np

img_name1 = 'image/01.png'
img_name2 = 'image/02.png'

size = (480, 320)

sift = cv2.xfeatures2d.SIFT_create()

img1 = cv2.imread(img_name1)
img1 = cv2.resize(img1, size)

gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)  # 灰度处理图像
kp1, des1 = sift.detectAndCompute(img1, None)  # des是描述子
print(kp1, des1)

img2 = cv2.imread(img_name2)
img2 = cv2.resize(img2, size)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # 灰度处理图像
kp2, des2 = sift.detectAndCompute(img2, None)  # des是描述子
print(kp2, des2)

merge = np.hstack((gray1, gray2))  # 水平拼接
# cv2.imshow("gray", merge)  # 拼接显示为gray
# cv2.waitKey(0)

img3 = cv2.drawKeypoints(img1, kp1, img1, color=(255, 0, 255))  # 画出特征点，并显示为红色圆圈
img4 = cv2.drawKeypoints(img2, kp2, img2, color=(255, 0, 255))  # 画出特征点，并显示为红色圆圈
merge = np.hstack((img3, img4))  # 水平拼接
# cv2.imshow("point", merge)  # 拼接显示为gray
# cv2.waitKey(0)

# BFMatcher解决匹配
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# 调整ratio
good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

img5 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
cv2.imshow("BFmatch", img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
