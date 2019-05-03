# GCD Function
import math
import string

inverse = []
for i in range(20128):
	if math.gcd(i,20128) == 1:
		inverse.append(i)
print(inverse)
print("Done")