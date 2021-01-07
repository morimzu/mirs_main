import serial
import time

if __name__ == "__main__":
        ser = serial.Serial('/dev/ttyACM0', 115200)

        input()
        print("Program start!")
        ser.write('a')

        ser.close()