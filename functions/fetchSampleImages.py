import glob
from PIL import Image

def bestCoordinate(path):
    sampleList = []
    for filename in glob.glob('assets/patterns/*.png'):
        im = Image.open(filename)
        sampleList.append(im)
