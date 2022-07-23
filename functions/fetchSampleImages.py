import glob
from PIL import Image
import cv2 as cv2


def fetchSampleImages():
    images = [cv2.imread(file) for file in glob.glob("./assets/patterns/*.png")]
    return images
