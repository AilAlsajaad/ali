# sbus_decoder.py
SBUS_FRAME_LENGTH = 25

class SBUSDecoder:
    def __init__(self):
        self.channels = [0]*16
        self.failsafe = False
        self.lost_frame = False

    def parse_frame(self, frame: bytes):
        """ يحلل 25 بايت من SBUS ويحدث قيم القنوات والفيلسيف/اللوس فريم """
        if len(frame) != SBUS_FRAME_LENGTH:
            print("Frame length error!")
            return False

        # SBUS يبدأ غالبًا بـ 0x0F أو 0x0E
        if frame[0] not in (0x0F, 0x0E):
            print("Invalid start byte:", frame[0])
            return False

        # فك ال 16 قناة (كل قناة 11 بت) من بايتات [1..22]
        data = int.from_bytes(frame[1:23], byteorder='little', signed=False)
        
        for ch in range(16):
            ch_data = (data >> (ch * 11)) & 0x7FF
            self.channels[ch] = ch_data

        # البايت رقم 23 يحتوي على فلاغز failsafe/lost frame
        flg = frame[23]
        self.lost_frame  = (flg & 0x04) != 0
        self.failsafe    = (flg & 0x08) != 0

        return True

    def get_channels(self):
        return self.channels

    def get_failsafe(self):
        return self.failsafe

    def get_lost_frame(self):
        return self.lost_frame
