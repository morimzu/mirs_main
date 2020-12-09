import time
import RPi.GPIO as GPIO
import numpy as np

i2c_addredd = 72
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

if __name__ == "__main__":
    while True:
        GPIO.setup(i2c_addredd, GPIO.IN)
        print(GPIO.input(i2c_addredd))
