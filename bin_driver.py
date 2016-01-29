#!/usr/bin/python

from bin import Bin

def main():
	b = Bin(6)
	print "b: " + str(b)

	i = int(b)
	print "int of b: " + str(i)

if __name__ == "__main__":
	main()