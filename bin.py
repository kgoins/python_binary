#!/usr/bin/python

from math import log
from math import floor

import bin_conversions as binconv
import bin_math as binmath

class Bin:
    def __init__(self, num):
        self.bin = binconv.to_bin(num)
        self.bits = len(self.bin)

    # conversion overrides
    def __str__(self):
        return "0b" + self.bin

    def __int__(self):
        return binconv.bin_to_int(self.bin)

    # math operator overrides
    def __add__(self, targ):
        return Bin(binmath.add(self.bin, targ.bin))


def bits_needed(num):
    if isinstance(num, int):
        return floor(log(num, 2)) +1