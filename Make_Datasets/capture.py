# 転移学習に用いるデータセット作成のために作っただけ

from camera_test import get_image
import time

if __name__ == "__main__":
    for i in range(100):
        count = ('0000' + str(i))[-5:]
        get_image(count)
        time.sleep(0.1)