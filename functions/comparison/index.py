from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	# setup the figure
	fig = plt.figure()
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()
	
def img_proc(image):
    img = cv2.imread(image,0)  # read in grayscale
    img = cv2.medianBlur(image,3)  #median filtering

    clahe = cv2.createCLAHE(clipLimit=3)
    final_img = clahe.apply(img)  # Adaptive Histogram Equalization

    bin_Thr = cv2.adaptiveThreshold(final_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
    bin_Thr=255 - bin_Thr  ## inverting the image B2W for pattern algorithm

    return bin_Thr
