import cv2 as cv2


def resizeByLengthWidth(img, length, width):
    resized_sample = cv2.resize(img, (length, width), cv2.INTER_LINEAR)
    return resized_sample

