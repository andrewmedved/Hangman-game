import sys
import graphics
import textwrap
from random import randrange


def get_word_from_base(position):

	"""Выбрать и считать слово из базы слов"""

	try:
		with open('base_of_words.txt') as file:
			return file.readlines()[position]

	except FileNotFoundError:
		return None

	except IndexError:
		return -1


def ciphered_word(word):
	for _ in range(len(word)):
		print("_ ")


def test():
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


def main():

	word = get_word_from_base(randrange(0, 213)).upper()

	if word == -1:
		print("OUT OF RANGE")

	if word != None:
		print(word)
	else:
		print("Occured error!")

	print(sys.argv[1])


def game_circle():

	hp = 6

	chosen_letters = []
	wrong_letters = []

	#print(graphics.pictures[0])

	start_game_choice = input("Would you like to start a game? yes/no ")

	while start_game_choice != 'no':

		
		start_game_choice = input("Do we play another game? yes/no ")



game_circle()