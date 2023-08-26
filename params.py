#################################################
# 定数
#################################################
ADR_H = 0x22
ADR_M = 0x21
ADR_S = 0x20

NUM_R = 0x13
NUM_L = 0x12

DIR_A = 0x00
DIR_B = 0x01

ALL_ZERO = b'\x00'
ALL_ONE = b'\xff'

NUM_ZERO = b'\x21'
NUM_ONE = b'\xf9'
NUM_TWO = b'\x15'
NUM_THREE = b'\x91'
NUM_FOUR = b'\xc9'
NUM_FIVE = b'\x83'
NUM_SIX = b'\x0b'
NUM_SEVEN = b'\xe1'
NUM_EIGHT = b'\x01'
NUM_NINE = b'\xc1'
NUM_DOT = b'\xfe'

#################################################
# ディスプレイに格納するデータを保持する。
# バイナリ形式に限定する。b'\x00'など。
#################################################
class store_time:
    def __init__(self, h_l, h_r, m_l, m_r, s_l, s_r, micro):
        self.hour_L=h_l
        self.hour_R=h_r
        self.min_L=m_l
        self.min_R=m_r
        self.sec_L=s_l
        self.sec_R=s_r
        self.micro=micro

#memo: pythonは参照渡し