"""
Author - Micah Hayden
Functions for Cryptography
"""
import math
import random


def lfsr(seed, taps):
	sr, xor = seed, 0
	print("Starting LFSR with initial state of {}:".format(sr))
	repeat = 1
	
	while 1:
		for t in taps:
			xor += int(sr[t])
		if xor%2 == 0.0:
			xor = 0
		else:
			xor = 1
		
		# Outputs: note, length of sr = 6
		length = len(sr) 
		print( "#{0}:    State = {1};  Output:  {2}".format(repeat, sr, sr[length - 1]))
		print
		repeat += 1
		
		sr, xor = str(xor) + sr[:-1], 0
		
		if sr == seed:
			break
		
	return
	
	
def DH_Encode(alpha, p, a, b):
	"""
	inputs - DH parameters
	output - secret integer
	"""
	print("Starting DH Key Encode")
	A = alpha ** a % p
	B = alpha ** b % p
	
	S1 = A ** b % p
	S2 = B ** a % p
	if (S1 == S2):
		return S1
	else:
		return -1


def DH_Decode(alpha, p, A, B):
	"""
	inputs - DH parameters
	outputs - secret integer
	"""
	print("Starting DH Decode:")
	for i in range(1, p):
		value = alpha ** i % p
		if value == A:
			a = i
		if value == B:
			b = i
	print("a = {}, b = {}".format(a, b))
	s1 = A ** b % p
	s2 = B ** a % p
	print("s = {}, {}".format(s1, s2))
	if (s1 == s2):
		return s1
	else:
		return -1
	
	
def find_generators(p):
	"""
	p = prime number
	returns set of generators 
	"""
	primes = []
	generators = []
	# Find all primes less than p:
	for i in range(2, p-1):
		if math.gcd(i, p) == 1:
			# Primes that divide p-1
			if ((p-1) % i) == 0:
				primes.append(i)
			
	for alpha in range(2, p-1):
		alpha_gen = True
		for prime in primes:
			num = int( (p-1) / prime )
			if (alpha**num % p == 1):
				alpha_gen = False
		if alpha_gen:
			generators.append(alpha)
	return generators
	
	
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
	

def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b
		

def rsa_decode(a, p, q):
	"""
	a - ciphertext
	p, q - primes
	returns - plaintext
	"""
	n = p * q
	d = 13127
	# plaintext = ciphertext ^ d mod n
	
	output = (a ** d) % n
	return output


def rsa_encode(pt, p, q, e):
	"""
	pt = plaintext
	e - public exponent
	p, q = primes
	returns - ciphertext
	"""
	n = p*q
	return (pt ** e) % n
	

def isPrime_fermat(p, s):
	exp = p - 1
	for i in range(s):
		temp = random.randint(2, p-2)
		if pow(temp, exp, p) != 1:
			return False
	return True
	
	
def isPrime_mr(p, s):
	# Get p-1 in terms of 2^u * r:
	temp = (p-1)
	count = 0
	while temp % 2 == 0:
		temp = temp//2
		count += 1
	u = count
	r = (p-1)//(2 ** u)
	#test = pow(2, u) * r
	
	# Start primality test:
	for i in range(s):
		a = random.randint(2, p-2)
		z = pow(a, r, p)
		if z == 1:
			return True
		if z != p-1:					# if z = 1, would have already returned
			for j in range(1, u-1):		# Loop from 1 to u-1
				z = pow(z, 2, p)		# z <- z^2 mod p
				if z == 1:				
					return False
				if z == (p-1):	
					return True
	return True

	
def DSA_Primes_Gen():
	# Generate q:
	foundQ = False
	foundP = False
	upper = pow(2, 161)
	lower = pow(2, 160)
	
	while( not foundQ ):
		q = random.randint(lower, upper)
		if q % 2 == 0:
			foundQ = False
		else:
			foundQ = isPrime_fermat(q, 15)
	for i in range(4096):
		upper = pow(2, 1024)
		lower = pow(2, 1023)
		M = random.randint(lower, upper)
		M_r = pow(M, 1, 2*q)
		p = M - M_r + 1
		if isPrime_fermat(p, 15):
			break
	return p, q
	

def DSA_PubKey(p, q):
	upper = pow(2, 161)
	lower = pow(2, 160)
	alpha = random.randint(lower, upper)
	d = random.randint(1, q-1)
	beta = pow(alpha, d, p)
	
	print("Public Key:")
	print("p = {}".format(p))
	print("q = {}".format(q))
	print("alpha = {}".format(alpha))
	print("beta = {}".format(beta))
	print("d = {}".format(d))
	return alpha, beta, d
	


	