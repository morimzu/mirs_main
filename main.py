import cv2

from camera import get_image
from ssd_model import detect
from arduino import My_Serial
from order import Order
from calc import calc

import timeit

if __name__ == "__main__":
    '''
    初期設定
    '''
    #ser = My_Serial('/dev/tty.usbmodem142401', 115200)
    
    count = 1
    img = get_image()
    image = cv2.imread(img, cv2.IMREAD_COLOR)

    '''
    デバッグ部分．一回の物体検知にどれだけの時間がかかったのかを計測するのに使った．
    result = timeit.timeit('detect(image, count)', globals=globals(), number=10)
    print(result / 10)
    '''

    labels, boxs = detect(image, count)
    print(count)
    count += 1
    labels.append(':')
    print(labels)
    for box in boxs:
        box.show()
        print(calc(box.width))

    #ser.send('a0a0a0a0:')
    #ser.send(order.order)
    #ser.checkout()