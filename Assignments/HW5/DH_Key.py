import math
import random

def DH_Encode(alpha, p, a, b):
	print("Starting DH Key Encode")
	A = alpha^a % p
	B = alpha^b % p
	
	S1 = A^b % p
	S2 = B^a % p
	if (S1 == S2):
		return S1
	else:
		return -1


def DH_Decode(alpha, p, A, B):
	print("Starting DH Decode:")
	for a in range(2, p-2):
		for b in range(2, p-2):
			if (A^b % p) == (B^a % p):
				print("a = {0}, b = {1}".format(a, b) )
				return (A^b % p)
	
	
def main():
	p, alpha, a, b = 1999, 1994, 1997, 2001
	print("Secret Key for Problem #3:  {}\n".format( DH_Encode(alpha, p, a, b) ) )
	
	# Problem 4:
	p, alpha, A, B = 2999, 161, 2341, 192
	S = DH_Decode(alpha, p, A, B)
	print ("Secret Key for Problem #4: {}".format(S) )

	
if __name__== "__main__":
	main()