import cv2 as cv2
from services.refrenceImageProcessor import *
from functions.indicator import *
from services.sampleImageProcessor import *
import io


def videoProcessor(sourceVid):
    out = cv2.VideoWriter('output.mp4', -1, 20.0, (640, 480))

    while True:
        ret, img = sourceVid.read()

        if img is None:
            break
        # ret1, thresh1 = cv2.threshold(img, 145, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
        thresh1 = referenceImageProcessor(img)
        m_px, m_py = sampleImageProcessor(thresh1)

        indicate_img = indicator(img, m_px, m_px)
        out.write(indicate_img)

        cv2.imshow("Live", thresh1)
        key = cv2.waitKey(1)
        # encode_return_code, image_buffer = cv2.imencode('.jpg', indicate_img)
        # io_buf = io.BytesIO(image_buffer)
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + image_buffer.read() + b'\r\n')
        # ggg
    return out
