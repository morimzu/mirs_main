# 検知したバインディングボックスの座標から机とMIRS本体の位置関係を求める
import numpy as np
import pandas as pd

df = pd.read_csv("data/Determination_factors.csv")
fact = df.values.tolist()

def calc(width):
    import numpy
    x = numpy.roots([fact[0][0], fact[0][1], fact[0][2], fact[0][3], fact[0][4], fact[0][5]-width])
    print(x)
    for dist in x:
        if dist >= 30.0 and dist <= 100.0 and dist.imag == 0:
            return dist.real

#print(calc(76.67501068115234))