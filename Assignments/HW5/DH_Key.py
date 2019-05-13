# 2 <= Si <= p-2
# Problem 3:
import math
import random

def DH_Encode(alpha, p, a, b):
	print("Starting DH Key Encode")
	A = alpha^a % p
	B = alpha^b % p
	
	S1 = A^b % p
	S2 = B^a % p
	print("S1 = {0}, S2 = {1}".format(S1, S2))
	return S1


def DH_Decode(alpha, p, A, B):
	print("Starting DH Decode:")
	running = True
	for a in range(2, p-2):
		for b in range(2, p-2):
			if (A^b % p) == (B^a % p):
				print("a = {0}, b = {1}".format(a, b) )
				return (A^b % p)
	
	
def main():
	print("Starting problem 3:")
	p = 1999
	alpha = 1994
	a = 1997
	b = 2001
	print("Secret Key = {}\n".format( DH_Encode(alpha, p, a, b) ) )
	
	# Problem 4:
	print("Starting Problem 4 Solve:")
	p = 2999
	alpha = 161
	A = 2341
	B = 192
	S = DH_Decode(alpha, p, A, B)
	print ("Secret Key for Problem 4: {}".format(S) )

	
if __name__== "__main__":
	main()