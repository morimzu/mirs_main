# 検知したバインディングボックスの座標から机とMIRS本体の位置関係を求める
import numpy as np
import pandas as pd

df = pd.read_csv("data/Determination_factors.csv")
fact = df.values.tolist()

def calc_dist(width):
    print("<calc module>")
    x = np.roots([fact[0][0], fact[0][1], fact[0][2]-width])
    #print(x)
    for dist in x:
        if dist >= 50.0 and dist <= 200.0 and dist.imag == 0:
            #print(dist.real)
            return dist.real
    return 0

def calc_devi(width, devi):
    sign = 1
    if devi <0: # ズレのピクセルの符号処理
        devi*=-1
        sign = -1
    t = width/27.5  # 机との距離において1cmが何ピクセルなのかを求める
    devi = devi/t
    if devi >=-100 and devi <= 100 and devi.imag == 0:
        devi = sign * devi
        return devi.real
    return 0