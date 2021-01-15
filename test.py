import serial
import time
 
ser = serial.Serial('/dev/tty.usbmodem141201', 115200)
time.sleep(1.0)
for i in range(10):
        ser.write('a'.encode())
        print("LED ON")
        time.sleep(0.5)
        ser.write('0'.encode())
        print("LED OFF")
        time.sleep(0.5)

ser.close()
print("bbb")