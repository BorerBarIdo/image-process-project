import cv2 as cv2


def idealSampleSizeCalculate(img, x_portion, y_portion):
    y_ref, x_ref, c = img.shape
    sample_size = (round(y_portion * y_ref), round(x_portion * y_ref))
    return sample_size

