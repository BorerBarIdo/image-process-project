import cv2 as cv2
import glob
import numpy as np


def referenceImageProcessor(img):
    image_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    image_bw = np.float32(image_bw)
    clahe = cv2.createCLAHE(clipLimit=3)
    clahe_img = clahe.apply(image_bw) + 30
    _, final_img = cv2.threshold(clahe_img, 145, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    return final_img
