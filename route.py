# 定数
st=256
#機体の縦幅
wi=815
#機体の横幅
hwi=wi/2
#機体の横幅/2
ma=200
ma2=200
#回転する時に必要な幅

import math
from pprint import pprint
from order import Order

VELOCITY = 1.5
VELOCITY_DEG = 0.5

def make_route(dist, dif):
    orders = []
    Negative = 0
    if dif < 0:
        dif *= -1
        Negative = 1
    
    Tst=dist-(ma+ma2+st)
    dist_run = math.sqrt( dif **2 + Tst**2)
    a=Tst/dif
    angle_direction=math.degrees(math.atan(a))
    angle_rotate=90-angle_direction
    
    if Negative == 1:
        angle_rotate *= -1

    #print(Tst)  #直線距離（機体幅と回転の時に必要な幅を削った時の残りの距離)
    #print(dist_run)   #斜めに進む分の距離
    #print(angle_direction)  #進みたい方向の角度
    #print(angle_rotate) #機体を移転させる角度 実際に回転させる角度 [deg]
    orders.append(Order('r', VELOCITY, ma/10).order)
    orders.append(Order('t', VELOCITY_DEG, angle_rotate).order)
    orders.append(Order('r', VELOCITY, dist_run/10).order)
    orders.append(Order('t', VELOCITY_DEG, -1*angle_rotate).order)
    orders.append(Order('r', VELOCITY, ma2/10).order)
    pprint(orders)
    return orders