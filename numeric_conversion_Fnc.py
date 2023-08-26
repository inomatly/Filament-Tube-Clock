from params import store_time, ADR_H, ADR_M, ADR_S, NUM_R, NUM_L, DIR_A, DIR_B, ALL_ZERO, ALL_ONE, NUM_ZERO, NUM_ONE, NUM_TWO, NUM_THREE, NUM_FOUR, NUM_FIVE, NUM_SIX, NUM_SEVEN, NUM_EIGHT, NUM_NINE, NUM_DOT

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
    NUM_ZERO
    NUM_ONE
    NUM_TWO
    NUM_THREE
    NUM_FOUR
    NUM_FIVE
    NUM_SIX
    NUM_SEVEN
    NUM_EIGHT
    NUM_NINE

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
