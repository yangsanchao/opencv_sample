import cv2
from matplotlib import pyplot


# 最简单的以huidu直方图作为相似比较的实现
def classify_gray_hist(image1, image2, size=(256, 256)):
    # 先调整大小
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 比较直方图
    pyplot.plot(range(256), hist1, 'r')
    pyplot.plot(range(256), hist2, 'y')
    pyplot.show()
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - (abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i])))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


if __name__ == '__main__':
    imgobj1 = cv2.imread('image/image.jpg')
    imgobj2 = cv2.imread('image/image2.jpg')
    degree = classify_gray_hist(imgobj1, imgobj2)
    print(degree)
