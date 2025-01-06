# sbus_serial.py
import serial
from .sbus_decoder import SBUSDecoder

class SBusSerial:
    def __init__(self, port="/dev/ttyAMA0", baudrate=100000):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.decoder = SBUSDecoder()

    def start(self):
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_TWO,
            timeout=0.02
        )

    def read_frame(self):
        """ يقرأ 25 بايت من المنفذ ويحاول تحليلها. يرجع True إذا نجح. """
        if self.ser.in_waiting >= 25:
            frame = self.ser.read(25)
            # لو أردت الانعكاس برمجيًا (إذا ما عندك عاكس عتادي) جرب:
            # frame = bytes([b ^ 0xFF for b in frame])
            success = self.decoder.parse_frame(frame)
            return success
        return False

    def get_channels(self):
        return self.decoder.get_channels()

    def get_failsafe(self):
        return self.decoder.get_failsafe()

    def get_lost_frame(self):
        return self.decoder.get_lost_frame()

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
