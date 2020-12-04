# 転移学習のためのデータセット作りのために作っただけ
from datetime import datetime
import cv2, os

def get_image(count):
    print("\n<camera module>")

    current_dir = os.path.dirname(os.path.abspath(__file__)) + '/'

    cam = cv2.VideoCapture(0)
    if cam == None:
        return False


    # カメラから映像を読み込む
    _, img = cam.read()

    # 保存先を設定
    shoot_time = datetime.now()
    image_file = "./deskImages/" + 'deskImages_' + str(count) +'.jpg'

    # 画像ファイルとして書き出す
    cv2.imwrite(image_file, img)

    # 事後処理
    cam.release()
    cv2.destroyAllWindows()

    return image_file