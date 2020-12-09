import time
import smbus

#SMBusの引数に1を指定する。Raspberry Piのi2cバスの番号
i2c = smbus.SMBus(1)
#デバイスのアドレス 0x68
addr = 0x72

if __name__ == "__main__":
    while True:
        data = i2c.read_byte_data(addr, 0x72)
        print(data)
        time.sleep(1.0)