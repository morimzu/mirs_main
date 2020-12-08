# 転移学習に用いるデータセット作成のために作っただけ

from camera_test import get_image
import time


if __name__ == "__main__":
    t = 0
    for j in range(15):
        for i in range(10):
            t = j * 10 + i
            count = ('0000' + str(t))[-5:]
            get_image(count)
        print(t)
        input("next session: ")
        