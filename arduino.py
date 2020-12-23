import serial

class My_Serial(serial.Serial):
    def send(self, msgs):
        print("<Arduino module>")
        for msg in msgs:
            self.write(str.encode(msg))
            print("sent Order: ", msg)
        
        #self.check_response()
        
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