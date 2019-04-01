print("Modular inverse:")

alpha = 7

running = True
i = 1
while running:
	if ( (alpha * i) % 26 == 1):
		print( "Inverse is:  {}".format(i) )
		running = False
	else:
		i += 1
