# 机とMIRS本体の位置関係をデータとして保存するためのモジュール
# MIRS本体の動作とは関係ないが走行制御に用いるモジュール作成のために作成した

import cv2
from ssd_model import detect
from camera import get_image
import pandas as pd
from random import randint

if __name__ == "__main__":
    objects = []
    count = 0

    for j in [10,20,30,40,50,60,70,80,90,100]:

        img = get_image()
        #img = './VOCdevkit/DESK/JPEGImages/deskImage_' + ("0000" + str(randint(0,425)))[-5:] + ".jpg"
        image = cv2.imread(img, cv2.IMREAD_COLOR)
        labels, boxs = detect(image, count)
        
        if boxs == False:
            continue

        for box in boxs:
            objects.append([j, box.x_pos, box.y_pos, box.width, box.height])
            
        count += 1
        print("IData collection has already been completed for a distance of {}cm".format(j))
        if j is not 100:
            print("Next Distance is {}cm".format(j+10))
        print("If you are ready press any keys and press Enter.")

        input()

    df = pd.DataFrame(objects,
    columns=['dist', 'x_pos', 'y_pos', 'width', 'height'])

    df.to_csv("../data/ObjectDistanceDatas.csv")