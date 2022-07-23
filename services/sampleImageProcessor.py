import cv2 as cv2
import glob
from functions.comparison.comparisonSample import *
from functions.fetchSampleImages import *
from functions.resizeByLendthWidth import *
from functions.idealSampleSizeCalculate import *

xPortion = 1/20
yPortion = 1/12


def sampleImageProcessor(img):
    if img is None:
        print("reference image in sampleProcessor is None")
    sample_size = idealSampleSizeCalculate(img, xPortion, yPortion)
    images = fetchSampleImages()

    min_mn = 1
    optimal_mn_loc = (1, 1)

    for sampleImg in images:
        resized_sample = resizeByLengthWidth(sampleImg, sample_size[1], sample_size[0])
        gray_sample = cv2.cvtColor(resized_sample, cv2.COLOR_BGR2GRAY)

        mn, mn_loc = comparisonSample(gray_sample, img)
        if mn < min_mn:
            min_mn = mn
            optimal_mn_loc = mn_loc

    print(min_mn)
    m_px, m_py = optimal_mn_loc
    return m_px , m_py

