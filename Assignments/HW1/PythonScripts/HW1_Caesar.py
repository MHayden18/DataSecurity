print("Homework 1: byte-wise caesar cypher")

def Caesar_Bytewise(shift, inFile, outFile):
	with open(inFile, "rb") as f:
		with open(outFile, "wb") as output:
			byte = f.read(1)
			while byte != b"":
				# Convert byte into an integer value
				value = int.from_bytes(byte, byteorder='big')
				# Calculate the output value given the shift
				out_value = ( value + shift) % 256
				# Write the output value to the output file, as a byte
				output.write( out_value.to_bytes(1, byteorder='big', signed=False))
				byte = f.read(1)
			output.close()
		f.close()

def main():
	Caesar_Bytewise(100, "Affine_Cipher.py", "HW1_output.txt")
	
	# Used for testing:
	#Caesar_Bytewise(156, "HW1_output.txt", "HW1_outputVerification.txt")


if __name__ == "__main__":
	main()