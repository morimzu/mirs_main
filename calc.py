# 検知したバインディングボックスの座標から机とMIRS本体の位置関係を求める
import numpy as np
import pandas as pd

df = pd.read_csv("data/Determination_factors.csv")
fact = df.values.tolist()

def calc_dist(width):
    x = np.roots([fact[0][0], fact[0][1], fact[0][2], fact[0][3], fact[0][4], fact[0][5]-width])
    #print(x)
    for dist in x:
        if dist >= 50.0 and dist <= 200.0 and dist.imag == 0:
            #print(dist.real)
            return dist.real
    raise Exception("The distance is out of range.")

def calc_devi(width, devi):
    if devi <0:
        devi =-devi
        sign = 1
    else: sign = 0
    t = width/27.5  # 机との距離において1cmが何ピクセルなのかを求める
    devi = devi/t
    if devi >=-100 and devi <= 100 and devi.imag == 0:
        if sign == 1:
            devi = -devi
        return devi.real
    raise Exception("The deviation is out of range.")