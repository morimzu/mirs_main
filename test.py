import serial
import time
from arduino import My_Serial

if __name__ == "__main__":
        ser = My_Serial('/dev/ttyACM0', 115200, timeout=50)
        ser.send('r;15;20.0:')
        ser.send('t;0.5;73.65182845264873:')
        ser.send('r;15;15.632018423735307:')
        ser.send('t;0.5;-73.65182845264873:')
        ser.send('r;15;20:')
        ser.close()