#!/usr/bin/python

from math import log
from math import floor

class Bin:
    def __init__(self, num):
        self.int = 0
        self.bin = ""
        self.len = 0

        if isinstance(num, int):
        	self.int = num
        	self.bin = int_to_bin(num)
        	self.len = len(bin)

        elif isinstance(num, str):
        	self.bin = num
        	self.len = len(num)


def bits_needed(num):
	if isinstance(num, int):
		return floor(log(num, 2)) +1

def int_to_bin(int):
	targ = int
	bits = ""

	while targ > 0:
		r = targ % 2
		bits = str(r) + bits
		targ = (targ - r) / 2

	return bits

def bin_to_int(bin):
	targ = bin
	int_result = 0

	for i in range(len(targ)-1,0, -1):
		print "i: " + str(i)
		print "bin[i]: " + bin[i]
		int_result += int(bin[i]) * 2**i
		print "result: " + str(int_result)

	return int_result