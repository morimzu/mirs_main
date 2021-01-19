import cv2

from camera import get_image
from ssd_model import detect
from route import make_route
from position import my_position
from arduino import My_Serial
from order import Order
from calc import *
import time
import numpy as np
import serial
import timeit

VELOCITY = 15
VELOCITY_DEG = 0.5
DISTANCE = 150
orders = []
orders = []
pos = 0

if __name__ == "__main__":
    '''
    初期設定
    '''
    ser = My_Serial('/dev/tty.usbmodem142101', 115200, timeout=0.3)
    
    #ser = My_Serial('/dev/ttyACM0', 115200, timeout=50)
    
    while True:
        count = 1
        img = get_image()
        image = cv2.imread(img, cv2.IMREAD_COLOR)
        IMAGE_WIDTH = image.shape[1]

        '''
        デバッグ部分．一回の物体検知にどれだけの時間がかかったのかを計測するのに使った．
        result = timeit.timeit('detect(image, count)', globals=globals(), number=10)
        print(result / 10)
        '''

        labels, boxs = detect(image, count)
        if labels == False: #机が見つからなかったときは以下の処理をスルーしてもう検知されるまで物体検知を繰り返す（変更予定）
            print("desk was not found.")
            continue

        count += 1
        #labels.append(':')
        #print(labels)
        for box in boxs:
            #box.show()
            print(box.x_pos + box.width / 2 - IMAGE_WIDTH/2)
            dist = calc_dist(box.width)                                             #机との距離の計算
            devi = calc_devi(box.width, box.x_pos + box.width / 2 - IMAGE_WIDTH/2)  #机のズレの計算
            print("dist: ", dist)
            print("devi: ", devi)
            if dist >= DISTANCE-50 and dist <= DISTANCE+50: #机との距離が規定の値の範囲内にあるかどうか
                route = make_route(dist, devi)
                for order, wait in route.orders:
                    ser.mysend(order.encode())
                    time.sleep(np.abs(wait))
                ser.mysend('l:'.encode())
                time.sleep(5)
                del(route)
            else:
                continue
        move, pos = my_position(pos)
        if move:
            break