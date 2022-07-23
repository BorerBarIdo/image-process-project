import cv2 as cv2
import glob
import numpy as np


# def multi_clahe(img):
#     for i in range(1):
#         img = cv2.createCLAHE(clipLimit=8.0, tileGridSize=(4 + i * 2, 4 + i * 2)).apply(img)
#     return img

def referenceImageProcessor(img):
    # image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # final = multi_clahe(gray)
    histogram = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8)).apply(gray)

    final = cv2.medianBlur(histogram, 11)
    # image_bw = np.float32(img)
    # clahe = cv2.createCLAHE(clipLimit=3)
    # clahe_img = clahe.apply(image_bw) + 30
    ret1, final_img = cv2.threshold(final, 137, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    return final_img
