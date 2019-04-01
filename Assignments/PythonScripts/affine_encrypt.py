import string
import math

alpha = 7
beta = 22
print("Starting affine encrypt with alpha = {0} and beta = {1}: \n".format(alpha, beta))
		
input = "firstthesentenceandthentheevidencesaidthequeen"
output = ""

for letter in input:
	in_index = string.ascii_lowercase.index(letter)
	out_index = ( in_index * alpha + beta) % 26 
	output += string.ascii_lowercase[out_index]

print("")

print( "The output is: \n" + output )

