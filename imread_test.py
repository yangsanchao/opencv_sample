import cv2

image = cv2.imread("image/image.jpg")
cv2.namedWindow("image")
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
