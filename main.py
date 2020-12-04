import cv2

from camera import get_image
from ssd_model import detect
from arduino import My_Serial
from order import Order


if __name__ == "__main__":
    '''
    初期設定
    '''
    #ser = My_Serial('/dev/tty.usbmodem142401', 115200)
    
    count = 1
    img = get_image()
    image = cv2.imread(img, cv2.IMREAD_COLOR)          
    labels, boxs = detect(image, count)
    print(count)
    count += 1
    labels.append(':')
    print(labels)
    for box in boxs:
        box.show()

    order = Order('l',000, 000, 3000)

    #ser.send('a0a0a0a0:')
    #ser.send(order.order)
    #ser.checkout()