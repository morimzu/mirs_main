# 机とMIRS本体の位置関係をデータとして保存するためのモジュール
# MIRS本体の動作とは関係ないが走行制御に用いるモジュール作成のために作成した

import cv2
from ssd_model import detect
from camera import get_image
import pandas as pd
from random import randint
import os

if __name__ == "__main__":
    count = 0
    if os.path.isfile("ObjectDistanceDatas.csv"):
        df1 = pd.read_csv("ObjectDistanceDatas.csv")
    else:
        print("I'll make ObjectDistanceDatas.csv file")
        df1 = pd.DataFrame([], columns=['dist', 'x_pos', 'y_pos', 'width', 'height'])
    
    dist = []
    x_pos = []
    y_pos = []
    width = []
    height = []
    for i in range(10):
        for j in range(5):
            img = get_image()
            #img = './VOCdevkit/DESK/JPEGImages/deskImage_' + ("0000" + str(randint(0,425)))[-5:] + ".jpg" テスト用，既存のファイルかrあランダムにデータを引っ張ってきてどうっしているのか確認した．
            image = cv2.imread(img, cv2.IMREAD_COLOR)
            labels, boxs = detect(image, count)
            for box in boxs:
                dist += [(i+1)*10]
                x_pos += [box.x_pos]
                y_pos += [box.y_pos]
                width += [box.width]
                height += [box.height]
                count += 1
                
        print("Data collection has already been completed for a distance of {}cm".format((i+1)*10))
        if i is not 10:
            print("Next Distance is {}cm".format((i+1)*10+10))
        
        print("If you are ready press any keys and Enter.")

        input()
    df2 = pd.DataFrame(
        data={'dist':dist, 'x_pos':x_pos, 'y_pos':y_pos, 'width':width, 'height':height},
        columns=['dist', 'x_pos', 'y_pos', 'width', 'height']
    )
    
    df = pd.concat([df1, df2], axis=0)
    df = df.sort_values(by='dist', ascending=True)
    print(df)
    df.to_csv("ObjectDistanceDatas.csv", index=False)