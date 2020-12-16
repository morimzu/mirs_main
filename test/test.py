import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

for i in range(10):
        ser.write(str.encode('a'))
        print("LED ON")
        time.sleep(2)
        ser.write(str.encode('0'))
        print("LED OFF")
        time.sleep(2)

ser.close()
print("bbb")