import serial
import time

if __name__ == "__main__":
        ser = serial.Serial('/dev/tty.usbmodem141401', 115200)

        input()
        print("Program start!")
        ser.write(str.encode('a'))

        ser.close()