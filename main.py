import cv2

from camera import get_image
from ssd_model import detect
from arduino import My_Serial
from order import Order
from calc import *

import timeit

if __name__ == "__main__":
    '''
    初期設定
    '''
    #ser = My_Serial('/dev/tty.usbmodem142401', 115200)
    
    count = 1
    img = get_image()
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    IMAGE_WIDTH = image.shape[0]
    #print(IMAGE_WIDTH)
    '''
    デバッグ部分．一回の物体検知にどれだけの時間がかかったのかを計測するのに使った．
    result = timeit.timeit('detect(image, count)', globals=globals(), number=10)
    print(result / 10)
    '''

    labels, boxs = detect(image, count)
    print(count)
    count += 1
    labels.append(':')
    #print(labels)
    for box in boxs:
        box.show()
        print(calc_dist(box.width))
        print(box.x_pos-IMAGE_WIDTH/2)
        print(calc_devi(box.x_pos-IMAGE_WIDTH/2))

    #ser.send('a0a0a0a0:')
    #ser.send(order.order)
    #ser.checkout()