import serial
import time
from arduino import My_Serial

if __name__ == "__main__":
        ser = My_Serial('/dev/tty.usbmodem141401', 115200)

        input()
        print("Program start!")
        ser.write('r;15;20:'.encode('utf-8'))
