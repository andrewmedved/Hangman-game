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
	return ['_' for x in range(len(word))]


def test():

	MAGIC_WORD = 'lighter'.upper()

	letter = 'g'.upper()

	print(MAGIC_WORD.index('G'))


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

	start_game_choice = input("Would you like to start a game? yes/no ")

	while start_game_choice != 'no':

		WORD = get_word_from_base(randrange(0, 213)).upper()

		print(WORD)
		secret_word = ciphered_word(WORD)

		while hp != 0:

			print(graphics.pictures[hp])


			print(secret_word)

			print(f"Chosen letters: {chosen_letters}")

			choice_letter = input("Enter guessing letter  ").upper()
			print(choice_letter)

			if choice_letter in WORD:
				print("RIGHT!")
				for letter in WORD:
					print(letter)
					if letter == choice_letter:
						print(WORD.index(letter))
						secret_word[WORD.index(letter)] = letter
						print(secret_word[WORD.index(letter)])
			else: 
				print("WRONG!")
				hp -= 1

			chosen_letters.append(choice_letter)

		print("=====GAME_OVER=====")

		start_game_choice = input("Do we play another game? yes/no ")
	


#test()
game_circle()