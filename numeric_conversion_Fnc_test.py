import numeric_conversion_Fnc as target_ncFnc
import pytest

###############################################
# 単体テスト
###############################################

class TestNumericConversionFnc:
    # tens_placeのテスト
    def test_tens_place(self):
        assert target_ncFnc.tens_place(11) == 1
        assert target_ncFnc.tens_place(99) == 9
    def test_tens_place_negative(self):
        assert target_ncFnc.tens_place(-11) == -1
        assert target_ncFnc.tens_place(-99) == -9

    # ones_placeのテスト
    def test_ones_place(self):
        assert target_ncFnc.ones_place(12) == 2
        assert target_ncFnc.ones_place(99) == 9

    def test_ones_place_negative(self):
        assert target_ncFnc.ones_place(-12) == 8
        assert target_ncFnc.ones_place(-99) == 1

    # ascii_to_numのテスト
    def test_ascii_to_num_0(self):
        assert target_ncFnc.ascii_to_num(ord('0')) == 0

    def test_ascii_to_num_1(self):
        assert target_ncFnc.ascii_to_num(ord('1')) == 1

    def test_ascii_to_num_2(self):
        assert target_ncFnc.ascii_to_num(ord('2')) == 2

    def test_ascii_to_num_3(self):
        assert target_ncFnc.ascii_to_num(ord('3')) == 3

    def test_ascii_to_num_4(self):
        assert target_ncFnc.ascii_to_num(ord('4')) == 4

    def test_ascii_to_num_5(self):
        assert target_ncFnc.ascii_to_num(ord('5')) == 5
    
    def test_ascii_to_num_6(self):
        assert target_ncFnc.ascii_to_num(ord('6')) == 6

    def test_ascii_to_num_7(self):
        assert target_ncFnc.ascii_to_num(ord('7')) == 7

    def test_ascii_to_num_8(self):
        assert target_ncFnc.ascii_to_num(ord('8')) == 8

    def test_ascii_to_num_9(self):
        assert target_ncFnc.ascii_to_num(ord('9')) == 9

    def test_ascii_to_num_error(self):
        assert target_ncFnc.ascii_to_num(ord('a')) == -1
        
    # dec_to_displayNumのテスト
    def test_dec_to_displayNum_0(self):
        assert target_ncFnc.dec_to_displayNum(0) == b'\x21'

    def test_dec_to_displayNum_1(self):
        assert target_ncFnc.dec_to_displayNum(1) == b'\xf9'

    def test_dec_to_displayNum_2(self):
        assert target_ncFnc.dec_to_displayNum(2) == b'\x15'

    def test_dec_to_displayNum_3(self):
        assert target_ncFnc.dec_to_displayNum(3) == b'\x91'

    def test_dec_to_displayNum_4(self):
        assert target_ncFnc.dec_to_displayNum(4) == b'\xc9'

    def test_dec_to_displayNum_5(self):
        assert target_ncFnc.dec_to_displayNum(5) == b'\x83'

    def test_dec_to_displayNum_6(self):
        assert target_ncFnc.dec_to_displayNum(6) == b'\x0b'

    def test_dec_to_displayNum_7(self):
        assert target_ncFnc.dec_to_displayNum(7) == b'\xe1'

    def test_dec_to_displayNum_8(self):
        assert target_ncFnc.dec_to_displayNum(8) == b'\x01'

    def test_dec_to_displayNum_9(self):
        assert target_ncFnc.dec_to_displayNum(9) == b'\xc1'

    def test_dec_to_displayNum_error_negative(self):
        assert target_ncFnc.dec_to_displayNum(-1) == 0

    def test_dec_to_displayNum_error_large(self):
        assert target_ncFnc.dec_to_displayNum(10) == 0
        
    def test_dec_to_displayNum_error(self):
        assert target_ncFnc.dec_to_displayNum(ord('a')) == 0
