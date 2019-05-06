import math

def aks(p):
	if p==2: return True
	c = 1
	for i in range(p//2+1):
		c = c*(p-i) // (i+1)
		if c%p: return False
	return True
	
def main():
	primes = []
	upper = 1000
	for number in range(1, upper):
		output = int( aks(number) )
		if output:
			primes.append(number)
			#print("p = {}, is Prime: {}".format(number, output) )
	print( len(primes) )	

	
if __name__ == "__main__":
	main()