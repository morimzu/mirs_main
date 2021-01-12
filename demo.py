import serial
import time

ser = serial.Serial('/dev/tty.usbmodem141401', 115200)
time.sleep(0.1)
ser.write('a'.encode('utf-8'))
