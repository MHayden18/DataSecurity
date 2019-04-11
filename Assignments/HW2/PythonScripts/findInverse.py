# GCD Function
import math
import string

for i in range(26):
	if math.gcd(i,26) == 1:
		print("Possible inverse:  " + str(i))
print("Done")