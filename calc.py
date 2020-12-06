# 検知したバインディングボックスの座標から机とMIRS本体の位置関係を求める
import numpy as np
import pandas as pd

df = pd.read_csv("data/Determination_factors.csv")
fact = df.values.tolist()

def calc_dist(width):
    x = np.roots([fact[0][0], fact[0][1], fact[0][2]-width])
    print(x)
    for dist in x:
        if dist >= 30.0 and dist <= 100.0 and dist.imag == 0:
            return dist.real

def calc_devi():
    pass