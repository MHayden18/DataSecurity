import math
import random
import myCrypto as mc
	

def p1():
	return
	

def p2():
	p, q, e = 315349, 259907, 5
	n = p * q
	phi_n = (p-1)*(q-1)
	print("Public Key:  ({}, {})".format(e, n))
	print("Totient: {}".format(phi_n) )
	print("-----------------------------------------\n")
	
	d = mc.mulinv(e, phi_n)
	print("Private Key: ({}, {})".format(d, n) )
	
	print("-----------------------------------------\n")
	
	values = [41, 43, 71, 73, 541]
	for value in values:
		print("{} Generators:  {}".format(value, mc.find_generators(value)) )
	
	
def p3():
	p, q, e = 315349, 259907, 5
	# Problem 3 Encryption:
	plaintext = "``The US Army will never control the ground under the sky, if the US Air Force does not control the sky over the ground.'' -- Col Gene Cirillo, USAF (Ret)."
	output = []
	ciphertext = ""
	for character in plaintext:
		ct = mc.rsa_encode(ord(character), p, q, e)
		output.append( ct )
	print("Plaintext: " + plaintext )
	print("Ciphtertext:")
	print(output)

	
def p4():
	p, alpha, a, b = 1999, 1994, 1997, 2001
	print("Secret Key for Problem #4:  {}\n".format( mc.DH_Encode(alpha, p, a, b) ) )


def p5():
	p, alpha, A, B = 2999, 161, 2341, 192
	S = mc.DH_Decode(alpha, p, A, B)

	
def main():
	# Problem 2:
	print("-----------------------------------------\n")
	print("Starting Problem 2:")
	p2()

	# Problem 3:
	print("-----------------------------------------\n")
	print("Starting Problem 3:")
	p3()
	
	# Problem 4
	print("-----------------------------------------\n")
	print("Starting Problem 4:")
	p4()
	
	# Problem 5:
	print("-----------------------------------------\n")
	print("Starting Problem 5:")
	p5()

	
if __name__== "__main__":
	main()