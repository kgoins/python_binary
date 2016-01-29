#!/usr/bin/python

from math import log
from math import floor

class Bin:
    def __init__(self, num):
        self.bin = to_bin(num)
        self.bits = len(self.bin)

    def __str__(self):
        return "0b" + self.bin

    def __int__(self):
        return bin_to_int(self.bin)


def to_bin(num):
    if isinstance(num, str):
        return str_to_bin(num)
    elif isinstance(num, int):
        return int_to_bin(num)

def bits_needed(num):
    if isinstance(num, int):
        return floor(log(num, 2)) +1

def str_to_bin(num):
    valid = True

    for i in num:
        if i not in ["0", "1"]:
            valid = False

    if valid == True:
        return num
    else:
        return None


def int_to_bin(num):
    bits = ""

    while num > 0:
        r = num % 2
        bits = str(r) + bits
        num = (num - r) / 2

    return bits


def bin_to_int(num):
    result = 0
    i = len(num)-1
    
    for bit in num:
        result += int(bit) * 2**i
        i -= 1

    return result