#!/usr/bin/python

def to_bin(num):
    if isinstance(num, str):
        return str_to_bin(num)
    elif isinstance(num, int):
        return int_to_bin(num)

def bin_to_int(num):
    result = 0
    i = len(num)-1

    for bit in num:
        result += int(bit) * 2**i
        i -= 1

    return result

def int_to_bin(num):
    bits = ""

    while num > 0:
        r = num % 2
        bits = str(r) + bits
        num = (num - r) / 2

    return bits

def str_to_bin(num):
    valid = True

    for i in num:
        if i not in ["0", "1"]:
            valid = False

    if valid == True:
        return num
    else:
        return None