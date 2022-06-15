import cv2 as cv2
import glob
from functions.comparison.comparisonSample import *

xPortion = 1/5
yPortion = 1/6

def sampleImageProcessor(img):
    if img is None:
        print("reference image in sampleProcessor is None")
    # sample = cv2.imread(cv2.samples.findFile("./assets/patterns/sample1.png"))
    y_ref, x_ref, c = img.shape
    images = [cv2.imread(file) for file in glob.glob("./assets/patterns/*.png")]
    min_mn = 1
    optimal_match = []
    sampleSize = (round(yPortion * y_ref), round(xPortion * y_ref))
    for sampleImg in images:
        resizedSample = cv2.resize(sampleImg, (sampleSize[1], sampleSize[0]), cv2.INTER_LINEAR)
        mn, mnLoc = comparisonSample(resizedSample, img)
        if mn < min_mn:
            min_mn = mn
            optimal_match = mnLoc
    m_px, m_py = mnLoc
    return m_px, m_py

    # resizedSample = cv2.resize(sample, (sampleSize[1], sampleSize[0]), cv2.INTER_LINEAR)
    #
    # ret2, thresh2 = cv2.threshold(resizedSample, 127, 255, cv2.THRESH_BINARY)
    # ySample, xSample, c2 = resizedSample.shape
