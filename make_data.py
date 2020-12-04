# 机とMIRS本体の位置関係をデータとして保存するためのモジュール
# MIRS本体の動作とは関係ないが走行制御に用いるモジュール作成のために作成した

import cv2
from ssd_model import detect
from camera import get_image

if __name__ == "__main__":
    objects = []
    objects.append('label', 'x_pos', 'y_pos', 'width', 'height')
    count = 0
    for i in range(100):
        img = get_image()
        image = cv2.imread(img, cv2.IMREAD_COLOR)
        labels, boxs = detect(image, count)

        for label, box in (labels, boxs):
            objects.append(label, box.x_pos, box.y_pos, box.width, box.height)

        count += 1




