error = None

try:
	with open('base_of_words.txt') as bw:
	    
		count = 0
		while True:
			count += 1
			line = bw.readline()

			if not line:
				break
			print("Line{}: {} \n==============\n".format(count, line.strip()))

except FileNotFoundError:
	print("ERROR, CAN\'T OPEN FILE!")
	error = 'yes'


if error != None:
	print("\nCatch error and operate.")
else:
	print("Program works in state mode.")