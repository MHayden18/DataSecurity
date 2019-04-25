def getLeft( input ):
	"""
	Left input is the lower order nibble of the input byte:
	"""
	return input & 15


def getRight( input ):
	"""
	Right input is the upper order nibble of the input byte:
	"""
	# Right shift by 4 will return desired bits by removing the lower order bits
	return input >> 4


def buildByte(right, left):
	""" 
	This function multiplies the right by 16 to return it to its higher order position
	"""
	right = right * 16
	return right + left
	
	
def Feistel(inByte):
	"""
	inByte - input data
	"""
	# S Boxes for each round:
	S = [ [5, 2, 15, 10, 6, 13, 7, 4, 14, 0, 1, 3, 12, 8, 9, 11],\
	[15, 5, 13, 11, 0, 12, 4, 8, 14, 10, 9, 2, 6, 1, 7, 3],\
	[7, 1, 2, 12, 0, 5, 9, 8, 14, 13, 15, 4, 10, 11, 3, 6] ]
			
	# Round Keys:
	keys = [15, 5, 9]
		
	# Pull nibbles from input byte:
	left, right = getLeft(inByte), getRight(inByte)
	
	for round in range(3):
		# xor right and round key:
		fOut = keys[round] ^ right
		
		# substitute the output of the fOut with the round's S-Box
		sOut = S[round][fOut]
		
		# Set next rounds inputs:
		rightOut = left ^ sOut
		leftOut = right
		
		# Reset inputs to next state:
		left = leftOut
		right = rightOut
	
	# Build output:
	outByte = buildByte(right, left)
	return outByte
	
	
def main():
	# print( lfsr('100100', (5, 0), 128) )
	bytes = [0xFA, 0xB1, 0x39, 0x45]
	outputs = []
	for byte in bytes:
		outputs.append( hex( Feistel( byte ) ) )
	
	# Print outputs:
	print(outputs)
	
	# Write outputs to file keeping array syntax:
	outFile = open("FeistelOut.txt", "w")
	outFile.write("[" + ", ".join(outputs) + "]")
	outFile.close()
	
	print("Done!")
	
	""" Function testing:
	# Used to test getLeft, getRight, and buildByte
	for byte in bytes:
		left = getLeft(byte)
		right = getRight(byte)
		print( "Left: " + str( getLeft(byte) ) )
		print( "Right: " + str( getRight(byte) ) )
		print( "Original: " + hex( buildByte(right, left) ) )
	"""

	
if __name__ == "__main__":
	main()