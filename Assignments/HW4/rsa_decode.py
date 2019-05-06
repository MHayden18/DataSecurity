import math

def find_factors(a):
	factors = []
	for p in range(2,a-1):
		if (a % p) == 0:
			factors.append(p)
			factors.append( int( a/p ) ) # Append q
			break
		
	if len(factors) == 0:
		print("{} is prime".format(a))
	else:
		print("p = {0}, q = {1}".format(factors[0], factors[1]))
	return factors
	
		
def rsa_decode(a, p, q):
	n = p * q
	d = 13127
	# plaintext = ciphertext ^ d mod n
	
	output = (a ** d) % n
	return output
	

def main():
	inputs = [236, 2743, 7983, 5919, 20213, 5520, 19563, 17083, 17083, 19326, 5919, 17258, 5919, 17215, 19563, 20213, 4940, 496]
	n = 20413
	e = 23
	p,q = find_factors(20413)
	outputs = ""
	plaintext = []
	for input in inputs:
		pt = rsa_decode(input, p, q)
		plaintext.append( pt )
		outputs +=  str( chr( pt ) )
	
	print("Plaintext: " + str(plaintext) )
	print("Output: " + outputs)
	

if __name__ == "__main__":
	main()