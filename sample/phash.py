import cv2
import numpy as np


def get_img_fingerprints(gray_dct_ul64_list, gray_dct_ul64_avg):
    """
    获取图片指纹：遍历灰度图左上8*8的所有像素，比平均值大则记录为1，否则记录为0。
    :param gray_dct_ul64_list: 灰度图左上8*8的所有像素
    :param gray_dct_ul64_avg: 灰度图左上8*8的所有像素平均值
    :return: 图片指纹
    """
    img_fingerprints = ''
    avg = gray_dct_ul64_avg[0]
    for i in range(8):
        for j in range(8):
            if gray_dct_ul64_list[i][j] > avg:
                img_fingerprints += '1'
            else:
                img_fingerprints += '0'
    return img_fingerprints


def pHash(imgfile, resize=(32, 32)):
    """get image pHash value"""
    img = cv2.imread(imgfile, cv2.IMREAD_UNCHANGED)
    # 修改图片大小
    image_resize = cv2.resize(img, resize, cv2.INTER_LINEAR)
    # 修改图片成灰度图
    image_gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
    # 转换灰度图成浮点型
    image_gray_f = np.float32(image_gray)
    # 获取灰度图的DCT集合
    image_gray_dct = cv2.dct(image_gray_f)
    # 获取灰度图DCT集合的左上角8*8
    gray_dct_ul64_list = image_gray_dct[0:8, 0:8]
    # 获取灰度图DCT集合的左上角8*8对应的平均值
    gray_dct_ul64_avg = cv2.mean(gray_dct_ul64_list)
    # 获取图片指纹
    img_fingerprints = get_img_fingerprints(gray_dct_ul64_list, gray_dct_ul64_avg)
    return img_fingerprints


if __name__ == "__main__":
    pHash = pHash("image/2.jpg")
    print(pHash)
