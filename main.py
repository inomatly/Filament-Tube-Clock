"""
MicroPython, TinyRTC
@tamagogyunyu@gmail.com
"""

from machine import I2C, Pin, RTC, UART, disable_irq, enable_irq
from ds1307 import DS1307
from time import sleep
from params import store_time
#import sys

sleep(5)

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
#関数宣言
#################################################

#################################################
# ディスプレイの設定
# input: I2Cオブジェクト(RTC)
# output: なし
#################################################

def display_init(d):
    d.writeto_mem(ADR_H,DIR_A,b'\x00')
    d.writeto_mem(ADR_H,DIR_B,b'\x00')
    d.writeto_mem(ADR_M,DIR_A,b'\x00')
    d.writeto_mem(ADR_M,DIR_B,b'\x00')
    d.writeto_mem(ADR_S,DIR_A,b'\x00')
    d.writeto_mem(ADR_S,DIR_B,b'\x00')
    return 0

#################################################
# ディスプレイをオフ
# input: I2Cオブジェクト(RTC)
# output: なし
#################################################
def display_off(d):
    d.writeto_mem(ADR_H,NUM_L,ALL_ONE)
    d.writeto_mem(ADR_H,NUM_R,ALL_ONE)
    d.writeto_mem(ADR_M,NUM_L,ALL_ONE)
    d.writeto_mem(ADR_M,NUM_R,ALL_ONE)
    d.writeto_mem(ADR_S,NUM_L,ALL_ONE)
    d.writeto_mem(ADR_S,NUM_R,ALL_ONE)
    return 0

#################################################
# test用の関数
# input: I2Cオブジェクト(RTC)
# output: なし
#################################################
def display_test_a(d):
    d.writeto_mem(ADR_H,NUM_L,NUM_ONE)
    d.writeto_mem(ADR_H,NUM_R,NUM_TWO)
    d.writeto_mem(ADR_M,NUM_L,NUM_THREE)
    d.writeto_mem(ADR_M,NUM_R,NUM_FOUR)
    d.writeto_mem(ADR_S,NUM_L,NUM_FIVE)
    d.writeto_mem(ADR_S,NUM_R,NUM_SIX)
    return 0

#################################################
# input:hexでもdecでも可。pythonの謎。
# output: 10の位を返す
#################################################
def tens_place(num):
    return int(num / 10)

#################################################
# input : hexでもdecでも可。pythonの謎。
# output: 1の位を返す
#################################################
def ones_place(num):
    return int(num % 10)

#################################################
# input : ascii code。0~9。
# output: decの0~9
#################################################
def ascii_to_num(ascii):
    if ascii == 48:
        return 0
    elif ascii == 49:
        return 1
    elif ascii == 50:
        return 2
    elif ascii == 51:
        return 3
    elif ascii == 52:
        return 4
    elif ascii == 53:
        return 5
    elif ascii == 54:
        return 6
    elif ascii == 55:
        return 7
    elif ascii == 56:
        return 8
    elif ascii == 57:
        return 9
    else:
        return -1  #一回くらいエラーが来てもOK

#################################################
# input: dec。ただしhexも可
# output: b'\x00'など，バイナリ。
#################################################
def dec_to_displayNum(decnum: int):
    global NUM_ZERO
    global NUM_ONE
    global NUM_TWO
    global NUM_THREE
    global NUM_FOUR
    global NUM_FIVE
    global NUM_SIX
    global NUM_SEVEN
    global NUM_EIGHT
    global NUM_NINE

    if decnum == 1:
        return NUM_ONE
    elif decnum == 2:
        return NUM_TWO
    elif decnum == 3:
        return NUM_THREE 
    elif decnum == 4:
        return NUM_FOUR
    elif decnum == 5:
        return NUM_FIVE
    elif decnum == 6:
        return NUM_SIX
    elif decnum == 7:
        return NUM_SEVEN
    elif decnum == 8:
        return NUM_EIGHT
    elif decnum == 9:
        return NUM_NINE
    elif decnum == 0:
        return NUM_ZERO
    else:
        return 0

#################################################
# input : hexでもdecでも可。pythonの謎。,I2Cオブジェクト(RTC)
# output: ディスプレイに表示
#################################################
def display_out(now: store_time, d):
    d.writeto_mem(ADR_H,NUM_L,dec_to_displayNum(now.hour_L))
    d.writeto_mem(ADR_H,NUM_R,dec_to_displayNum(now.hour_R))
    d.writeto_mem(ADR_M,NUM_L,dec_to_displayNum(now.min_L))
    d.writeto_mem(ADR_M,NUM_R,dec_to_displayNum(now.min_R))
    d.writeto_mem(ADR_S,NUM_L,dec_to_displayNum(now.sec_L))
    d.writeto_mem(ADR_S,NUM_R,dec_to_displayNum(now.sec_R))
    return 0

#################################################
# input : rtcのタプル[7], 更新するインスタンス
# output: store_time 型のインスタンスに値を格納する
#################################################
def update_time(now):
    ts = store_time(0,0,0,0,0,0,0)
    ts.hour_L=tens_place(now[4])
    ts.hour_R=ones_place(now[4])
    ts.min_L=tens_place(now[5])
    ts.min_R=ones_place(now[5])
    ts.sec_L=tens_place(now[6])
    ts.sec_R=ones_place(now[6])
    return ts

#################################################
# input : GPSのbyte, rtcオブジェクト
# output: rtcオブジェクト内部のメモリに書き込み
#################################################
def correct_time(buff, rtc_write):
    #print(str(buff)+"type: "+str(type(buff))) 
    year = ascii_to_num(buff[24])*1000+ascii_to_num(buff[25])*100 + ascii_to_num(buff[26])*10 + ascii_to_num(buff[27])
    #print("Y: "+str(year))
    month = ascii_to_num(buff[21])*10 + ascii_to_num(buff[22])
    #print("M: "+str(month))
    date = ascii_to_num(buff[18])*10 + ascii_to_num(buff[19])
    #print("d: "+str(date))
    day = 2
    hour = ascii_to_num(buff[7])*10 + ascii_to_num(buff[8]) + 9
    if hour >25:
        hour = hour-24
    #print("h: "+str(hour))
    mini = ascii_to_num(buff[9])*10 + ascii_to_num(buff[10])
    #print("m: "+str(mini))
    sec = ascii_to_num(buff[11])*10 + ascii_to_num(buff[12])
    mic = ascii_to_num(buff[14])
    #print("s: "+str(sec)+"."+str(mic))
    rtc=(year,month,date,day,hour,mini, sec,mic)
    print("rtc: "+str(rtc))
    rtc_write.datetime(rtc)
    return 0

#################################################
# gpsからデータを受信。
# input : GPS(UARTオブジェクト)
# output: GPSからのデータ byte
#################################################
def read_gps(gps):
    i = 0
    while i < 2:
        if gps.any() > 26:
            buffer = gps.read()
            i = i+1
    return buffer

#################################################
# 割り込み
#################################################
def callback(pin):
    global ledRed
    global uart
    global ds_rtc
    ledRed.high()
    i=0
    b= read_gps(uart)
    correct_time(b,ds_rtc) #後で変更
    ledRed.low()
    return 0

#################################################
# configuration
#################################################
led25 = Pin(25, Pin.OUT)
ledRed = Pin(15, Pin.OUT, Pin.PULL_UP)

sw = Pin(14, Pin.IN, Pin.PULL_UP)
sw.irq(trigger=Pin.IRQ_FALLING, handler=callback)

i2c = I2C(1,scl = Pin(3),sda = Pin(2), freq=100000)
ds_rtc = DS1307(i2c)
sleep(1)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))#GPS
#state = disable_irq()

#################################################
# main関数
#################################################
def main():
    global led25
    global ledRed
    global sw
    global i2c
    global ds_rtc

    #
    # 変数定義
    time_s = store_time(0,0,0,0,0,0,0) #h,h,m,m,s,s,f
    # 初期化処理
    led25.high()
    ledRed.high()
    display_init(i2c)
    display_off(i2c)

    buf=read_gps(uart)
    correct_time(buf,ds_rtc)
    sleep(1)
    print("#"+str(ds_rtc.datetime()))
    ledRed.low()

    while (1):
        #enable_irq(state)
        rtc_now = ds_rtc.datetime()
        time_s = update_time(rtc_now) #rtcから構造体にデータ取得
        display_out(time_s,i2c)
        sleep(0.5)
        if ((time_s.hour_L==1 and time_s.hour_R==1 and time_s.min_L == 5 and time_s.min_R == 9 and time_s.sec_L == 5 and time_s.sec_R >= 9) or (time_s.hour_L==1 and time_s.hour_R==2 and time_s.min_L == 0 and time_s.min_R == 0 and time_s.sec_L == 0 and time_s.sec_R < 1) ):
            led25.high()
            buf=read_gps(uart)
            correct_time(buf,ds_rtc)
            led25.low()
    print("stop")

if __name__ == '__main__':
    main()