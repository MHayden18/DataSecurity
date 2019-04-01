import string
import math

alpha = 7
beta = 22
print("Starting affine decrypt with alpha = {0} and beta = {1}: \n".format(alpha, beta))

print("Finding modular inverse:")
running = True
inv_alpha = 1
while running:
	if ( (alpha * inv_alpha) % 26 == 1):
		print( "Inverse is:  {}".format(inv_alpha) )
		running = False
	else:
		inv_alpha += 1
		
input = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
output = ""

for letter in input:
	in_index = string.ascii_lowercase.index(letter)
	out_index = ( inv_alpha * (in_index - beta) ) % 26 
	output += string.ascii_lowercase[out_index]

print("")

print( "The output is: \n" + output )

