import string
import math

def ModularInverse(alpha, alphabet):
	running = True
	size = len(alphabet)
	inv_alpha = 1
	while (running and inv_alpha < size):
		if ( (alpha * inv_alpha) % size == 1):
			print( "Modular inverse of {0} is: {1}".format(alpha, inv_alpha) )
			running = False
			return inv_alpha
		else:
			inv_alpha += 1
			
	# No modular inverse for alpha
	return 0

def affineDecrypt(inv_alpha, beta, input, alphabet):
	output = ""
	for letter in input:
		in_index = alphabet.index(letter)
		out_index = ( inv_alpha * (in_index - beta) ) % len(alphabet)
		output += alphabet[out_index]
	return output

def affineEncrypt(alpha, beta, input, alphabet):
	output = ""
	for letter in input:
		in_index = alphabet.index(letter)
		out_index = ( in_index * alpha + beta) % len(alphabet)
		output += alphabet[out_index]
	return output

	
def checkInputs(alpha, beta, alphabet):
	
	# Is alphabet in length requirements:
	if (len(alphabet) < 26 or len(alphabet) > 256):
		print("Invalid alphabet size")
		return 1
		
	# Is alpha within bounds:
	if (alpha == 0 or alpha > len(alphabet)-1):
		print("Invalid value for alpha")
		return 1
	
	# Is beta within bounds:
	if (beta < 0 or beta >= len(alphabet)):
		print("Invalid value for beta")
		return 1
		
	# Does alpha have modular inverse:
	gcd = math.gcd(alpha, len(alphabet))
	if (gcd != 1):
		print("Invalid value for alpha - no modular inverse")
		return 1
	
	return 0
		
def main():

	# Input your alphabet here:
	alphabet = "abcdefghijklmnopqrstuvwxyz"
			
	# input your key values here:
	alpha = 12
	beta = 25
	
	# Which mode are we in:
	encrypt = False
	
	if (checkInputs(alpha, beta, alphabet)):
		print("Exiting due to invalid input")
		return
		
	if encrypt:
		print("Starting encrypt with alpha = {0} and beta = {1}: \n".format(alpha, beta))
		input = "firstthesentenceandthentheevidencesaidthequeen"
		output = affineEncrypt(alpha, beta, input, alphabet)
	else:
		print("Starting decrypt with alpha = {0} and beta = {1}: \n".format(alpha, beta))
		input = "!f@jvvwpjphvphupzhdvwphvwppqfdphupjzfdvwpoepph"
		output = affineDecrypt(ModularInverse(alpha, alphabet), beta, input, alphabet)
	
	print( "The output is: \n" + output )

if __name__ == "__main__":
	main()
