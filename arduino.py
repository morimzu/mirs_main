import serial
import time

'''
#ser = serial.Serial('/dev/ttyACM0', 9600)
ser = serial.Serial('/dev/tty.usbmodem142401', 115200)  # PCでArduinoを動かす時用 ls /dev　をしてそれっぽいのを入れておく．

def arduino(orders):
    print("\n<arduino module>")
    
    for order in orders:
        ser.write(str.encode(order))
        print(order)
    
    response = ser.read_until(str.encode("OK"))

    print(response)
    print("status: OK")

    ser.close()
    print('Serial closed!')
'''

class My_Serial(serial.Serial):
    def send(self, msgs):
        for msg in msgs:
            self.write(str.encode(msg))
            print("sent Order: ", msg)
        
        self.check_response()
        
    def check_response(self):
        print("Now waiting a response from the Arduino.")
        self.response = self.read_until(str.encode("OK"))[-2:]
        self.show_response()
    
    def show_response(self):
        print(self.response)

    def checkout(self):
        print("Now closing serial connection.")
        self.close()
        print("closed.")

    def __del__(self):
        self.checkout()


'''
for i in range(10):
        ser.write(str.encode('a'))
        print("LED ON")
        time.sleep(0.5)
        ser.write(str.encode ('0'))
        print("LED OFF")
        time.sleep(0.5)

ser.write(str.encode('motor'))
time.sleep(0.5)

ser.close()
print("bbb")
'''