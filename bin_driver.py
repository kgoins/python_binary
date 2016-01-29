#!/usr/bin/python

from bin import Bin

def main():
	b = Bin(6)
	print "b: " + str(b)

	i = int(b)
	print "int of b: " + str(i)

	b1 = Bin("101")
	print "b1: " + str(b1)

	print b + b1

if __name__ == "__main__":
	main()