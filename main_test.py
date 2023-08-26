import pytest
from main import read_gps, correct_time, update_time
from unittest.mock import MagicMock

###############################################
# スタブ
###############################################

class I2CStub:
    def __init__(self):
        self.memory = {}

    def readfrom_mem(self, addr, reg, num):
        return self.memory.get(reg)

    def writeto_mem(self, addr, reg, val):
        self.memory[reg] = val

class DS1307Stub:
    def __init__(self, i2c, addr=0x68):
        self.datetime_value = None

    def datetime(self, val=None):
        if val is None:
            return self.datetime_value
        self.datetime_value = val

class UARTStub:
    def __init__(self):
        self.buffer = None
        self.count = 0

    def any(self):
        return len(self.buffer) if self.buffer else 0

    def read(self):
        self.count += 1
        if self.count > 5 :
            #複数回繰り返すと正常な値が取得できる想定
            self.buffer = b'$GPZDA,131954.000,27,10,2022,,*5B\r\n'
        return self.buffer

# スタブを使用してDS1307からのデータを模倣する
def mock_ds1307_datetime():
    return (2022, 11, 10, 5, 12, 56, 11, 0)

###############################################
# 単体テスト
###############################################

class TestMain:
    # read_gpsのテスト
    def test_read_gps_normal(self):
        # Arrange
        uart_stub = UARTStub()
        message = b'$GPZDA,131954.000,27,10,2022,,*5B\r\n'
        uart_stub.buffer = message
        # Act
        read=read_gps(uart_stub)
        # Assert
        assert read == message

    def test_read_gps_invalid(self):
        # Arrange
        uart_stub = UARTStub()
        message = b'$GPZDA,501954.000,27,10,2022,,*5B\r\n'
        uart_stub.buffer = message
        # Act
        read=read_gps(uart_stub)
        # Assert
        assert read == b'$GPZDA,131954.000,27,10,2022,,*5B\r\n' #スタブで設定したメッセージ

#    def test_read_gps_nodata(self):
#        # Arrange
#        uart_stub = UARTStub()
#        # Act
#        read=read_gps(uart_stub)
#        # Assert
#        assert read == b'$GPZDA,131954.000,27,10,2022,,*5B\r\n' #スタブで設定したメッセージ

    # correct_timeのテスト
    def test_correct_time(self):
        i2c_stub = I2CStub()
        ds1307_stub = DS1307Stub(i2c_stub)
        buffer = b"$GPZDA,131954.000,27,10,2022,,*5B\r\n"
        correct_time(buffer, ds1307_stub)
        assert ds1307_stub.datetime_value == (2022, 10, 27, 2, 22, 19, 54, 0)

    def test_correct_time_invalid_data(self):
        i2c_stub = I2CStub()
        ds1307_stub = DS1307Stub(i2c_stub)
        buffer = b"$GPZDA,55555.000,55,99,9999,,*5B\r\n"
        correct_time(buffer, ds1307_stub)
        assert ds1307_stub.datetime_value != (9999, 99, 55, 2, 64, 55, 55, 0)


    # update_timeのテスト
    def test_update_time(self):
        ds_rtc = MagicMock()
        ds_rtc.datetime = mock_ds1307_datetime
        ts = update_time(ds_rtc.datetime())
        assert ts.hour_L == 1
        assert ts.hour_R == 2
        assert ts.min_L == 5
        assert ts.min_R == 6
        assert ts.sec_L == 1
        assert ts.sec_R == 1