import math
import random


def rsa_decrypt(e, n):
	for p in range(math.floor(math.sqrt(n)), 2, -1):
		if n % p == 0:
			q = n/p
			return p, q
		
		
def main():
	e = 5
	n = 2962324423598608965862974910236458725007437939684789550178974023998496502140571365918899417655751929
	
	p, q = rsa_decrypt(e, n)
	print("p = {0}, q = {1}".format(p, q))
	
	
if __name__== "__main__":
	main()