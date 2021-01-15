import serial
ser = serial.Serial('/dev/tty.usbmodem141201', 115200, timeout=0.3)
ser.write('r;15;20:'.encode())
