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