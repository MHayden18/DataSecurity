import string
import math

def ModularInverse(alpha):
	running = True
	inv_alpha = 1
	while running:
		if ( (alpha * inv_alpha) % 26 == 1):
			print( "Modular inverse of {0} is: {1}".format(alpha, inv_alpha) )
			running = False
			return inv_alpha
		else:
			inv_alpha += 1
			

def affineDecrypt(inv_alpha, beta, input):
	output = ""
	for letter in input:
		in_index = string.ascii_lowercase.index(letter)
		out_index = ( inv_alpha * (in_index - beta) ) % 26 
		output += string.ascii_lowercase[out_index]
	return output

def affineEncrypt(alpha, beta, input):
	output = ""
	for letter in input:
		in_index = string.ascii_lowercase.index(letter)
		out_index = ( in_index * alpha + beta) % 26 
		output += string.ascii_lowercase[out_index]
	return output

def main():
	encrypt = True
	alpha = 7
	beta = 22
	if encrypt:
		print("Starting encrypt with alpha = {0} and beta = {1}: \n".format(alpha, beta))
		input = "firstthesentenceandthentheevidencesaidthequeen"
		output = affineEncrypt(alpha, beta, input)
	else:
		print("Starting decrypt with alpha = {0} and beta = {1}: \n".format(alpha, beta))
		input = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
		output = affineDecrypt(ModularInverse(alpha), beta, input)
	
	print( "The output is: \n" + output )

if __name__ == "__main__":
	main()
