#!/usr/bin/python

# any bins passed to normalize will have unequal lengths
def normalize(bin1,bin2):
	if len(bin1) < len(bin2):
		bin1, bin2 = bin2, bin1
	diff = len(bin1) - len(bin2)
	for i in range(0, diff):
		bin2 = '0' + bin2
	return (bin1, bin2)

# bin1/2 are binary numbers represented by strings
def add(bin1, bin2):
	if len(bin1) != len(bin2):
		bin1, bin2 = normalize(bin1, bin2)

	result = ""
	cin = 0	
	for i in range(0,len(bin1)):
		bitsum = int(bin1[i]) + int(bin2[i]) + cin
		cin = 0

		if bitsum > 1:
			cin = 1
			if bitsum == 2:
				bitsum = 0
			elif bitsum == 3:
				bitsum = 1

		result = str(bitsum) + result
		i += 1

	return result

print add("101", "1")



