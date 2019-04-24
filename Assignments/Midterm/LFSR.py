def lfsr(IV, taps, numOut):
	"""
	IV - initialization vector
	taps - tap indices
	numOut - number of outputs desired 
	"""
	state = IV
	sum = 0
	print("Starting LFSR with initial state of {}:".format(state))
	round = 0
	output = []
	while round <= numOut:
		for tap in taps:
			sum += int(state[tap])	# Sum taps
		if sum % 2 == 0.0:
			sum = 0
		else:
			sum = 1
		
		# Append final register to output:
		output.append( state[-1] )
		
		# Move sum to first register, shift all others over
		state = str( sum ) + state[:-1]
		
		# Reset sum to zero:
		sum = 0
		
		# Increment round:
		round += 1
	# First output was the clocking of the IV, not an actual output
	# This was verified by testing this on the LFSR of HW3.
	return output[1:]


def main():
	# print( lfsr('100100', (5, 0), 128) )
	print( lfsr('010101', (1, 0), 100) )
	

if __name__ == "__main__":
	main()