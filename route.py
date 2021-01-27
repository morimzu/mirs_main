# 定数
st=25.6
#機体の縦幅
wi=81.5
#機体の横幅
hwi=wi/2
#機体の横幅/2
ma=20
ma2=20
#回転する時に必要な幅

import math
import numpy as np
from pprint import pprint
from order import Order

VELOCITY = 15
VELOCITY_DEG = 15

def make_route(dist, dif):
    orders = []
    Negative = 0
    if dif < 0:
        dif *= -1
        Negative = 1
    
    Tst=dist-40-st
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
    route = Route(ma, angle_rotate, dist_run, dif)
    return route

class Route:
    def __init__(self, ma, angle_rotate, dist_run, devi):
        self.ma = ma
        self.angle_rotate = angle_rotate
        self.dist_run = dist_run
        self.devi = np.abs(devi)
        self.orders = []
        self.make_order()

    def make_order(self):
        self.orders.append([Order('r', VELOCITY, self.ma).order, self.ma/VELOCITY + 0.5])
        self.orders.append([Order('t', VELOCITY_DEG, -1*self.angle_rotate).order, self.angle_rotate/VELOCITY_DEG + 0.5])
        self.orders.append([Order('r', VELOCITY, self.dist_run).order, self.dist_run/VELOCITY + 0.5])
        self.orders.append([Order('t', VELOCITY_DEG, self.angle_rotate).order, self.angle_rotate/VELOCITY_DEG + 0.5])
        self.orders.append([Order('r', VELOCITY, self.ma + 10 + self.devi**2/50).order, (self.ma + 10 + self.devi**2/50)/VELOCITY + 0.5])