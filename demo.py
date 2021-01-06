import serial
import time
from arduino import My_Serial

if __name__ == "__main__":
        ser = My_Serial('/dev/ttyACM0', 115200, timeout=50)
        ser.send('a')
        ser.close()