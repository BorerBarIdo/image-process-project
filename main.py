import cv2 as cv2
from services.videoProcessor import *
from services.sampleImageProcessor import *
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from skimage.metrics import structural_similarity as ssim

# xPortion = 1/5
# yPortion = 1/6
# cv2.destroyAllWindows()

# sample = cv.imread(cv.samples.findFile("assets/patterns/sample1.png"))
img = cv2.imread(cv2.samples.findFile("_test/veins2.png"))
sourceVid = cv2.VideoCapture("_test/vid_veins_leg1.mp4")


videoProcessor(sourceVid)
# yRef, xRef, c = img.shape
# sampleSize = (round(yPortion * yRef), round(xPortion * xRef))
# resizedSample = cv.resize(sample, (sampleSize[1], sampleSize[0]), cv.INTER_LINEAR)
# print(img.shape[:2])
# ret1, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
#
# ret2, thresh2 = cv.threshold(resizedSample, 127, 255, cv.THRESH_BINARY)
# ySample, xSample, c2 = resizedSample.shape
#
# # pix_val = list(img.getdata())
# if img is None:
#     sys.exit("Could not read the image.")
# # print(thresh1)
#
#
# method = cv.TM_SQDIFF_NORMED
#
# # Read the images from the file
#
# result = cv.matchTemplate(thresh2, thresh1, method)
# mn,_,mnLoc,_ = cv.minMaxLoc(result)
# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx,MPy = mnLoc
#
# # Step 2: Get the size of the template. This is the same size as the match.
# trows,tcols = thresh1.shape[:2]
# # Step 3: Draw the rectangle on large_image
# # cv.rectangle(thresh1, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
#
# # Display the original image with the rectangle around the match.
# # cv.imshow('output',thresh1)

# plt.imshow(thresh1)
# plt.plot(MPx + sampleSize[1]/2, MPy + sampleSize[0]/2, "or", 8)
# plt.show()
#
# cv.waitKey(0)

# # The image is o
# # H: {} = {"mseVal": 1, "x": 0, "y": 0}
# # j: int = ySample
# # i: int = xSample
# # while j < yRef:
# #     while i < xRef:
# #         regionMse = mse(thresh1[(j-ySample):j, (i-xSample):i], thresh2)
# #         if (H["mseVal"] > regionMse) or (H["mseVal"] == 1):
# #             H["mseVal"] = regionMse
# #             H["x"] = j-ySample/2
# #             H["y"] = i-xSample/2
#
# #
# # plt.imshow(thresh1)
# # plt.plot(H["x"], H["y"], "og", 4)
# plt.show()