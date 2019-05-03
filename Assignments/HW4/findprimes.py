import math

def findprimes(a):
	primes = []
	for i in range(2,a-1):
		diff = a/i
		if diff.is_integer():
			primes.append(i)
	if len(primes) == 0:
		print("{} is prime".format(a))
	else:
		print(primes)


def main():
	findprimes(20413)
	

if __name__ == "__main__":
	main()