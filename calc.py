# 検知したバインディングボックスの座標から机とMIRS本体の位置関係を求める
import numpy as np
import pandas as pd

df = pd.read_csv("data/Determination_factors.csv")
fact = df.values.tolist()

def calc_dist(width):
    x = np.roots([fact[0][0], fact[0][1], fact[0][2], fact[0][3]-width])
    #print(x)
    for dist in x:
        if dist >= 30.0 and dist <= 100.0 and dist.imag == 0:
            print(dist.real)
            return dist.real
    raise Exception("The distance is out of range.")

def calc_devi(devi):
    y = np.roots([fact[0][0]/27.5, fact[0][1]/27.5, fact[0][2]/27.5, fact[0][3]/27.5-devi])
    #print(y)
    for devi in y:
        if devi >=-100 and devi <= 100 and devi.imag == 0:
            return devi.real
    raise Exception("The deviation is out of range.")