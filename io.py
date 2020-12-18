import time
import smbus

i2c = smbus.SMBus(1)
address = 0x71
SLEEPTIME = 0.5
DELAY = 0.1

if __name__ == '__main__':
    try:
        print ("cancel：CTRL+C")
        cnt = 1
        while True:
            i2c.write_i2c_block_data(address,0x00,[0x51])
            # 0x51が測定コマンド 51で単位がセンチメートル
            time.sleep(DELAY)

            block = i2c.read_i2c_block_data(address,0x00,4)
            distance = (block[2]<<8 | block[3])
            print(int(cnt),distance)
            cnt = cnt + 1
            time.sleep(SLEEPTIME)

    except KeyboardInterrupt:
        print("finishing...")
    finally:
        print("finish!!")