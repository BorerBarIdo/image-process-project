import cv2 as cv2
from services.sampleImageProcessor import *
# sourceVid= cv2.VideoCapture("_test/vid_veins_leg1.mp4")
def videoProcessor(sourceVid):
    while True:
        ret, img = sourceVid.read()

        if img is None:
            break
        ret1, thresh1 = cv2.threshold(img, 135, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        m_px, m_py = sampleImageProcessor(img)

        cv2.imshow("Live", thresh1)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

