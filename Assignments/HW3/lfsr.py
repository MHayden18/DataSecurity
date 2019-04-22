def lfsr(seed, taps):
	sr, xor = seed, 0
	print("Starting LFSR with initial state of {}:".format(sr))
	repeat = 1
	
	while 1:
		for t in taps:
			xor += int(sr[t])
		if xor%2 == 0.0:
			xor = 0
		else:
			xor = 1
		
		# Outputs: note, length of sr = 6
		length = len(sr) 
		print( "#{0}:    State = {1};  Output:  {2}".format(repeat, sr, sr[length - 1]))
		print
		repeat += 1
		
		sr, xor = str(xor) + sr[:-1], 0
		
		if sr == seed:
			break
		
	return


def main():
	lfsr('100100', (5, 0))
	

if __name__ == "__main__":
	main()