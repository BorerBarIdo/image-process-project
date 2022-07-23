import cv2 as cv2
from services.videoProcessor import *
from services.sampleImageProcessor import *
from flask import Flask, render_template, Response

sourceVid = cv2.VideoCapture("_test/veins_web_nir_2.mp4")


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

# @app.route('/video_feed')
# def video_feed():
#     return Response(videoProcessor(), mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# if __name__ == '__main__':
#     app.run()
