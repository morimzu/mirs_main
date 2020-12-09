import time
import RPI.GPIO as GPIO
import numpy as np

i2c_addredd = 0x72
GPIO.setup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

if __name__ == "__main__":
    while True:
        GPIO.setup(i2c_addredd, GPIO.IN)
        print(GPIO.input(i2c_addredd))
