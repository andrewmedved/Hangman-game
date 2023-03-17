import textwrap

def ciphered_word(word):
	for _ in range(len(word)):
		print("_ ")


print("Hello, game!")

MAGIC_WORD = 'lighter'.upper()

logic_rule = 'yes'
counter = 0

while logic_rule == 'yes':
	logic_rule = input("Continue our cicle? ")
	print(counter)
	counter += 1

print("The last iteration {}".format(counter))
print("End of the cicle.\nGoodbye!!!\n\n")
ciphered_word(MAGIC_WORD)


