import math
import random
import myCrypto as mc
import exam_q1 as q1

def p1():
	q1.rsa_crt()
	

def p2():
	p, q = mc.DSA_Primes_Gen()
	alpha, beta, d = mc.DSA_PubKey(p, q)
	h_x = 120654484320263588514608261628026439285
	
	# Generate signature:
	ke = random.randint(1, q)
	k_inv = mc.mulinv(ke, q)
	r = pow(alpha, ke, p) % q
	print("r = {}".format(r))
	
	s = ((h_x + d*r) * k_inv ) % q
	print("s = {}".format(s))
	
	# Verification:
	w = mc.mulinv(s, q)
	u1 = pow( w * h_x, 1, q)
	u2 = pow(w * r, 1, q)
	v = (pow(alpha, u1, p) * pow(beta, u2, p) ) % q

	print("\nVerification:")
	print( "v = {}".format( v ) )
	print( "r = {}".format( r ) )
def p3():

	numbers = [1798758724805508496502821597814073869874527469062680029407582127634855549890892589223,\
	1590185219871957542493116114600499667909712644341208146306088343203153786078500704513,\
	1558300851914478563667041381534759830705314746936787434965724391346205826745658837071,\
	1114877723960165303086266262246739999351736545842688547890178051251754046778209265277,\
	1701649747274389836328758796469387963534468348605280671300393693087386178552597581769,\
	1117051982972964176255977546560314971353934122161907626868626575920914731369490827133,\
	1611569730562977142991554343582160703829926902359468746732249403748667962099955153711,\
	1006744242693144138991183226283715627966199890221950842268830665672999172760980350997,\
	1478334445679686145289703414648978484686846953084162826560705697383514195532048498801,\
	1551284045384578966055927057771184821750749160366773302510856670260232043818664801937]
	
	
	s = 100
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	count = 0
	isPrime = False
	for number in numbers:
		if mc.isPrime_fermat(number, s):
			if mc.isPrime_mr(number, s):
				print("{} - {} is probably prime".format(letters[count], number))
			else:
				print("{} - {} is composite".format(letters[count], number))
		else:
			print("{} - {} is composite".format(letters[count], number))
		count += 1


def main():
	
	# Problem 1:
	#print("-----------------------------------------\n")
	#print("Starting Problem 1:")
	#p1()
	
	# Problem 2:
	#print("-----------------------------------------\n")
	#print("Starting Problem 2:")
	p2()

	# Problem 3:
	#print("-----------------------------------------\n")
	#print("Starting Problem 3:")
	#p3()
	

	
if __name__== "__main__":
	main()