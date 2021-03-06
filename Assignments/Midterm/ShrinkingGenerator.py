def lfsr(state, taps):
	"""
	state - current state, initialized to IV
	taps - tap indices
	
	"""
	sum = 0
	for tap in taps:
		sum += int(state[tap])	# Sum taps
	if sum % 2 == 0.0:
		sum = 0
	else:
		sum = 1
	
	# Final register contains output bit:
	output = state[-1]
	
	# Move sum to first register, shift all others over
	state = str( sum ) + state[:-1]
	
	return output, state


def main():
	# Define variables, and define IV/taps for each LFSR:
	outputs_A = []
	states_A, states_S = [], []
	IV_A = '010101'
	IV_S = '11100'
	
	# Taps are indexed from left to right:
	taps_A = (0, 5)
	taps_S = (1, 4)
	
	# Clock both LFSRs from their IV:
	outBit_A, stateOut = lfsr(IV_A, taps_A )
	states_A.append( stateOut )
	
	outBit_S, stateOut = lfsr(IV_S, taps_S )
	states_S.append( stateOut )
	# Check if first bit is counted:
	if outBit_S == '1':
		outputs_A.append( outBitA )
	
	while len(outputs_A) < 100:
		# Run S-LFSR:
		outBit_S, stateOut_S = lfsr(states_S[-1], taps_S)
		states_S.append(stateOut_S)
		
		# Run A-LFSR
		outBit_A, stateOut_A = lfsr(states_A[-1], taps_A)
		states_A.append(stateOut_A)
		
		if outBit_S == '1':
			outputs_A.append( outBit_A )
	
	
	# Output vector to file:
	outFile = open("ShrinkingGen_Output.txt", "w")
	outFile.write("[" + ", ".join( outputs_A ) + "]")
	outFile.close()
	

if __name__ == "__main__":
	main()