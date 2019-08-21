from itertools import chain

import cv2
import numpy


def avash(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)
    print(img)

    # 缩放为8*8
    img = cv2.resize(img, (8, 8))
    # print(img)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(gray)
    img_list = list(chain.from_iterable(gray))
    # print(img_list)
    avg = sum(img_list) * 1. / len(img_list)
    # print(avg)
    avg_list = ['0' if i < avg else '1' for i in img_list]
    hash_str = ''.join(avg_list[x] for x in range(0, 64))
    print(img_name + ':' + '\n' + hash_str)

    return hash_str


if __name__ == "__main__":
    avash("image/1.jpg")
