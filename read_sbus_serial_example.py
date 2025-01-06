# read_sbus_serial_example.py
import time
from mysbus.sbus_serial import SBusSerial

def main():
    # تقدر تعدل البورت حسب إعداد الـPi
    reader = SBusSerial(port="/dev/ttyAMA0", baudrate=100000)
    reader.start()

    print("Reading SBUS frames... Press Ctrl+C to stop.")
    try:
        while True:
            if reader.read_frame():
                channels = reader.get_channels()
                fs = reader.get_failsafe()
                lf = reader.get_lost_frame()
                print(f"Channels: {channels}, Failsafe={fs}, LostFrame={lf}")
            time.sleep(0.01)
    except KeyboardInterrupt:
        reader.close()

if __name__ == "__main__":
    main()
