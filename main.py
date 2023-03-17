print("Hello, game!")

logic_rule = 'yes'
counter = 0

while logic_rule == 'yes':
	logic_rule = input("Continue our cicle? ")
	print(counter)
	counter += 1

print("The last iteration {}".format(counter))
print("End of the cicle.\nGoodbye!!!")


